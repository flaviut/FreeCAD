# FreeCAD Viewport Renderer: Comparison with Major CAD Programs

## FreeCAD (Coin3D / Open Inventor)
- **API**: OpenGL via Coin3D scene graph
- **Shaders**: None authored by FreeCAD — Coin3D generates fixed-function-style shading internally
- **Lights**: Camera-tracked directional lights (headlight always on, fill/back optional)
- **Architecture**: Scene graph traversal with custom actions for selection; separate scene graphs for background/foreground layers

---

## Blender (Workbench / EEVEE / Cycles)
- **Much more sophisticated**. The default **Workbench** viewport (closest analog to FreeCAD's use case) uses hand-written GLSL shaders with a deferred-like multi-pass pipeline: geometry pass → shadow pass → composite pass. Matcap shading is a single-pass trick that encodes lighting into a spherical texture lookup.
- **EEVEE** is a full PBR rasterizer: screen-space reflections, bloom, depth of field, volumetrics — all GLSL shader passes managed by a `DrawManager` abstraction.
- **Lights**: Scene lights are real scene objects; Workbench uses studio presets (HDRI-like sphere maps). FreeCAD's headlight has no analog in a default Blender scene.
- **Key difference**: Blender writes and ships its own shaders. FreeCAD delegates entirely to Coin3D.

---

## Autodesk Inventor / Fusion 360
- Uses a **proprietary DX11/OpenGL abstraction** (not a public scene graph). Fusion 360 moved to a custom GPU renderer with PBR materials, real-time ambient occlusion (SSAO), and environment lighting via HDRI.
- **Lights**: Default is an environment light (HDRI dome), not a headlight. Physical light falloff.
- **Shaders**: Full GLSL/HLSL PBR shader pipeline with roughness/metalness workflow.
- **Key difference**: FreeCAD's flat directional headlight looks "CAD-simple" precisely because Inventor/Fusion default to environment-based soft lighting that makes parts look photographic.

---

## SolidWorks
- Historically used **OpenGL with fixed-function** shading (similar vintage to FreeCAD's approach), but modern versions use a custom **RealView** renderer with per-pixel lighting, reflections, and ambient occlusion — hardware-dependent, requires certified Quadro/FirePro cards to enable.
- **Lights**: Directional + ambient by default; RealView adds HDRI environment maps.
- **Key difference**: SolidWorks' baseline (non-RealView) is architecturally the closest to FreeCAD — both descend from the era of fixed-function OpenGL CAD viewports.

---

## CATIA (V5 / V6 / 3DExperience)
- V5 uses a scene graph architecture (descended from the same Open Inventor lineage as Coin3D — CATIA's VPM/ENOVIA uses SGM, a proprietary scene graph). Lighting is similarly directional + ambient, though V5 has optional ambient occlusion passes.
- **3DExperience** platform moved to a WebGL2/GPU-accelerated pipeline with PBR shading.
- **Key difference**: FreeCAD and CATIA V5 are the most architecturally similar of this group — both rooted in the Open Inventor tradition.

---

## Rhino 3D (Rhino 8 / OpenNURBS)
- Uses a custom **OpenGL 3.3 core profile** renderer called **Rhino Display Pipeline** with hand-written GLSL. Shader programs are loaded from `.glsl` files and compiled at runtime.
- Supports display modes (Wireframe, Shaded, Rendered, Arctic, etc.) where each mode is a different shader configuration.
- **Lights**: Supports up to 8 scene lights plus a directional sun light and a skylight (ambient dome). Default Shaded mode uses a two-light setup (key + fill), similar to FreeCAD's three-point system but enabled by default.
- **Key difference**: Rhino's display pipeline is the most similar architecturally to what FreeCAD *could* evolve toward — it's a scene graph + explicit GLSL approach, but with shaders actually authored by the app team.

---

## Summary Table

| Program | Render API | Shaders | Default Lighting | Selection |
|---|---|---|---|---|
| **FreeCAD** | OpenGL via Coin3D | None (Coin3D internal) | 1 directional headlight | Custom Coin3D actions |
| **Blender Workbench** | OpenGL/Vulkan | Hand-written GLSL | Studio HDRI preset | GPU picking |
| **Fusion 360** | DX11/OpenGL PBR | GLSL/HLSL PBR | HDRI environment | Proprietary |
| **SolidWorks** | OpenGL (RealView optional) | Fixed-func / RealView GLSL | Directional + ambient | Proprietary |
| **CATIA V5** | Open Inventor lineage | Fixed-function | Directional + ambient | Scene graph actions |
| **Rhino 8** | OpenGL 3.3 core | Explicit GLSL files | 2-light key+fill | GPU picking + display pipeline |

---

## Bottom Line

FreeCAD's approach is the most "retro" of the group — it inherits 1990s Open Inventor conventions and adds no shaders of its own. This is why the viewport looks flat compared to modern CAD tools. The biggest gap is the absence of environment lighting (HDRI), ambient occlusion, and PBR materials, all of which the commercial tools now consider baseline.
