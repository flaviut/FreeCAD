#!/usr/bin/env python3
"""Run fc-build's CMake command and archive its Ninja log and build context."""

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import subprocess
import sys
import time


def ninja_records(path):
    if not path.is_file():
        return None, {}
    records = {}
    with path.open("rb") as stream:
        header = stream.readline().decode("utf-8", "replace").strip()
        for line in stream:
            fields = line.rstrip(b"\r\n").split(b"\t")
            if len(fields) >= 4:
                records[os.fsdecode(fields[3])] = [os.fsdecode(field) for field in fields]
    return header, records


def git_context():
    context = {}
    for key, args in (
        ("commit", ["git", "rev-parse", "HEAD"]),
        ("status", ["git", "status", "--short", "--untracked-files=normal"]),
    ):
        try:
            result = subprocess.run(args, capture_output=True, text=True, timeout=5, check=True)
            context[key] = result.stdout.strip()
        except (OSError, subprocess.SubprocessError):
            context[key] = None
    return context


def cmake_context(build_dir):
    wanted = {
        "CMAKE_BUILD_TYPE", "CMAKE_C_COMPILER", "CMAKE_CXX_COMPILER",
        "CMAKE_GENERATOR", "FREECAD_USE_PCH", "FREECAD_USE_CCACHE",
        "BUILD_ENABLE_TIME_TRACE",
    }
    result = {}
    try:
        with (build_dir / "CMakeCache.txt").open(errors="replace") as stream:
            for line in stream:
                if ":" in line and "=" in line:
                    name, value = line.rstrip("\n").split("=", 1)
                    key = name.split(":", 1)[0]
                    if key in wanted:
                        result[key] = value
    except OSError:
        pass
    return result


def archive(build_dir, command, started, elapsed, exit_code, before_header, before,
            git, child_cpu_before):
    log = build_dir / ".ninja_log"
    after_header, after = ninja_records(log)
    changed = {output: row for output, row in after.items() if before.get(output) != row}
    build_id = hashlib.sha256(os.fsencode(build_dir)).hexdigest()[:12]
    stamp = started.strftime("%Y%m%dT%H%M%S.%fZ")
    folder = Path.home() / ".cache/freecad-build" / f"{build_dir.name}-{build_id}" / started.strftime("%Y-%m") / f"{stamp}-{os.getpid()}"
    folder.mkdir(parents=True, exist_ok=False)
    if log.is_file():
        shutil.copyfile(log, folder / ".ninja_log")
    child_cpu_after = resource.getrusage(resource.RUSAGE_CHILDREN)
    metadata = {
        "schema_version": 1,
        "started_utc": started.isoformat(),
        "elapsed_s": elapsed,
        "child_user_cpu_s": child_cpu_after.ru_utime - child_cpu_before.ru_utime,
        "child_system_cpu_s": child_cpu_after.ru_stime - child_cpu_before.ru_stime,
        "exit_code": exit_code,
        "cwd": str(Path.cwd()),
        "build_dir": str(build_dir),
        "command": command,
        "jobs": os.environ.get("FREECAD_BUILD_JOBS", "44"),
        "remote_worker_available": os.environ.get("FREECAD_BUILD_REMOTE") == "1",
        "distcc_hosts": os.environ.get("DISTCC_HOSTS", ""),
        "ccache_prefix": os.environ.get("CCACHE_PREFIX", ""),
        "cmake": cmake_context(build_dir),
        "git_before_build": git,
        "ninja_log_before_header": before_header,
        "ninja_log_after_header": after_header,
        "ninja_log_before_outputs": len(before),
        "ninja_log_after_outputs": len(after),
        "changed_outputs": changed,
    }
    (folder / "build.json").write_text(json.dumps(metadata, indent=2) + "\n")


def main():
    try:
        separator = sys.argv.index("--")
        if sys.argv[1] != "--build-dir" or separator != 3 or separator == len(sys.argv) - 1:
            raise ValueError
    except (ValueError, IndexError):
        print("usage: record-build.py --build-dir DIR -- COMMAND [ARGS...]", file=sys.stderr)
        return 2

    build_dir = Path(sys.argv[2]).resolve()
    command = sys.argv[separator + 1:]
    log = build_dir / ".ninja_log"
    before_header, before = ninja_records(log)
    git = git_context()
    child_cpu_before = resource.getrusage(resource.RUSAGE_CHILDREN)
    started = dt.datetime.now(dt.timezone.utc)
    start = time.monotonic()
    exit_code = 1
    try:
        exit_code = subprocess.call(command)
    finally:
        elapsed = time.monotonic() - start
        try:
            archive(build_dir, command, started, elapsed, exit_code, before_header,
                    before, git, child_cpu_before)
        except (OSError, ValueError) as error:
            print(f"fc-build: unable to archive build log: {error}", file=sys.stderr)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
