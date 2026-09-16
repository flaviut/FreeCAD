#!/usr/bin/env python3
"""Replay independent, clean-state content edits against an existing Ninja graph.

Paths in --changed are relative to the Git root (or absolute). Paths in
--target, duration CSV and scenario JSON are Ninja paths (relative to the build
root, or absolute). Duration CSV columns: output,seconds; these are explicit
measurements and require --jobs unless a capture supplies it.

Scenario JSON is a list of {"id": "...", "assumption": "...", "remove":
[{"output": "...", "input": "...", "kind": "dirty"|"order"}], "seconds":
{"output": 1.0}} objects. Either intervention field can be omitted. An entry
with only id and assumption is listed as unranked. Removing a dirty input
removes both invalidation and its scheduling constraint. Removals and costs
must name exact, existing graph entries. Each scenario is independent.
"""

import argparse
from collections import Counter, defaultdict, deque
import csv
from dataclasses import dataclass, replace
from fnmatch import fnmatchcase
from graphlib import TopologicalSorter
import heapq
import json
import math
import os
from pathlib import Path
import re
from statistics import median
import subprocess
import sys


ASSIGN = re.compile(r"([\w.-]+) *= *(.*)$")
ESC = re.compile(r"\$(?:[ $:]|\{[\w.-]+\}|[\w-]+)")
TOKEN = re.compile(r"\|\||\|@|\||:|(?:\$(?:[ $:]|\{[\w.-]+\}|[\w-]+)|[^ $:|])+")
DEPS = re.compile(r"(.*): #deps (\d+), deps mtime -?\d+ \((VALID|STALE)\)")
CONFIG = {"CMakeLists.txt", "CMakePresets.json", "CMakeUserPresets.json", "CMakeCache.txt",
          "flake.nix", "flake.lock", ".envrc", ".gitmodules", "package.xml", "pixi.toml", "pixi.lock"}


def run(*args, cwd):
    return subprocess.check_output(args, cwd=cwd, stderr=subprocess.PIPE).decode(
        errors="surrogateescape")


def absolute(base, path):
    return os.path.abspath(base / path)


def expand(text, lookup):
    def get(match):
        key = match[0][1:]
        if key in " $:":
            return key
        return lookup(key.strip("{}"))

    if "$" in ESC.sub("", text):
        raise ValueError(f"unsupported Ninja escape: {text[:120]}")
    return ESC.sub(get, text)


def statements(path):
    pending = ""
    for line in path.read_text(errors="surrogateescape").splitlines():
        line = pending + line.lstrip(" ") if pending else line
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        dollars = len(line) - len(line.rstrip("$"))
        pending = line[:-1] if dollars % 2 else ""
        if not pending:
            yield line
    if pending:
        raise ValueError(f"unfinished continuation in {path}")


def blocks(path):
    head, bindings = None, {}
    for line in statements(path):
        if not line.startswith(" "):
            if head is not None:
                yield head, bindings
            head, bindings = line, {}
            continue
        match = ASSIGN.fullmatch(line.lstrip(" "))
        if not match or head is None:
            raise ValueError(f"unsupported Ninja binding in {path}: {line[:100]}")
        bindings[match[1]] = match[2]
    if head is not None:
        yield head, bindings


def path_tokens(text, env):
    pos = 0
    for match in TOKEN.finditer(text):
        if text[pos:match.start()].strip():
            raise ValueError(f"unsupported Ninja path syntax: {text[:120]}")
        pos = match.end()
        token = match[0]
        if token in (":", "|", "||", "|@"):
            yield token, token
        else:
            path = expand(token, lambda key: env.get(key, ""))
            if not path:
                raise ValueError("empty Ninja path")
            yield "path", os.path.normpath(path)
    if text[pos:].strip():
        raise ValueError(f"unsupported Ninja path syntax: {text[:120]}")


@dataclass
class Edge:
    outputs: tuple
    rule: str
    dirty: set
    order: set
    validation: set
    pool: str
    deps: str
    depfile: str
    restat: bool
    generator: bool
    dyndep: str

    @property
    def name(self):
        return self.outputs[0]

    @property
    def phony(self):
        return self.rule == "phony"


