---
name: gzs-pythonic-pattern-apply
description: Apply one authorized Pythonic design-pattern refactor while proving behavior and relevant boundaries remain intact. Use after a concrete candidate and target are selected; do not activate for general feature work or an unapproved codebase-wide rewrite.
compatibility: Requires Python source and a runnable project-approved behavioral verification seam.
metadata:
  govzero-version: "0.2.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Pythonic Pattern Application

Refactor one selected pattern shape into a simpler Python form while preserving
its observable behavior. An active project-owned implementation workflow owns
its scope, ordering, gates, and evidence; return results to it rather than
creating parallel lifecycle state.

## Project Python version and policy

For Python work, read project instructions and adopted policy before selecting
idioms, APIs or runtime targets. Resolve version evidence from the relevant
project's `.python-version` first, `pyproject.toml` second, and `.venv` third.
The version file records an execution selection; `requires-python` declares a
support range; the environment supplies an observed installed version. Use later
signals for fallback and consistency checks, not to override declared policy.
Inspect `pyvenv.cfg` and the environment interpreter when available; do not
create, activate or update an environment just to discover its version.

Reconcile these signals with tool/CI targets and the actual validation
interpreter. Report absent, ambiguous or conflicting evidence; do not infer
freshness from an installed version or a minimum supported version from one pin.
For host-bound code, inspect the host runtime separately; a development
interpreter does not establish the host's version or installed packages.

Within this skill's existing task scope, observe the selected family's current
Python idioms, stdlib advances and deprecations using versioned official
documentation. Preserve the project's tested support range and public behavior;
record concrete benefits, risks and adopt/defer/retain decisions. Follow project
policy over upstream defaults. A runtime upgrade alone does not establish code
currency, and this guidance does not authorize a broad modernization campaign or
turn this skill into a comprehensive Python-version audit.

## Discovery and fallback

Prefer the active project workflow and its test and metric commands. Otherwise
use the repository's documented checks and neighboring test style. Direct
source and test inspection is the floor for understanding the candidate; if
there is no runnable behavioral verification seam, identify that gap before
rewriting instead of claiming equivalence from code shape alone. No gzkit
receipt, external pattern archive, or specific test framework is required.

## Apply one candidate

1. Confirm the authorized candidate, intended Python construct, affected
   callers, supported Python version, and public or plugin contracts. If the
   proposed construct would erase a useful domain concept or architectural
   port, revise the target or return the candidate for review.
2. Establish a focused behavior test or executable characterization that
   covers the candidate's purpose and meaningful edge cases. Run it against
   the original implementation and record a pass. If it exposes a defect,
   distinguish defect repair from behavior-preserving refactoring and follow
   the project's correction route. Do not change an assertion merely to match
   the new implementation.
3. Capture only relevant before-state evidence, such as public API behavior,
   dependency direction, complexity, or class/module size, using project-owned
   probes when configured. Metrics inform the decision; they do not override a
   demonstrated semantic or boundary regression.
4. Change the smallest coherent slice. Recheck the focused behavior test
   unchanged, then affected callers and neighboring tests. Preserve
   observable behavior, compatibility, and required domain boundaries. If the
   selected Python form proves unsuitable, explain the revised form or stop;
   do not silently substitute a different design.
5. Run relevant after-state probes and the repository's complete required
   quality gate, unless the active workflow already owns that final gate.
   Investigate a meaningful metric regression rather than assuming fewer
   classes means a better design. Fix or revert a behavioral or boundary
   regression before calling the refactor complete.

Report the candidate and selected target, original and final shape, unchanged
behavior witness with before/after commands and results, relevant metric or
boundary changes, final gate outcome, and any limits. When a project workflow
requires receipts or reports, use its own mechanism and never invent evidence.
