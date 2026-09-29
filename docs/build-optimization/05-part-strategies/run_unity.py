#!/usr/bin/env python3
"""Run batch-four and batch-eight Part unity trials under an external flock."""

from pathlib import Path
import subprocess
import sys

import run


OUT = Path(__file__).resolve().parent
EXCLUSIONS = (OUT / "unity-exclusions.txt").read_text().splitlines()


def configuration(batch):
    files = "\n    ".join(EXCLUSIONS)
    return (f"\nset_source_files_properties(\n    {files}\n"
            f"    PROPERTIES SKIP_UNITY_BUILD_INCLUSION ON)\n"
            f"set_target_properties(Part PROPERTIES UNITY_BUILD ON UNITY_BUILD_BATCH_SIZE {batch})\n")


def main():
    original_cmake = run.CMAKE.read_bytes()
    try:
        for batch in (4, 8):
            label = f"unity-{batch}"
            snippet = configuration(batch)
            (OUT / f"{label}-configuration.cmake").write_text(snippet)
            run.CMAKE.write_bytes(original_cmake + snippet.encode())
            run.prepare(label)
            run.rebuild(f"{label}-target")
            run.source_touch(f"{label}-excluded-source")
    finally:
        run.CMAKE.write_bytes(original_cmake)
        run.prepare("restored-after-unity")


if __name__ == "__main__":
    main()