class Manifest:
    def __init__(self, root):
        self.root = root
        self.edges = []
        self.outputs = {}
        self.defaults = []
        self.pools = {"console": 1}
        self.files = set()
        self.load(root / "build.ninja", {}, {"phony": {}})
        self.dep_status = {}

    def load(self, path, env, rules):
        if path in self.files:
            raise ValueError(f"repeated manifest inclusion: {path}")
        self.files.add(path)
        for line, bindings in blocks(path):
            kind, _, text = line.partition(" ")
            if kind == "rule":
                rules[text] = bindings
            elif kind == "pool":
                self.pools[text] = positive(bindings["depth"])
            elif kind == "build":
                self.add_edge(text, bindings, env, rules)
            elif kind == "default":
                self.defaults.extend(path for _, path in path_tokens(text, env))
            elif kind in ("include", "subninja"):
                paths = list(path_tokens(text, env))
                if len(paths) != 1 or paths[0][0] != "path":
                    raise ValueError(f"unsupported manifest include: {text}")
                local = (env.copy(), rules.copy()) if kind == "subninja" else (env, rules)
                self.load(self.root / paths[0][1], *local)
            else:
                match = ASSIGN.fullmatch(line)
                if not match or bindings:
                    raise ValueError(f"unsupported Ninja statement in {path}: {line[:120]}")
                env[match[1]] = expand(match[2], lambda key: env.get(key, ""))

    def add_edge(self, text, bindings, env, rules):
        columns = defaultdict(list)
        column = "outputs"
        for kind, value in path_tokens(text, env):
            if kind == "path":
                columns[column].append(value)
                if column == ":":
                    column = "explicit"
            else:
                column = "byproducts" if kind == "|" and column == "outputs" else kind
        rule, = columns[":"]
        outputs = tuple(columns["outputs"] + columns["byproducts"])
        specials = {"out": " ".join(columns["outputs"]), "in": " ".join(columns["explicit"]),
                    "in_newline": "\n".join(columns["explicit"])}

        def local(key):
            if key in bindings:
                return expand(bindings[key], lambda k: env.get(k, ""))
            return env.get(key, "")

        def value(key):
            if key not in bindings and key in rules[rule]:
                return expand(rules[rule][key], lambda k: specials[k] if k in specials else local(k))
            return local(key)

        edge = Edge(outputs, rule, set(columns["explicit"] + columns["|"]),
                    set(columns["||"]), set(columns["|@"]), value("pool"), value("deps"),
                    value("depfile"), bool(value("restat")), bool(value("generator")), value("dyndep"))
        for output in outputs:
            if output in self.outputs:
                raise ValueError(f"duplicate Ninja output: {output}")
            self.outputs[output] = len(self.edges)
        self.edges.append(edge)

    def add_deps(self):
        # Only the first output is the key Ninja consults for deps-log records.
        records = read_deps(self.root)
        pool_names = self.pools.keys() | {""}
        for node, edge in enumerate(self.edges):
            if edge.pool not in pool_names:
                raise ValueError(f"unknown Ninja pool on {edge.name}: {edge.pool}")
            if edge.deps:
                deps = records.get(edge.name)
                if deps is None:
                    self.dep_status[node] = "missing_or_stale_log_edges"
                    continue
                self.dep_status[node] = "valid_log_edges"
            elif edge.depfile:
                deps = read_depfile(self.root / edge.depfile, edge.outputs)
                self.dep_status[node] = "plain_depfile_edges" if deps is not None else "unread_depfile_edges"
                if deps is None:
                    continue
            else:
                continue
            edge.dirty.update(deps)
            edge.order.difference_update(edge.dirty)


def read_deps(root):
    records = {}
    with subprocess.Popen(("ninja", "-t", "deps"), cwd=root, stdout=subprocess.PIPE,
                          text=True, errors="surrogateescape") as proc:
        remaining, inputs = 0, None
        for row in proc.stdout:
            line = row.rstrip("\n")
            if remaining:
                if not line.startswith("    "):
                    raise ValueError(f"truncated Ninja deps record: {line}")
                remaining -= 1
                if inputs is not None:
                    inputs.add(os.path.normpath(line[4:]))
                continue
            if not line:
                continue
            match = DEPS.fullmatch(line)
            if not match:
                raise ValueError(f"unsupported Ninja deps record: {line}")
            output, size, state = match.groups()
            remaining = int(size)
            inputs = None
            if state == "VALID":
                inputs = records.setdefault(os.path.normpath(output), set())
        if remaining or proc.wait():
            raise ValueError("ninja -t deps did not return complete records")
    return records


