---
name: gzs-root-cause-debugging
description: Diagnose technical failures through reproducible evidence and falsifiable hypotheses. Use when diagnosing or fixing a bug, failing test, regression, intermittent failure, or unexplained performance problem whose cause is not yet demonstrated; yield to any active project-owned incident, execution, or governance workflow.
compatibility: Works where a failure can be observed directly or through safe diagnostic instrumentation.
metadata:
  govzero-version: "0.1.1"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Root-Cause Debugging

Establish why the failure occurs before changing production behavior. Produce a
causal explanation supported by a repeatable observation, not a plausible story
or a patch that merely hides the symptom.

## Precedence and authority

1. Read the repository's active instructions and workflow state first.
2. When a project-owned incident, execution, or governance workflow is active,
   stay inside it. Supply the diagnostic discipline below without bypassing its
   stages, gates, state, locks, receipts, review, or attestation.
3. A request to diagnose authorizes read-only observation and safe runtime
   probes, not persistent repository edits or a production fix. Use additional
   instrumentation only when the request or active workflow authorizes it.
4. Skip this workflow for a mechanical correction whose cause is already
   demonstrated. Do not manufacture diagnostic ceremony around known facts.
5. Do not expose secrets, personal data, or sensitive payloads in logs or
   evidence. Redact while preserving the facts needed to distinguish hypotheses.

## Discovery and fallback

Prefer, in order:

1. An active project-owned incident or execution workflow, whose stages and
   gates stay in control.
2. The narrowest existing test or repository probe that exhibits the failure.
3. A minimal reproduction written for the occasion and run directly with the
   language's own interpreter or runtime.

The third rung is the floor and cannot be taken away: a reproduction you wrote
needs no project surface. Prefer the higher rungs anyway, because an existing
test names the seam the project already considers meaningful.

## Workflow

1. **Define the failure.** Record expected behavior, observed behavior, scope,
   environment, and the complete error or anomalous measurement. Separate facts
   from interpretations.
2. **Build the tightest reproduction.** Prefer the narrowest existing test,
   command, request replay, fixture, or safe probe that preserves the failure.
   For intermittent behavior, measure frequency and correlate conditions rather
   than calling one successful run a resolution.
3. **Localize the boundary.** Inspect the failing entry point, recent relevant
   changes, data and control flow, immediate callers, shared utilities, and a
   nearby working analogue. Prefer available tracing and logs. Add
   instrumentation only where it can distinguish upstream input, local
   transformation, and downstream output, and only with the required authority.
4. **Test one hypothesis.** State one proposed cause and the observation it
   predicts. Run the smallest probe that could disprove it, changing one
   variable at a time. Record the result before forming the next hypothesis.
5. **Reassess instead of guessing.** After three materially different
   hypotheses fail, revisit the reproduction, assumptions, and system boundary.
   Surface the remaining uncertainty or missing access rather than escalating to
   speculative changes.
6. **Fix only when authorized.** If no existing test demonstrates the defect,
   add the smallest regression test and observe an assertion-level failure for
   the expected reason. Apply the narrowest change that corrects the causal
   failure class; avoid unrelated cleanup.
7. **Verify the result.** Re-run the original reproduction, the focused
   regression coverage, and then the repository's required quality gate. When
   another active workflow owns verification, return the evidence to that
   workflow instead of declaring its lifecycle complete.

## When the cause cannot be proven

A bounded diagnosis is a valid result when the failure cannot be reproduced or
the decisive system boundary is inaccessible. Preserve safe instrumentation or
a precise next probe when authorized, state what was ruled out, and name the
missing observation. Do not label a correlation or leading hypothesis as root
cause.

## Completion evidence

For diagnosis-only work, report the reproduction, observations, hypotheses and
outcomes, demonstrated cause or bounded uncertainty, and the smallest justified
next action. For an authorized fix, also report the regression witness, changed
causal boundary, original-reproduction result, focused verification, and the
project quality-gate outcome or its owning workflow.
