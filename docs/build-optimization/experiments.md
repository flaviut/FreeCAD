# Build optimization lab log

## 01 — Initial Clang analysis

Date: 2026-09-28. Status: complete; original artifacts archived.

Clang 21.1.8, Release (`-O3 -DNDEBUG`), Ninja, eight compile jobs,
`BUILD_ENABLE_TIME_TRACE=ON`, ccache disabled, PCH disabled. The separate
`build/clang-profile` configuration leaves the existing GCC build available.

| Measurement | Baseline |
| --- | ---: |
| Build elapsed time from Ninja log | 1,672.3 s (27m 52s) |
| Translation units with traces | 3,857 |
| Cumulative compiler time | 12,298.6 s |
| Frontend | 10,405.3 s (84.6%) |
| Backend | 1,842.4 s |
| Slowest translation unit | Pivy wrapper, 81.1 s |

The dominant opportunity is repeated frontend work across translation units.
Qt, application/geometry headers, and `<format>` recur among expensive includes;
formatting and Qt metatype templates recur among costly instantiations. Header
and template rankings are inclusive: nested event times must not be added as
independent savings. Compiler durations are elapsed times under parallel load,
not CPU accounting and not a direct prediction of build wall time.

The existing CMake PCH option was declared only under MSVC. The Clang cache had
no PCH setting, and its Ninja graph contained no PCH compilation rules.

Artifacts: [original analysis](01-initial-analysis/analysis.md),
[translation units](01-initial-analysis/translation-units.csv),
[trace manifest](01-initial-analysis/trace-manifest.json), and
[metadata](01-initial-analysis/metadata.json). The original analyzer is preserved
beside them. All 3,857 JSON traces (2,309,811,473 bytes) were moved into
`01-initial-analysis/traces/`, preserving their build-relative paths. Build logs,
cache, compile commands, and Ninja graph/log are in `01-initial-analysis/provenance/`.
Raw traces and provenance remain local, ignored by VCS; summaries and the checksum
manifest are tracked. The original analyzer assumes the old build directory layout;
use the shared analyzer for subsequent experiments.

The source snapshot at archival is Jujutsu change `tmllswqn`, commit `11eaf92b`.
The initial build may precede the latest TechDraw edits, so comparisons with it
are exploratory rather than a perfectly controlled source-identical benchmark.

## 02 — Enable and tune PCH on Clang

Date: 2026-09-28. Status: complete; PCH enabled and QtCore tuning retained.

### Hypothesis

Reusing parsed headers within FreeCAD targets will materially reduce repeated
frontend work and clean-build elapsed time. Savings should exceed the cost of
creating PCH files. Existing PCH contents may need Clang compatibility fixes or
additional frequently used stable headers. PCH construction, memory use, and
invalidation can offset benefits; a source edit and a representative header edit
will help distinguish clean-build gains from development iteration costs.

### Procedure

1. Preserve experiment 01 before rebuilding. Isolate build-system/PCH source
   changes in separate Jujutsu commits, with `fc-format` before committing.
2. Expose `FREECAD_USE_PCH` for all compilers, retaining current defaults
   (MSVC on, other compilers off). Enable it explicitly in `build/clang-profile`.
3. Keep compiler, Release flags, dependency versions, time tracing, disabled
   ccache, and eight jobs fixed. Configure with CMake; execute builds only through
   `FREECAD_BUILD_DIR=$PWD/build/clang-profile FREECAD_BUILD_JOBS=8 fc-build`.
4. Run a compatibility build using existing PCH contents. Record failures and
   isolate any required fixes. Do not count failed/resumed build timings as a
   successful clean-build measurement.
5. Once compatible, clean the build through `fc-build --target clean`, archive
   previous traces/logs, and run a complete build. Save elapsed time, build log,
   Ninja log, ordinary TU traces, and PCH traces separately. Count PCH creation
   in the total cost and report missing traces explicitly.
6. Compare total wall time, frontend/backend totals, and matched per-target
   compilation costs with experiment 01. Inspect PCH coverage and remaining
   expensive repeated headers. If justified, tune one representative target and
   compare it before/after with the same target and job count, including its PCH
   creation cost. Keep tuning changes separately identifiable.
7. Measure a representative `.cpp` rebuild and a shared-header rebuild without
   changing file contents; report which targets are requested. Use headless
   tests relevant to the built configuration through `fc-test`; never start the GUI.
