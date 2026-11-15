# Architectural decisions: implementation review checkpoint

Date: 2026-11-15. Scope: the approved portable ADR contribution, not the planned
starter CLI. Baseline bundle 0.12.0 -> pending 0.13.0; new skill 0.1.0 and router
0.7.0. Implementation commit: `d65460efeba1cba8a3907b3b3e33c46c3fb9c650`.

The [owning design](../superpowers/specs/2026-11-15-architectural-decisions-design.md),
[plan](../superpowers/plans/2026-11-15-architectural-decisions.md) and actual Current
[ADR-0001 edition 1](../decisions/ADR-0001-001-standalone-architectural-decision-procedure.md)
govern this work. Actual separate approval and reviewed bytes remain in that ADR's
linked history. They were reused without new or inferred approval.

Shared B01-B16 canonical-source observations and publisher stop/continue controls
are preserved in [the canonical receipt](../evidence/2026-11-15-adr-canonical.json)
and its byte-exact ZIP. [Earlier runs](../evidence/2026-11-15-adr-behavior.md)
retain failures, environment limitations, newline reconciliation and reruns.
The canonical publisher stop fixture clarifies that local proposal drafting is
authorized while the real publisher remains read-only; it produces an identified
replacement proposal, leaves dependent configuration untouched and completes the
independent correction. The original less-explicit fixture omitted the proposal;
its stopping behavior is not presented as complete B01 acceptance.

Fresh Windows Codex discovery through the supported project-scoped vendored
installation advertises and reads the committed skill/template with observed
matching hashes. [Native candidate installations](../evidence/2026-11-15-0.13.0-native-candidate.json)
match all 21 skills/48 tracked resources in disposable Codex and explicitly
project-scoped Claude installations. These are separate observations; neither
substitutes for tagged channel acceptance. Actual model identity remains UNKNOWN.

Genuine internal use: during this implementation the controller reused real
ADR-0001 edition 1's approved choice of one portable skill/template under consumer
authority. The resulting change adds that skill, template and existing-router
routing; it adds no CLI behavior, runtime dependency, approval service, ledger,
consumer lifecycle or setup schema. Publisher instructions select the actual
policy, collection and canonical procedure. This is actual approved-decision use,
not fictional fixture approval. Independent implementation-alignment review is
still required and must be recorded before qualification/release completion.

The existing 32 unittest checks, Ruff lint/format, ty, 21 skill validators and
strict Claude validation pass on the implementation inputs. A nonblocking
missing-directory-icon warning remains; no directory submission is requested.
[Release freshness](../evidence/2026-11-15-0.13.0-freshness.json) verifies current
exact development selections; no upgrade is needed. Python 3.14 adds no required
runtime mechanism to this documentation-only contribution.

Remaining gates: the plan's additional unavailable-procedure/template and legacy
mapping controls, independent final alignment review, final clean package checks,
immutable publication and tagged channels. Backplane integration, starter/lite/
heavy binding qualification and other publishers' genuine use remain separate
owning work. No starter 0.10.0 release acceptance or CLI implementation is claimed.

The remaining named instruction controls now PASS on unchanged canonical source:
missing selected procedure and missing required template preserve explicit gaps
while independent correction proceeds; legacy `DECISION-A` edition 7 advances to
8 using the declared field/filename mapping and unchanged approval/history;
identity 9999 advances to new proposal ADR-10000 edition 001 with no cap or
renumbering. Actions and bytes are in the canonical archive and supplemental
receipt. These extend the existing runner only; no new verification framework
or product executable was introduced.

Task 1's original no-skill baseline covered standard naming/edition overflow,
missing approval/vague assent and material replacement. The legacy-convention
and identity-overflow supplements were run after authorship as positive controls;
they are not misrepresented as pre-authorship baseline observations. Their exact
inputs and actual results are preserved separately.

Independent final alignment review is now PASS; see the
[faithful returned review](architectural-decisions-2026-11-15-final.md).
No defects or fix pass. The genuine approved-decision reuse/alignment gate for
this publisher is satisfied. Release remains held for current OpenCode native
channel evidence, final immutable publication and tagged arrival; no CLI work.
