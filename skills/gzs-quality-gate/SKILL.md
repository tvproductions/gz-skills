---
name: gzs-quality-gate
description: Run and evidence the repository's complete required quality gate for the current change. Use for pre-handoff, pre-merge, pre-release, or explicit full-verification requests; use the project's declared commands rather than assuming a language or toolchain.
compatibility: Requires the target repository's documented verification tools.
metadata:
  govzero-version: "0.1.3"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Quality Gate

Prove the current tree satisfies the repository's own completion contract. The
portable invariant is complete, observed verification; the project supplies the
commands, thresholds, and required evidence.

## Discovery and fallback

Prefer, in order:

1. A documented aggregate gate the repository already owns. Read its
   implementation or help before assuming which dimensions it covers.
2. The per-dimension commands the repository declares, assembled into the
   smallest complete sequence.
3. The tools actually configured in the tree, discovered from the build or
   project manifest, the task runner, and the continuous-integration
   definition, then invoked one dimension at a time.

The third rung is the floor and it always exists: a repository that configures
a linter or a test runner can be verified through those tools directly, even
with no aggregate to call. Record which dimensions had no owning command rather
than reporting a pass that covered fewer of them. For a planning or documentation
repository, discover checks for its actual artifacts; do not infer a requirement
for runtime code or behavioral tests from a scaffolded tool configuration.

## Applicability before execution

Resolve required dimensions from project policy, the declared stage and the
complete tree, including scripts, untracked files, existing tests, hooks and CI.
Distinguish an applicable pass, an evidenced **not applicable** dimension and an
unresolved failure or unavailable check. A documentation-only diff does not make
an existing implementation's required tests inapplicable.

Behavioral tests may be **not applicable: pre-implementation** when no implemented
behavior or test assets exist and project policy permits that result. Record the
inspected scope and authority, and run the applicable document, instruction,
configuration and repository checks. Do not create runtime code or placeholder
tests merely to make a planning-stage gate green. An approved inapplicable
dimension is not a skipped required gate or a passing test suite.

Diagnose zero-test discovery independently of its exit code. Existing runtime
code, executable helpers or tests require investigation of discovery, imports,
environment and missing tests; zero discovered tests alone never proves
inapplicability. Check the actual command/output rather than translating a
runner status into a universal allow-empty rule.

If the project permits pre-implementation work but its aggregate unconditionally
requires nonexistent tests, identify the owning configuration mismatch. When
repair is authorized, align the project-owned command, hook, CI and guidance as
applicable, then rerun the full aggregate. An inapplicability condition must
explain its evidence and automatically require tests when implementation,
executable tooling or test assets appear. A manual phase flag alone, permanent
allow-empty mode, hook skip or blanket status suppression is not a repair.
Preserve explicit unconditional requirements and approval rules; name the exact
policy conflict and smallest required correction when authority is absent.

## Workflow

1. Read applicable repository guidance and inspect the current diff. Determine
   which verification policy governs the changed scope.
2. Discover the canonical aggregate quality command. Prefer a documented
   repository script or task that already sequences lint, formatting checks,
   types, tests, builds, documentation, generated surfaces, and policy checks.
   Read its implementation or help before assuming what it covers.
3. If no aggregate exists, construct the smallest complete sequence from the
   repository's documented commands. Record each required dimension and its
   owning command, plus evidenced inapplicable dimensions, before running
   anything; completion means no required dimension is silently omitted.
4. Run the gate without filters that mask its exit status. Capture the command,
   exit code, relevant counts, warnings, and generated receipts or reports.
5. When the request includes fixing failures, diagnose and correct failures
   caused by the current work, then rerun from the first affected gate. Preserve
   unrelated user changes and do not weaken thresholds or suppress findings to
   manufacture a pass.
6. Run the final canonical aggregate gate or, when none exists, the complete
   verification sequence resolved during discovery on the unchanged candidate
   tree. Completion requires every command's observed exit status to be
   successful and every required artifact or report to exist. Justified
   inapplicability must be explicit in the final result; never relabel an
   observed failed aggregate as passed without correcting and rerunning it.
   Missing required commands remain explicit gaps and prevent a full-pass claim.

## Evidence

Report the verified tree identity or worktree scope, commands and exit codes,
test and coverage counts when available, warnings, generated evidence paths,
and every inapplicable, skipped or unavailable dimension with its authority and
reason. State which applicable checks passed without implying nonexistent
behavioral coverage. A partial or unavailable required gate is not a full pass.
