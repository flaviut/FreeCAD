# GUI dialog policy

FreeCAD dialogs follow a native, content-led design. The application supplies
the window relationship and semantic structure; Qt and the active platform
style supply sizing, spacing, decoration, and interaction affordances.

This policy applies to secondary top-level windows derived from `QDialog`,
including dialogs defined in Designer files and dialogs assembled in C++ or
Python. Embedded preference pages, task panels, dock widgets, and ordinary
message boxes are outside the catalog described below, although the layout and
accessibility principles still apply to them.

## Window relationship

Every dialog must have the narrowest correct parent. A dialog associated with a
document, view, or other window uses that widget as its parent. An
application-level dialog falls back to `Gui::getMainWindow()`.

The parent is not only a C++ ownership detail. On Wayland it makes the dialog an
`xdg_toplevel` transient and provides protocol-visible placement, stacking,
workspace, activation, and modal relationships. Calling `exec()` without a
parent does not provide equivalent information.

Do not compensate for a missing parent with compositor rules based on a window
title or application ID. Such rules are user overrides, not application
semantics.

## Geometry and resizing

Layouts, size hints, and size policies define dialog behavior. Explicit
geometry defines only a useful initial size; for example, 320 x 100 logical
pixels is a reasonable compact initial geometry when the content fits. Do not
increase the initial geometry to hide a broken layout.

Editors and selectors that benefit from space should grow horizontally. Action
controls and compact choices should remain at their size hint. Add stretch
after a compact group when surplus space should remain unused instead of being
distributed between related controls.

Avoid fixed pixel margins, offsets, widths, and heights unless the value models
intrinsically fixed content and the reason is documented. Minimum sizes may
protect a genuine usability constraint but must not substitute for a correct
layout.

## Content structure

Use one form row per semantic field. Each row has a label and its corresponding
editor or choice group; position alone must not explain a control. A group such
as Height/Width therefore belongs in a labeled row such as `Size by`, with the
choices kept together at the leading edge.

Prefer standard Qt controls, `QFormLayout`, and `QDialogButtonBox`. Use the
standard `QLineEdit` clear button where clearing input is useful. Avoid custom
colors, theme-like styling, bespoke replacements for standard controls, and
manual button placement that competes with the platform style.

## Keyboard, accessibility, and translation

Labels for editable fields and choice groups must have buddies. Add translated
mnemonics so keyboard users can focus the associated control. Define a logical
tab order when widget construction order does not produce one.

Give controls accessible names or descriptions when their label, role, or
state is not otherwise exposed clearly by Qt. All user-visible text must be
translatable. Layouts must tolerate long translations and must not depend on a
particular label width.

## Review checklist

A dialog conforms when all applicable statements are true:

1. It has the narrowest correct parent, with `Gui::getMainWindow()` as the
   application-level fallback.
2. Layouts and size policies, rather than fixed geometry, govern resizing.
3. Editors and selectors expand while action and choice controls keep their
   size hints.
4. Every semantic field or choice group occupies a labeled form row.
5. It uses native Qt widgets and a `QDialogButtonBox` where standard dialog
   actions are appropriate.
6. It provides buddies or equivalent keyboard focus, logical tab order,
   accessible labeling, and translation-safe text.
7. It does not rely on compositor-specific rules for application behavior.

Idiomatic construction is sufficient evidence for normal platform behavior.
Runtime checks are needed only when static inspection finds custom painting,
style-specific dimensions or workarounds, unusual window management, missing
or ambiguous parenting, or another departure from these conventions. In those
cases, test the affected behavior with `fc-run` in the reference style and the
supported light and dark themes. Add a maintained platform style when native
styling is involved, and exercise the relevant combinations of Wayland
transience, 100% and 200% scaling, long translations, keyboard-only operation,
and narrow and wide resizing.

## Catalog and audit

`GuiDialogCatalog.md` records the in-tree dialog inventory and its static policy
audit. The catalog includes top-level `QDialog` Designer forms and dialogs
declared directly in C++ or Python. It excludes generated/build output,
third-party code, templates, tests, embedded pages and panels, and calls to
standard convenience dialogs such as `QMessageBox` and `QFileDialog`.

The inventory is a maintenance aid, not a substitute for review. Dynamic Python
construction, aliases, generated types, and locally declared classes can make
static discovery incomplete. Update the catalog when adding, removing, or
materially changing a dialog.
