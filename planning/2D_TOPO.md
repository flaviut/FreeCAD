# Derived Geometry in the Sketcher — Topological Naming Analysis

This document breaks down the FreeCAD Sketcher architecture relevant to adding a
"derived geometry" feature (offsets of b-splines etc.), and answers whether the
3D topological-naming (TNP) infrastructure is reusable for 2D sketches.

## The mental model: three layers

The Sketcher is three layers that talk to each other through a sync cycle on
every recompute (`SketchObject::execute()`, `src/Mod/Sketcher/App/SketchObject.cpp:186`):

```
┌─ Data model ─────────────────────────────────────────────┐
│  SketchObject (Part::Part2DObject)                        │
│   • Geometry         PropertyGeometryList  (Part::Geometry*)
│   • Constraints      PropertyConstraintList               │
│   • ExternalGeometry PropertyLinkSubList   (links to 3D)  │
│   • ExternalGeo      PropertyGeometryList  (projected)    │
│   • Shape / InternalShape  Part::TopoShape (the output)   │
└──────────────────────────────────────────────────────────┘
              │ setUpSketch() ▼        ▲ extractGeometry()
┌─ Solver ─────────────────────────────────────────────────┐
│  Sketch (Base::Persistence)  — Sketch.h:41                │
│   • GCS::System GCSsys  (planegcs, the LM/DogLeg solver)  │
│   • GeoDef[] Geoms, Points[], Lines[], Circles[], BSpline[]
└──────────────────────────────────────────────────────────┘
              │ buildShape() ▼
┌─ Output shape ───────────────────────────────────────────┐
│  Part::TopoShape with an ElementMap (toponaming!)         │
└──────────────────────────────────────────────────────────┘
```

Recompute path: `Part2DObject::execute()` (positions the plane) →
`rebuildExternalGeometry()` → `solve()` (push geometry+constraints into GCS,
solve, pull solved geometry back into the `Geometry` property) → `buildShape()`
(turn solved curves into a `TopoShape`).

### Key files

| Component | Header | Notes |
|---|---|---|
| Main sketch object | `src/Mod/Sketcher/App/SketchObject.h` | `Geometry`, `Constraints`, `ExternalGeometry`, `Shape`, `InternalShape` |
| Solver interface | `src/Mod/Sketcher/App/Sketch.h:41` | wraps `GCS::System GCSsys` |
| Geometry IDs/enums | `src/Mod/Sketcher/App/GeoEnum.h` | `GeoEnum`, `PointPos`, `GeoElementId` |
| Per-geometry extension | `src/Mod/Sketcher/App/SketchGeometryExtension.h` | the stable `long Id`, `InternalType`, `GeometryMode` |
| External geometry | `src/Mod/Sketcher/App/ExternalGeometryExtension.h` | flags + `Ref`/`RefIndex` recovery |
| Constraint solver | `src/Mod/Sketcher/App/planegcs/GCS.h` | LM / BFGS / DogLeg |

## How geometry is identified today — three distinct identities

This is the crux for the feature:

| Identity | What it is | Where | Stable across edits? |
|---|---|---|---|
| **GeoId** | array index into `Geometry` (≥0 internal; ≤−3 external; −1/−2 are axes) | `GeoEnum.h:69` | **No** — shifts when geometry added/removed |
| **Geometry `Id`** | a `long`, from an atomic counter `_GeometryID` | `SketchGeometryExtension.h:174,180` | **Yes** — assigned once, survives edits/reorder |
| **Element-map name** | `Edge3`, `Vertex5`… mapped to a `Data::MappedName` on the output `TopoShape` | `buildShape()`, `SketchObject.cpp:254` | Stable as long as the mapping is stable |

`GeoId` + `PointPos` (`none/start/end/mid`, `GeoEnum.h:86`) is how constraints
and the solver address geometry internally. The `long Id` is the Sketcher's
*existing* answer to "stable whole-curve identity" — effectively a hand-rolled,
per-curve topo-name that predates and is independent of the OCC TNP system.

## Key finding: the Sketcher already uses the toponaming core

The generic element-map machinery is not just reusable for 2D — it is **already
wired in**. See `buildShape()` (`SketchObject.cpp:254-360`):

```cpp
vertex.resetElementMap(std::make_shared<Data::ElementMap>());
vertex.setElementName(Data::IndexedName::fromConst("Vertex", 1),
                      Data::MappedName::fromRawData(name.c_str()), 0L);
...
result.makeElementWires(shapes, Part::OpCodes::Sketch);   // op-coded, history-aware
result.Tag = getID();
Shape.setValue(result);                                    // TopoShape carries the ElementMap
```

It constructs the output `Part::TopoShape` with a real `Data::ElementMap`, uses
`Data::IndexedName`/`Data::MappedName`, tags everything with the
`Part::OpCodes::Sketch` op code, and uses the document's `StringHasher`.
`getEdge()` (`SketchObject.cpp:1585`) even names the sub-vertices of each edge.
So the generic machinery already crosses the 2D boundary.

### Why it works for 2D: the element-map core is not coupled to OpenCascade

The element-map infrastructure lives in `src/App` and is geometry-agnostic:

- `Data::ComplexGeoData` (`src/App/ComplexGeoData.h`) — holds the `ElementMap`
  and the whole `getMappedName`/`setElementName`/`getElementHistory` API.
- `Data::ElementMap`, `Data::IndexedName`, `Data::MappedName`,
  `Data::MappedElement`, `App::StringHasher`/`StringID`, `ElementNamingUtils.h`
  — all generic name/lookup/compression code.
- Only `Part::TopoShape` (`src/Mod/Part/App`) ties it to `TopoDS_Shape`, plus
  `TopoShapeOpCode.h` (which already defines `Offset="OFS"` and `Offset2D="OFF"`).
- Mesh, Fem, and Points modules reuse the same `ComplexGeoData` base for non-OCC
  geometry — proof it is geometry-agnostic.

Reusability requirements for any geometry type: inherit from
`Data::ComplexGeoData`, implement `getElementTypes()`/`countSubElements()`/
`getSubElement()`, and have a `Tag` and optional `Hasher`.

## What is actually new work for "derived geometry"

The naming **plumbing** exists; what's missing is a true **derivation/history
naming algorithm** and reconciling it with the solver's index-based world. The
current `buildShape` naming is *trivial* — `Edge{geoId}` derived directly from
array position, not from operation history. That's fine when geometry maps 1:1 to
user input. It breaks exactly in the offset scenario, where curves can
appear/disappear/split.

Problems, in order of difficulty:

1. **The solver/data-model side is the hard part, not the Shape side.**
   GCS (`Sketch.h`) and the `Geometry` list are indexed by `GeoId` = array
   position, and constraints reference `GeoId`. Derived geometry that
   appears/disappears (an offset that splits, self-intersects, or collapses)
   changes the count and shifts every index after it. You need a stable name that
   survives that — which is what the `long Id` *partially* provides, but `Id` has
   no notion of "I am the 2nd piece generated by offsetting curve Id=N." Extend
   identity to encode derivation, analogous to `encodeElementName` with an op code
   (`OFF`) + source tag + sub-index.

2. **Where to compute the offset and capture history.**
   OCC's `BRepOffsetAPI_MakeOffset` (wrapped in
   `src/Mod/Part/App/BRepOffsetAPI_MakeOffsetFix.h`) produces a `TopoDS_Shape`
   with generated/modified history. `Part::TopoShape`'s element-mapping
   (`TopoShapeMapper`, the `makeElement*` methods) already turns that BRep history
   into stable mapped names automatically. So the cleanest architecture is likely:
   do the derivation as a `TopoShape` operation (history-based toponaming for
   free), then map the resulting edges back into `Part::Geometry` for the solver,
   carrying derived `Id`s computed from the mapped names. The Sketcher already has
   OCC→`Part::Geometry` conversion helpers
   (`curveToLine`/`curveToCircleOrArc`/`curveToEllipseOrArc` in
   `src/Mod/Sketcher/Gui/DrawSketchHandlerOffset.h`); the gap there is b-spline
   conversion (there is a literal `TODO Bspline support`).

3. **Dependency between geometries inside one sketch.**
   Today all internal geometry is peer-level; the only intra-sketch dependency is
   *internal alignment* (ellipse foci, b-spline poles/knots) tracked via
   `internalAlignmentGeometryMap` (`Sketch.cpp`) and `InternalType`
   (`SketchGeometryExtension.h:39`). Derived geometry introduces a genuine
   *source → derived* DAG within the sketch that has to be (a) recomputed in
   topological order before/within the solve, and (b) made non-editable (like
   construction/blocked modes in `GeometryMode`). There is no existing mechanism
   for "this curve is a pure function of that curve" inside a single sketch.
   `ExternalGeometry` is the closest pattern (derive-from-elsewhere + frozen flags
   + a `Ref` recovery string) and is the best design template.

## Bottom line

- **Yes — the toponaming core is reusable for 2D, and it is not hypothetical:**
  `buildShape()` already builds the output sketch shape with the same
  `ElementMap`/`MappedName`/`StringHasher`/op-code machinery used by the 3D
  engine. Nothing in `src/App`'s element-map code is OCC-bound.
- The missing piece is a **history-encoding naming step for derived 2D geometry**
  (using the op-code/`encodeElementName` mechanism with an `OFF`/`OFS` op + source
  identity) and, more importantly, the **data-model work** to let curves inside a
  sketch depend on other curves and survive count/index changes. The existing
  `long Id` and the `ExternalGeometry` subsystem are the two patterns to build on.
- **Promising shortcut:** perform the derivation at the `Part::TopoShape` level
  (offset via `BRepOffsetAPI`), inherit OCC's generated/modified history → mapped
  names automatically, then round-trip back to `Part::Geometry` for the solver.

## Open follow-ups

- Trace exactly how `extractGeometry()`/`setUpSketch()` round-trips `Id`s through
  the solver — to find where derived identity must be threaded.
- Map how `ExternalGeometry`'s rebuild + `Ref` recovery works
  (`SketchObjectExternal.cpp:2294 rebuildExternalGeometry()`) as a template for an
  internal derived-geometry feature.
