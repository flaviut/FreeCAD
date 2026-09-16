#!/usr/bin/env python3
"""Analyze record-build.py captures without consulting the live build tree."""

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
import heapq
import json
import math
from pathlib import Path
import posixpath
import re
import sys


US = 1_000_000
PSI_KEYS = [f"{resource} {kind}" for resource in ("cpu", "memory", "io")
            for kind in ("some", "full")]
CPU_BUSY = {"user", "nice", "system", "irq", "softirq", "steal"}
FAILURE = re.compile(r"^FAILED:\s*(?:\[code=(-?\d+)\]\s*)?(.*)")
KILL = re.compile(r"Killed signal terminated program cc1plus\b")
NUMBER = r"\d+(?:\.\d+)?"


def read_json(path, default):
    return json.loads(path.read_text()) if path.is_file() else default


def read_jsonl(path):
    if not path.is_file():
        return
    with path.open() as stream:
        for number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as error:
                # An interrupted recorder can leave one partial final record.
                if line.endswith("\n"):
                    raise ValueError(f"{path}:{number}: {error}") from error
                print(f"Ignoring partial final record: {path}:{number}", file=sys.stderr)


def utc_us(value):
    if value is None:
        return None
    date = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if date.tzinfo is None:
        raise ValueError(f"UTC timestamp has no offset: {value}")
    return round(date.timestamp() * US)


def micros(value):
    return round(value * US) if value is not None else None


def numeric(values):
    return {key: value for key, value in values.items()
            if type(value) in (int, float) and math.isfinite(value)}


def meta(pid, tid, kind, name):
    return {"ph": "M", "pid": pid, "tid": tid, "name": kind, "args": {"name": name}}


def event(pid, tid, category, name, ts, args, dur=None):
    result = {"pid": pid, "tid": tid, "cat": category, "name": name, "ts": ts, "args": args}
    if dur is None:
        return dict(result, ph="i", s="t")
    return dict(result, ph="X", dur=dur)


@dataclass
class Step:
    start: int
    end: int
    hash: str
    raw: list
    outputs: list
    reports: list = field(default_factory=list)
    cache: list = field(default_factory=list)
    identity: str = "single normalized output"

    @property
    def name(self):
        return self.outputs[0]

    @property
    def object(self):
        return any(path.endswith((".o", ".obj")) for path in self.outputs)


def ninja_groups(folder):
    run = folder / "run.ninja_log"
    groups = defaultdict(list)
    if run.is_file():
        # The recorder already subtracts the before log, including after compaction.
        with run.open(errors="surrogateescape") as stream:
            for number, line in enumerate(stream, 1):
                if line.startswith("# ninja log ") or not line.strip():
                    continue
                fields = line.rstrip("\n").split("\t")
                if len(fields) != 5:
                    if not line.endswith("\n"):
                        break
                    raise ValueError(f"{run}:{number}: invalid Ninja row")
                start, end, _, output, command = fields
                groups[int(start), int(end), command].append(output)
        return groups, run.name

    steps = folder / "steps.jsonl"
    for row in read_jsonl(steps):
        groups[row["start_ms"], row["end_ms"], row["command_hash"]].extend(row["outputs"])
    return groups, steps.name if steps.is_file() else None


def make_steps(folder, normalize):
    groups, source = ninja_groups(folder)
    manifest = defaultdict(set)
    for index, edge in enumerate(read_jsonl(folder / "manifest-edges.jsonl")):
        for output in edge["outputs"]:
            manifest[normalize(output)].add(index)

    steps = []
    for (start, end, command), raw in sorted(groups.items()):
        if not raw or start < 0 or end < start:
            raise ValueError(f"{folder}: invalid Ninja group at {start}–{end} ms")
        outputs = list(dict.fromkeys(map(normalize, raw)))
        partitions = defaultdict(list)
        if len(outputs) > 1 and all(len(manifest[path]) == 1 for path in outputs):
            for path in raw:
                partitions[next(iter(manifest[normalize(path)]))].append(path)
        else:
            partitions[None] = raw

        for edge, paths in partitions.items():
            outputs = list(dict.fromkeys(map(normalize, paths)))
            step = Step(start, end, command, paths, outputs)
            if edge is not None:
                step.identity = "archived manifest edge"
            elif len(outputs) > 1:
                step.identity = "unresolved multi-output Ninja group"
            steps.append(step)

    return steps, source


