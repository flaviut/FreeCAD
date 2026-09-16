export CCACHE_LOG_DIR="$NIX_BUILD_TOP/ccache-log/objects"
export CCACHE_STATSLOG="$NIX_BUILD_TOP/ccache-log/stats.log"
mkdir -p "$CCACHE_LOG_DIR" "$buildLog"

ccache --show-config > "$NIX_BUILD_TOP/ccache-log/config.txt"
env | sort > "$NIX_BUILD_TOP/ccache-log/environment.txt"
printf '%s\n' "$out" > "$NIX_BUILD_TOP/ccache-log/output.txt"
printf 'ccache logs: %s\n' "$NIX_BUILD_TOP/ccache-log"

cacheReport() {
    if [[ ! -f "$CCACHE_STATSLOG" ]]; then
        echo 'No ccache calls recorded.'
        return
    fi

    ccache --show-log-stats --verbose > "$NIX_BUILD_TOP/ccache-log/summary.txt"
    cat "$NIX_BUILD_TOP/ccache-log/summary.txt"
}

cacheConfig() {
    if [[ -f CMakeCache.txt ]]; then
        cp CMakeCache.txt "$NIX_BUILD_TOP/ccache-log/"
    fi
}

cacheSave() {
    cacheReport
    cp -R "$NIX_BUILD_TOP/ccache-log/." "$buildLog/"
    printf 'ccache logs saved: %s\n' "$buildLog"
}

postConfigureHooks+=(cacheConfig)
failureHooks+=(cacheReport)
postFixupHooks+=(cacheSave)
