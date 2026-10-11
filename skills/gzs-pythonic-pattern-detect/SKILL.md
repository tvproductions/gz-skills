---
name: gzs-pythonic-pattern-detect
description: Review Python code for concrete design-pattern shapes that could be simpler with Python constructs. Use for a requested Pythonic pattern review or to triage suspected Java-style class scaffolding; do not use as a general lint or architecture audit.
compatibility: Requires inspectable Python source and its supported runtime policy; optional project-owned static analyzers.
metadata:
  govzero-version: "0.2.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Pythonic Pattern Detection

Review a bounded Python surface for pattern machinery that obscures behavior or
adds avoidable indirection. A recognizable pattern is a question to investigate,
not a defect by itself. This skill is read-only; do not rewrite code, create
work items, or mark a refactor complete.

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

Prefer the active project-owned review workflow and its configured scanner
when one exists. Otherwise inspect the selected source and callers directly,
using repository-owned complexity or type checks where useful. Source review
is the floor: the review must work without gzkit, an external pattern corpus,
or a particular analyzer.

## Review

1. Read repository guidance and resolve the requested code population. Keep
   generated files, tests, and unrelated modules outside scope unless they are
   needed to establish behavior or ownership.
2. Identify the pattern's roles from actual construction, calls, state,
   variation, and effects. Examples worth testing include a Strategy hierarchy
   that only dispatches one function, a Singleton that holds immutable shared
   data, or a Visitor that only selects behavior by a closed data type. Do not
   infer a rewrite solely from a class name, AST match, or complexity rank.
3. For each plausible candidate, compare its current responsibilities with a
   concrete Python alternative. Account for extension points, runtime version,
   public API and serialization contracts, dependency direction, domain terms,
   plugin behavior, and whether the existing abstraction isolates a real
   boundary. Preserve useful DDD and hexagonal seams even when they use classes.
4. Give each reviewed candidate a disposition: **refactor candidate** with a
   proposed target, **defer** with the missing evidence or constraint, or
   **retain** with the reason the current form earns its complexity. Explain
   the expected simplification and the behavior that a later application must
   preserve. Treat scanner hits as leads and record false positives.
5. Report file and line evidence, the observed roles, proposed Python form,
   disposition, risks, and the smallest useful verification seam. If no
   candidates survive review, state the inspected scope and limits; a quiet
   scanner alone does not prove the codebase is Pythonic.

When the user authorizes a specific refactor, route that one candidate to
`gzs-pythonic-pattern-apply` or the active project-owned implementation
workflow. Do not turn this review into a mandatory rewrite campaign.
