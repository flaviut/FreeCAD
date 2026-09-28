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


## 03 — Reduce material header dependencies

Date: 2026-09-28. Status: complete; both header dependency reductions retained.

### Initial analysis

With PCH enabled, project headers account for much of the remaining repeated
parsing. The experiment 02 profile reports cumulative inclusive times of 472 s
for `DocumentObject.h`, 428 s for `PartFeature.h`, 327 s for `Application.h`,
274 s for `PropertyMaterial.h`, and 272 s for `Materials.h`. These times overlap
and must not be added as independent savings.

One dependency path is `PartFeature.h` → `PropertyMaterial.h` → `Materials.h`.
`Materials.h` includes `App/Application.h` and `MaterialValue.h`; the latter
includes `Gui/MetaTypes.h`, which brings in document objects, observers, geometry
and Qt metatype declarations. The material implementation files already include
several of these dependencies directly. Inspect which declarations the public
headers actually need before changing the implementation boundary.

Include What You Use (IWYU) can suggest missing and unnecessary includes and
forward declarations. Clangd Include Cleaner provides editor diagnostics;
clang-tidy's `misc-include-cleaner` provides batch diagnostics for the main file.
These tools check symbol dependencies, not build cost, and cannot decide which
inline operations should move into implementation files. IWYU rejects PCH
invocations; a separate configuration without PCH is needed for its analysis.
For Clang 21, the corresponding IWYU release is 0.25. Tool suggestions require
review for Qt metatype declarations, generated code, and conditional builds.

