#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1-or-later

"""
Manage baselines for FreeCAD visual snapshot tests.

Configure the existing FreeCAD unittests through environment variables.
Add --headless to run either suite under private Xvfb.

Examples:

  tools/rendering/visual_baselines.py update --suite TestCoinNodeSnapshots --headless \
    --freecad build/<preset>/bin/FreeCAD

  tools/rendering/visual_baselines.py compare --suite TestView3DRenderSnapshots --headless \
    --freecad build/<preset>/bin/FreeCAD --baseline-dir /tmp/reference/actual
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import html
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# pylint: disable=broad-exception-caught,duplicate-code

def _default_freecad() -> str | None:
    # Allow explicit override from the environment.
    val = os.environ.get("FREECAD", "").strip()
    if val:
        return val

    # Common local build layouts.
    executable = "FreeCAD"
    candidates: list[Path] = [
        Path("build/bin") / executable,
        *sorted(Path("build").glob(f"*/bin/{executable}")),
        *sorted(Path("build").glob(f"*/bin/{executable}.exe")),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)

    return shutil.which(executable)


def _default_baseline_dir(suite: str) -> str:
    # This script lives in-tree under `tools/rendering/`.
    repo_root = Path(__file__).resolve().parents[2]
    return str(repo_root / "tests" / "visual" / "baselines" / suite)


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--suite", default="TestCoinNodeSnapshots", help="Test module name")
    common.add_argument("--headless", action="store_true", help="Run on a private Xvfb display")
    common.add_argument(
        "--freecad",
        help="Path to FreeCAD (default: environment, build tree, or PATH)",
    )
    common.add_argument(
        "--qt-platform",
        default="",
        help=(
            "Value for QT_QPA_PLATFORM. By default this script does not override it; "
            "if no DISPLAY/WAYLAND is available, it auto-sets QT_QPA_PLATFORM=offscreen. "
            "With --headless, either suite uses xcb under private Xvfb."
        ),
    )
    common.add_argument(
        "--baseline-dir",
        help="Baseline directory containing/writing *.png files (default: suite baselines)",
    )
    common.add_argument(
        "--out-dir",
        help="Empty artifact output directory (default: a fresh temporary directory)",
    )
    common.add_argument("--nodes", default="", help="Comma-separated node type list (optional)")
    common.add_argument("--label", default="", help="Revision/build label for the report")
    common.add_argument("--timeout", type=int, default=180, help="Test timeout in seconds")

    sub.add_parser("update", parents=[common], help="Write/update baselines")
    sub.add_parser("compare", parents=[common], help="Compare against baselines")
    sub.add_parser("record", parents=[common], help="Record without updating baselines")
    args = parser.parse_args(argv)
    if args.freecad is None:
        args.freecad = _default_freecad()
    if args.baseline_dir is None:
        args.baseline_dir = _default_baseline_dir(args.suite)
    return args


def _gallery(output, report):
    rows = []
    for name, result in sorted(report.get("snapshots", {}).items()):
        cells = []
        for directory in ("expected", "actual", "diff"):
            path = output / directory / f"{name}.png"
            if path.is_file():
                relative = html.escape(path.relative_to(output).as_posix(), quote=True)
                cells.append(f'<td><a href="{relative}"><img src="{relative}"></a></td>')
            else:
                cells.append("<td>—</td>")
        status = "pass" if result["passed"] else "fail"
        rows.append(f'<tr><th>{html.escape(name)}<br>{status}</th>{"".join(cells)}</tr>')
    checks = "".join(
        f'<li>{"PASS" if item["passed"] else "FAIL"}: '
        f'{html.escape(item["name"])} — {html.escape(item["message"])}</li>'
        for item in report.get("checks", [])
    )
    label = html.escape(report.get("label", "") or "Rendering snapshots")
    page = (
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        f'<title>{label}</title><style>'
        'body{font:14px sans-serif}table{border-collapse:collapse}'
        'td,th{border:1px solid #ccc;padding:8px}img{max-width:350px;height:auto}'
        '</style>'
        f'<h1>{label}</h1><p>Success: {report.get("success", False)}</p>'
        f'<ul>{checks}</ul><table><tr><th>Step</th><th>Expected</th>'
        f'<th>Actual</th><th>Diff</th></tr>{"".join(rows)}</table></html>\n'
    )
    (output / "index.html").write_text(page)


def _partial_report(output, args):
    return {
        "label": args.label,
        "success": False,
        "snapshots": {
            path.stem: {"file": f"actual/{path.name}", "passed": False}
            for path in sorted((output / "actual").glob("*.png"))
        },
    }


def _headless_cmd(cmd: list[str], env: dict[str, str], output: Path) -> list[str]:
    # Isolate display and preferences independently of the selected test suite.
    env.pop("WAYLAND_DISPLAY", None)
    env.update(QT_QPA_PLATFORM="xcb", QT_SCALE_FACTOR="1", QT_FONT_DPI="96",
               QT_STYLE_OVERRIDE="Fusion", LIBGL_ALWAYS_SOFTWARE="1",
               MESA_LOADER_DRIVER_OVERRIDE="llvmpipe", LANG="C.UTF-8",
               LC_ALL="C.UTF-8", LANGUAGE="en_US")
    return ["xvfb-run", "-a", "-s", "-screen 0 1280x1024x24 -dpi 96 -nolisten tcp",
            cmd[0], "--user-cfg", str(output / "user.cfg"),
            "--system-cfg", str(output / "system.cfg"), *cmd[1:]]


def _run(args, cmd, env):
    output = Path(args.out_dir)
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        print("ERROR: --out-dir must be empty; stale snapshots cannot count as a run",
              file=sys.stderr)
        return 2
    output.mkdir(parents=True, exist_ok=True)

    # Both suites write candidate references; only a successful update promotes them.
    with tempfile.TemporaryDirectory(prefix="freecad-baseline-candidates-") as candidates:
        if args.mode in ("record", "update"):
            env["FC_VISUAL_BASELINE_DIR"] = candidates
            env["FC_VISUAL_UPDATE_BASELINE"] = "1"

        print(f"Running: {' '.join(cmd)}", flush=True)
        if "QT_QPA_PLATFORM" in env:
            print(f"  QT_QPA_PLATFORM={env['QT_QPA_PLATFORM']}")
        print(f"  FC_VISUAL_BASELINE_DIR={env['FC_VISUAL_BASELINE_DIR']}")
        print(f"  FC_VISUAL_OUT_DIR={env['FC_VISUAL_OUT_DIR']}")
        if "FC_VISUAL_NODES" in env:
            print(f"  FC_VISUAL_NODES={env['FC_VISUAL_NODES']}")

        try:
            proc = subprocess.run(cmd, env=env, cwd=str(Path.cwd()), check=False,
                                  timeout=args.timeout)
            returncode = proc.returncode
        except subprocess.TimeoutExpired:
            print("ERROR: tests timed out", file=sys.stderr)
            returncode = 1

        report_path = output / "results.json"
        if report_path.is_file():
            report = json.loads(report_path.read_text())
        else:
            report = _partial_report(output, args)
            report["success"] = returncode == 0 and bool(report["snapshots"])
            for result in report["snapshots"].values():
                result["passed"] = report["success"]
        report.update(command=cmd, recorded_at=datetime.now(timezone.utc).isoformat(),
                      returncode=returncode)
        report["success"] = report["success"] and returncode == 0
        report_path.write_text(json.dumps(report, indent=2) + "\n")
        _gallery(output, report)
        print(f"Snapshots: {output / 'index.html'}")
        if not report["success"]:
            print("ERROR: rendering checks failed", file=sys.stderr)
            return returncode or 1

        if args.mode == "update":
            baseline_dir = Path(args.baseline_dir)
            baseline_dir.mkdir(parents=True, exist_ok=True)
            for path in Path(candidates).glob("*.png"):
                shutil.copyfile(path, baseline_dir / path.name)
    return 0


def main(argv: list[str]) -> int:
    """Entry point."""
    args = _parse_args(argv)

    if not args.freecad:
        print(
            "ERROR: could not auto-detect executable; pass --freecad "
            "build/<preset>/bin/FreeCAD",
            file=sys.stderr,
        )
        return 2

    freecad = Path(args.freecad)
    if not freecad.is_file():
        print(f"ERROR: executable not found: {freecad}", file=sys.stderr)
        return 2

    baseline_dir = Path(args.baseline_dir)
    if args.mode == "compare" and not baseline_dir.is_dir():
        print(
            f"ERROR: baseline directory not found: {baseline_dir} "
            "(pass --baseline-dir or run `update` first)",
            file=sys.stderr,
        )
        return 2

    if args.timeout <= 0:
        print("ERROR: --timeout must be positive", file=sys.stderr)
        return 2
    if args.out_dir is None:
        args.out_dir = tempfile.mkdtemp(prefix=f"freecad-{args.suite}-")
    args.out_dir = str(Path(args.out_dir).resolve())
    env = os.environ.copy()
    if args.qt_platform.strip():
        env["QT_QPA_PLATFORM"] = args.qt_platform.strip()
    else:
        has_display = bool(env.get("DISPLAY") or env.get("WAYLAND_DISPLAY"))
        if not has_display and not env.get("QT_QPA_PLATFORM"):
            env["QT_QPA_PLATFORM"] = "offscreen"
    env["FC_VISUAL_BASELINE_DIR"] = str(baseline_dir.resolve())
    env["FC_VISUAL_OUT_DIR"] = str(Path(args.out_dir).resolve())
    if args.nodes.strip():
        env["FC_VISUAL_NODES"] = args.nodes

    env.pop("FC_VISUAL_UPDATE_BASELINE", None)
    env.update(FC_VISUAL_MODE=args.mode, FC_VISUAL_LABEL=args.label)
    root = Path(__file__).resolve().parents[2]
    cmd = [str(freecad), "--python-path", str(root / "src/Mod/Test"),
           "-t", args.suite]
    if args.headless:
        if not sys.platform.startswith("linux") or shutil.which("xvfb-run") is None:
            print("ERROR: --headless requires Linux/Xvfb", file=sys.stderr)
            return 2
        cmd = _headless_cmd(cmd, env, Path(args.out_dir))

    return _run(args, cmd, env)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