def tool_stats(kind, text):
    if kind == "gcc":
        lines = text.splitlines()
        wall_column = lines[0].split().index("wall") - 2 if lines and "wall" in lines[0].split() else None
        if wall_column is None:
            return {}
        values = {}
        for line in lines[1:]:
            match = re.match(r"\s*(.*?)\s+:\s*(.*)", line)
            if not match:
                continue
            name, columns = match.groups()
            # Remove percent annotations before indexing the header's time columns.
            columns = re.sub(r"\([^)]*\)", "", columns).split()
            if len(columns) > wall_column and re.fullmatch(NUMBER, columns[wall_column]):
                values[name] = float(columns[wall_column])
        return {"wall_s_by_row": values}

    if kind == "gnu-ld":
        pattern = re.compile(rf"^Stats: (.+?)\s+(\d+)\s+(\d+)\s+({NUMBER})\s+({NUMBER})\s+(\d+)\s*$")
        rows = {}
        for line in text.splitlines():
            match = pattern.fullmatch(line)
            if match:
                name, cpu, rss, user, system, memory = match.groups()
                rows[name.strip()] = {"cpu_us": int(cpu), "rss_kib": int(rss),
                                      "user_s": float(user), "system_s": float(system),
                                      "memory_kib": int(memory)}
        return {"stats_by_row": rows}

    return {}


def read_failures(folder):
    failures = {}
    orphan_kills = 0
    no_work = False
    log = folder / "build.log"
    if log.is_file():
        current = None
        with log.open(errors="replace") as stream:
            for number, line in enumerate(stream, 1):
                line = line.strip()
                match = FAILURE.match(line)
                if match:
                    code, target = match.groups()
                    current = {"line_number": number, "target": target,
                               "exit_code": int(code) if code is not None else None,
                               "cc1plus_killed": False}
                    failures[number] = current
                elif line.startswith("ninja: no work to do."):
                    no_work = True
                    current = None
                elif line.startswith(("ninja:", "[")):
                    current = None
                elif KILL.search(line):
                    if current is None:
                        orphan_kills += 1
                    else:
                        current["cc1plus_killed"] = True

    for row in read_jsonl(folder / "failures.jsonl"):
        # The timestamp denotes log receipt, not the command's finish time.
        key = row.get("line_number", -len(failures) - 1)
        failures.setdefault(key, {}).update(row)
    known = log.is_file() or (folder / "failures.jsonl").is_file()
    return list(failures.values()), orphan_kills, known, no_work


def deltas(before, after, key):
    left, right = numeric(before.get(key, {})), numeric(after.get(key, {}))
    return {name: right[name] - value for name, value in left.items() if name in right}


def host_data(samples, pid, build_start, build_duration):
    events, anomalies, build_samples = [], [], []
    psi_us, psi_span, swap = Counter(), Counter(), Counter()
    busy, cpu_total = 0, 0
    previous = None
    for sample in samples:
        ts = micros(sample["monotonic_s"])
        inside = (build_start is not None and build_duration is not None
                  and build_start <= ts <= build_start + build_duration)
        if inside:
            build_samples.append(sample)
        values = {"Host memory (KiB)": numeric(sample.get("memory_kib", {})),
                  "Host swap (cumulative pages)": numeric(sample.get("vmstat", {}))}
        if previous is not None:
            old, old_ts, old_inside = previous
            span = ts - old_ts
            if span <= 0:
                anomalies.append({"monotonic_us": ts, "metric": "non-increasing sample time"})
            else:
                for key in ("pressure_us", "cpu_ticks", "vmstat"):
                    diff = deltas(old, sample, key)
                    for name in [name for name in diff if diff[name] < 0]:
                        anomalies.append({"monotonic_us": ts, "metric": f"{key}: {name} reset"})
                        del diff[name]
                    if key == "pressure_us":
                        rates = {name: delta * 100 / span for name, delta in diff.items()}
                        values["Host PSI (%)"] = rates
                        for name, rate in rates.items():
                            if rate > 100:
                                anomalies.append({"monotonic_us": ts, "span_us": span,
                                                  "metric": name, "percent": rate})
                        if inside and old_inside:
                            psi_us.update(diff)
                            psi_span.update({name: span for name in diff})
                    elif key == "cpu_ticks" and CPU_BUSY | {"idle", "iowait"} <= diff.keys():
                        total = sum(diff.values())
                        if total > 0:
                            values["Host CPU (%)"] = {name: delta * 100 / total
                                                       for name, delta in diff.items()}
                            if inside and old_inside:
                                busy += sum(diff[name] for name in CPU_BUSY)
                                cpu_total += total
                    elif key == "vmstat" and inside and old_inside:
                        swap.update(diff)

        for name, counters in values.items():
            if counters:
                events.append({"ph": "C", "pid": pid, "tid": 0, "cat": "host", "name": name,
                               "ts": ts, "args": counters})
        previous = sample, ts, inside

    memory = [numeric(sample.get("memory_kib", {})) for sample in build_samples]
    available = [row["MemAvailable"] for row in memory if "MemAvailable" in row]
    swap_used = [row["SwapTotal"] - row["SwapFree"] for row in memory
                 if {"SwapTotal", "SwapFree"} <= row.keys()]
    stats = {"samples": len(samples), "build_samples": len(build_samples),
             "min_available_kib": min(available, default=None),
             "max_swap_used_kib": max(swap_used, default=None),
             "busy_pct": 100 * busy / cpu_total if cpu_total else None,
             "psi_pct": {name: 100 * psi_us[name] / time for name, time in psi_span.items()},
             "psi_delta_us": dict(psi_us), "psi_window_us": dict(psi_span),
             "swap_pages": dict(swap), "anomalies": anomalies}
    return events, stats


