#!/usr/bin/env python3
"""Measure Part PCH headers used by most ordinary Part source objects."""

import run


def main():
    original_pch = run.PCH.read_bytes()
    try:
        run.PCH.write_bytes(original_pch + b"\r\n#include <App/ComplexGeoData.h>\r\n"
                            + b"#include <Mod/Part/App/TopoShape.h>\r\n")
        run.prepare("majority-pch")
        run.rebuild("majority-pch-target")
        (run.ROOT / "src/Mod/Part/App/FeaturePartBox.cpp").touch()
        run.measure("majority-pch-eligible-source")
    finally:
        run.PCH.write_bytes(original_pch)
        run.prepare("restored-after-majority-pch")


if __name__ == "__main__":
    main()