def read_depfile(path, outputs):
    if not path.is_file():
        return None
    # Support a single GCC-style rule; reject make constructs rather than guess.
    text = path.read_text(errors="surrogateescape").replace("\\\n", " ").strip()
    tokens = re.findall(r"(?:\\[ #:\\]|\$\$|[^\s:#$\\])+|:", text)
    residue = re.sub(r"(?:\\[ #:\\]|\$\$|[^\s:#$\\])+|:", "", text)
    if residue.strip() or "\n" in text or tokens.count(":") != 1:
        return None
    split = tokens.index(":")
    paths = [os.path.normpath(re.sub(r"\\([ #:\\])|\$\$", lambda m: m[1] or "$", token))
             for token in tokens]
    if not paths[:split] or not set(paths[:split]).issubset(outputs) or outputs[0] not in paths[:split]:
        return None
    return set(paths[split + 1:])


class Graph:
    def __init__(self, manifest, targets, overrides=None):
        self.manifest = manifest
        self.edges = manifest.edges if overrides is None else overrides
        producers = manifest.outputs
        self.parents = {}
        self.follow = defaultdict(set)
        self.always = set()
        # Validations extend reachability but do not order or dirty the requester.
        pending = [producers[target] for target in targets]
        while pending:
            node = pending.pop()
            if node in self.parents:
                continue
            edge = self.edges[node]
            if edge.dyndep:
                raise ValueError(f"dyndep is unsupported on reachable edge {edge.name}")
            if edge.generator:
                raise ValueError(f"generator in target graph is unsupported: {edge.name}")
            parents = {producers[path] for path in edge.dirty | edge.order if path in producers}
            self.parents[node] = parents
            pending.extend(parents)
            pending.extend(producers[p] for p in edge.validation if p in producers)
            for path in edge.validation - producers.keys():
                if not (manifest.root / path).exists():
                    raise ValueError(f"missing validation input: {path}")
            for path in edge.dirty:
                self.follow[path].add(node)
            if edge.phony and not (edge.dirty or edge.order):
                self.always.update(path for path in edge.outputs if not (manifest.root / path).exists())
        self.topo = tuple(TopologicalSorter(self.parents).static_order())
        self.tasks = {node for node in self.parents if not self.edges[node].phony}

    def dirty(self, paths, restat="propagate"):
        queue = deque(self.always | paths)
        seen = set()
        while queue:
            for node in self.follow.get(queue.popleft(), ()):
                if node in seen:
                    continue
                seen.add(node)
                edge = self.edges[node]
                if restat == "propagate" or not edge.restat:
                    queue.extend(edge.outputs)
        return seen & self.tasks

    def dependencies(self, dirty):
        # A clean or phony bridge can still hold a dirty consumer until its
        # order-only prerequisites finish. Collapse only the non-running edges.
        waiting = {}
        actual = {}
        for node in self.topo:
            needed = set().union(*(waiting[p] for p in self.parents[node]))
            if node in dirty:
                actual[node] = needed
                waiting[node] = {node}
            else:
                waiting[node] = needed
        return actual

    def schedule(self, parents, seconds, jobs):
        if not parents:
            return 0.0
        children = defaultdict(list)
        degree = {node: len(pred) for node, pred in parents.items()}
        for node, pred in parents.items():
            for parent in pred:
                children[parent].append(node)
        bottom = {}
        for node in reversed(parents):
            bottom[node] = seconds[node] + max((bottom[c] for c in children[node]), default=0)
        ready = [(-bottom[n], n) for n, d in degree.items() if not d]
        heapq.heapify(ready)
        running = []
        used = Counter()
        now = 0.0
        while ready or running:
            deferred = []
            while ready and len(running) < jobs:
                priority, node = heapq.heappop(ready)
                pool = self.edges[node].pool
                if pool and used[pool] >= self.manifest.pools[pool]:
                    deferred.append((priority, node))
                    continue
                used[pool] += 1
                heapq.heappush(running, (now + seconds[node], node))
            for item in deferred:
                heapq.heappush(ready, item)
            now = running[0][0]
            while running and running[0][0] == now:
                _, node = heapq.heappop(running)
                used[self.edges[node].pool] -= 1
                for child in children[node]:
                    degree[child] -= 1
                    if degree[child] == 0:
                        heapq.heappush(ready, (-bottom[child], child))
        return now


def positive(value):
    number = int(value)
    if number <= 0:
        raise ValueError(f"expected a positive integer: {value}")
    return number


