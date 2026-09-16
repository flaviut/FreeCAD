# Normalize checkout paths without changing the shell or Qt tools.
build_dir=$PWD
while [[ ! -f "$build_dir/CMakeCache.txt" && $build_dir != / ]]; do
    build_dir=$(dirname "$build_dir")
done

source_dir=""
if [[ -f "$build_dir/CMakeCache.txt" ]]; then
    while IFS= read -r entry; do
        case "$entry" in
            CMAKE_HOME_DIRECTORY:INTERNAL=*) source_dir=${entry#*=}; break ;;
        esac
    done < "$build_dir/CMakeCache.txt"
fi

if [[ -n $source_dir ]]; then
    export CCACHE_BASEDIR="${CCACHE_BASEDIR:-$source_dir}"
    set -- "$1" "-fdebug-prefix-map=$source_dir=." "${@:2}"
fi

if [[ -n ${INCLUDE_SERVER_PORT:-} ]]; then
    # Pump must see dependency flags normally hidden inside the Nix compiler wrapper.
    read -r -a flags <<< "${NIX_CFLAGS_COMPILE:-}"
    set -- "$@" "${flags[@]}"
fi

if [[ -z ${CCACHE_LOG_DIR:-} ]]; then
    exec @ccache@ "$@"
fi

log=$(mktemp "$CCACHE_LOG_DIR/XXXXXX.log.zst") || exit 1

# Compress each compiler's log before it reaches disk.
exec 3> >(@zstd@ -q -3 -c > "$log")
compressor=$!

unset CCACHE_DEBUG
CCACHE_NODEBUG=1 CCACHE_LOGFILE=/dev/fd/3 @ccache@ "$@"
status=$?

exec 3>&-
wait "$compressor" || exit 1
exit "$status"
