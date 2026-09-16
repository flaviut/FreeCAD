This is FreeCAD, a cmake + Qt + OCCT project.

You should already be in the Nix devshell.

Dependency source path: `nix eval --inputs-from . --raw nixpkgs#<nixpkgs-attribute>.src`

Building: ONLY EVER USE `fc-build <cmake build args>`
Testing: `fc-test <ctest args>`

## Git workflow

Use Git for commits, branches, and history changes.

Repository topology:

- `origin` is the upstream `FreeCAD/FreeCAD` repository and default fetch
  remote.
- `mine` is the personal fork and default push remote.
- `origin/main` is upstream trunk.
- The local `main` branch and `mine/main` are the mutable personal stack;
  local `main` is intentionally not an upstream mirror.

Inspect the personal stack with `git log --oneline origin/main..main`.
Use `git rebase -i origin/main` to edit, squash, or reorder stack commits.

To update the whole personal stack onto current upstream trunk, run
`git fetch origin`, then `git rebase origin/main main`. After a PR lands via
squash or another history-rewriting merge, use
`git rebase --onto origin/main <last-landed-local-commit> main` after fetching,
so the landed local commits are not replayed. After the rebase completes, run
`git submodule update --init --recursive` to restore the exact submodule
commits pinned by FreeCAD.

## When committing (only if asked):

- run `fc-format`. Only ever format when committing or asked.
- title convention is "type[scope]: summary"
- requires an Assisted-by: GPT-5.6 (or your model) trailer

## Testing

Do not start the GUI. Starting the GUI is infuriating to the user, as it steals
focus and cases unexpected and unwanted flashes on the screen.