def seconds_value(value):
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"expected finite, nonnegative seconds: {value}")
    return number


def ninja_log(path):
    rows = {}
    with path.open(errors="surrogateescape") as stream:
        header = stream.readline().strip()
        if header not in {"# ninja log v5", "# ninja log v6", "# ninja log v7"}:
            raise ValueError(f"unsupported log header in {path}: {header}")
        for line in stream:
            start, end, _, output, digest = line.rstrip("\n").split("\t")
            rows[os.path.normpath(output)] = (int(start), int(end), digest)
    return header, rows


class Costs:
    def __init__(self, manifest, captures, duration_file, jobs):
        self.notes = []
        usable = []
        for directory in captures:
            meta = json.loads((directory / "build.json").read_text())
            if meta.get("exit_code") != 0 or meta.get("capture_exit_code", 0) != 0:
                self.notes.append(f"Excluded unsuccessful capture {directory} ({meta.get('jobs')} jobs).")
                continue
            if Path(meta["build_dir"]).resolve() != manifest.root:
                self.notes.append(f"Excluded capture from another build directory: {directory}.")
                continue
            usable.append((directory, meta, positive(meta["jobs"])))
        self.jobs = jobs or (usable[0][2] if usable else None)
        if self.jobs is None:
            raise ValueError("provide --jobs or a successful capture from this build directory")
        self.direct = {}
        self.replay = None
        current = None
        for directory, meta, count in usable:
            if count != self.jobs:
                self.notes.append(f"Excluded different-concurrency capture {directory} ({count} jobs).")
                continue
            if current is None:
                current = ninja_log(manifest.root / ".ninja_log")
            header, rows = ninja_log(directory / "run.ninja_log")
            if header != current[0]:
                self.notes.append(f"Excluded incompatible Ninja log version: {directory}.")
                continue
            records = defaultdict(set)
            excluded = Counter()
            for output, (start, end, digest) in rows.items():
                node = manifest.outputs.get(output)
                if node is None or manifest.edges[node].phony:
                    excluded["unknown_output_rows"] += 1
                elif current[1].get(output, (None, None, None))[2] != digest:
                    excluded["hash_unmatched_output_rows"] += 1
                elif not 0 <= start <= end:
                    excluded["invalid_interval_output_rows"] += 1
                else:
                    records[node].add((start, end))
            intervals = {node: times.pop() for node, times in records.items() if len(times) == 1}
            excluded["conflicting_edge_intervals"] = len(records) - len(intervals)
            self.notes.append(f"Capture {directory}: {len(intervals)} matched edges; exclusions {dict(excluded)}.")
            self.notes.append(f"Capture Git commit: {meta.get('git_before_build', {}).get('commit', 'unknown')}.")
            if not intervals:
                continue
            if self.replay is None:
                self.replay = (directory, meta, intervals)
            for node, (start, end) in intervals.items():
                self.direct.setdefault(node, (end - start) / 1000)
        if duration_file:
            self.load_csv(manifest, duration_file)
        if not self.direct:
            raise ValueError("no usable captured or supplied durations")
        by_rule, by_class = defaultdict(list), defaultdict(list)
        for node, duration in self.direct.items():
            rule = manifest.edges[node].rule
            by_rule[rule].append(duration)
            by_class[rule_class(rule)].append(duration)
        rules = {rule: median(vals) for rule, vals in by_rule.items() if rule != "CUSTOM_COMMAND"}
        classes = {kind: median(vals) for kind, vals in by_class.items()}
        self.seconds, self.labels = {}, {}
        for node, edge in enumerate(manifest.edges):
            if edge.phony:
                continue
            rule, kind = edge.rule, rule_class(edge.rule)
            if node in self.direct:
                duration, label = self.direct[node], "direct"
            elif rule in rules:
                duration, label = rules[rule], "rule_estimate"
            elif kind in classes:
                duration, label = classes[kind], "class_estimate"
            else:
                duration, label = 1.0, "fallback"
            self.seconds[node] = duration
            self.labels[node] = label

    def load_csv(self, manifest, path):
        seen = set()
        with path.open(newline="") as stream:
            for row in csv.DictReader(stream):
                node = manifest.outputs.get(os.path.normpath(row["output"]))
                if node is None or manifest.edges[node].phony or node in seen:
                    raise ValueError(f"unknown, phony or repeated duration edge: {row['output']}")
                seen.add(node)
                self.direct.setdefault(node, seconds_value(row["seconds"]))
        self.notes.append(f"Supplied durations for {len(seen)} edges: {path} (capture values take precedence).")


