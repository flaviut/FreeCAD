#!/usr/bin/env python3
"""Capture fc-build, or record the CMake invocation from inside its wrapper."""

from collections import Counter, defaultdict
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
import time


def ninja_log(path):
    try:
        return path.read_bytes()
    except FileNotFoundError:
        return b""


def ninja_records(lines):
    for line in lines:
        fields = os.fsdecode(line).split("\t")
        if len(fields) == 5:
            yield fields


def git_context():
    context = {}
    for key, args in (
        ("commit", ["git", "rev-parse", "HEAD"]),
        ("status", ["git", "status", "--short", "--untracked-files=normal"]),
    ):
        try:
            result = subprocess.run(args, capture_output=True, text=True, timeout=5, check=True)
            context[key] = result.stdout.strip()
        except (OSError, subprocess.SubprocessError):
            context[key] = None
    return context


def cmake_context(build_dir):
    wanted = {
        "CMAKE_BUILD_TYPE", "CMAKE_C_COMPILER", "CMAKE_CXX_COMPILER",
        "CMAKE_GENERATOR", "FREECAD_USE_PCH", "FREECAD_USE_CCACHE", "CCACHE_PROGRAM",
        "BUILD_ENABLE_TIME_TRACE",
    }
    result = {}
    try:
        with (build_dir / "CMakeCache.txt").open(errors="replace") as stream:
            for line in stream:
                if ":" in line and "=" in line:
                    name, value = line.rstrip("\n").split("=", 1)
                    key = name.split(":", 1)[0]
                    if key in wanted:
                        result[key] = value
    except OSError:
        pass
    return result


def archive(folder, build_dir, command, started, start, elapsed, exit_code, before_log,
            git, cpu, profile):
    after_log = ninja_log(build_dir / ".ninja_log")
    before_header, *before_lines = before_log.splitlines() or [b""]
    after_header, *after_lines = after_log.splitlines() or [b""]
    before = {row[3]: row for row in ninja_records(before_lines)}
    after = {row[3]: row for row in ninja_records(after_lines)}
    changed = {output: row for output, row in after.items() if before.get(output) != row}

    if after_log:
        (folder / ".ninja_log").write_bytes(after_log)

    if profile:
        # Ninja can compact the log instead of appending to it.
        if after_log.startswith(before_log):
            lines = after_log[len(before_log):].splitlines() if before_log else after_lines
        else:
            counts = Counter(before_lines)
            lines = []
            for line in after_lines:
                if counts[line]:
                    counts[line] -= 1
                else:
                    lines.append(line)
        (folder / "run.ninja_log").write_bytes(b"\n".join([after_header, *lines]) + b"\n")
    metadata = {
        "schema_version": 1,
        "started_utc": started.isoformat(),
        "elapsed_s": elapsed,
        "build_start_monotonic_s": start,
        "child_user_cpu_s": cpu[0],
        "child_system_cpu_s": cpu[1],
        "exit_code": exit_code,
        "cwd": str(Path.cwd()),
        "build_dir": str(build_dir),
        "command": command,
        "jobs": os.environ.get("FREECAD_BUILD_JOBS"),
        "remote_worker_available": os.environ.get("FREECAD_BUILD_REMOTE") == "1",
        "distcc_hosts": os.environ.get("DISTCC_HOSTS", ""),
        "ccache_prefix": os.environ.get("CCACHE_PREFIX", ""),
        "cmake": cmake_context(build_dir),
        "git_before_build": git,
        "ninja_log_before_header": os.fsdecode(before_header) or None,
        "ninja_log_after_header": os.fsdecode(after_header) or None,
        "ninja_log_before_outputs": len(before),
        "ninja_log_after_outputs": len(after),
        "changed_outputs": changed,
    }
    (folder / "build.json").write_text(json.dumps(metadata, indent=2) + "\n")


def inner_folder(build_dir, started):
    build_id = hashlib.sha256(os.fsencode(build_dir)).hexdigest()[:12]
    stamp = started.strftime("%Y%m%dT%H%M%S.%fZ")
    root = Path.home() / ".cache/freecad-build" / f"{build_dir.name}-{build_id}"
    folder = root / started.strftime("%Y-%m") / f"{stamp}-{os.getpid()}"
    folder.mkdir(parents=True, exist_ok=False)
    return folder


