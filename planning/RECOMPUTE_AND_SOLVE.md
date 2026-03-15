# Sketcher recompute & solve cycle — what exists today

Factual survey of how a `SketchObject` recomputes and solves, and where geometry
positions are produced. Companion to `2D_TOPO.md` (naming) and
`EXTERNAL_GEOMETRY.md` (the derive-from-elsewhere subsystem). This document
records *what the code does* and *what is and isn't available* to a feature that
needs to recompute one piece of geometry from another. It does not recommend a
design.

## The geometry lists and how they are addressed

`SketchObject` (`src/Mod/Sketcher/App/SketchObject.h`) holds two geometry
properties:

- `Geometry` — `Part::PropertyGeometryList`, the internal geometry.
- `ExternalGeo` — `Part::PropertyGeometryList`, projected/external geometry
  (always contains the H and V axes at indices 0/1).

Three identities address geometry; only the first is used by the solver and
constraints:

| Identity | Stable across edits? | Source |
|---|---|---|
| **GeoId** (array index; ≥0 internal, ≤−3 external, −1/−2 axes) | No — shifts on add/remove | `GeoEnum.h:69` |
| **`long Id`** (atomic counter) | Yes | `SketchGeometryExtension.h:174,180`; assigned in `SketchObject.cpp:982-1000` |
| element-map name (`Edge3`…) | While mapping is stable | `buildShape()` |

`getCompleteGeometry()` (`SketchObjectGeometry.cpp:1412`) is the list the solver
sees. It is internal geometry followed by external geometry **in reverse order**:

```cpp
std::vector<Part::Geometry*> vals = getInternalGeometry();
const auto &geos = getExternalGeometry();
vals.insert(vals.end(), geos.rbegin(), geos.rend()); // in reverse order
```

So the external geometry forms a fixed-length tail of this combined list; its
length is `getExternalGeometryCount()` (`SketchObject.h:304`).

## What triggers a recompute

`mustExecute()` (`SketchObject.cpp:173`) returns 1 (needs execute) when any of
`Geometry`, `Constraints`, `ExternalGeometry`, or `ExternalGeo` is touched:

```cpp
if (Geometry.isTouched())         return 1;
if (Constraints.isTouched())      return 1;
if (ExternalGeometry.isTouched()) return 1;
if (ExternalGeo.isTouched())      return 1;
return Part2DObject::mustExecute();
```

`onChanged()` (`SketchObject.cpp:928`) routes each property change to a handler
(`onGeometryChanged`, `onConstraintsChanged`, `onExternalGeoChanged`,
`onExternalGeometryChanged`, `onPlacementChanged`, …).

Document-level recompute is driven by the dependency graph between
`DocumentObject`s. `ExternalGeometry` is an `App::PropertyLinkSubList` to *other*
document objects, so a change in a referenced object marks the sketch touched
through that graph. There is **no analogous graph edge for one piece of geometry
depending on another within the same `SketchObject`** — a single sketch is one
node in the document DAG.

## Path A: full recompute — `execute()`

`SketchObject::execute()` (`SketchObject.cpp:186-244`), in order:

```cpp
Part2DObject::execute();                          // 189  position plane by support
rebuildExternalGeometry();                        // 200  re-project ExternalGeo from links
Constraints.acceptGeometry(getCompleteGeometry());// 201  sync constraint indices
int err = this->solve(true);                      // 213  set up GCS, solve, write back Geometry
// ... error handling for err in {-1..-5} ...
buildShape();                                     // 241  solved curves -> TopoShape
```

Fact relevant to derive-from-internal: `rebuildExternalGeometry()` runs **before**
`solve()`. External geometry is regenerated from its links (whose sources are
upstream in the document DAG and already final) prior to solving. Internal
geometry positions are *not* final until `solve()` returns at line 213.

## Path B: dragging / programmatic move — `moveGeometries()`

`moveGeometries()` (`SketchObjectOperations.cpp:47-93`) does **not** call
`execute()` and does **not** call `rebuildExternalGeometry()`. It optionally
re-sets up the solver, moves in the solver, and writes the result straight into
the `Geometry` property:

```cpp
if (updateGeoBeforeMoving || solverNeedsUpdate) {
    lastDoF = solvedSketch.setUpSketch(getCompleteGeometry(),
                                       Constraints.getValues(),
                                       getExternalGeometryCount());   // 63
    ...
}
lastSolverStatus = solvedSketch.moveGeometries(geoEltIds, toPoint, relative); // 77
if (lastSolverStatus == 0) {
    std::vector<Part::Geometry*> geomlist = solvedSketch.extractGeometry();
    Geometry.setValues(geomlist);                                     // 84
    ...
}
```

So interactive dragging updates internal geometry positions on a path that never
visits the `execute()` recompute or any `ExternalGeo` rebuild. (External geometry
does not need updating here because it does not move with internal geometry.)

## How the solver treats internal vs external geometry

`SketchObject::solve()` (`SketchObjectConstraints.cpp:76`) calls:

```cpp
lastDoF = solvedSketch.setUpSketch(getCompleteGeometry(),
                                   Constraints.getValues(),
                                   getExternalGeometryCount());   // 92-93
...
lastSolverStatus = solvedSketch.solve();                          // 131
```

