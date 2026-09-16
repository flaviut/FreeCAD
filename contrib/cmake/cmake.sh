set -e

# Non-build invocations must retain CMake's configure and discovery behavior.
if [[ ${1-} != --build || $# -lt 2 || $2 == -* ]]; then
  exec @cmake@ "$@"
fi

build_dir=$2
shift 2

cmake_args=()
native_args=()
jobs=${FREECAD_BUILD_JOBS:-@jobs@}
explicit_jobs=0
verbose=0
while (( $# )); do
  case "$1" in
    --)
      shift
      native_args=("$@")
      break
      ;;
    -j|--parallel)
      explicit_jobs=1
      jobs=""
      if [[ ${2-} =~ ^[0-9]+$ ]]; then
        jobs=$2
      fi
      ;;
    -j[0-9]*|--parallel=*)
      explicit_jobs=1
      jobs=${1#-j}
      jobs=${jobs#--parallel=}
      ;;
    -v|--verbose) verbose=1 ;;
  esac
  cmake_args+=("$1")
  shift
done
if (( ! explicit_jobs )) && [[ -n $jobs ]]; then
  cmake_args+=(--parallel "$jobs")
fi
export FREECAD_BUILD_JOBS=$jobs

if [[ -f "$build_dir/build.ninja" ]]; then
  # Ninja 1.13.2 needs explicit recompaction to recover corrupt dependency logs.
  @ninja@ -C "$build_dir" -t recompact
  quiet=1
  for arg in "${native_args[@]}"; do
    case "$arg" in
      -v|--verbose|--quiet) quiet=0 ;;
    esac
  done
  if (( quiet && ! verbose )); then
    native_args+=(--quiet)
  fi
fi

command=(@cmake@ --build "$build_dir" "${cmake_args[@]}")
if (( ${#native_args[@]} )); then
  command+=(-- "${native_args[@]}")
fi

exec @python@ @recorder@ --build-dir "$build_dir" -- "${command[@]}"
