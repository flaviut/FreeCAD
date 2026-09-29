#!/usr/bin/env python3
"""Measure one fc-build invocation and archive its changed compiler traces."""

import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
BUILD = ROOT / "build/clang-profile"
PROVENANCE = OUT / "provenance"


def ninja_entries():
    path = BUILD / ".ninja_log"
    return {
        parts[3]: line
        for line in path.read_text().splitlines()
        if not line.startswith("#") and len(parts := line.split("\t")) >= 4
    }


def memory_kib(root_pid):
    processes = {}
    for entry in Path("/proc").iterdir():
        if not entry.name.isdecimal():
            continue
        try:
            status = (entry / "status").read_text().splitlines()
            fields = dict(line.split(":", 1) for line in status if ":" in line)
            ppid = int(fields["PPid"].strip())
            rss = int(fields.get("VmRSS", "0 kB").split()[0])
            processes[int(entry.name)] = (ppid, rss)
        except (OSError, ValueError, KeyError):
            continue
    family = {root_pid}
    changed = True
    while changed:
        old = len(family)
        family.update(pid for pid, (ppid, _) in processes.items() if ppid in family)
        changed = len(family) != old
    rss_values = [rss for pid, (_, rss) in processes.items() if pid in family]
    return sum(rss_values), max(rss_values, default=0)


def main():
    label, *targets = sys.argv[1:]
    PROVENANCE.mkdir(exist_ok=True)
    command = ["fc-build", *(["--target", *targets] if targets else [])]
    env = os.environ | {
        "FREECAD_BUILD_DIR": str(BUILD),
        "FREECAD_BUILD_JOBS": "8",
    }
    before = ninja_entries()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    start = time.monotonic()
    max_aggregate = max_process = 0
    with (PROVENANCE / f"{label}.log").open("w") as stream:
        process = subprocess.Popen(command, cwd=ROOT, env=env, stdout=stream,
                                   stderr=subprocess.STDOUT)
        while process.poll() is None:
            aggregate, child = memory_kib(process.pid)
            max_aggregate = max(max_aggregate, aggregate)
            max_process = max(max_process, child)
            time.sleep(0.1)
        elapsed = time.monotonic() - start
    after = ninja_entries()
    changed = {output: line for output, line in after.items() if before.get(output) != line}
    dataset = PROVENANCE / label
    dataset.mkdir(exist_ok=True)
    (dataset / ".ninja_log").write_text("# ninja log v5\n" + "\n".join(changed.values()) + "\n")
    compiler_outputs = []
    traced_outputs = []
    for output in changed:
        artifact = BUILD / output
        if output.endswith(".o"):
            trace = Path(str(artifact)[:-1] + "json")
        elif output.endswith(".pch"):
            trace = artifact.with_suffix(".json")
        else:
            continue
        compiler_outputs.append(output)
        if trace.is_file():
            dest = dataset / trace.relative_to(BUILD)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(trace, dest)
            traced_outputs.append(output)
    metrics = {
        "label": label,
        "command": command,
        "started_utc": started,
        "elapsed_s": elapsed,
        "exit_code": process.returncode,
        "jobs": 8,
        "changed_ninja_outputs": len(changed),
        "compiler_outputs": len(compiler_outputs),
        "traced_compiler_outputs": len(traced_outputs),
        "missing_traces": sorted(set(compiler_outputs) - set(traced_outputs)),
        "peak_sampled_descendant_rss_kib": max_aggregate,
        "peak_sampled_single_process_rss_kib": max_process,
        "memory_note": "RSS sampled at 0.1 s intervals for fc-build and descendants; aggregate is concurrent process RSS and may double count shared pages.",
    }
    (OUT / f"{label}-metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    print(json.dumps(metrics, indent=2), flush=True)
    return process.returncode


if __name__ == "__main__":
    sys.exit(main())