def rule_class(rule):
    if "_COMPILER" in rule:
        return rule.split("_", 1)[0] + "/compile"
    if "_LINKER" in rule:
        return "link"
    return rule


def calibration(graph, costs):
    if costs.replay is None:
        return {"status": "No compatible run capture; no elapsed comparison."}
    directory, meta, captured = costs.replay
    observed = {node: times for node, times in captured.items() if node in graph.tasks}
    if not observed:
        return {"status": "No matched capture intervals in target graph."}
    seconds = {node: (end - start) / 1000 for node, (start, end) in observed.items()}
    parents = graph.dependencies(observed.keys())
    conflicts = sum(observed[parent][1] > observed[node][0] + 1
                    for node, preds in parents.items() for parent in preds)
    return {"status": "In-sample timing replay, not validation of incremental invalidation or queue order.",
            "capture": str(directory), "replayed_edges": len(observed),
            "matched_edges_outside_targets": len(captured) - len(observed),
            "observed_subset_span_s": (max(b for _, b in observed.values()) -
                                       min(a for a, _ in observed.values())) / 1000,
            "observed_cmake_wall_s": meta.get("elapsed_s"),
            "scheduled_subset_s": graph.schedule(parents, seconds, costs.jobs),
            "predecessor_overlaps_gt_1ms": conflicts}


@dataclass
class Workload:
    id: str
    kind: str
    paths: tuple
    errors: tuple = ()


def workloads(repo, args, ref):
    if args.changed:
        yield Workload("explicit", "explicit", tuple(args.changed))
    if args.count == 0:
        return
    commits = run("git", "rev-list", "--first-parent", f"--max-count={args.count + 1}",
                  ref, cwd=repo).splitlines()
    for commit, parent in zip(commits, commits[1:]):
        raw = run("git", "diff-tree", "--no-commit-id", "-r", "--raw", "--no-renames", "-z",
                  parent, commit, cwd=repo)
        fields = raw.split("\0")[:-1]
        paths, errors = [], []
        for header, path in zip(fields[::2], fields[1::2]):
            old, new, _, _, status = header[1:].split()
            paths.append(path)
            if status != "M" or old != new or new not in {"100644", "100755"}:
                errors.append(f"structural {status} {old}->{new}: {path}")
        yield Workload(commit, "historical", tuple(paths), tuple(errors))


class PathIndex:
    def __init__(self, manifest):
        self.root = manifest.root
        self.generator = set(manifest.files)
        self.aliases = defaultdict(set)
        for edge in manifest.edges:
            for path in edge.dirty | edge.order | edge.validation:
                physical = absolute(self.root, path)
                self.aliases[physical].add(path)
                if edge.generator and path in edge.dirty:
                    self.generator.add(physical)
        self.generator = {str(path) for path in self.generator}

    def classify(self, repo, batch, inert_globs):
        errors = list(batch.errors)
        paths, inert = set(), []
        for path in batch.paths:
            file = Path(path)
            name = absolute(repo, path)
            if (name in self.generator or file.name in CONFIG or
                    file.name.endswith((".cmake", ".cmake.in", ".ninja"))):
                errors.append(f"configuration: {path}")
            elif not Path(name).is_file() or Path(name).is_symlink():
                errors.append(f"not a current regular file: {path}")
            elif name in self.aliases:
                paths.update(self.aliases[name])
            elif any(fnmatchcase(os.path.relpath(name, repo), glob) for glob in inert_globs):
                inert.append(path)
            else:
                errors.append(f"unrecognized path: {path}")
        return paths, inert, errors


@dataclass
class Variant:
    id: str
    assumption: str
    graph: Graph | None
    seconds: dict
    reason: str = ""


