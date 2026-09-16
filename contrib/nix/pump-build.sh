set -e

ssh=(@ssh@ -o BatchMode=yes -o ConnectTimeout=5)
workers=()
roots=()
release() {
    for i in "${!roots[@]}"; do
        "${ssh[@]}" "${workers[$i]}" \
            "rm -f '${roots[$i]}/inputs'; rmdir '${roots[$i]}'" || true
    done
}
trap release EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

# Provision every pump worker before exposing its store to the include server.
hosts=$(@distcc@ --show-hosts)
while IFS= read -r spec; do
    [[ $spec == localhost/* || $spec != *,cpp* ]] && continue

    worker=${spec%%/*}
    worker=${worker%%,*}
    worker=${worker#@}
    worker=${worker%%:*}
    if [[ $worker == 192.168.86.244 ]]; then
        worker=flaviu@$worker
    fi

    # Development outputs are unsigned; SSH authenticates the transfer.
    NIX_SSHOPTS="${NIX_SSHOPTS:-} -o BatchMode=yes -o ConnectTimeout=5" \
        @nix@ copy --no-check-sigs --to "ssh-ng://$worker" @inputs@

    root=$("${ssh[@]}" "$worker" sh -s -- @inputs@ <<'SH'
set -eu
root=$(mktemp -d /tmp/freecad-pump.XXXXXXXX)
trap 'rmdir "$root"' EXIT
nix-store --add-root "$root/inputs" --indirect --realise "$1" >/dev/null
trap - EXIT
printf '%s\n' "$root"
SH
    )
    workers+=("$worker")
    roots+=("$root")
done <<< "$hosts"

# Only immutable dependencies use the worker's store; checkout files still travel.
export DISTCC_PREINSTALLED_DIRS=/nix/store
@pump@ "$@"
