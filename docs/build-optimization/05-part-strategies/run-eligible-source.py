#!/usr/bin/env python3
"""Measure a unity-eligible source edit in each Part configuration."""

from pathlib import Path
import run
import run_unity


OUT = Path(__file__).resolve().parent
SOURCE = run.ROOT / "src/Mod/Part/App/FeaturePartBox.cpp"


def touch(label):
    SOURCE.touch()
    run.measure(label)


def main():
    original_cmake = run.CMAKE.read_bytes()
    original_pch = run.PCH.read_bytes()
    try:
        run.prepare("eligible-baseline")
        touch("baseline-eligible-source")

        run.PCH.write_bytes(original_pch + b"\r\n#include <App/DocumentObject.h>\r\n"
                            + b"#include <Mod/Part/App/PartFeature.h>\r\n")
        run.prepare("eligible-project-pch")
        touch("project-pch-eligible-source")
        run.PCH.write_bytes(original_pch)

        for batch in (4, 8):
            run.CMAKE.write_bytes(original_cmake + run_unity.configuration(batch).encode())
            run.prepare(f"eligible-unity-{batch}")
            touch(f"unity-{batch}-eligible-source")
    finally:
        run.PCH.write_bytes(original_pch)
        run.CMAKE.write_bytes(original_cmake)
        run.prepare("restored-after-eligible-source")


if __name__ == "__main__":
    main()
