#!/usr/bin/env bash

set -euo pipefail

repo_root=$(git rev-parse --show-toplevel)
optional_provenance=c379af213c5ac5e9aa212547a964a6a7f97fbcc2
indirect_provenance=422cfd282d8c7cbddcb7db594d42c782f0345481
benchmark_base=$(git rev-parse "$optional_provenance^")
benchmark_runs=${BENCHMARK_RUNS:-10}
result_dir=${BENCHMARK_OUTPUT_DIR:-/tmp/freecad-vcs-provenance-benchmark}
script_path=${BENCHMARK_RUNNER_PATH:-$repo_root/tools/profile/benchmark-vcs-provenance.sh}

cd "$repo_root"

setup_state() {
    local state=$1

    git reset --hard "$benchmark_base" >/dev/null
    case "$state" in
        baseline)
            ;;
        c379af2)
            git cherry-pick "$optional_provenance" >/dev/null
            ;;
        422cfd2)
            git cherry-pick "$indirect_provenance" >/dev/null
            ;;
        combined)
            git cherry-pick "$optional_provenance" >/dev/null
            git cherry-pick "$indirect_provenance" >/dev/null
            ;;
        *)
            echo "Unknown benchmark state: $state" >&2
            exit 2
            ;;
    esac
    fc-build >/dev/null
}

run_benchmark() {
    local scenario=$1

    case "$scenario" in
        empty)
            git commit --allow-empty -m "benchmark revision change" >/dev/null
            ;;
        source)
            perl -pi -e \
                'if (/autoRecompute = hGrp/) { s/const bool/bool/ || s/bool/const bool/ }' \
                src/Mod/Sketcher/Gui/Utils.cpp
            git add src/Mod/Sketcher/Gui/Utils.cpp
            git commit -m "benchmark Sketcher source change" >/dev/null
            ;;
        *)
            echo "Unknown benchmark scenario: $scenario" >&2
            exit 2
            ;;
    esac
    fc-build
}

conclude_state() {
    git reset --hard "$benchmark_base" >/dev/null
}

run_suite() {
    local scenario=$1

    hyperfine --runs "$benchmark_runs" --sort command \
        --parameter-list state baseline,c379af2,422cfd2,combined \
        --setup "$script_path setup {state}" \
        --cleanup "$script_path conclude" \
        --command-name "{state}" "$script_path run $scenario" \
        --export-json "$result_dir/$scenario.json" \
        --export-markdown "$result_dir/$scenario.md"
}

restore_checkout() {
    if [[ ${checkout_restored:-false} == true ]]; then
        return
    fi
    checkout_restored=true
    trap - EXIT INT TERM HUP
    git reset --hard "$benchmark_base" >/dev/null 2>&1 || true
    if [[ -n $original_branch ]]; then
        git switch "$original_branch" >/dev/null 2>&1 || true
    else
        git switch --detach "$original_head" >/dev/null 2>&1 || true
    fi
    if [[ -n ${runner_dir:-} && -d $runner_dir ]]; then
        rm -r -- "$runner_dir"
    fi
}

handle_signal() {
    local status=$1
    restore_checkout
    exit "$status"
}

run_all() {
    command -v fc-build >/dev/null || {
        echo "fc-build is unavailable; enter the FreeCAD development shell first." >&2
        exit 1
    }
    command -v hyperfine >/dev/null || {
        echo "hyperfine is unavailable; install it or run nix shell nixpkgs#hyperfine." >&2
        exit 1
    }
    if ! git diff --quiet || ! git diff --cached --quiet; then
        echo "Refusing to benchmark with tracked or staged changes in the checkout." >&2
        exit 1
    fi
    git cat-file -e "$optional_provenance^{commit}"
    if ! git cat-file -e "$indirect_provenance^{commit}" 2>/dev/null; then
        git fetch origin refs/pull/32673/head
    fi

    original_branch=$(git branch --show-current)
    original_head=$(git rev-parse HEAD)
    export original_branch original_head
    trap restore_checkout EXIT
    trap 'handle_signal 130' INT
    trap 'handle_signal 143' TERM
    trap 'handle_signal 129' HUP

    mkdir -p "$result_dir"
    runner_dir=$(mktemp -d)
    cp "$script_path" "$runner_dir/benchmark-vcs-provenance.sh"
    script_path=$runner_dir/benchmark-vcs-provenance.sh
    export BENCHMARK_RUNNER_PATH=$script_path
    git switch --detach "$benchmark_base" >/dev/null

    echo "=== Empty commit ==="
    run_suite empty
    echo
    echo "=== Minimal Utils.cpp change ==="
    run_suite source
    echo
    echo "Results: $result_dir"
}

case "${1:-all}" in
    all)
        run_all
        ;;
    setup)
        setup_state "$2"
        ;;
    run)
        run_benchmark "$2"
        ;;
    conclude)
        conclude_state
        ;;
    *)
        echo "Usage: $0 {all|setup STATE|run SCENARIO|conclude}" >&2
        exit 2
        ;;
esac