`Sketch::setUpSketch(GeoList, ConstraintList, extGeoCount)`
(`Sketch.cpp:193`) splits the combined list at the `extGeoCount` boundary:

```cpp
std::copy(GeoList.begin(), GeoList.end() - extGeoCount, back_inserter(intGeoList));
std::copy(GeoList.end() - extGeoCount, GeoList.end(),  back_inserter(extGeoList)); // 212-213
// "these geometries are blocked, frozen and sent as fixed parameters to the solver" (215)
addGeometry(intGeoList, onlyBlockedGeometry, inGroupGeoIds);   // 262  free / conditionally fixed
addGeometry(extGeoList, true);                                 // 264  fixed = true
```

`Sketch::addGeometry(geo, fixed)` (`Sketch.cpp:695`) and the per-type adders
(`addPoint`, `addLineSegment`, …) route parameters by the `fixed` flag:

```cpp
std::vector<double*>& params = fixed ? FixParameters : Parameters;   // e.g. addPoint, 794
```

`FixParameters` are held constant by the solver (reset to their values each
solve, `Sketch.cpp:108-111`); `Parameters` are the free variables. Consequence:
**anything stored in `ExternalGeo` enters the solve as constants, not free
variables.** Constraints may reference these constants (via negative GeoIds), the
same way dimensions can be placed against external geometry today.

## Facts that bear on "recompute one geometry from another, inside the sketch"

These follow directly from the above; they are constraints any such feature
operates under, not a chosen design:

1. **The document DAG does not order intra-sketch dependencies.** One sketch is
   one node. Source-curve → derived-curve ordering within a sketch is not
   expressed in the recompute graph; `mustExecute`/`onChanged` operate at the
   whole-`SketchObject` granularity.

2. **`ExternalGeo` contents are already grounded in the solve** (the `fixed=true`
   path above). Storing recomputed geometry there makes it constant in planegcs
   automatically, and it is already addressable by constraints via negative
   GeoIds.

3. **`rebuildExternalGeometry()` runs before `solve()`.** Geometry whose inputs
   are external links can be produced before solving. Geometry whose inputs are
   *internal* curves cannot be produced from final positions at line 200, because
   those positions are only computed at line 213.

4. **Two write paths produce internal positions:** `execute()` → `solve()`
   (line 213) and `moveGeometries()` → `extractGeometry()`/`Geometry.setValues()`
   (line 84). A recompute keyed on final internal positions would have to be
   reachable from both; the latter does not currently invoke any rebuild step.

5. **GeoId is positional; `long Id` is stable.** Add/remove of internal geometry
   shifts GeoIds (and constraints are renumbered accordingly); `Id` survives.
   `ExternalGeo` already keys its source bookkeeping by `Id`
   (`externalGeoMap`/`externalGeoRefMap`, see `EXTERNAL_GEOMETRY.md`).

## Options on the table (neutral)

Ways the existing machinery *could* be arranged for a recompute-from-internal
feature, with the trade-off each carries. No recommendation is made here.

- **Where to place the recompute relative to `solve()`:**
  - Before solve (where `rebuildExternalGeometry` sits) — matches the external
    pattern, but reads internal source positions that are not yet final on this
    pass.
  - After solve — reads final source positions, but any constraint that
    references the recomputed geometry was solved this pass against its previous
    values, so a second solve would be needed for consumers to react on the same
    recompute.
  - Staged (solve → recompute → solve) — produces final source positions, then
    final consumer positions. Because `ExternalGeo` contributes only
    `FixParameters`, the source's solve does not depend on the recomputed
    geometry, so the source side is unaffected by the second pass. This holds
    only while the source does not transitively depend on the recomputed
    geometry's consumers; a constraint that creates such a cycle is not resolved
    by a fixed number of passes. There is no existing intra-sketch cycle check
    for this boundary.

- **Reacting during a drag:** `moveGeometries()` has no rebuild hook today.
  Real-time tracking of recomputed geometry during dragging would require adding
  one on that path (and on the edit-mode preview path in `ViewProviderSketch`);
  not tracking during drag and deferring to the next `execute()` is the
  alternative.

- **Source reference key:** positional GeoId (renumbers on edit, matches how
  constraints are stored) vs. stable `long Id` (survives edits, matches how
  `ExternalGeo` keys its sources). Deletion detection ("source no longer exists")
  differs accordingly — by index shift vs. by absence of an `Id`.

## Pointers

- `SketchObject::execute` — `SketchObject.cpp:186`
- `SketchObject::mustExecute` — `SketchObject.cpp:173`
- `SketchObject::onChanged` — `SketchObject.cpp:928`
- `SketchObject::solve` — `SketchObjectConstraints.cpp:76`
- `SketchObject::moveGeometries` — `SketchObjectOperations.cpp:47`
- `Sketch::setUpSketch` — `Sketch.cpp:193`
- `Sketch::addGeometry(geo, fixed)` — `Sketch.cpp:695`
- `Sketch::solve` — `Sketch.cpp:4842`
- `getCompleteGeometry` — `SketchObjectGeometry.cpp:1412`
- `getExternalGeometryCount` — `SketchObject.h:304`
