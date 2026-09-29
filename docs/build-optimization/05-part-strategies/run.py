#!/usr/bin/env python3
"""Run the controlled Part strategy series under an external flock."""

import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BUILD = ROOT / "build/clang-profile"
PCH = ROOT / "src/Mod/Part/App/PreCompiled.h"
CMAKE = ROOT / "src/Mod/Part/App/CMakeLists.txt"
TARGET_DIR = BUILD / "src/Mod/Part/App/CMakeFiles/Part.dir"
SOURCE = ROOT / "src/Mod/Part/App/PartFeature.cpp"
ENV = os.environ | {"FREECAD_BUILD_DIR": str(BUILD), "FREECAD_BUILD_JOBS": "8"}


def command(args, log):
    with (OUT / "provenance" / f"{log}.log").open("w") as stream:
        subprocess.run(args, cwd=ROOT, env=ENV, stdout=stream,
                       stderr=subprocess.STDOUT, check=True)


def measure(label):
    command([sys.executable, str(OUT / "measure.py"), label, "Part"],
            f"{label}-driver")
    command([sys.executable, str(ROOT / "docs/build-optimization/analyze.py"),
             "--build-dir", str(OUT / "provenance" / label),
             "--output-dir", str(OUT / label)], f"{label}-analyze")


def rebuild(label):
    removed = []
    for path in TARGET_DIR.rglob("*"):
        if path.suffix in (".o", ".pch"):
            removed.append(str(path.relative_to(BUILD)))
            path.unlink()
    (OUT / f"{label}-removed.json").write_text(json.dumps(removed, indent=2) + "\n")
    measure(label)


def source_touch(label):
    SOURCE.touch()
    measure(label)


def prepare(label):
    command(["fc-build", "--target", "Part"], f"{label}-prepare")


def main():
    (OUT / "provenance").mkdir(exist_ok=True)
    original_pch = PCH.read_bytes()
    original_cmake = CMAKE.read_bytes()
    try:
        prepare("baseline")
        rebuild("baseline-target")
        source_touch("baseline-source")

        PCH.write_bytes(original_pch + b"\r\n#include <App/DocumentObject.h>\r\n"
                        + b"#include <Mod/Part/App/PartFeature.h>\r\n")
        prepare("project-pch")
        rebuild("project-pch-target")
        source_touch("project-pch-source")

    finally:
        PCH.write_bytes(original_pch)
        CMAKE.write_bytes(original_cmake)
        prepare("restored")


if __name__ == "__main__":
    main()