class Attempt:
    def __init__(self, folder, number):
        self.folder = folder
        self.number = number
        self.info = read_json(folder / "build.json", {})
        self.build_dir = self.info.get("build_dir")
        self.build_start = micros(self.info.get("build_start_monotonic_s"))
        self.ninja_start = micros(self.info.get("ninja_start_monotonic_s"))
        self.build_duration = micros(self.info.get("elapsed_s"))
        self.capture_duration = micros(self.info.get("capture_elapsed_s"))
        self.utc = utc_us(self.info.get("capture_started_utc"))
        self.boot = self.info.get("boot_id")
        self.steps, self.source = make_steps(folder, self.normalize)
        self.index = defaultdict(list)
        for index, step in enumerate(self.steps):
            for output in step.outputs:
                self.index[output].append(index)
        self.failures, self.orphan_kills, self.failure_log, self.no_work = read_failures(folder)
        self.samples = list(read_jsonl(folder / "host.jsonl"))
        if not any(folder.joinpath(name).is_file() for name in (
                "build.json", "build.log", "host.jsonl", "steps.jsonl", "run.ninja_log", "failures.jsonl")):
            raise ValueError(f"{folder}: no capture files")
        self.capture_start, self.origin = self.find_origin()
        self.lifecycle_start = self.capture_start
        if (self.lifecycle_start is None and self.utc is not None and not self.samples
                and self.build_start is None and self.ninja_start is None
                and not any(row.get("received_monotonic_s") is not None for row in self.failures)):
            self.lifecycle_start = 0
            self.origin = "capture-local origin; no monotonic reference"
        self.events, self.host = host_data(self.samples, number * 2, self.build_start,
                                          self.build_duration)
        self.join_counts = Counter()
        self.unassigned = []
        self.read_reports()
        self.peak = self.add_steps()
        self.add_lifecycle()
        stamps = [(item["ts"], item["ts"] + item.get("dur", 0))
                  for item in self.events if "ts" in item]
        self.first = min(begin for begin, _ in stamps)
        self.last = max(end for _, end in stamps)
        self.has_monotonic = not self.local_ninja and (
            bool(self.samples) or any(value is not None for value in (
                self.capture_start, self.build_start, self.ninja_start)))

    def normalize(self, path):
        # Lexical normalization only: symlink outputs are distinct Ninja edges.
        if not self.build_dir:
            return posixpath.normpath(path)
        absolute = posixpath.normpath(posixpath.join(self.build_dir, path))
        prefix = posixpath.normpath(self.build_dir).rstrip("/") + "/"
        return absolute[len(prefix):] if absolute.startswith(prefix) else absolute

    def find_origin(self):
        saved = micros(self.info.get("capture_start_monotonic_s"))
        if saved is not None:
            return saved, "recorded monotonic origin"
        # The legacy recorder exported its first memory counter relative to capture start.
        sample = next((row for row in self.samples if row.get("memory_kib")), None)
        if sample is not None:
            old_trace = read_json(self.folder / "trace.json", {})
            memory = next((row for row in old_trace.get("traceEvents", [])
                           if row["ph"] == "C" and row["name"] == "Host memory (KiB)"), None)
            if memory and memory["args"] == sample["memory_kib"]:
                return micros(sample["monotonic_s"]) - memory["ts"], "recovered from legacy trace"

        return None, "monotonic origin unavailable"

    def join(self, report, kind):
        output = report.get("output")
        candidates = self.index.get(self.normalize(output), []) if output else []
        if report.get("command_hash") is not None:
            candidates = [i for i in candidates if self.steps[i].hash == report["command_hash"]]
        if report.get("exit_code", 0) not in (None, 0):
            status = "failed"
        elif len(candidates) == 1:
            status = "matched"
            step = self.steps[candidates[0]]
            collection = step.cache if kind == "cache" else step.reports
            # Keep parsed aggregates and a reference to the original report, not verbose ld argv.
            collection.append({key: value for key, value in report.items() if key != "report"}
                              if report.get("stats") else report)
        else:
            status = "ambiguous" if candidates else "unmatched"

        self.join_counts[kind, status] += 1
        if status != "matched":
            self.unassigned.append(dict(report, join=status,
                                        candidates=[self.step_id(i) for i in candidates]))

    def read_reports(self):
        for path in sorted((self.folder / "phases").glob("*.json")):
            report = read_json(path, {})
            kind = report.get("kind", "unknown")
            self.join(dict(report, source=path.name,
                           stats=tool_stats(kind, report.get("report", ""))), kind)
        for row in read_jsonl(self.folder / "cache-outcomes.jsonl"):
            self.join(dict(row, kind="cache"), "cache")

    def step_id(self, index):
        return f"{self.number}:{index + 1}"

    def add_steps(self):
        pid = self.number * 2 - 1
        anchor = self.ninja_start
        self.ninja_clock = "recorded Ninja origin"
        self.local_ninja = False
        if anchor is None:
            anchor = self.build_start
            self.ninja_clock = "approximate CMake launch anchor"
        if anchor is None:
            # Isolate Ninja offsets from host time when the recorder supplied no bridge.
            end = max((row["ts"] for row in self.events), default=0)
            end = max(end, (self.lifecycle_start or 0) + (self.capture_duration or 0),
                      *(micros(row.get("received_monotonic_s")) or 0 for row in self.failures))
            anchor = end + US
            self.ninja_clock = "unanchored Ninja offsets in a separate display segment"
            self.local_ninja = bool(self.steps)

        active, free = [], []
        slots, peak = 0, 0
        for index, step in enumerate(self.steps):
            while active and active[0][0] <= step.start:
                _, slot = heapq.heappop(active)
                heapq.heappush(free, slot)
            # Equal timestamps remain zero-duration. Use the Ninja log lane, not a job slot.
            slot = 1
            if step.start < step.end:
                if free:
                    slot = heapq.heappop(free)
                else:
                    slots += 1
                    slot = slots + 1
                heapq.heappush(active, (step.end, slot))
                peak = max(peak, len(active))
            args = {"id": self.step_id(index), "command_hash": step.hash,
                    "start_ms": step.start, "end_ms": step.end, "raw_outputs": step.raw,
                    "outputs": step.outputs, "identity": step.identity, "clock": self.ninja_clock}
            if step.reports:
                args["tool_reports"] = step.reports
            if step.cache:
                args["cache_outcomes"] = step.cache
            elif step.object:
                args["cache_outcome"] = "unknown"
            self.events.append(event(pid, slot, "ninja", step.name, anchor + step.start * 1000,
                                     args, (step.end - step.start) * 1000))
        self.events.extend(meta(pid, i + 1, "thread_name", f"Job slot {i}")
                           for i in range(1, slots + 1))
        return peak

    def add_lifecycle(self):
        ninja, host = self.number * 2 - 1, self.number * 2
        label = f"Attempt {self.number}"
        self.events.extend([meta(ninja, 0, "process_name", f"{label} · Ninja"),
                            meta(host, 0, "process_name", f"{label} · Host"),
                            meta(ninja, 1, "thread_name", "Ninja log"),
                            meta(host, 0, "thread_name", "Host samples"),
                            meta(ninja, 0, "thread_name", "Attempt lifecycle")])
        args = {key: self.info.get(key) for key in (
            "capture_started_utc", "capture_elapsed_s", "capture_exit_code", "started_utc",
            "elapsed_s", "exit_code", "jobs", "build_dir", "boot_id", "page_size_bytes",
            "oom_evidence", "ccache")}
        args.update(capture=str(self.folder), origin=self.origin, ninja_clock=self.ninja_clock,
                    capture_start_monotonic_us=self.capture_start, build_start_monotonic_us=self.build_start,
                    failures=self.failures, orphan_cc1plus_kills=self.orphan_kills,
                    no_work_reported=self.no_work, unassigned_reports=self.unassigned, host=self.host)
        if self.lifecycle_start is not None and self.capture_duration is not None:
            self.events.append(event(ninja, 0, "attempt", label, self.lifecycle_start, args,
                                     self.capture_duration))
        else:
            # A display marker carries untimed details when no lifecycle bounds were recorded.
            first = min((row["ts"] for row in self.events if "ts" in row), default=0)
            self.events.append(event(ninja, 0, "attempt", f"{label} · lifecycle unavailable",
                                     self.capture_start if self.capture_start is not None else first, args))
        for failure in self.failures:
            ts = micros(failure.get("received_monotonic_s"))
            if ts is not None:
                self.events.append(event(ninja, 1, "failure", "Failure line received", ts, failure))