def capture_env(folder, build_dir):
    env = os.environ.copy()
    env["CCACHE_STATSLOG"] = str(folder / "ccache.log")
    env["LD_STATS"] = "-"

    ccache = cmake_context(build_dir).get("CCACHE_PROGRAM")
    if not ccache or not Path(ccache).is_file():
        return env

    compilers = []
    for path in (build_dir / "CMakeFiles").glob("*/CMake*Compiler.cmake"):
        text = path.read_text(errors="replace")
        match = re.search(r'^set\(CMAKE_(C|CXX)_COMPILER "([^"]+)"\)', text, re.M)
        if match and f'set(CMAKE_{match[1]}_COMPILER_ID "GNU")' in text:
            compilers.append(match[2])
    if not compilers:
        return env

    prefix = subprocess.run([ccache, "-k", "prefix_command"], capture_output=True, text=True)
    if prefix.returncode:
        return env

    launcher = folder / "compile-prefix"
    cmd = shlex.join([sys.executable, str(Path(__file__).resolve()), "--compile"])
    launcher.write_text(f'#!/bin/sh\nexec {cmd} "$@"\n')
    launcher.chmod(0o700)
    env["CCACHE_PREFIX"] = str(launcher)
    env["FREECAD_PROFILE_PREFIX"] = prefix.stdout.strip()
    env["FREECAD_PROFILE_GCC"] = json.dumps(compilers)
    return env


def compile_output(args):
    try:
        return args[args.index("-o") + 1]
    except (ValueError, IndexError):
        return None


def compile_capture(args):
    prefix = os.environ["FREECAD_PROFILE_PREFIX"].split()
    output = compile_output(args)
    if args[0] not in json.loads(os.environ["FREECAD_PROFILE_GCC"]) or not output:
        os.execvp((prefix + args)[0], prefix + args)

    result = subprocess.run(prefix + args + ["-ftime-report"], stderr=subprocess.PIPE)
    # ccache stores stderr. Remove the phase table before it can be cached and replayed.
    table = re.search(rb"(?m)^Time variable[^\n]*\n(?:[^\n]*\n)*?^[ \t]*TOTAL[ \t]+[^\n]*\n",
                      result.stderr)
    if not table:
        sys.stderr.buffer.write(result.stderr)
        return result.returncode

    phases = Path(os.environ["FREECAD_PROFILE_DIR"]) / "phases"
    report = {"kind": "gcc", "output": str(Path(output).absolute()),
              "exit_code": result.returncode, "report": os.fsdecode(table[0])}
    try:
        with tempfile.NamedTemporaryFile(mode="w", dir=phases, prefix="gcc-", suffix=".json",
                                         delete=False) as stream:
            json.dump(report, stream)
            stream.write("\n")
    except OSError:
        sys.stderr.buffer.write(result.stderr)
        return result.returncode

    sys.stderr.buffer.write(result.stderr[:table.start()] + result.stderr[table.end():])
    return result.returncode


def proc_values(path, wanted):
    try:
        lines = Path(path).read_text().splitlines()
    except OSError:
        return {}
    return {key.rstrip(":"): int(value) for key, value, *_ in map(str.split, lines)
            if key.rstrip(":") in wanted}


def host_sample():
    sample = {"monotonic_s": time.monotonic()}
    try:
        with Path("/proc/stat").open() as stream:
            fields = stream.readline().split()
            sample["cpu_ticks"] = dict(zip(
                ("user", "nice", "system", "idle", "iowait", "irq", "softirq", "steal"),
                map(int, fields[1:9])))
    except OSError:
        pass

    sample["memory_kib"] = proc_values("/proc/meminfo", {"MemTotal", "MemAvailable",
                                                         "SwapTotal", "SwapFree"})
    sample["vmstat"] = proc_values("/proc/vmstat", {"pswpin", "pswpout"})
    sample["pressure_us"] = {}
    for resource_name in ("cpu", "memory", "io"):
        try:
            lines = Path(f"/proc/pressure/{resource_name}").read_text().splitlines()
        except OSError:
            continue
        for line in lines:
            kind, *fields = line.split()
            sample["pressure_us"][f"{resource_name} {kind}"] = int(fields[-1].split("=")[1])
    return sample


