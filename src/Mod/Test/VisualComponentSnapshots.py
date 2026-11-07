# SPDX-License-Identifier: LGPL-2.1-or-later

"""Widget and property-editor snapshots for stock FreeCAD themes.

Run through tools/rendering/visual_baselines.py with --headless --suite VisualComponentSnapshots.
"""

import json
import os
from pathlib import Path
import sys
import unittest

import FreeCAD

from VisualTestSupport import baseline_dir, compare_images, widget_font, write_baseline


_PAGES = (
    "buttons", "text", "numbers", "labels", "views", "containers", "spreadsheet",
    "property-states", "property-scalars", "property-geometry", "property-collections",
    "property-editors-states", "property-editors-scalars",
    "property-editors-geometry", "property-editors-collections",
)

_PLAN = (
    ("classic-light", _PAGES),
    ("classic-dark", _PAGES),
    ("dark", _PAGES),
    ("light", _PAGES),
)


class ComponentSnapshotTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not FreeCAD.GuiUp:
            raise unittest.SkipTest("Use FreeCAD -t; GUI widgets are required")
        if os.environ.get("CI") and not sys.platform.startswith("linux"):
            raise unittest.SkipTest("Visual snapshots are only supported on Linux CI")

        from PySide import QtCore, QtWidgets
        import QtUnitGui

        cls.zoo = QtUnitGui.componentZoo
        output = os.environ.get("FC_VISUAL_OUT_DIR")
        if not output or Path(FreeCAD.ConfigGet("UserParameter")).resolve() != (
            Path(output) / "user.cfg"
        ).resolve():
            raise unittest.SkipTest("Run through tools/rendering/visual_baselines.py with --headless")
        cls.output = Path(output)
        cls.output.mkdir(parents=True, exist_ok=True)
        cls.baselines = baseline_dir(Path(__file__).stem)
        cls.mode = os.environ.get("FC_VISUAL_MODE", "compare")
        if cls.mode not in ("compare", "record", "update"):
            raise ValueError(f"Unknown FC_VISUAL_MODE: {cls.mode}")
        cls.snapshots = {}

        app = QtWidgets.QApplication
        app.setStyle("Fusion")
        QtCore.QLocale.setDefault(QtCore.QLocale.c())
        FreeCAD.Units.setSchema(0)
        app.setFont(widget_font())
        app.setCursorFlashTime(0)

    @classmethod
    def tearDownClass(cls):
        expected = {f"{page}-{theme}" for theme, pages in _PLAN for page in pages}
        report = {
            "label": os.environ.get("FC_VISUAL_LABEL", ""),
            "snapshots": cls.snapshots,
            "success": cls.snapshots.keys() == expected
            and all(item["passed"] for item in cls.snapshots.values()),
        }
        (cls.output / "results.json").write_text(json.dumps(report, indent=2) + "\n")

    def test_snapshots(self):
        for theme, pages in _PLAN:
            images = self.zoo(theme, list(pages))
            for page in pages:
                with self.subTest(snapshot=f"{page}-{theme}"):
                    self._snapshot(f"{page}-{theme}", images[page])

    def _snapshot(self, name, image):
        result = {"file": f"actual/{name}.png", "passed": False}
        self.snapshots[name] = result
        actual = self.output / result["file"]
        actual.parent.mkdir(parents=True, exist_ok=True)
        self.assertTrue(image.save(str(actual)), f"Cannot save {actual}")
        for path in (self.output / "expected" / f"{name}.webp",
                     self.output / "diff" / actual.name):
            path.unlink(missing_ok=True)

        if self.mode in ("record", "update"):
            if os.environ.get("FC_VISUAL_UPDATE_BASELINE", "").lower() in ("1", "true"):
                write_baseline(actual, self.baselines / f"{name}.webp")
            result["passed"] = True
            return

        baseline = self.baselines / f"{name}.webp"
        self.assertTrue(baseline.is_file(), f"Missing baseline: {baseline}")
        expected = self.output / "expected" / baseline.name
        expected.parent.mkdir(parents=True, exist_ok=True)
        expected.write_bytes(baseline.read_bytes())
        passed, message = compare_images(
            expected, actual, self.output / "diff" / actual.name,
            tolerance=2, ignore_alpha=False, max_mismatched_pixels=0,
        )
        result.update(passed=passed, message=message)
        self.assertTrue(passed, f"{name}: {message}")