def place(attempts):
    previous = None
    offset = 0
    by_boot = None
    calibration = None
    for attempt in attempts:
        boot = attempt.boot
        origin = attempt.capture_start
        wall_offset = attempt.utc - origin if origin is not None and attempt.utc is not None else None
        comparable = previous is not None and attempt.has_monotonic and previous.has_monotonic
        same_boot = comparable and boot is not None and boot == by_boot
        legacy = (comparable and boot is None and previous.boot is None and wall_offset is not None
                  and calibration is not None and abs(wall_offset - calibration) <= US)
        if previous is None:
            offset = -attempt.first
            attempt.placement = "trace start"
        elif (same_boot or legacy) and attempt.first >= previous.last:
            attempt.placement = "same boot" if same_boot else "legacy monotonic (UTC-consistent)"
        else:
            offset = previous.display_end + US - attempt.first
            attempt.placement = "display-only separator"

        attempt.start = attempt.first + offset
        attempt.display_end = attempt.last + offset
        attempt.gap = (attempt.start - previous.display_end) / US if previous else None
        for item in attempt.events:
            if "ts" in item:
                item["ts"] += offset
            if item.get("cat") == "attempt":
                item["args"]["placement"] = attempt.placement
        if not legacy or attempt.placement == "display-only separator":
            calibration = wall_offset
        by_boot = boot
        previous = attempt


