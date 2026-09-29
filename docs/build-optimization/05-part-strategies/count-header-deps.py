#!/usr/bin/env python3
"""Count Part object dependencies from streamed `ninja -t deps` output."""

import json
from pathlib import Path
import sys
from collections import defaultdict


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
removed = json.loads((OUT / "baseline-target-removed.json").read_text())
expected = {x for x in removed if x.endswith(".o")}
headers = {
    "DocumentObject.h": str(ROOT / "src/App/DocumentObject.h"),
    "PartFeature.h": str(ROOT / "src/Mod/Part/App/PartFeature.h"),
    "ComplexGeoData.h": str(ROOT / "src/App/ComplexGeoData.h"),
    "TopoShape.h": str(ROOT / "src/Mod/Part/App/TopoShape.h"),
}
matched = set()
dependency_sets = {name: set() for name in headers}
project_dependencies = defaultdict(set)
current = None
for line in sys.stdin:
    if not line.startswith(" "):
        output = line.split(": #deps", 1)[0]
        current = output if ": #deps" in line and output in expected else None
        if current is not None:
            matched.add(current)
    elif current is not None:
        dep = line.strip()
        if dep.startswith(str(ROOT / "src") + "/") and dep.endswith(".h"):
            project_dependencies[str(Path(dep).relative_to(ROOT))].add(current)
        for name, path in headers.items():
            if dep == path:
                dependency_sets[name].add(current)

result = {
    "source": "Current build/clang-profile Ninja dependency database, Part ordinary object outputs",
    "expected_part_objects": len(expected),
    "objects_with_dependency_records": len(matched),
    "missing_dependency_records": sorted(expected - matched),
    "headers": {
        name: {"dependent_objects": len(dependency_sets[name]),
               "object_outputs": sorted(dependency_sets[name])}
        for name in headers
    },
    "project_header_ranking": [
        {"header": path, "dependent_objects": len(objects)}
        for path, objects in sorted(project_dependencies.items(),
                                    key=lambda item: (-len(item[1]), item[0]))
    ],
}
(OUT / "header-dependencies.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"expected_part_objects": len(expected),
                  "objects_with_dependency_records": len(matched),
                  "headers": {name: len(outputs) for name, outputs in dependency_sets.items()}},
                 indent=2))