def variants(manifest, graph, costs, source, targets):
    yield Variant("baseline", "Current graph", graph, {})
    if source is None:
        return
    specs = json.loads(source.read_text())
    if not isinstance(specs, list):
        raise ValueError("scenario file must contain a list")
    ids = {"baseline"}
    for spec in specs:
        name, assumption = spec["id"], spec["assumption"]
        if (not isinstance(name, str) or not name or name in ids or
                not isinstance(assumption, str) or not assumption.strip()):
            raise ValueError(f"scenario needs a unique id and nonempty assumption: {name}")
        ids.add(name)
        if spec.keys() - {"id", "assumption", "remove", "seconds"}:
            raise ValueError(f"unknown scenario fields: {name}")
        edits, costs_ = spec.get("remove", []), spec.get("seconds", {})
        local = manifest.edges.copy()
        try:
            if not (edits or costs_):
                raise ValueError("no graph or duration intervention supplied")
            seconds = {}
            for output, value in costs_.items():
                node = manifest.outputs.get(os.path.normpath(output))
                if node not in graph.tasks or node in seconds:
                    raise ValueError(f"unreachable, phony or repeated duration edge: {output}")
                seconds[node] = seconds_value(value)
            for edit in edits:
                output, path, kind = edit["output"], os.path.normpath(edit["input"]), edit["kind"]
                node = manifest.outputs.get(os.path.normpath(output))
                if node not in graph.parents or kind not in {"dirty", "order"}:
                    raise ValueError(f"unsupported dependency selector: {edit}")
                edge = local[node]
                inputs = getattr(edge, kind)
                if path not in inputs:
                    raise ValueError(f"dependency not found: {edit}")
                local[node] = replace(edge, **{kind: inputs - {path}})
            altered = Graph(manifest, targets, local) if edits else graph
            yield Variant(name, assumption, altered, seconds)
        except (ValueError, KeyError) as exc:
            yield Variant(name, assumption, None, {}, str(exc))


FIELDS = ("kind", "changeset", "scenario", "status", "paths", "inert_paths", "issues", "dirty_edges", "work_s",
          "elapsed_s", "direct_edges", "direct_work_s", "rule_estimate_edges", "class_estimate_edges",
          "fallback_edges", "assumed_edges", "low_elapsed_s", "high_elapsed_s", "restat_edges",
          "restat_unchanged_edges", "restat_unchanged_elapsed_s")


def evaluate(variant, costs, paths):
    graph = variant.graph
    dirty = graph.dirty(paths)
    counts = Counter("assumed" if node in variant.seconds else costs.labels[node] for node in dirty)
    times = {node: variant.seconds.get(node, costs.seconds[node]) for node in dirty}
    parents = graph.dependencies(dirty) if dirty else {}
    variable = {node for node in dirty if node not in costs.direct and node not in variant.seconds}

    def schedule(scale=1):
        durations = {node: value * scale if node in variable else value for node, value in times.items()}
        return graph.schedule(parents, durations, costs.jobs)

    point = schedule()
    restat_count = sum(graph.edges[node].restat for node in dirty)
    unchanged, unchanged_s = dirty, point
    if restat_count:
        unchanged = graph.dirty(paths, "unchanged")
        unchanged_s = graph.schedule(graph.dependencies(unchanged), times, costs.jobs)
    metrics = {"dirty_edges": len(dirty), "work_s": sum(times.values()), "elapsed_s": point,
               "direct_work_s": sum(times[node] for node in dirty if node in costs.direct and
                                    node not in variant.seconds),
               "low_elapsed_s": schedule(.25) if variable else point,
               "high_elapsed_s": schedule(4) if variable else point,
               "restat_edges": restat_count, "restat_unchanged_edges": len(unchanged),
               "restat_unchanged_elapsed_s": unchanged_s}
    for label in ("direct", "rule_estimate", "class_estimate", "fallback", "assumed"):
        metrics[f"{label}_edges"] = counts[label]
    return metrics, sorted(graph.edges[node].name for node in dirty)


def replay(repo, args, ref, index, proposals, costs):
    rows, explicit = [], {}
    for batch in workloads(repo, args, ref):
        paths, inert, errors = index.classify(repo, batch, args.inert_glob)
        for proposal in proposals:
            if proposal.graph is None:
                continue
            row = {"kind": batch.kind, "changeset": batch.id, "scenario": proposal.id,
                   "paths": json.dumps(batch.paths), "inert_paths": json.dumps(inert), "issues": json.dumps(errors)}
            if errors:
                row["status"] = "unsupported"
            else:
                metrics, outputs = evaluate(proposal, costs, paths)
                row.update(metrics, status="affected" if outputs else "unaffected")
                if batch.kind == "explicit":
                    explicit[proposal.id] = outputs
            rows.append(row)
    return rows, explicit