def fmt(value, digits=2):
    if value is None:
        return "—"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(title, headings, rows):
    lines = [f"## {title}", "", "| " + " | ".join(headings) + " |",
             "| " + " | ".join("---" for _ in headings) + " |"]
    lines.extend("| " + " | ".join(map(cell, row)) + " |" for row in rows)
    return lines + [""]


def timing_row(attempt):
    info = attempt.info
    return (attempt.number, attempt.folder.name, fmt(info.get("capture_started_utc")),
            fmt(info.get("jobs")), f"{fmt(info.get('capture_exit_code'))}/{fmt(info.get('exit_code'))}",
            fmt(info.get("capture_elapsed_s")), fmt(info.get("elapsed_s")), fmt(attempt.gap),
            attempt.placement)


def ninja_row(attempt, seen, seen_raw):
    info, steps = attempt.info, attempt.steps
    last = max((step.end for step in steps), default=None)
    tails = [step.name.rsplit("/", 1)[-1] for step in steps if step.end == last]
    earlier_end = max((step.end for step in steps if step.end != last), default=None)
    tail = ", ".join(tails[:3]) + (f" (+{len(tails) - 3})" if len(tails) > 3 else "")
    if earlier_end is not None and len(tails) == 1:
        start = next(step.start for step in steps if step.end == last)
        tail += f" ({(last - max(start, earlier_end)) / 1000:.3f} s alone)"
    paths = {(attempt.build_dir, path) for step in steps for path in step.outputs}
    raw_paths = {(attempt.build_dir, path) for step in steps for path in step.raw}
    repeated = (f"{len(raw_paths & seen_raw)}/{len(paths & seen)}"
                if attempt.build_dir and attempt.source else "—")
    if attempt.build_dir:
        seen.update(paths)
        seen_raw.update(raw_paths)
    return (attempt.number, fmt(sum(len(step.raw) for step in steps) if attempt.source else None),
            fmt(len(steps) if attempt.source else None), fmt(attempt.peak if attempt.source else None),
            f"{fmt(info.get('ninja_log_before_outputs'))} → {fmt(info.get('ninja_log_after_outputs'))}",
            fmt(repeated), tail or "—", fmt(last / 1000 if last is not None else None, 3))


def host_row(attempt):
    info, host = attempt.info, attempt.host
    user, system = info.get("child_user_cpu_s"), info.get("child_system_cpu_s")
    cores = (user + system) / info["elapsed_s"] if (user is not None and system is not None
                                                   and info.get("elapsed_s")) else None
    memory, swap = host["min_available_kib"], host["max_swap_used_kib"]
    page = info.get("page_size_bytes")
    pages = [host["swap_pages"].get(name) for name in ("pswpin", "pswpout")]
    traffic = "/".join(fmt(value * page / 2**30 if page and value is not None else value)
                       for value in pages)
    if any(value is not None for value in pages):
        traffic += " GiB" if page else " pages"
    pressure = " / ".join("/".join(fmt(host["psi_pct"].get(f"{name} {kind}"))
                                   for kind in ("some", "full"))
                          for name in ("cpu", "memory", "io"))
    return (attempt.number, host["build_samples"], fmt(cores), fmt(host["busy_pct"]),
            fmt(memory / 2**20 if memory is not None else None),
            fmt(swap / 2**20 if swap is not None else None), traffic, pressure)


def phase_total(report):
    stats = report["stats"]
    if report["kind"] == "gcc":
        return stats.get("wall_s_by_row", {}).get("TOTAL")
    cpu = stats.get("stats_by_row", {}).get("ALL", {}).get("cpu_us")
    return cpu / US if cpu is not None else None


