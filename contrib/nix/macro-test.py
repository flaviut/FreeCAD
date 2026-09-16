import json
import os
import sys
from pathlib import Path
import traceback

import FreeCAD as App
import FreeCADGui as Gui
import Part
from PySide import QtCore

macro = Path(os.environ["FC_MACRO_FILE"])
output = Path(os.environ["FC_MACRO_OUTPUT"])
result = {
    "macro": str(macro),
    "freecad": App.Version(),
    "occt": Part.OCC_VERSION,
    "success": False,
}


def finish():
    try:
        screenshot = Gui.getMainWindow().grab()
        if not screenshot.save(str(output / "screenshot.png")):
            raise RuntimeError("Could not save screenshot")
    except Exception:
        result["success"] = False
        result["error"] = traceback.format_exc()

    with (output / "result.json").open("w") as stream:
        json.dump(result, stream, indent=2)

    if not result["success"]:
        print(result["error"], file=sys.stderr, flush=True)

    sys.stdout.flush()
    sys.stderr.flush()

    # Avoid save dialogs from documents created by the macro.
    os._exit(0 if result["success"] else 1)


def run():
    try:
        namespace = {"__name__": "__main__", "__file__": str(macro)}
        exec(compile(macro.read_bytes(), str(macro), "exec"), namespace)
        result["success"] = True
    except BaseException:
        result["error"] = traceback.format_exc()

    QtCore.QTimer.singleShot(1000, finish)


Gui.getMainWindow().resize(1440, 1000)
QtCore.QTimer.singleShot(0, run)
