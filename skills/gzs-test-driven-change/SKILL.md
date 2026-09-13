---
name: gzs-test-driven-change
description: Implement one authorized behavior change through a tight red-green-refactor loop with an assertion-level failing test as the negative control. Use when the user explicitly requests test-driven development, test-first work, or red-green-refactor; do not activate merely because an ordinary implementation should include tests.
compatibility: Requires an executable behavioral surface or a repository-approved way to create the smallest runnable test scaffold.
metadata:
  govzero-version: "0.1.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Test-Driven Change

Drive one authorized behavior change with a meaningful red-green-refactor loop.
The failing test is a negative control that proves the test can detect the
missing behavior; the loop is not a ceremony for maximizing test count.

## Precedence and fit

1. Read repository instructions, the authorized behavior, current worktree,
   and any active project-owned execution workflow. Stay within its allowed
   paths, ordering, state, gates, review, and attestation.
2. Identify the observable seam and the smallest next behavior. Prefer a public
   interface or stable internal boundary and the repository's existing test
   style. Do not change an interface, broaden scope, or invent behavior merely
   to make it easier to test.
3. Skip or adapt this workflow when the change has no executable behavioral
   surface. Generated artifacts, prose, and purely declarative metadata should
   be verified through their owning source or validator rather than forced into
   a low-value unit test.

## Red-green-refactor loop

1. **Red:** Write one focused test whose name and assertion express the missing
   behavior from an independent source of truth such as the request,
   specification, known-good example, or reproduced defect. Exercise real code;
   mock only nondeterministic or external boundaries that the repository
   already treats as replaceable seams.
2. Run the narrowest owning test command. A valid red is an assertion-level
   failure for the expected missing behavior. Import, collection, fixture,
   syntax, environment, or unrelated failures are test-infrastructure problems;
   correct them and rerun before changing production behavior. If the test
   passes immediately, determine whether the behavior already exists or the
   test is insensitive.
3. **Green:** Implement only enough production behavior to satisfy the failing
   example. Do not anticipate later cases, add speculative options, weaken the
   assertion, or rewrite unrelated code.
4. Rerun the focused test, then the smallest relevant neighboring coverage. If
   another test fails, correct the implementation or resolve a genuine contract
   conflict; do not change established expectations solely to obtain green.
5. **Refactor:** After green, improve names, duplication, or structure only
   within the authorized surface. Keep observable behavior fixed and rerun the
   affected tests after each refactor.
6. Repeat with the next independent example. Work in vertical slices—one test,
   one minimal behavior, one green result—rather than writing all imagined tests
   before learning from the implementation.

## Difficult seams

- For legacy behavior, first add a characterization test only when the current
  contract must be preserved, then create a separate red example for the
  intended change.
- For time, randomness, concurrency, networks, or processes, use existing
  controllable boundaries or introduce the smallest production-appropriate
  seam; do not add test-only production APIs or rely on sleeps.
- For migrations and generated outputs, test the owning transformation and
  regenerate with the repository's tool. Do not hand-edit generated artifacts.
- When no test can run until a minimal importable scaffold exists, create only
  the scaffold required by the repository, prove the test infrastructure works,
  and then obtain the behavior-specific red.
- For intermittent failures, first use the repository's diagnostic workflow to
  establish a repeatable witness. One lucky red or green run is not evidence.

## Completion evidence

Run the repository's complete required quality gate after the final green when
the containing workflow does not already own it. Report each behavior slice,
the red command and expected failure, the production change, focused and
neighboring green results, refactors, final gate result, and any behavior that
could not support a valid test-first loop. Return this evidence to an active
project workflow without declaring its broader lifecycle complete.