def hotspots(attempt):
    if not attempt.steps:
        return []
    steps = attempt.steps
    slow = max(steps, key=lambda step: step.end - step.start)
    elapsed = (slow.end - slow.start) / 1000
    rows = [(attempt.number, "Ninja elapsed", slow.name, f"{elapsed:.3f} s")]
    for kind, title in (("gcc", "GCC wall"), ("gnu-ld", "ld CPU column")):
        candidates = []
        for step in steps:
            reports = [report for report in step.reports if report["kind"] == kind]
            # Keep duplicates in the trace; do not aggregate or rank an uncertain edge.
            if len(reports) == 1 and (total := phase_total(reports[0])) is not None:
                candidates.append((total, step, reports[0]))
        if not candidates:
            continue
        total, step, report = max(candidates, key=lambda row: row[0])
        text = f"{total:.3f} s (Ninja {(step.end - step.start) / 1000:.3f} s)"
        phases = report["stats"].get("wall_s_by_row", {})
        if (optim := phases.get("phase opt and generate")) is not None:
            text += f"; optimization/codegen {optim:.2f} s"
            if (tracking := phases.get("var-tracking dataflow", 0)) >= optim / 10 and tracking > 0:
                text += f" (includes {tracking:.2f} s variable-tracking dataflow)"
        rows.append((attempt.number, title, step.name, text))
        if kind == "gnu-ld":
            elapsed, step, _ = max(candidates, key=lambda row: row[1].end - row[1].start)
            rows.append((attempt.number, "Ninja elapsed (ld reported)", step.name,
                         f"{(step.end - step.start) / 1000:.3f} s (ld CPU {elapsed:.3f} s)"))
    return rows


def tool_row(attempt):
    counts = attempt.join_counts
    gcc_edges, ld_edges, duplicate_edges, reportless = 0, 0, 0, 0
    for step in attempt.steps:
        kinds = Counter(report["kind"] for report in step.reports)
        gcc_edges += "gcc" in kinds
        ld_edges += "gnu-ld" in kinds
        duplicate_edges += any(count > 1 for count in kinds.values())
        reportless += step.object and "gcc" not in kinds
    cache = attempt.info.get("ccache", {})
    return (attempt.number, gcc_edges, ld_edges, duplicate_edges, reportless,
            sum(count for (_, status), count in counts.items() if status != "matched"),
            "/".join(fmt(cache.get(key)) for key in (
                "cache_miss", "direct_cache_hit", "preprocessed_cache_hit", "compile_failed")),
            fmt(cache.get("remote_storage_error")))


def throughput(attempt):
    changes = Counter()
    work = 0
    for step in attempt.steps:
        if step.end <= step.start:
            continue
        changes[step.start] += 1
        changes[step.end] -= 1
        work += step.end - step.start
    end = max((step.end for step in attempt.steps), default=0)
    jobs = int(attempt.info.get("jobs") or 0)
    last_full, full, active, prior = None, 0, 0, 0
    for boundary, change in sorted(changes.items()):
        if jobs > 0 and active == jobs:
            full += boundary - prior
            last_full = boundary
        active += change
        prior = boundary
    return (attempt.number, fmt(work / 1000 if attempt.source else None),
            fmt(len(attempt.steps) * 1000 / end if end else None), fmt(work / end if end else None),
            fmt(100 * full / end if end and jobs > 0 else None),
            fmt(work / (1000 * jobs) if attempt.source and jobs > 0 else None),
            fmt((end - last_full) / 1000 if last_full is not None else None, 3))


def gcc_cost(attempt):
    totals = Counter()
    covered = 0
    for step in attempt.steps:
        reports = [report for report in step.reports if report["kind"] == "gcc"]
        if not step.object or len(reports) != 1:
            continue
        rows = reports[0]["stats"].get("wall_s_by_row", {})
        if "TOTAL" not in rows:
            continue
        covered += 1
        for key in ("TOTAL", "phase parsing", "phase lang. deferred", "phase opt and generate"):
            totals[key] += rows.get(key, 0)
    total = totals["TOTAL"]
    front = totals["phase parsing"] + totals["phase lang. deferred"]
    optimize = totals["phase opt and generate"]
    return (attempt.number, covered, fmt(total if covered else None),
            fmt(front if covered else None), fmt(100 * front / total if total else None, 1),
            fmt(optimize if covered else None), fmt(100 * optimize / total if total else None, 1))


