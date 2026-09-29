## 05 — Part compilation strategies

Date: 2026-09-28. Status: measured, temporary changes restored.

Clang 21.1.8, Release, PCH and time tracing enabled, ccache disabled, eight
jobs. Each target run removes only Part's objects and PCH, then runs `fc-build
--target Part`. All compiler outputs have traces. The live Ninja history stays
intact. One run per case gives directional results, not a calibrated speedup.

| Part | Existing PCH | Majority PCH | High-cost PCH | Unity 4 | Unity 8 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Target elapsed, s | 69.52 | 47.93 | 40.34 | 43.97 | 38.17 |
| Compiler outputs, incl. PCH | 204 | 204 | 204 | 62 | 38 |
| Cumulative frontend incl. PCH, s | 317.36 | 153.88 | 86.53 | 143.48 | 106.65 |
| Peak sampled concurrent RSS, GiB | 2.74 | 2.60 | 2.53 | 2.82 | 3.01 |
| FeaturePartBox.cpp touch, s | 6.51 | 4.84 | 3.88 | 6.18 | 7.26 |
| Touch compiler outputs | 1 | 1 | 1 | 1 | 1 |

Majority PCH adds `App/ComplexGeoData.h` and `Mod/Part/App/TopoShape.h` to
Part's existing PCH. Current Ninja dependencies record them in 116 and 115 of
203 ordinary Part objects. Baseline traces attribute 69.4 and 33.3 inclusive
frontend seconds to them. PCH creation frontend rose from 3.62 to 4.22 seconds.

The earlier high-cost PCH trial adds `App/DocumentObject.h` and
`Mod/Part/App/PartFeature.h`. These reach only 63 and 54 of 203 objects, so
they do not meet the majority-use criterion, although baseline traces attribute
19.6 and 76.5 inclusive seconds to them. Its PCH creation frontend was 5.45
seconds. [Dependency counts](header-dependencies.json) include every baseline
Part object. Source edits did not rebuild either PCH. An edit to an added
header would rebuild all Part sources; that cost is unmeasured.

Unity uses the same [190 eligible sources](unity-eligible-sources.txt) for both batch sizes. The other 13
remain separate because a broad batch-four compatibility build found duplicate
`FC_LOG_LEVEL_INIT` globals and repeated definitions from the unguarded
`TopoShapeMapper.h`. The [exclusion list](unity-exclusions.txt) and CMake
snippets for [batch four](unity-4-configuration.cmake) and [batch eight](unity-8-configuration.cmake)
record the exact trial. The failed automatic-unity build is excluded from
timings. An eligible source edit rebuilds its whole unity batch; the measured
batch-eight edit took longer than the ordinary TU edit.

The high-cost PCH and unity eight had similar Part target times in these runs,
with different memory and incremental behavior. None can be extrapolated
to a whole-project clean build. Sampled RSS sums concurrent descendant process
RSS every 0.1 seconds; it can count shared pages more than once and miss brief
peaks. Preparation, trace archival, and analysis are outside the timed target
build. [Coverage](coverage.json) verifies 203 baseline sources partition into
190 unity sources and 13 exclusions, and all measured compiler outputs have
traces. [Metadata](metadata.json) records source hashes. Full metrics and trace summaries are in this directory; raw traces and
logs are under ignored `provenance/`.

Reproduce in the configured `build/clang-profile` directory with no other
builds running. Run `flock /tmp/freecad-build-optimization.lock python3
docs/build-optimization/05-part-strategies/run.py` for baseline and project
PCH, then the same command with `run-majority-pch.py` for the majority PCH,
`run_unity.py` for selective unity, and `run-eligible-source.py` for the
matched source edit. The scripts restore the
original Part PCH and CMake files and bring Part up to date at exit.
