# FreeCAD Coin3D Render Pipeline

## Overview
FreeCAD uses **Coin3D** (an Open Inventor implementation) as its 3D scene graph engine, with **Quarter** as the Qt integration layer. There are **no custom GLSL shaders** — all shading is handled by Coin3D's built-in material and lighting system.

---

## Scene Graph Structure

The root is `SoFCUnifiedSelection` (a custom `SoSeparator`) in `View3DInventorViewer.cpp`:

```
SoFCUnifiedSelection (pcViewProviderRoot)
├─ SoTransformSeparator (threePointLightingSeparator)
│  ├─ lightRotation          ← rotates with camera
│  └─ fillLight              ← SoDirectionalLight (off by default)
├─ SoEnvironment
├─ SoSkipBoundingGroup       ← hidden anchor for transparency init
├─ SoEventCallback
├─ SoSwitch (dimensionRoot)
├─ SoSeparator (pcEditingRoot)
└─ SoGroup (objectGroup)     ← where ViewProviders add geometry
```

Plus two additional separate scene graphs:
- **backgroundroot** — orthographic camera + `SoFCBackgroundGradient` (custom gradient node)
- **foregroundroot** — orthographic camera + `BASE_COLOR` light model (no shading) for overlays

---

## Lights

Three lights are configured at init (`View3DInventorViewer.cpp` ~lines 476–495):

| Light | Type | Default | Notes |
|---|---|---|---|
| **headlight** | `SoDirectionalLight` | ON | Inherited from Quarter; camera-facing key light |
| **backlight** | `SoDirectionalLight` | off | Opposite direction of headlight; optional rim light |
| **fillLight** | `SoDirectionalLight` | off | Direction `(-0.60, -0.35, -0.79)`, intensity 0.6, slightly blue-white `(0.95, 0.95, 1.0)` |

Fill and backlight form an optional **three-point lighting** setup. The fill light lives inside a `SoTransformSeparator` with a `lightRotation` node that keeps the light direction camera-relative as the view rotates. Light settings are exposed in preferences at `User parameter:BaseApp/Preferences/View/LightSources`.

---

## Render Passes (`renderScene()`, ~lines 2500–2645)

1. **Setup** — clear color/depth buffers, configure viewport
2. **Background pass** — apply `backgroundroot` → `SoFCBackgroundGradient` draws gradient
3. **Main pass** — `inherited::actualRedraw()` via Quarter → Coin3D traverses the main scene graph using `SoBoxSelectionRenderAction` (a custom `SoGLRenderAction`); transparency mode: `SORTED_OBJECT_SORTED_TRIANGLE_BLEND`
4. **Annotation pass** — `So3DAnnotation` nodes rendered with priority ordering
5. **Foreground pass** — apply `foregroundroot` (overlays, no lighting)
6. **Post-render** — axis cross, dimension text, NaviCube, FPS counter

Depth ranges can be split (via `ENABLE_GL_DEPTH_RANGE`): background uses 10–100% of z-buffer, foreground uses 0–10%, preventing depth fighting between layers.

---

## Selection / Custom Actions

The pipeline uses several custom Coin3D actions that traverse the scene graph independently:
- `SoFCPreselectionAction` — hover highlight updates
- `SoFCSelectionAction` — selection state updates
- `SoBoxSelectionRenderAction` — the main render action, extends `SoGLRenderAction`

Custom state elements propagated through traversal: `SoGLWidgetElement`, `SoGLRenderActionElement`, `SoGLVBOActivatedElement`, `SoDevicePixelRatioElement`.

---

## Key Files

| File | Role |
|---|---|
| `src/Gui/View3DInventorViewer.cpp` | Core viewer, all of the above |
| `src/Gui/Inventor/SoFCBackgroundGradient.h` | Gradient background node |
| `src/Gui/Selection/SoFCUnifiedSelection.h` | Root selection container |
| `src/Gui/Selection/SoFCSelectionAction.h` | Custom render/selection actions |
| `src/Gui/SoFCInteractiveElement.h` | Custom Coin3D state elements |
| `src/Gui/PreferencePages/DlgSettingsLightSources.cpp` | Light settings UI |