def retry_rows(attempts):
    seen, hashed, pending, recovered = set(), set(), set(), set()
    for attempt in attempts:
        build = attempt.build_dir
        if not build or not attempt.source:
            yield (attempt.number, "—", "—", "—", "—", "—", "—")
        else:
            repeated = repeated_ms = recoveries = recovery_ms = repeat_recovery = 0
            object_keys, new_recoveries = set(), set()
            for step in sorted(attempt.steps, key=lambda step: step.end):
                keys = {(build, path) for path in step.outputs}
                duration = step.end - step.start
                if keys & seen:
                    repeated += 1
                    repeated_ms += duration
                object_keys.update((build, path, step.hash) for _, path in keys
                                   if path.endswith((".o", ".obj")) and (build, path, step.hash) in hashed)
                recovered_now = keys & pending
                if recovered_now:
                    recoveries += 1
                    recovery_ms += duration
                    pending.difference_update(recovered_now)
                if keys & recovered:
                    repeat_recovery += 1
                new_recoveries.update(recovered_now)
            recovered.update(new_recoveries)
            yield (attempt.number, repeated, fmt(repeated_ms / 1000), len(object_keys),
                   recoveries, fmt(recovery_ms / 1000), repeat_recovery)
            for step in attempt.steps:
                seen.update((build, path) for path in step.outputs)
                hashed.update((build, path, step.hash) for path in step.outputs)
        if build:
            pending.update((build, attempt.normalize(row["target"])) for row in attempt.failures
                           if row.get("target"))


def details(attempt):
    result = []
    info = attempt.info
    if not attempt.steps and attempt.no_work and info.get("exit_code") == 0:
        result.append("Ninja reported no work; build succeeded.")
    elif not attempt.source:
        result.append("No per-run Ninja log; completed work is unknown.")
    elif not attempt.steps:
        result.append("No Ninja completions recorded; absence alone does not establish a no-op.")
    unresolved = sum(step.identity.startswith("unresolved") for step in attempt.steps)
    if unresolved:
        result.append(f"{unresolved} multi-output groups lack a unique archived manifest match.")
    if attempt.steps:
        result.append(f"Ninja clock: {attempt.ninja_clock}.")
    if not attempt.samples:
        result.append("No host samples.")
    elif not info.get("page_size_bytes") and attempt.host["swap_pages"]:
        result.append("Page size not recorded; swap traffic remains in pages.")
    if attempt.host["anomalies"]:
        anomalies = attempt.host["anomalies"]
        highest = max((row for row in anomalies if "percent" in row),
                      key=lambda row: row["percent"], default=None)
        text = f"{len(anomalies)} host interval anomalies"
        if highest:
            text += f"; highest PSI sample: {highest['metric']} {highest['percent']:.1f}%"
        result.append(text + ".")
    statuses = Counter(row["join"] for row in attempt.unassigned)
    if statuses:
        result.append("Unassigned reports/outcomes: " + ", ".join(
            f"{count} {status}" for status, count in sorted(statuses.items())) + ".")
    if not attempt.failure_log:
        result.append("No failure log; failed-edge count is unknown.")
    else:
        killed = sum(bool(row.get("cc1plus_killed")) for row in attempt.failures)
        result.append(f"Failed edges: {len(attempt.failures)}; killed cc1plus: {killed}." + (
            f" Additional unassociated kill lines: {attempt.orphan_kills}." if attempt.orphan_kills else ""))
        for row in attempt.failures:
            time = "receipt timestamped" if row.get("received_monotonic_s") is not None else "untimed"
            result.append(f"  - `{row.get('target', 'unknown target')}` (exit {fmt(row.get('exit_code'))}; {time})")
        if killed or attempt.orphan_kills:
            evidence = info.get("oom_evidence")
            result.append(f"Recorded OOM evidence: {evidence}." if evidence else
                          "No kernel/cgroup OOM evidence recorded; compiler kills alone do not establish OOM.")
    return result


