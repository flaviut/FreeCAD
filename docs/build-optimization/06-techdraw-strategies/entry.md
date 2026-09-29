# TechDraw compilation strategies

Clang 21 Release, eight jobs, ccache off, time tracing on. Each target measurement
removed only `TechDraw` compiler outputs after a successful compatibility build.
The live Ninja log was preserved. One `HatchLine.cpp` timestamp touch followed each
target run. All 98/98 baseline, 29/29 unity4, and 17/17 unity8 target compiler
outputs have valid traces; the source touches each have 1/1.

| Configuration | Target s | Frontend s incl. PCH | Peak sampled aggregate RSS GiB | Source touch s |
| --- | ---: | ---: | ---: | ---: |
| Existing PCH | 45.83 | 159.86 | 3.23 | 6.56 |
| PCH + `DocumentObject.h`, `DrawView.h` | 40.42 | 109.14 | 3.05 | 5.99 |
| Existing PCH + unity4 | 34.96 | 71.58 | 3.32 | 11.42 |
| Existing PCH + unity8 | 31.82 | 46.50 | 3.42 | 16.78 |

The baseline compiled 97 ordinary objects and one PCH. Unity4 compiled 24 unity
objects, four standalone objects, and one PCH; unity8 compiled 12 unity objects,
four standalone objects, and one PCH. The [unity4](unity4-source-manifest.json)
and [unity8](unity8-source-manifest.json) manifests confirm that both grouped
the same 93 baseline sources and left the same four sources standalone. The
excluded files are four `Property*List.cpp` sources. The initial unity8
compatibility build failed when
their `using namespace App` directives made `Part` ambiguous in a later source;
that attempt is excluded from timings. The final configurations built cleanly.

The source touch rebuilt `HatchLine.cpp` alone with PCH, a four-source unity group
with unity4, and a seven-source group with unity8. The corresponding frontend
times were 1.78, 3.21, and 4.40 seconds (expanded PCH: 1.34 seconds). Thus the
clean target gain has a visible incremental cost. Aggregate RSS is the 0.1-second
sampled sum of `fc-build` and descendant process RSS; shared pages may be counted
more than once. These are single runs, so the wall-time differences are
directional.

The baseline Ninja dependency records include `App/DocumentObject.h` in 90 of
97 ordinary objects and `TechDraw/App/DrawView.h` in 69. They appear in zero of
one PCH output, so adding them targets repeated work. The same records include
`DrawViewPart.h` and `Part/App/TopoShape.h` in 52 ordinary objects each. Candidate
PCH construction and import costs are included in the target numbers.

See [metadata](metadata.json) for source hashes, exact touched group members,
compiler totals, and coverage. [run-series.py](run-series.py) applies each
temporary configuration under the shared build lock, uses [measure.py](measure.py)
for timing, then restores original source and configuration and builds TechDraw.
Raw logs and traces are under the local ignored `provenance/` directory.
