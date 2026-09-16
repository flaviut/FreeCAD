This is FreeCAD, a cmake + Qt + OCCT project.

You should already be in the Nix devshell.

Dependency source path: `nix eval --inputs-from . --raw nixpkgs#<nixpkgs-attribute>.src`

Building: `fc-build`
Testing: `fc-test <ctest args>`

## Qt UI validation

`fc-run` uses a maintained Qt style as the reproducible reference environment.
Set `FREECAD_QT_STYLE_OVERRIDE` to test another style.

For UI changes:

- Rely on layouts, size hints, size policies, and standard controls rather than
  theme-specific dimensions or offsets.
- Validate against the reference environment and the project's supported light
  and dark themes. Check an additional maintained platform style when the
  change depends on native styling behavior.
- Reduce style-dependent failures to a minimal example before changing
  application code. Add a compatibility workaround only when the affected
  style is supported and maintained, and document why the workaround belongs
  in the application.
- Check long translated text, keyboard navigation, and 100% and 200% display
  scaling for layout changes.

Formatting: Before completing any task that changes files, run `fc-format`.
Treefmt reports failure when it rewrites files, so rerun
`fc-format` until it passes. Review and retain the resulting formatter changes.
This repository does not use Git hooks.

When committing (only if asked):

- title convention is "type[scope]: summary"
- requires an Assisted-by: GPT-5.6 (or your model) trailer