8. Record results, limitations, source change IDs, and whether to retain each
   change here. One run gives directional evidence; do not present it as a
   statistically established speedup.

### Results

The compatibility build passed with existing PCH contents. No C++ compatibility
fixes were needed. Source changes are isolated:

- `lltqvzlk` (`c135c63b`): expose the CMake PCH option with unchanged defaults.
- `muynlmvt` (`ed360be4`): analyzer that includes PCH creation costs. Validation
  includes a synthetic TU/PCH fixture and comparison with the archived baseline.

The compatibility log contains Python/zipios macro redefinition warnings.
`fc-build --target clean` removed 8,620 outputs but exited nonzero because four
populated preference-pack directories could not be removed. These are resource
directories; verify compilation coverage after the measured rebuild before
accepting it as the clean compilation result. The clean log is retained.

The complete PCH build passed. All 3,857 baseline compilation outputs were rebuilt,
and all 3,902 compiler jobs (including 45 PCH jobs) have valid traces. This confirms
that the preference-pack cleanup errors did not leave compiled outputs cached.

| Measurement | Initial analysis | PCH enabled | Change |
| --- | ---: | ---: | ---: |
| Build elapsed | 1,672.3 s | 1,144.2 s | -31.6% |
| Combined compiler time | 12,298.6 s | 8,058.2 s | -34.5% |
| Combined frontend time | 10,405.3 s | 6,053.8 s | -41.8% |
| Backend time | 1,842.4 s | 1,896.1 s | +2.9% |
| Ordinary TU compiler time | 12,298.6 s | 7,822.6 s | -36.4% |
| PCH creation compiler time | 0 s | 235.6 s | included above |

The measured full build uses source state `muynlmvt` (`ed360be4`) and existing
PCH contents. PCH generation accounts for 2.9% of combined traced compiler time.
See [analysis](02-clang-pch/analysis.md), [summary](02-clang-pch/summary.json),
[wall-time measurement](02-clang-pch/clean-build-metrics.json), and
[compilation coverage](02-clang-pch/clean-build-coverage.json).

Measurement limitations: the initial elapsed value comes from Ninja; the new
value includes the `fc-build` wrapper. The baseline analyzer validation overlapped
the beginning of the new full build, adding some CPU/I/O load. It reproduced all
initial phase totals and found all 3,857 traces. These are single-run exploratory
measurements, with the source-snapshot caveat described in experiment 01.

A first target-only attempt was discarded: removing `.ninja_log` invalidated
Ninja's command history and caused dependencies to rebuild. It was interrupted;
its log and partial traces are retained under `provenance/discarded-target-log-reset`.
Subsequent target measurements preserve the live Ninja log and extract only
changed output records into a separate dataset. Dependencies are brought up to
date before each controlled target rebuild.

### Target tuning: explicit `<format>`

The controlled target baseline removes only SketcherGui's 52 object files and
one PCH, preserves Ninja command history, and builds `--target SketcherGui` at
eight jobs. The live build log is retained; each measurement captures changed
Ninja output records and their traces under `02-clang-pch/provenance/<label>`.
Incremental runs touch (without changing contents) `Utils.cpp` or
`ViewProviderSketch.h`, then build the same target. The `.cpp` touch actually
recompiled seven TUs; the header touch recompiled 32. Both configurations rebuilt
the same TU sets. Reports and metrics record the actual work, not an assumption
that one source touch always means one compile.

| SketcherGui measurement | Existing PCH | Explicit `<format>` |
| --- | ---: | ---: |
| Target rebuild elapsed (52 TUs + PCH) | 52.565 s | 56.328 s |
| Combined compiler time | 329.862 s | 324.867 s |
| PCH creation compiler time | 5.832 s | 5.729 s |
| `Utils.cpp` touch elapsed (7 TUs) | 14.410 s | 13.930 s |
| `ViewProviderSketch.h` touch elapsed (32 TUs) | 45.999 s | 45.920 s |

Trial commit: `ksrwqrsw` (`79cc4abb`). Decision: reject the explicit `<format>`
addition. Both PCH traces already contain `<format>` through transitive includes;
the incremental differences are small and the target wall time did not improve.
The existing-PCH and format-PCH datasets are named `sketchergui-existing-*` and
`sketchergui-format-*`, with per-run metrics alongside them.

### Target tuning: broader QtCore precompilation

