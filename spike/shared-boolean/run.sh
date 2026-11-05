#!/usr/bin/env bash
# Reproduce one baseline and one candidate; never launches FreeCAD or its GUI.
set -euo pipefail
repo=$(cd "$(dirname "$0")/../.." && pwd)
out=/home/user/tmp/freecad-33687/spikes/shared-boolean
wrapper=/home/user/tmp/freecad-33687/spikes/run-limited.py
mkdir -p "$out"
export FREECAD_BUILD_DIR="$out/build"
cmake -S "$repo/spike/shared-boolean" -B "$FREECAD_BUILD_DIR" -G Ninja -DCMAKE_BUILD_TYPE=Release 2>&1 | tee "$out/configure.log"
python "$wrapper" build shared-boolean-build fc-build --target shared-boolean 2>&1 | tee "$out/build.log"
python "$wrapper" probe shared-boolean-baseline fc-test -V -R '^shared-boolean-baseline$' 2>&1 | tee "$out/baseline.log"
python "$wrapper" probe shared-boolean-candidate fc-test -V -R '^shared-boolean-candidate$' 2>&1 | tee "$out/candidate.log"