def summarize(rows, variants_):
    summaries = {}
    for variant in variants_:
        if variant.graph is None:
            summaries[variant.id] = {"unranked": variant.reason, "assumption": variant.assumption}
            continue
        history = [r for r in rows if r["kind"] == "historical" and r["scenario"] == variant.id]
        replayable = [r for r in history if r["status"] != "unsupported"]
        affected = [r for r in replayable if r["status"] == "affected"]
        total = sum(r["elapsed_s"] for r in replayable)
        work = sum(r["work_s"] for r in replayable)
        summary = {"assumption": variant.assumption, "examined": len(history),
                   "replayable": len(replayable), "affected": len(affected),
                   "unaffected": len(replayable) - len(affected),
                   "replayed_with_inert_declaration": sum(r["inert_paths"] != "[]" for r in replayable),
                   "unsupported": len(history) - len(replayable),
                   "dirty_edges": sum(r["dirty_edges"] for r in replayable),
                   "work_s": work, "elapsed_s": total,
                   "direct_work_pct": 100 * sum(r["direct_work_s"] for r in replayable) / work if work else None,
                   "affected_median_s": median(r["elapsed_s"] for r in affected) if affected else None}
        for label in ("direct", "rule_estimate", "class_estimate", "fallback", "assumed"):
            key = f"{label}_edges"
            summary[key] = sum(r[key] for r in replayable)
        for key in ("elapsed_s", "low_elapsed_s", "high_elapsed_s", "restat_unchanged_elapsed_s"):
            summary[key.removesuffix("_s") + "_s_per_100"] = (
                100 * sum(r[key] for r in replayable) / len(replayable) if replayable else None)
        if variant.id != "baseline" and replayable:
            base = summaries["baseline"]
            summary["saved_dirty_edges"] = base["dirty_edges"] - summary["dirty_edges"]
            summary["saved_work_s"] = base["work_s"] - work
            summary["saved_elapsed_s_per_100"] = base["elapsed_s_per_100"] - summary["elapsed_s_per_100"]
        summaries[variant.id] = summary
    return summaries


LIMITS = (
    "Independent content edits of existing files on today's graph; no historical configuration, source, or timing snapshots.",
    "Unrecognized files, structural changes and known configuration edits are excluded, not counted as zero. Explicit inert declarations cover only existing files absent from the graph and are recorded in the CSV. Unaffected means no modeled dirty edge, not a universal no-op.",
    "Assumes a clean prior build: no missing ordinary inputs/outputs, command changes, new/disappearing includes, build-log invalidation, or generator preflight. Missing/stale discovered dependencies can hide invalidation; see graph counts.",
    "Dependency snapshots come from valid Ninja deps-log records and single-rule GCC-style depfiles where applicable. Reachable dyndep or generator edges are rejected. Repeated manifest inclusion and unsupported syntax are rejected.",
    "Restat outputs all propagate in the main model. The alternate assumes every reached restat edge runs but none of its outputs changes; real effects can fall between these cases.",
    "Critical-tail-first list scheduling with job and pool limits (including console depth), not Ninja ready-queue order. No launch, load, jobserver, contention, or cache-state model.",
    "Direct costs match captured output names and command hashes in the current build log, not current manifest commands or input contents. Explicit CSV measurements are also direct. Other costs are same-rule medians (except CUSTOM_COMMAND), then class medians, then 1 s defaults.",
    "Low/high elapsed reruns scale only estimated/fallback costs by 0.25/4. These are sensitivity tests, not bounds or confidence intervals. Capture and scenario assumptions stay fixed.",
    "Totals per 100 replayable changesets include unaffected edits and exclude unsupported edits; they do not estimate frequency across all Git changesets.",
)


