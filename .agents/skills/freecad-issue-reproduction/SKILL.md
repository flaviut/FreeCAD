---
name: freecad-issue-reproduction
description: Reproduces FreeCAD issues with self-contained macros and checks whether they are fixed. Use for issue links or numbers, runtime confirmation, and requests for a reusable macro ZIP and FreeCAD screenshot.
---

# Reproduce a FreeCAD issue

Test the reported behavior; do not fix production code unless asked.

## 1. Establish the case

Read the issue and comments with `gh issue view <number> --repo FreeCAD/FreeCAD --comments`. Inspect attachments and existing local reproductions. Preserve supplied files; use temporary copies.

Identify the failing operation and expected result. A similar model is a control, not a replacement for the reported case. Keep deliverables under `freecad-<number>/`.

## 2. Create the macro

Write `issue-<number>.FCMacro` that runs in ordinary FreeCAD without the repository, network, or external files. Generate geometry or embed the attachment as base64 and extract it temporarily.

Exercise the reported FreeCAD feature and recompute it; do not substitute a workaround or cached shape. Assert feature status and the defining geometric behavior against an independent expectation. Shape validity alone does not prove correctness. For property-triggered bugs, check the original, changed, and restored states.

Leave the tested model visible with an informative camera and zoom. Raise on failure; leave screenshot capture and shutdown to `fc-macro`. Optional exports may use `FC_MACRO_OUTPUT`, but the macro must also run without it.

## 3. Test the full builds

Use `fc-macro` from the repository root. It builds the full selected variant, supplies Python dependencies, isolates preferences, and captures FreeCAD under Xvfb. Do not patch module paths or launch on the user's desktop.

For example, for issue 5824:

```bash
issue=5824
failed=0
for variant in occt-7_9 occt-8_0 occt-8_1; do
  nix develop ".#$variant" --command \
    fc-macro "$PWD/freecad-$issue/issue-$issue.FCMacro" \
    "$PWD/freecad-$issue/$variant" || failed=1
done
test "$failed" -eq 0
```

Inspect each `result.json` and `freecad.log`. Harness success proves only that the macro completed; its assertions must establish correctness. Record the source revision and actual FreeCAD/OCCT versions. Increase `FREECAD_MACRO_TIMEOUT` only if the operation needs more than 120 seconds.

If a check fails, distinguish a reproduction failure from a harness error before drawing a conclusion.

## 4. Verify and deliver artifacts

Open the screenshots with the image-reading tool. Confirm the intended model is visible, without dialogs or obscuring panels. Use geometry assertions for invisible defects such as filled cavities.

Create `issue-<number>-macro.zip` containing only the self-contained macro. Extract it into a fresh directory and rerun it to check independence from working files.

Report the verdict, per-version results, decisive checks, and artifact paths. If fixed, supply the ZIP and an inspected screenshot of the correct model. If broken, label any screenshot as a failure reproduction. If blocked, report the blocker instead of claiming fixed or broken. A local pass does not establish an upstream fix.

When evaluating changes to this skill, use [the evaluation cases](evaluations.md).
