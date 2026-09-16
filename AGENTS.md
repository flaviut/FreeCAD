This is FreeCAD, a cmake + Qt + OCCT project.

You should already be in the Nix devshell.

Dependency source path: `nix eval --inputs-from . --raw nixpkgs#<nixpkgs-attribute>.src`

Building: ONLY EVER USE `fc-build <cmake build args>`
Testing: `fc-test <ctest args>`

## Jujutsu workflow

This is a colocated Jujutsu/Git repository. Use `jj` for commit, bookmark, and
history mutations. Read-only Git commands remain safe, but avoid mixing
mutating Git commands into the Jujutsu workflow.

Repository topology:

- `origin` is the upstream `FreeCAD/FreeCAD` repository and default fetch
  remote.
- `mine` is the personal fork and default push remote.
- `main@origin` is immutable upstream trunk.
- The local `main` bookmark and `main@mine` are the mutable personal stack;
  local `main` is intentionally not an upstream mirror.

Inspect the personal stack with `jj log -r 'main@origin..main'`. Prefer stable
Jujutsu change IDs when editing or rebasing commits. Bookmarks do not advance
automatically; move `main` or a PR bookmark explicitly after adding a change.

Use normal Jujutsu commands directly, for example `jj edit <change-id>`,
`jj new`, `jj squash`, and `jj split`. Jujutsu automatically rebases descendant
changes after an earlier change is rewritten.

To update the whole personal stack onto current upstream trunk, run
`fc-jj-update`. After a PR lands via squash or another history-rewriting merge,
run `fc-jj-update <first-unmerged-change-id>` so the landed local commit is not
replayed. The helper fetches `origin`, rebases, and only then restores the exact
submodule commits pinned by FreeCAD.

## When committing (only if asked):

- run `fc-format`. Only ever format when committing or asked.
- title convention is "type[scope]: summary"
- requires an Assisted-by: GPT-5.6 (or your model) trailer

## Testing

Do not start the GUI. Starting the GUI is infuriating to the user, as it steals
focus and cases unexpected and unwanted flashes on the screen.
