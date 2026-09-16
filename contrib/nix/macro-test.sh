if (( $# < 1 || $# > 2 )); then
  echo "Usage: fc-macro MACRO [OUTPUT_DIR]" >&2
  exit 2
fi

macro="$(realpath -e "$1")"
if [[ ! -f "$macro" ]]; then
  echo "Not a macro file: $macro" >&2
  exit 2
fi

output="${2:-$(mktemp -d -t freecad-macro-XXXXXXXX)}"
mkdir -p "$output"
output="$(realpath "$output")"
work="$(mktemp -d -t freecad-macro-run-XXXXXXXX)"
trap 'rm -rf "$work"' EXIT

export FC_MACRO_FILE="$macro"
export FC_MACRO_OUTPUT="$output"
export QT_QPA_PLATFORM=xcb
export QT_STYLE_OVERRIDE=Fusion
export QT_USE_PORTAL=0
export LIBGL_ALWAYS_SOFTWARE=1
export COIN_GL_NO_CURRENT_CONTEXT_CHECK=1

# Keep desktop preferences and startup macros out of the test process.
export XDG_CONFIG_HOME="$work/config"
export XDG_DATA_HOME="$work/data"
mkdir -p "$XDG_CONFIG_HOME" "$XDG_DATA_HOME"
cp @runner@ "$work/run.FCMacro"
rm -f "$output/result.json" "$output/screenshot.png"

@build@
printf 'Artifacts: %s\n' "$output"
status=0
timeout --kill-after=5s "${FREECAD_MACRO_TIMEOUT:-120}s" \
  xvfb-run -a -s '-screen 0 1440x1000x24 -nolisten tcp' \
  @run@ --user-cfg "$work/user.cfg" --system-cfg "$work/system.cfg" \
  "$work/run.FCMacro" > "$output/freecad.log" 2>&1 || status=$?

if (( status != 0 )); then
  tail -n 40 "$output/freecad.log" >&2
  exit "$status"
fi

# A clean process exit alone does not prove that the macro ran to completion.
@python@ - "$output/result.json" <<'PY'
import json
import sys

with open(sys.argv[1]) as stream:
    result = json.load(stream)

if not result["success"]:
    print(result["error"], file=sys.stderr)
    sys.exit(1)
PY
