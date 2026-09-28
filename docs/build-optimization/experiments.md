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

Date: 2026-09-28. Status: procedure recorded before execution.

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

Pending.
