# External Geometry subsystem — how it works today

Factual survey of the existing `ExternalGeometry` / `ExternalGeo` subsystem:
storage, references, rebuild, flags, deletion, and change handling. Companion to
`2D_TOPO.md` (naming) and `RECOMPUTE_AND_SOLVE.md` (the solve cycle). This
documents the subsystem as it stands; it is the closest existing pattern to
"geometry recomputed from a reference" and so is a candidate template, but no
design choice is asserted here.

## The four properties involved

On `SketchObject` (`SketchObject.h`):

| Property | Type | Role |
|---|---|---|
| `ExternalGeometry` | `App::PropertyLinkSubList` | links to source objects + subelements (`(Pad, "Edge1")`) |
| `ExternalTypes` | `App::PropertyIntegerList` | per-link type: projection / intersection / both |
| `ExternalGeo` | `Part::PropertyGeometryList` | the produced `Part::Geometry` (projected/intersected); axes at idx 0/1 |
| `Geometry` | `Part::PropertyGeometryList` | internal geometry (for contrast) |

`ExternalGeometry` is the *input* (links into the document DAG). `ExternalGeo` is
the *output* (geometry living in the sketch, addressed by GeoId ≤ −3).

## Identity and bookkeeping maps

Three in-memory maps (`SketchObject.h:1216-1231`) connect references, stable Ids,
and array positions:

```cpp
std::map<std::string, std::vector<long>> externalGeoRefMap; // 1216  ref string -> stable Ids
std::vector<std::string>                 externalGeoRef;    // 1220  backup of ref strings
std::map<long, int>                      externalGeoMap;    // 1223  stable Id -> ExternalGeo index
std::map<long, int>                      geoMap;            // 1226  stable Id -> Geometry index (internal)
long                                     geoLastId;         // 1231  atomic-ish Id counter
```

Each produced geometry carries an `ExternalGeometryExtension` (accessed through
`ExternalGeometryFacade`) holding its source `Ref` string and a flag set. The
stable `long Id` is the same `Id` mechanism internal geometry uses
(`SketchGeometryExtension`), so one source link producing several curves is
expressed as one `Ref` → several `Id`s in `externalGeoRefMap`.

## Flags

`ExternalGeometryExtension::Flag` (`ExternalGeometryExtension.h:75-88`):

```cpp
enum Flag {
    Defining = 0,  // allow an external geometry to build shape
    Frozen   = 1,  // freeze an external geometry
    Detached = 2,  // signal the intention of detaching the geometry from external reference
    Missing  = 3,  // geometry with missing external reference
    Sync     = 4,  // signal the intention to synchronize a frozen geometry
    NumFlags
};
```

- `Frozen` — rebuild skips this geometry; its last projection is retained even if
  the source changes.
- `Missing` — set when the reference cannot be resolved; the geometry is kept but
  flagged rather than deleted.
- `Sync` — request to refresh a frozen geometry from its source once.
- `Defining` — whether the geometry contributes to the built shape.

## Lifecycle

### Init
`initExternalGeo()` (`SketchObjectExternal.cpp:103`) always creates the H and V
axes as the first two `ExternalGeo` entries (GeoId −1/−2). They are never deleted.

### Add
`addExternal(Obj, SubName, defining, intersection)`
(`SketchObjectExternal.cpp:735`): validates the link (same document, no circular
dependency), appends to `ExternalGeometry` + `ExternalTypes`, then calls
`rebuildExternalGeometry(...)` to produce the geometry, then `acceptGeometry()`
to sync constraint indices.

### Rebuild
`rebuildExternalGeometry(std::optional<ExternalToAdd>)`
(`SketchObjectExternal.cpp:2294`): resolves each link to a `TopoDS_Shape`,
projects or intersects it against the sketch plane (`processEdge`/`processFace`
for the various curve types; OCC section for intersection), assigns/reuses stable
`Id`s, repopulates `externalGeoMap`/`externalGeoRefMap`, copies flags across a
rebuild, and sets `Missing` for unresolved references. Called from `execute()`
(`SketchObject.cpp:200`), i.e. **before** the solve.

### Delete
`delExternal()` (`SketchObjectExternal.cpp:871`/`876`) →
`delExternalPrivate(ids, removeRef)` (`901`): maps GeoIds/Ids to `ExternalGeo`
entries, removes them (axes protected), deletes constraints that referenced them,
and removes the matching entries from `ExternalGeometry`. Related geometries (same
source `Ref`) are handled together via `externalGeoRefMap`.

### Reference repair
`updateGeometryRefs()` (`SketchObjectExternal.cpp:2797`): remaps `Ref` strings
when referenced elements are renamed (topological naming on the source object),
keeping `externalGeoRefMap`/`externalGeoRef` consistent.

## Change handling

`onChanged()` (`SketchObject.cpp:928-941`) distinguishes the two directions:

```cpp
else if (prop == &ExternalGeo && !prop->testStatus(App::Property::User3))
    onExternalGeoChanged();       // the produced geometry changed
else if (prop == &ExternalGeometry)
    onExternalGeometryChanged();  // the links changed -> updateGeometryRefs()
```

`mustExecute()` reports the sketch dirty when either `ExternalGeometry` or
`ExternalGeo` is touched (`SketchObject.cpp:179-182`).

## How this maps to the solve

Per `RECOMPUTE_AND_SOLVE.md`: `ExternalGeo` is the fixed-length tail of
`getCompleteGeometry()` (reversed), its length is `getExternalGeometryCount()`,
and `Sketch::setUpSketch` sends that tail through `addGeometry(..., fixed=true)`
so its parameters are solver constants (`FixParameters`). Constraints reference it
by negative GeoId.

## What is specific to "external" (i.e. would differ for an internal source)

Stated as facts of the current code, not as obstacles:

- The *source* of `ExternalGeo` is another `DocumentObject`, reached via
  `App::PropertyLinkSubList`. That link is what places the source upstream of the
  sketch in the document recompute DAG, and what makes "rebuild before solve"
  (`execute():200`) sufficient — the source is already final. A source that is
  internal geometry of the same sketch is not reached through a link and is not a
  separate DAG node (see `RECOMPUTE_AND_SOLVE.md`).
- `Ref` is a topological-naming string into another object; reference repair
  (`updateGeometryRefs`) is built around that. An internal source would instead be
  identified by the stable `long Id` already present on internal geometry
  (`geoMap`), and "reference lost" would mean "that `Id` is gone from `geoMap`"
  rather than an unresolved element name.
- The projection/intersection step (`processEdge`/`processFace`) is geometric
  transformation from a 3D shape onto the sketch plane. A transformation between
  two pieces of geometry already on the sketch plane is a different computation;
  what carries over is the surrounding bookkeeping (Id assignment, the maps, flag
  copy-on-rebuild, `Missing`-style handling, delete-with-constraints), not the
  projection math itself.

## Pointers

- `initExternalGeo` — `SketchObjectExternal.cpp:103`
- `addExternal` — `SketchObjectExternal.cpp:735`
- `delExternal` / `delExternalPrivate` — `SketchObjectExternal.cpp:871`, `901`
- `rebuildExternalGeometry` — `SketchObjectExternal.cpp:2294`
- `updateGeometryRefs` — `SketchObjectExternal.cpp:2797`
- bookkeeping maps — `SketchObject.h:1216-1231`
- flags — `ExternalGeometryExtension.h:75`
- `onChanged` external branches — `SketchObject.cpp:936-941`
