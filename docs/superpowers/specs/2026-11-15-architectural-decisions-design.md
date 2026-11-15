# Portable architectural decisions: owning design

Status: DESIGN APPROVED, November 15, 2026. The main conversation approved the
original design at `f847de530acb3e1ef0716b18b09a2ea48c2fdcae` (reply: “yes”),
then reviewed the remote GZKit naming precedent and directed “proceed with that
design”. The responsibility split and H5 naming clarification are retained.
Separate actual architectural approval is captured in
[Current ADR-0001 edition 1](../../decisions/ADR-0001-001-standalone-architectural-decision-procedure.md)
with its original reviewed bytes and exact human response. Design assent is not
substituted for that architectural response. Implementation-plan review remains
pending; no implementation or qualification is claimed by this status.

## Intent, authority and inputs

Deliver the portable ADR procedure/template required by starter 0.10.0 without
making its consumers adopt starter tooling, a language, or another lifecycle.
Read governing project policy and applicable decisions at design, execution and
review; reuse approved choices and expose consequential new choices before work.

Reviewed gz-skills base: `4a7abd79f483c6c9abfc8f9470694be847f1347d`, equal to remote main during reconnaissance. Published baseline: v0.12.0 at
`a8f67160475a6995391d2244188d7c38eda65dfb`. Starter authority is exact revision `f42e6f186f062493c09fc2c2dc935e9a64310e33`:
[approved contract](https://github.com/tvproductions/gz-starter/blob/f42e6f186f062493c09fc2c2dc935e9a64310e33/docs/superpowers/specs/2026-11-08-adr-practice-design.md),
[policy](https://github.com/tvproductions/gz-starter/blob/f42e6f186f062493c09fc2c2dc935e9a64310e33/docs/engineering/architectural-decisions.md)
and ADR-0001-001 at that revision. They establish shared requirements, not approval of companion internals. Preserve COB lightweight-source provenance
`dd1ab883c04e884678ed723959b17c5c364263d1` and its final audience guidance.

## Naming precedent: remote GZKit drydock

Reviewed the remote [classic ADR change order](https://github.com/tvproductions/gzkit/blob/8208381d149b8b8704bd012849332ed3a1f2fb38/docs/governance/harbor-classic-adr-change-order.md) at
`8208381d149b8b8704bd012849332ed3a1f2fb38`, especially the settled design and
H5 ruling of November 8. Reuse its decision/edition grammar rather than presenting
this contribution as inventing a naming scheme:

- Stable identity: `ADR-[0-9]{4,}`, starting with `ADR-0001` in a new collection.
- Edition file: `ADR-[0-9]{4,}-[0-9]{3,}-<slug>.md`; number and edition are
  zero-padded to minimum widths four and three, with no overflow rename or cap.
- Slug uses the stated `[a-z0-9-]+` grammar. Keep the readable kebab-case title;
  do not silently substitute a stricter parser contract.
- A revision changes the edition/filename, not the stable decision identity.
  Neither number is a product/release version. Preserve prior editions/history.
- Preserve suitable existing conventions and legacy records; an actual migration
  needs an explicit crossover and reconciliation, not a blanket rename.

The starter already uses `ADR-0001-001-title-in-kebab-case.md` from the shared
lightweight source. The precise width/slug rules above were reviewed in the main conversation
and accepted when the maintainer directed proceeding with this design.
GZKit records this as ratified planning; it is not proof of landed implementation.
Its drydock orders, resolver, ledger/event machinery, operator identity and
GZKit-specific crossover are outside this contribution. No GZKit dependency or
integration follows. Existing consumer policy retains authority.

## Approaches and proposed decision

1. **One supporting skill and template, with existing router integration.**
   Independently readable; an active project workflow retains ordering and state.
   Recommended agent proposal: it fits canonical horizontal-discipline ownership.
2. **Place the complete procedure in the router.** Fewer catalog entries, but
   conflates routing with decision authoring/review and lacks a focused primitive.
3. **Add a CLI/schema or approval service.** Deterministic enforcement could be a
   future separately justified product; it adds runtime/state contracts this
   increment does not need. Do not implement it through this contribution.

The separately reviewable architectural proposal is [ADR-0001 edition 1](proposals/ADR-0001-001-standalone-architectural-decision-procedure.md).
Require explicit approval of this design and separate explicit approval of that identified edition before dependent implementation. Preserve proposal bytes and
actual approval context; design, plan, test or release assent cannot substitute.

## Deliverables and behavior

Add `skills/gzs-architectural-decisions/SKILL.md`, `references/adr-template.md` and `agents/openai.yaml` beneath that skill. Use
independent version 0.1.0, display name GovZero Architectural Decisions, an explicit skill-naming default prompt and implicit invocation for relevant work.
Activate for consequential ownership, interface, dependency, persistence, recovery, trust, deployment or operational choices; direct ADR requests; decision
amendment/replacement; and review alignment. Exclude routine covered edits, generic architecture explanation and an unsolicited historical backfill program.

The skill MUST discover project instructions, selected policy source, actual ADR collection, applicable decisions, approval content and active workflow first.
Use project tooling where available, then direct readable records as the floor.
A missing tool never forces installation; inaccessible required authority remains
a gap. Respect suitable existing conventions through a stated semantic mapping. Do not impose this publisher's Python, branch, release or heavy-mode choices.

At design, execution and review checkpoints: cite and reuse applicable approved decisions; otherwise explain the choice, credible alternatives, rationale,
consequences and important uncertainty, then prepare an identified edition.
Verify separate human approval and reviewed content before dependent work. Pause
only that work; continue independent authorized tasks. Detect mid-work choices,
conflicting authorities and wrong-edition approval. Review drift requires a
correction or separately approved replacement; green tests confer no approval.
ADR approval grants no additional migration, deployment or publication authority.

The template MUST contain identity/edition, title, scope, context, alternatives,
decision/rationale, consequences, optional confirmation, approval evidence and
amendment history. Map `id`, `title`, `revision`, `state`, `decision_date`,
`revision_date`, `approved_by`, `approved_revision`, `approval_ref` explicitly.
For a new collection use `ADR-0001-001-title-in-kebab-case.md`; ids are stable and
never reused. Authoritative records use Current/Retired. Keep unapproved drafts
with design material, with approval fields unfilled and no authoritative state.
Do not require an index, ledger, machine-readable registry or receipt file.

Preserve actual explicit approval of the identified edition and exact reviewed
content through durable interaction/content references or an honest transcript
with source context, date, human identity and reviewed bytes/hash. A hash proves
content identity only. Preserve the proposal before administrative approval
capture and explain that transition. Never invent approval, history or dates.
Editorial amendments increment edition/date/filename, retain original approval
and decision date, and record the edit/history without architectural reapproval.
Material replacement gets a new identity and explicit approval; retirement needs
explicit authority, date/reason and replacement where applicable. Backfill states
observation, inference and unknowns separately; missing approval must be obtained
now. Requirements, plans, ADRs, evidence and releases evolve independently.

Selected immutable policy links and provenance-bound local copies both work.
Use the selected available policy, preserve adaptations and surface applicable
local/source conflicts. Missing policy/workflow/approval content withholds only
affected completion claims; no configuration or source copy proves discovery.

## Integration, scope and release accounting

Update the existing router/catalog and workflow guide to route ADR support at
all three checkpoints, standalone or under SP/project authority. Do not restart
an active process. Bind gz-skills AGENTS.md to its actual policy, collection and
selected skill. Select the immutable policy link above, `docs/decisions/`, and the
canonical skill path for this publisher. Add no mandatory extra stage to every small edit. Keep setup
schema, CLI, installers and other skills unchanged unless a demonstrated gap
requires a separately reviewed scope change. No SP fork or Backplane activation.

Reconcile README/catalog count, Claude's explicit catalog, origins/provenance,
individual review queue, roadmap, changelog and source-applicability record.
Retain existing uncommitted changes for separate review. Record finite release
scope in the existing roadmap: baseline 0.12.0 -> proposed 0.13.0 for this new
capability; new skill 0.1.0; router 0.6.0 -> proposed 0.7.0 for new routing support.
No major or stable promotion is proposed. Synchronize four bundle manifests,
source version fallback and owning-tool lock metadata during implementation;
marketplace refs/examples change through release preparation only.
Exclude published-dogfood environment implementation, profile integration,
MPAS additions, CLI/schema changes, new service/lifecycle and consumer propagation.

## Qualification and completion

Run actual agent behavior against frozen skill/template/policy inputs:

| Cases | Required observations |
| --- | --- |
| B01-B03 | Missing-approval stop, approved reuse/continuation, explicit conflict handling. |
| B04-B07 | Vague assent rejected, exact approval captured and work continued, wrong edition rejected, mid-work stop with independent work continued. |
| B08-B11 | Editorial history preserved, replacement/retirement authorized, honest backfill, independent record evolution. |
| B12-B13 | Drift reported despite green tests; no new operation authority; authorized local work proceeds. |
| B14 | Immutable source, offline selected local copy, conflicts and missing policy/workflow/approval subcases. |
| B15-B16 | Human-initiated ADR route; evidence recovery with uncertainty and focused supplement/ruling. |

Execute every B01-B16 case using the starter matrix's full verdicts; no keyword
or schema-only proxy. Preserve prompt, fixture bytes/hashes, loaded sources,
host/model/settings when available, operator responses, actions, verdicts,
failures and reruns. Mark unavailable metadata UNKNOWN. Fictional staged
approval is evaluation input, never genuine architectural approval. Compare a
bounded no-skill baseline; include post-approval action in continuation controls.

Exercise gz-skills' actual design/execution/review binding with B01 stop and B02
continue controls. Obtain genuine internal use of an approved/reused decision,
followed by alignment review; this contribution's owning ADR can supply it only
after actual approval and work. Starter/SP-BP owners supply their own bindings,
both adopter lanes and supported integration checks. Record reused shared
results/applicability; expand affected cases when a binding changes behavior or
reveals a discrepancy. Fresh-session native discovery and actual loaded sources
are separate from manual text loading, configuration and behavioral results.

Run README validation, native validators and packaging's clean release/artifact
checks, including source-independent reproducible builds and installed behavior.
Use project-owned managed/locked Python and tools; complete required release-time
freshness maintenance separately. Verify exact-tag Codex, Claude, OpenCode and
uvx channels under supported scope; unsupported host proof remains unverified.
No public-directory or registry claim follows. Recheck final immutable released
sources before the starter qualifies its exact combination. Keep component
versions/publication independent; all three internal uses remain propagation gates.

Drafting occurs in a registered detached worktree at the reviewed base. Preserve
the original dirty main and user settings. Before integration, review divergence
and reconcile only approved scope. Rollback unapproved drafts without resetting
main or changing installs; later release rollback preserves published identities.
A fresh builder checked the design and found nothing important left unresolved.
Actual design/architectural approval evidence is recorded above and in the Current
ADR. Remaining gates are implementation-plan review, execution, qualification and
release evidence; do not claim those results from the approvals.