References: [IWYU](https://include-what-you-use.org/),
[clangd Include Cleaner](https://clangd.llvm.org/guides/include-cleaner), and
[clang-tidy include cleaner](https://clang.llvm.org/extra/clang-tidy/checks/misc/include-cleaner.html).

### Hypothesis

Removing `Application.h` from `Materials.h` and replacing `Gui/MetaTypes.h` in
`MaterialValue.h` with its specific required type headers will reduce frontend
work in material consumers. Moving metatype-dependent inline operations into
implementation files is an additional candidate only if required by the audit.
Expect a smaller compilation gain than enabling PCH, but potentially fewer
recompiled translation units after editing common application or GUI headers.
Alternative paths and PCH contents may preserve these dependencies and limit
the rebuild benefit; measure that explicitly.

### Procedure

1. Preserve the current PCH configuration and source baseline. Keep Clang 21,
   Release flags, disabled ccache, time tracing, and eight jobs fixed.
2. Bring the selected targets (`Materials`, `Part`, and `SketcherGui`) up to date.
   Measure a rebuild after deleting only their object and PCH outputs, preserving
   Ninja command history. Include prerequisite work and report actual TU/PCH sets.
3. Touch `src/App/Application.h` and `src/Gui/MetaTypes.h` separately and build
   those same targets. Capture elapsed time, changed Ninja outputs and traces.
   Record dependency membership to distinguish alternate include paths from
   actual removal of header dependencies.
4. Audit material headers and consumers. Remove `Application.h` in one Jujutsu
   commit, then replace the broad metatype include in a separate commit. Add
   direct includes where consumers previously relied on transitive declarations.
   Format before committing; preserve each change ID in the results.
5. Build after each change. Once stable, repeat the identical target deletion
   and header-touch measurements with PCH enabled. Archive failed attempts but
   exclude them from performance comparisons.
6. Verify a complete build with PCH disabled to expose dependencies masked by
   PCH, then restore PCH and verify the complete build. Run relevant headless
   CTest checks through `fc-test`, excluding `CommandLine_characterization`.
   Never start the GUI. Use `fc-build` for every build.
7. Record results, source revisions, actual compilation coverage, and limitations.
   Keep the two source changes independently identifiable; make no whole-project
   clean-build speedup claim from target-only measurements. Single runs provide
   directional evidence, not a statistically established speedup.


### Results

Both changes passed the selected-target compatibility builds with PCH enabled:

- `tkkwtqno` (`9a779000`): remove `App/Application.h` from `Materials.h`.
  `Materials.cpp` already includes it directly.
- `onqurqry` (`48b06005`): replace `Gui/MetaTypes.h` in `MaterialValue.h` with
  direct Base and Qt type headers and `<utility>`. Add explicit metatype includes
  to three material GUI delegate implementations that convert quantities.

No inline operations needed moving: the inline list conversions use Qt's
`QList<QVariant>` metatype, while quantity conversions already live in `.cpp`
files. No new metatype header or duplicate declarations were introduced.

The target rebuild deletes exactly 287 objects (32 Materials, 203 Part, 52
SketcherGui) and three PCH files. Baseline and reduced configurations rebuilt
identical compilation output sets. Header touches request the same three targets
and include their prerequisite targets; the TU counts below include that work.
Neither header-touch case rebuilt a PCH. All six datasets have complete valid
trace coverage, with no missing or invalid traces.

| Measurement | Baseline | Reduced headers | Change |
| --- | ---: | ---: | ---: |
| Target rebuild elapsed, including PCH | 142.254 s | 128.084 s | -10.0% |
| Target combined compiler time | 848.759 s | 748.883 s | -11.8% |
| Target combined frontend time | 630.213 s | 544.680 s | -13.6% |
| `Application.h` touch elapsed | 253.338 s | 236.520 s | -6.6% |
| `Application.h` touch TUs | 515 | 500 | -2.9% |
| `Gui/MetaTypes.h` touch elapsed | 180.986 s | 104.993 s | -42.0% |
| `Gui/MetaTypes.h` touch TUs | 293 | 152 | -48.1% |
| `Gui/MetaTypes.h` touch frontend time | 867.651 s | 382.544 s | -55.9% |

The strongest result is reduced rebuild scope after the GUI metatype header
changes. Of the 141 eliminated recompilations, 54 are in Part, 38 in PartGui,
21 in SketcherGui, 15 in Materials, 12 in Sketcher, and one in MatGui. No new TUs
were added to that rebuild. The application header removes only 15 recompilations
(five Materials and ten MatGui); other include paths preserve the dependency in
the remaining targets. This confirms why removing a direct include does not
necessarily eliminate the corresponding rebuild dependency.

See [comparison and exact TU differences](03-material-headers/comparison.json),
[target baseline](03-material-headers/baseline-targets/analysis.md),
[target result](03-material-headers/reduced-targets/analysis.md), and
[metatype touch result](03-material-headers/reduced-metatypes-touch/analysis.md).
Per-run metrics, TU/PCH CSVs and trace summaries are retained alongside them.
Raw traces, logs, dependency snapshots, configuration, compilation database, and
the measurement scripts remain local under `03-material-headers/provenance/`.

A focused Clang 21 `misc-include-cleaner` audit analyzed both headers as main
files with a filtered compilation database without PCH. It did not recommend
restoring either expensive include. It identified additional direct-include
hygiene opportunities (`QtGlobal` for `Q_UNUSED`, and providers for several
container and value types in `Materials.h`), plus a `QStringList` provider
warning despite that header already being included. These suggestions were
reviewed and left outside this experiment's two dependency removals. IWYU was
not run: the pinned Nix package provides IWYU 0.26 with Clang 22; the matched
Clang 21 include cleaner was readily available instead. Audit logs are preserved
in provenance.

The measurements compare the combined changes, not their separate performance
contributions. These are single runs under the same PCH configuration and eight
jobs. No whole-project clean-build speedup is inferred, and rebuild counts apply
to the selected target dependency closure. The final full builds and tests are
correctness checks rather than controlled performance measurements.


### Validation and decision

The complete build with PCH disabled passed without further source fixes. It
rebuilt 2,109 objects; all 3,857 commands in the compilation database were free
of `-include-pch`. Objects unaffected by the configuration and header changes
were reused, so this is a full build validation, not a clean-build measurement.
The subsequent complete build after restoring `FREECAD_USE_PCH=ON` also passed.
The existing `build/clang-profile` directory was reused for these validation
configurations; the measured baseline and reduced-header series both used PCH.

Headless CTest validation passed: 2,189 reported tests, including two skipped
tests, with zero failures; eight additional tests were disabled. Runtime was
26.95 s including the wrapper. `CommandLine_characterization` was excluded
because it invokes the main executable. `DISPLAY` and `WAYLAND_DISPLAY` were
unset and Qt used the offscreen platform. See
[test summary](03-material-headers/tests-summary.json) and the local test log
and JUnit report under provenance. No GUI was started. GCC, MSVC, and other Qt
configurations were not revalidated.

Decision: retain both source commits. The measurements support the frontend
cost hypothesis and show a substantial reduction in rebuild scope for
`Gui/MetaTypes.h`; the application-header scope reduction is smaller. Preserve
the changes separately for later isolation. Clang's include cleaner is useful
as an advisory audit, with provider warnings reviewed before applying fixes.
Further direct-include cleanup and broader metatype-header splitting remain
separate experiments.

To repeat the selected-target measurements after bringing dependencies up to
date, use the preserved `provenance/run-series.py` with a fresh label. It records
Ninja dependencies, removes only the selected targets' object/PCH files, then
runs the target rebuild and the two header-touch rebuilds using `fc-build`.
It preserves the live Ninja log and archives only changed output records and
traces. Run the shared analyzer on each resulting provenance dataset. Avoid
other compilation or analysis jobs during the measured series.


## 04 — Separate value and document Qt metatypes

Date: 2026-09-28. Status: proposed; not executed.

### Initial analysis

Experiment 03 removed 141 recompilations after a `Gui/MetaTypes.h` edit, but
material implementation files still include that header for value conversions.
The header combines declarations for Base vectors, matrices, placements,
rotations, and quantities with `App::SubObjectT` and `App::DocumentObject*`.
It includes both `App/DocumentObject.h` and `App/DocumentObserver.h` to supply
the document types. A consumer needing only quantity conversion therefore
also receives document dependencies.

The remaining material consumers include `MaterialValue.cpp`, `Materials.cpp`,
`PyVariants.h`, and the three delegates updated in experiment 03. The delegates
use `Base::Quantity` QVariant conversions; audit their other dependencies before
migrating them. `Gui/CMakeLists.txt` explicitly lists `MetaTypes.h`, so the new
header should follow that source-list convention.

### Hypothesis

Extract the Base value metatype declarations into a small companion header,
initially beside `Gui/MetaTypes.h`, and keep the existing header as a compatible
umbrella that includes it. Switch material consumers that need only these value
metatypes to the companion header. This should reduce their frontend work and
rebuild scope after edits to document headers or the remaining umbrella.
Alternative include paths and PCH may limit the gain; measure dependency removal
instead of assuming that changing an include removes it.

This tests the broader metatype split deferred by experiment 03 without changing
material storage, solver ownership, or PCH contents. The post-experiment-03
[target profile](03-material-headers/reduced-targets/analysis.md) still attributes
39.9 inclusive seconds to `DocumentObject.h`; this is a ranking signal, not an
estimate of recoverable time or evidence that all of it comes from metatypes.

### Procedure

1. Record the current source revision and preserve experiment 03 artifacts.
   Keep Clang 21, Release flags, PCH enabled, time tracing, disabled ccache,
   dependencies, and eight jobs fixed. Use fresh datasets under
   `04-metatype-split/`; run every build through `fc-build`.
2. Audit `Gui/MetaTypes.h` consumers in `Materials` and `MatGui`, including
   shared headers such as `PyVariants.h`. Identify the metatypes each actually
   uses and record existing dependency membership for `DocumentObject.h`,
   `DocumentObserver.h`, and `Gui/MetaTypes.h`. Leave consumers requiring
   document metatypes on the umbrella. Check PCH and alternate include paths.
3. Move the Base declarations, with their direct type and Qt includes, into
   the companion header. Keep each `Q_DECLARE_METATYPE` in exactly one place;
   preserve the existing type names and registrations. Include the companion
   from the umbrella and update only audited material consumers. Add missing
   direct includes where needed. Register the header in the relevant CMake
   source/install lists if required by their existing conventions.
4. After compatibility builds, compare baseline and candidate using the same
   requested targets: `Materials`, `MatGui`, `Part`, and `SketcherGui`. Bring
   prerequisites up to date before each series. Measure deletion-only rebuilds
   of those targets' objects and PCH files, then separate touches of the three
   audited headers. Preserve the live Ninja log and capture only each run's
   changed output records and traces, including prerequisite work.
5. Run at least three series per variant, alternating baseline and candidate.
   Settle source-switch rebuilds before timing. Report individual wall times,
   medians and ranges, combined TU/PCH frontend costs, and exact changed output
   sets. Keep other compilation and analysis jobs idle during measurements.
   Record trace coverage and exclude failed/resumed runs from comparisons.
6. Validate complete builds with PCH disabled and then restored. Run relevant
   headless checks through `fc-test` with display variables unset and Qt's
   offscreen platform, excluding `CommandLine_characterization`. Exercise
   quantity/list QVariant round trips and existing document metatype consumers;
   add a focused regression test only if existing tests lack this coverage.
   Never start the GUI. Record compiler and Qt configurations actually checked.

### Decision criteria

Retain the split if correctness checks pass and it removes document-header
dependencies from audited consumers or produces a repeatable frontend/wall-time
gain without a material rebuild regression. Report scope reductions separately
from timing improvements. If alternate paths preserve all dependencies and
timing differences remain within observed variation, reject or narrow the trial.
Do not infer a whole-project clean-build speedup from these target measurements.
Record results and source change IDs here before considering migration of
additional modules or further splitting individual value metatypes.