def sample_host(folder, stop):
    with (folder / "host.jsonl").open("w", buffering=1) as stream:
        while True:
            stream.write(json.dumps(host_sample()) + "\n")
            if stop.is_set():
                return
            stop.wait(1)


def tee_build(folder, env):
    with (folder / "build.log").open("wb") as log:
        with subprocess.Popen(["fc-build", "--verbose", "--", "-d", "stats"],
                              env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
            show = True
            for line in proc.stdout:
                log.write(line)
                if not show:
                    continue
                try:
                    sys.stdout.buffer.write(line)
                    sys.stdout.buffer.flush()
                except BrokenPipeError:
                    show = False
            return proc.wait()


def link_reports(folder, build_dir):
    # Ninja keeps each link's stdout together, even when several links run at once.
    report = []
    with (folder / "build.log").open(errors="replace") as stream:
        for line in stream:
            begins_report = line.startswith("Stats: linker version:")
            if report and (begins_report or (line.strip() and not line.startswith("Stats: "))):
                save_link(folder, build_dir, report)
                report = []
            if begins_report or report:
                report.append(line)
    if report:
        save_link(folder, build_dir, report)


def save_link(folder, build_dir, lines):
    # GNU ld prints argv without quoting; retain the raw command with the report.
    args = next((line for line in lines if line.startswith("Stats: args: ")), "")
    output = re.search(r"(?:^| )-o ([^\s]+)", args)
    report = {"kind": "gnu-ld", "output": str(build_dir / output[1]) if output else None,
              "report": "".join(lines)}
    with tempfile.NamedTemporaryFile(mode="w", dir=folder / "phases", prefix="link-",
                                     suffix=".json", delete=False) as stream:
        json.dump(report, stream)
        stream.write("\n")


def export_steps(folder, start, metadata):
    rows = ninja_records(ninja_log(folder / "run.ninja_log").splitlines()[1:])
    groups = defaultdict(list)
    for begin, end, _, output, command_hash in rows:
        groups[int(begin), int(end), command_hash].append(output)

    events = []
    lanes = []
    anchor = metadata.get("build_start_monotonic_s", start) - start
    with (folder / "steps.jsonl").open("w") as stream:
        for (begin, end, command_hash), outputs in sorted(groups.items()):
            stream.write(json.dumps({"start_ms": begin, "end_ms": end,
                                     "command_hash": command_hash, "outputs": outputs}) + "\n")
            lane = next((i for i, limit in enumerate(lanes) if limit <= begin), len(lanes))
            if lane == len(lanes):
                lanes.append(end)
            else:
                lanes[lane] = end
            events.append({"name": outputs[0], "cat": "ninja", "ph": "X", "pid": 1,
                           "tid": lane, "ts": round(anchor * 1e6) + begin * 1000,
                           "dur": (end - begin) * 1000, "args": {"outputs": outputs}})
    events.extend(host_events(folder, start))
    (folder / "trace.json").write_text(json.dumps({"traceEvents": events}))


def host_events(folder, start):
    prev = None
    with (folder / "host.jsonl").open() as stream:
        for line in stream:
            sample = json.loads(line)
            counters = {"Host memory (KiB)": sample["memory_kib"],
                        "Host swap (pages)": sample["vmstat"]}
            if prev:
                span = sample["monotonic_s"] - prev["monotonic_s"]
                if span > 0:
                    counters["Host pressure (%)"] = {
                        k: (v - prev["pressure_us"][k]) / (span * 1e4)
                        for k, v in sample["pressure_us"].items() if k in prev["pressure_us"]}
                ticks = {k: v - prev["cpu_ticks"][k] for k, v in sample.get("cpu_ticks", {}).items()
                         if k in prev.get("cpu_ticks", {})}
                total = sum(ticks.values())
                if total > 0:
                    counters["Host CPU (%)"] = {k: 100 * v / total for k, v in ticks.items()}
            for name, values in counters.items():
                if values:
                    yield {"name": name, "ph": "C", "pid": 2, "tid": 0, "args": values,
                           "ts": round((sample["monotonic_s"] - start) * 1e6)}
            prev = sample


def finish_capture(folder, started, start, elapsed, exit_code):
    path = folder / "build.json"
    metadata = json.loads(path.read_text()) if path.is_file() else {}
    metadata.update(capture_started_utc=started.isoformat(), capture_elapsed_s=elapsed,
                    capture_exit_code=exit_code,
                    gcc_phase_capture_enabled=(folder / "compile-prefix").is_file(),
                    trace_clock="Ninja offsets anchored approximately at CMake build start")
    export_steps(folder, start, metadata)
    link_reports(folder, Path(metadata.get("build_dir", Path.cwd())))

    ccache = metadata.get("cmake", {}).get("CCACHE_PROGRAM") or shutil.which("ccache")
    if ccache and (folder / "ccache.log").exists():
        result = subprocess.run([ccache, "--format", "json", "--print-log-stats"],
                                env={**os.environ, "CCACHE_STATSLOG": str(folder / "ccache.log")},
                                capture_output=True, text=True)
        if result.returncode == 0:
            metadata["ccache"] = json.loads(result.stdout)

    path.write_text(json.dumps(metadata, indent=2) + "\n")


def capture():
    started = dt.datetime.now(dt.timezone.utc)
    root = Path.home() / ".cache/freecad-build" / started.strftime("%Y-%m")
    root.mkdir(parents=True, exist_ok=True)
    folder = Path(tempfile.mkdtemp(prefix=started.strftime("%Y%m%dT%H%M%SZ-"), dir=root))
    (folder / "phases").mkdir()
    print(f"Build capture: {folder}", flush=True)

    stop = threading.Event()
    sample = threading.Thread(target=sample_host, args=(folder, stop))
    start = time.monotonic()
    sample.start()
    exit_code = 1
    try:
        exit_code = tee_build(folder, {**os.environ, "FREECAD_PROFILE_DIR": str(folder)})
    except FileNotFoundError as error:
        print(error, file=sys.stderr)
    except KeyboardInterrupt:
        exit_code = 130
    finally:
        elapsed = time.monotonic() - start
        stop.set()
        sample.join()
        try:
            finish_capture(folder, started, start, elapsed, exit_code)
        except (OSError, ValueError) as error:
            print(f"fc-build: unable to finish capture: {error}", file=sys.stderr)
    return exit_code if exit_code >= 0 else 128 - exit_code


def record():
    try:
        separator = sys.argv.index("--")
        if sys.argv[1] != "--build-dir" or separator != 3 or separator == len(sys.argv) - 1:
            raise ValueError
    except (ValueError, IndexError):
        print("usage: record-build.py --build-dir DIR -- COMMAND [ARGS...]", file=sys.stderr)
        return 2

    build_dir = Path(sys.argv[2]).resolve()
    command = sys.argv[separator + 1:]
    before_log = ninja_log(build_dir / ".ninja_log")
    git = git_context()
    started = dt.datetime.now(dt.timezone.utc)
    profile = os.environ.get("FREECAD_PROFILE_DIR")
    env = capture_env(Path(profile), build_dir) if profile else None
    cpu_before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    exit_code = 1
    try:
        exit_code = subprocess.call(command, env=env)
    except KeyboardInterrupt:
        exit_code = 130
    finally:
        elapsed = time.monotonic() - start
        cpu_after = resource.getrusage(resource.RUSAGE_CHILDREN)
        cpu = (cpu_after.ru_utime - cpu_before.ru_utime, cpu_after.ru_stime - cpu_before.ru_stime)
        try:
            folder = Path(profile) if profile else inner_folder(build_dir, started)
            archive(folder, build_dir, command, started, start, elapsed, exit_code, before_log,
                    git, cpu, profile)
        except (OSError, ValueError) as error:
            print(f"fc-build: unable to archive build log: {error}", file=sys.stderr)
    return exit_code if exit_code >= 0 else 128 - exit_code


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(capture())
    if sys.argv[1] == "--compile":
        sys.exit(compile_capture(sys.argv[2:]))
    sys.exit(record())