def write_reports(args, manifest, costs, graph, rows, explicit, proposals, repo, ref):
    result = {"repo": str(repo), "repo_head": run("git", "rev-parse", "HEAD", cwd=repo).strip(),
              "history_ref": args.ref, "history_tip": ref, "history_count_requested": args.count,
              "scenario_file": str(args.scenarios.resolve()) if args.scenarios else None,
              "build_dir": str(manifest.root), "jobs": costs.jobs,
              "targets": args.target or manifest.defaults, "pools": manifest.pools,
              "graph_nonphony_edges": len(graph.tasks), "inert_globs": args.inert_glob,
              "dep_stats_all_edges": dict(Counter(manifest.dep_status.values())),
              "dep_stats_active_edges": dict(Counter(manifest.dep_status[n]
                                                     for n in graph.tasks if n in manifest.dep_status)),
              "active_incomplete_dependency_edges": sorted(
                  manifest.edges[n].name for n in graph.tasks if manifest.dep_status.get(n) in
                  {"missing_or_stale_log_edges", "unread_depfile_edges"}),
              "always_dirty_edges": len(graph.dirty(set())), "timing_sources": costs.notes,
              "calibration": calibration(graph, costs), "limits": LIMITS,
              "historical": summarize(rows, proposals), "explicit": {
                  row["scenario"]: {**row, "outputs": explicit.get(row["scenario"], [])}
                  for row in rows if row["kind"] == "explicit"}}
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "report.json").write_text(json.dumps(result, indent=2) + "\n")
    with (args.output / "changesets.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"{args.output}: {costs.jobs} jobs; {len(graph.tasks)} actionable edges")
    for name, summary in result["historical"].items():
        if "unranked" in summary:
            print(f"{name}: unranked ({summary['unranked']})")
        elif summary["replayable"]:
            median_s = summary["affected_median_s"]
            median_text = f"{median_s:.2f} s" if median_s is not None else "none"
            print(f"{name}: {summary['elapsed_s_per_100']:.2f} s/100 replayable; "
                  f"{summary['affected']} affected, {summary['unaffected']} unaffected, "
                  f"{summary['unsupported']} unsupported; affected median {median_text}")
        elif summary["examined"]:
            print(f"{name}: no replayable changesets; {summary['unsupported']} unsupported")
    for name, row in result["explicit"].items():
        if row["status"] == "unsupported":
            print(f"{name} explicit: {row['issues']}")
        else:
            print(f"{name} explicit: {row['dirty_edges']} dirty edges, {row['work_s']:.2f} job-s, "
                  f"{row['elapsed_s']:.2f} elapsed s ({row['direct_edges']} direct)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--build-dir", type=Path, required=True, help="existing Ninja build directory")
    parser.add_argument("--capture", type=Path, action="append", default=[], help="recorder output; repeat in priority order")
    parser.add_argument("--durations", type=Path, help="CSV with output,seconds columns")
    parser.add_argument("--jobs", type=positive, help="defaults to first successful capture from this build dir")
    parser.add_argument("--repo", type=Path, default=Path.cwd(), help="path inside the source Git repository")
    parser.add_argument("--ref", default="origin/main", help="local historical ref (default: origin/main)")
    parser.add_argument("--count", type=int, default=200, help="first-parent diffs (default: 200; 0 skips)")
    parser.add_argument("--changed", nargs="+", help="one explicit content-edit path set, in addition to history")
    parser.add_argument("--target", action="append", default=[], help="Ninja target; repeat (default: manifest defaults)")
    parser.add_argument("--scenarios", type=Path, help="JSON proposal interventions")
    parser.add_argument("--inert-glob", default=[], action="append",
                        help="declare reviewed non-build paths, e.g. '.github/workflows/*'; repeatable")
    parser.add_argument("--output", type=Path, required=True, help="new output directory")
    args = parser.parse_args()
    if args.count < 0 or (args.count == 0 and not args.changed):
        parser.error("specify a positive count, or --count 0 with --changed")
    if not (args.capture or args.durations):
        parser.error("supply --capture or --durations")
    if args.output.exists():
        parser.error("--output must not exist")
    try:
        repo = Path(run("git", "rev-parse", "--show-toplevel", cwd=args.repo).strip())
        ref = run("git", "rev-parse", "--verify", f"{args.ref}^{{commit}}", cwd=repo).strip() if args.count else None
        manifest = Manifest(args.build_dir.resolve())
        manifest.add_deps()
        targets = [os.path.normpath(p) for p in (args.target or manifest.defaults)]
        if not targets:
            raise ValueError("manifest has no explicit defaults; specify --target")
        graph = Graph(manifest, targets)
        costs = Costs(manifest, args.capture, args.durations, args.jobs)
        proposals = list(variants(manifest, graph, costs, args.scenarios, targets))
        rows, explicit = replay(repo, args, ref, PathIndex(manifest), proposals, costs)
        write_reports(args, manifest, costs, graph, rows, explicit, proposals, repo, ref)
    except subprocess.CalledProcessError as exc:
        parser.exit(1, f"{exc}: {(exc.stderr or b'').decode(errors='replace')}\n")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"simulation failed: {exc}\n")


if __name__ == "__main__":
    main()