Hypothesis recorded before execution: adding `<QtCore>` to SketcherGui's PCH
will amortize the remaining umbrella-header parsing, especially SIMD/intrinsic
headers. Existing-PCH traces attribute 35.844 inclusive seconds to `QtCore/QtCore`
across ordinary TUs, mostly reached through `ViewProviderPreviewExtension.h`.
This uses a stable external dependency rather than a frequently edited project
header. The larger PCH has a construction/deserialization cost, so compare the
same full target and both incremental rebuilds, including PCH generation.
Remove the redundant `<format>` trial inclusion as part of this change.

Trial commit: `loktkmvz` (`2471be9f`). The net tuning relative to existing PCH
contents is one additional `<QtCore>` include; the explicit `<format>` addition
is absent in the final source.

| SketcherGui measurement | Existing PCH | With `<QtCore>` | Change |
| --- | ---: | ---: | ---: |
| Target rebuild elapsed (52 TUs + PCH) | 52.565 s | 49.654 s | -5.5% |
| Combined compiler time | 329.862 s | 287.268 s | -12.9% |
| Combined frontend time | 243.390 s | 203.599 s | -16.4% |
| PCH creation compiler time | 5.832 s | 6.875 s | +17.9% |
| `Utils.cpp` touch elapsed (7 TUs) | 14.410 s | 13.080 s | -9.2% |
| `ViewProviderSketch.h` touch elapsed (32 TUs) | 45.999 s | 39.754 s | -13.6% |

Decision: retain QtCore precompilation provisionally. Its extra PCH construction
cost is outweighed by reduced ordinary-TU frontend work, and both incremental
measurements improved. This is one run per case, not a statistical performance
guarantee. Reports use the `sketchergui-qtcore-*` prefix. All nine target/incremental
measurements have complete trace coverage. Editing the PCH source also triggers
Qt autogen, so the tuned target runs record four more noncompiler Ninja output
records than the deletion-only baseline; compiler job counts remain identical.

The final full build with the retained tuning passed. The 19m 4s whole-project
measurement above predates the QtCore tuning; only the target measurements
quantify its extra benefit. No whole-project speedup is extrapolated from them.
Headless regression checks completed with zero failures. CTest reports 2,189
tests, including two skipped tests; eight additional tests were disabled.
The run took 28.01 s. `CommandLine_characterization` was excluded because it
invokes the main executable. `DISPLAY` and `WAYLAND_DISPLAY` were unset and Qt
used its offscreen platform. Command:

```sh
env -u DISPLAY -u WAYLAND_DISPLAY QT_QPA_PLATFORM=offscreen \
  FREECAD_BUILD_DIR=$PWD/build/clang-profile \
  fc-test -j 8 --timeout 120 -E '^CommandLine_characterization$'
```

See [test summary](02-clang-pch/tests-summary.json); the full test log and final
build log are retained under `02-clang-pch/provenance/`.

### Reproduction and follow-up

The current Clang configuration has PCH enabled. Reconfigure an equivalent Clang
build with `FREECAD_USE_PCH=ON`, `BUILD_ENABLE_TIME_TRACE=ON`,
`FREECAD_USE_CCACHE=OFF`, and `CMAKE_BUILD_TYPE=Release`, then run:

```sh
FREECAD_BUILD_DIR=$PWD/build/clang-profile FREECAD_BUILD_JOBS=8 fc-build
```

The compiler and all original dependency/cache details are retained in experiment
01 provenance. Full and target trace datasets, per-run logs, Ninja records, and
the timing harness are retained locally in experiment 02; summaries/metrics are
tracked. To analyze a live build or a target dataset with its own `.ninja_log`:

```sh
python3 docs/build-optimization/analyze.py \
  --build-dir docs/build-optimization/02-clang-pch/provenance/sketchergui-qtcore-pch \
  --output-dir /tmp/sketchergui-qtcore-analysis
```

Preserve the live Ninja log when timing partial rebuilds. A measurement dataset
must contain only that invocation's changed output records, not the accumulated
log from multiple invocations. For the complete archived builds, raw traces are
under `traces/` and the corresponding Ninja log is under `provenance/`; stage them
with the Ninja log at the trace root before passing that root to the analyzer.

Recommended next investigation: repeat the controlled target comparison to
establish variance, then consider applying stable-header PCH tuning to other
large targets. The remaining SketcherGui profile also points to project header
coupling (`ViewProviderSketch.h`, `SketchObject.h`, and related geometry headers),
which merits a separate header-dependency experiment. Defaults outside MSVC
remain off; this experiment opts Clang in explicitly. GCC and MSVC builds were
not revalidated here.