def report(attempts):
    lines = ["# Build capture analysis", "",
             "Successive captures of a build directory are retries, not benchmarks.", "",
             "Time uses a shared monotonic axis for the same boot. Legacy captures use the original "
             "trace to recover the monotonic origin; absent boot IDs, matching UTC offsets (within 1 s) "
             "support but do not prove a shared boot. Other captures are separated by a display-only "
             "second. Gaps use the ends of all observed timestamps/slices; UTC is for reference. "
             "Ninja offsets use the recorded Ninja origin or approximate CMake launch, not inferred "
             "command timestamps. Unanchored offsets are plotted separately.", ""]
    lines += table("Attempts", ["#", "Capture", "Start (UTC)", "Jobs", "Exit capture/build",
                                "Capture s", "Build s", "Gap s", "Placement"], map(timing_row, attempts))
    seen, seen_raw = set(), set()
    lines += table("Ninja completions", ["#", "Output rows", "Groups", "Peak overlap", "Log size",
                                          "Prior paths (raw/normalized)",
                                          "Last recorded successful completion", "Ninja end s"],
                   (ninja_row(attempt, seen, seen_raw) for attempt in attempts))
    lines += ["Slots show half-open interval overlap, not workers or dependencies. Completion of a "
              "link does not mean its executable ran.", ""]
    lines += table("Throughput and tail", ["#", "Slot-s", "Completions/s", "Mean active",
                                           "At job limit %", "Slot-s/jobs", "After last full load s"],
                   map(throughput, attempts))
    lines += ["Rates cover Ninja origin through last recorded completion; failed executions are absent. "
              "Slot-s/jobs is a lower bound at fixed durations, not a wall-time forecast.", ""]
    lines += table("Repeated completions and failure recoveries", ["#", "Repeated edges", "Slot-s",
                   "Same-hash object outputs", "Recovered edges", "Recovery slot-s",
                   "Previously recovered edges rerun"], retry_rows(attempts))
    lines += ["Repeats match normalized outputs from earlier attempts in the same build directory. "
              "Recoveries match an earlier `FAILED:` target string to its first later successful output. "
              "These are costs of successful executions, not failure durations, invalidation causes, "
              "or elapsed savings.", ""]
    lines += table("Host during build", ["#", "Samples", "Child CPU cores", "Host busy %",
                                          "Min available GiB", "Max swap used GiB", "Swap in/out",
                                          "PSI % some/full: CPU / memory / I/O"], map(host_row, attempts))
    lines += ["Host summaries use samples and adjacent intervals wholly inside the recorded build, "
              "not the entire capture. PSI values over 100% are flagged, not clipped.", ""]
    lines += table("Tools and cache", ["#", "GCC edges", "ld edges", "Duplicate-report edges",
                                        "Reportless object edges", "Unassigned reports/outcomes",
                                        "ccache miss/direct hit/preprocessed hit/failed", "Remote errors"],
                   map(tool_row, attempts))
    lines += ["Reportless edges have unknown cache status unless an output-keyed outcome was recorded. "
              "Remote errors overlap cache outcomes. Tool stats are aggregates, not trace intervals.", ""]
    lines += table("GCC phase balance", ["#", "Profiled object edges", "GCC wall-s",
                                        "Front-end s", "Front-end %", "Optimizer/codegen s",
                                        "Optimizer/codegen %"], map(gcc_cost, attempts))
    lines += ["Front-end adds parsing and deferred language work. Only top-level phases count here; "
              "nested rows such as variable tracking are not added again.", ""]
    lines += table("Hotspots", ["#", "Metric", "Output", "Cost"],
                   (row for attempt in attempts for row in hotspots(attempt)))
    for attempt in attempts:
        lines.extend([f"### Attempt {attempt.number} notes", ""])
        lines.extend(line if line.startswith("  - ") else f"- {line}" for line in details(attempt))
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, epilog=(
        "Optional capture data: build.json may include boot_id, capture_start_monotonic_s, "
        "ninja_start_monotonic_s, page_size_bytes and oom_evidence. manifest-edges.jsonl indexes "
        "the matching archived manifest with one {outputs: [...]} record per edge. "
        "failures.jsonl records line_number (1-based in build.log), target, exit_code and "
        "received_monotonic_s. cache-outcomes.jsonl records output, outcome and optional command_hash."))
    parser.add_argument("captures", nargs="+", type=Path, help="capture directories in attempt order")
    parser.add_argument("--out", type=Path, required=True, help="new or empty analysis directory")
    args = parser.parse_args()
    folders = [path.expanduser().resolve() for path in args.captures]
    out = args.out.expanduser().resolve()
    if any(not path.is_dir() for path in folders):
        parser.error("every capture must be an existing directory")
    if len(set(folders)) != len(folders):
        parser.error("duplicate capture directory")
    if any(folder == out or folder in out.parents for folder in folders):
        parser.error("--out must be outside the captures")
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        parser.error("--out must be new or empty")

    try:
        attempts = [Attempt(folder, number) for number, folder in enumerate(folders, 1)]
        place(attempts)
        events = [row for attempt in attempts for row in attempt.events]
        events.sort(key=lambda row: row.get("ts", -1))
        trace = json.dumps({"traceEvents": events}, allow_nan=False, separators=(",", ":"))
        summary = report(attempts)
        out.mkdir(parents=True, exist_ok=True)
        with (out / "trace.json").open("x") as stream:
            stream.write(trace + "\n")
        with (out / "report.md").open("x") as stream:
            stream.write(summary)
    except (OSError, KeyError, TypeError, ValueError) as error:
        parser.exit(1, f"{parser.prog}: {error}\n")


if __name__ == "__main__":
    main()
