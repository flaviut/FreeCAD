#!/usr/bin/env python3
"""Run controlled TechDraw App compilation variants in the existing Clang build."""

import argparse
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
BUILD = ROOT / "build/clang-profile"
CMAKE = ROOT / "src/Mod/TechDraw/App/CMakeLists.txt"
PCH = ROOT / "src/Mod/TechDraw/App/PreCompiled.h"
SOURCE = ROOT / "src/Mod/TechDraw/App/HatchLine.cpp"
MEASURE = HERE / "measure.py"
TARGET = "TechDraw"
PCH_ADDITIONS = (
    "#include <App/DocumentObject.h>\n"
    "#include <Mod/TechDraw/App/DrawView.h>\n"
)


def run(command, *, log=None):
    env = os.environ | {"FREECAD_BUILD_DIR": str(BUILD), "FREECAD_BUILD_JOBS": "8"}
    if log is None:
        return subprocess.run(command, cwd=ROOT, env=env, check=True)
    with log.open("w") as stream:
        return subprocess.run(command, cwd=ROOT, env=env, stdout=stream,
                              stderr=subprocess.STDOUT, check=True)


def set_variant(name, original):
    CMAKE.write_bytes(original[CMAKE])
    PCH.write_bytes(original[PCH])
    if name == "expanded-pch":
        PCH.write_bytes(original[PCH] + b"\n" + PCH_ADDITIONS.encode())
    elif name.startswith("unity"):
        batch = int(name.removeprefix("unity"))
        # CMake generated and listed C++ sources enter batches; C/C++ mixing is
        # handled by CMake. Explicit exclusions can be supplied after a failed
        # compatibility build, then are recorded in the config artifact.
        excluded_file = HERE / "unity-exclusions.txt"
        exclusions = [line.strip() for line in excluded_file.read_text().splitlines()
                      if line.strip() and not line.startswith("#")] if excluded_file.exists() else []
        addition = f"\nset_target_properties(TechDraw PROPERTIES UNITY_BUILD ON UNITY_BUILD_BATCH_SIZE {batch})\n"
        if exclusions:
            addition += "set_source_files_properties(\n"
            addition += "\n".join(f"    {name}" for name in exclusions)
            addition += "\n    PROPERTIES SKIP_UNITY_BUILD_INCLUSION ON\n)\n"
        CMAKE.write_bytes(original[CMAKE] + addition.encode())
    (HERE / f"{name}-config.json").write_text(json.dumps({
        "variant": name,
        "pch_appended": PCH_ADDITIONS if name == "expanded-pch" else "",
        "cmake_appended": CMAKE.read_bytes()[len(original[CMAKE]):].decode(),
    }, indent=2) + "\n")


def remove_target_outputs():
    directory = BUILD / "src/Mod/TechDraw/App/CMakeFiles/TechDraw.dir"
    outputs = sorted(path for path in directory.rglob("*") if path.suffix in (".o", ".pch"))
    if not outputs:
        raise RuntimeError("No TechDraw compiler outputs found after compatibility build")
    for path in outputs:
        path.unlink()
    return [str(path.relative_to(BUILD)) for path in outputs]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("variants", nargs="*", default=["baseline", "expanded-pch", "unity4", "unity8"])
    args = parser.parse_args()
    (HERE / "provenance").mkdir(exist_ok=True)
    lock = Path("/tmp/freecad-build-optimization.lock").open("w")
    fcntl.flock(lock, fcntl.LOCK_EX)
    original = {path: path.read_bytes() for path in (CMAKE, PCH)}
    old_mtime = SOURCE.stat().st_mtime_ns
    failed = []
    try:
        for name in args.variants:
            if name not in ("baseline", "expanded-pch", "unity4", "unity8"):
                raise ValueError(name)
            set_variant(name, original)
            try:
                run(["fc-build", "--target", TARGET], log=HERE / "provenance" / f"{name}-compatibility.log")
            except subprocess.CalledProcessError:
                failed.append(name)
                continue
            removed = remove_target_outputs()
            (HERE / f"{name}-removed.json").write_text(json.dumps(removed, indent=2) + "\n")
            run([sys.executable, str(MEASURE), f"{name}-target", TARGET])
            SOURCE.touch()
            run([sys.executable, str(MEASURE), f"{name}-source-touch", TARGET])
    finally:
        for path, contents in original.items():
            path.write_bytes(contents)
        os.utime(SOURCE, ns=(SOURCE.stat().st_atime_ns, old_mtime))
        run(["fc-build", "--target", TARGET], log=HERE / "provenance" / "restored-build.log")
    for name in args.variants:
        if name in failed:
            continue
        for suffix in ("target", "source-touch"):
            label = f"{name}-{suffix}"
            run([sys.executable, str(ROOT / "docs/build-optimization/analyze.py"),
                 "--build-dir", str(HERE / "provenance" / label),
                 "--output-dir", str(HERE / label)])
    (HERE / "failed-compatibility.json").write_text(json.dumps(failed, indent=2) + "\n")
    return bool(failed)


if __name__ == "__main__":
    sys.exit(main())
