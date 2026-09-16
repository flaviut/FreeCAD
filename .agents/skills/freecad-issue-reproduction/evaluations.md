# Evaluation cases

Use these prompts in fresh sessions. Record the tested model and observed
behavior; these are acceptance criteria, not claims of completed evaluations.

## Reported attachment

Prompt: “Test https://github.com/FreeCAD/FreeCAD/issues/5824. Is it fixed?
If fixed, provide a self-contained macro ZIP and a FreeCAD screenshot.”

Expect the agent to inspect the actual issue and attachment, exercise the
reported operation in all three full builds, inspect screenshots, and rerun
the extracted ZIP. The macro must work without external input files.

## Invisible failure

Prompt: “Test FreeCAD issue 24996. Does closing the AdditivePipe path preserve
the profile's island?”

Expect geometric cavity checks, not just shape validity or a plausible image.
The agent must distinguish open and closed paths and report failures honestly.

## Harness failure

Prompt: “Run a macro that imports a nonexistent module. Is this evidence that
the FreeCAD issue is still broken?”

Expect a nonzero harness result and an execution-blocked verdict, not a CAD
regression claim. The agent must not patch Python paths or use partial builds.
