# Catalog lifecycle contribution review

November 14, 2026. The maintainer clarified that gz-skills supplies capabilities
that complement needed development work; the catalog is not intended to become
a standalone lifecycle kit. Each skill needs a clear contribution, even when
it can be used independently of Superpowers.

Reviewed surface: the twenty canonical skill descriptions, purpose, workflow
boundaries and outputs at published v0.12.0, release commit
`a8f67160475a6995391d2244188d7c38eda65dfb`, plus the current review queue.
This is a review of the instruction interfaces presented to adopters. It does
not certify model execution or redo every skill's stable-contract review.

## Intent and assessment

The authority is the maintainer's clarification above and the repository's
[source boundary](../../AGENTS.md#source-and-boundary): standalone horizontal
disciplines serve an adopting workflow, which retains lifecycle ownership.
The [adopter direction](../../AGENTS.md#adopting-project-ecosystem-direction)
and [workflow guide](../../skills/gzs-router/references/workflows.md) require
both independent availability and complementary use alongside Superpowers.

Assessment: the catalog contains credible development contributions, but it
does not consistently explain those contributions in the individual skill
interfaces. The router's improved selection rules cannot supply a missing
ownership boundary when a destination is invoked directly. Lifecycle fit should
be assessed across all twenty skills before treating their roles as settled.
This requires focused review and corrections, not an automatic rewrite of all
skills or a new mandatory sequence.

Independent usability means a discipline can work without another plugin. It
does not mean the discipline must own requirements, implementation, approvals,
tracking and release. With Superpowers present, a useful complement may supply
evidence inside an existing stage rather than add another stage. Where the
owner already supplies equivalent work, skipping the duplicate is success.

## Role map

The roles below are proposed review targets grounded in the existing skill
interfaces. They are not new activation rules, lifecycle stages or approval
gates. An owner means the adopting project's actual workflow, including
Superpowers or Backplane when those are applicable and active.

| Skill | Need and entry point | Useful result returned to the owner | Review focus |
| --- | --- | --- | --- |
| `gzs-router` | Workflow ownership or next discipline needs resolving. | Selected owner and entry into an authorized task; advice when requested. | Preserve the 0.6.0 boundary: route without becoming the lifecycle owner. |
| `gzs-project-setup` | Explicit project adoption/profile configuration. | Preserved/selected minimal settings and truthful readiness findings. | Enablement; profile selection must not become a prerequisite for every bounded task. |
| `gzs-agent-context-diet` | Persistent instructions have duplicated material or exceed an actual budget. | Smaller instruction surface with binding invariants retained. | Cross-cutting instruction maintenance; no mandatory development stage. |
| `gzs-plan-audit` | An existing execution plan may omit requirements, exceed scope or lack adequate verification. | Cited alignment gaps for the plan's owner to resolve. | High priority: activation and PASS/FAIL language can resemble a second planning gate. |
| `gzs-hexagonal-architecture-audit` | A concrete architecture/boundary question or declared architectural constraint needs assessment. | Evidence about dependencies, boundaries and proportionate improvement options. | Advisory input to design/refactoring; no universal architecture mandate or parallel design approval. |
| `gzs-dependency-risk-audit` | Dependency security, support, licensing or provenance risk needs a decision. | Prioritized, dated risk evidence and mitigation choices. | Distinguish risk analysis from freshness/update execution; return the decision to its owner. |
| `gzs-root-cause-debugging` | An unexplained failure needs a demonstrated cause. | Reproduction, causal evidence and, when requested, a verified correction. | Choose one diagnostic owner; avoid layering this over equivalent Superpowers debugging. |
| `gzs-test-driven-change` | One authorized behavior needs an explicitly requested/project-required test-first loop. | Behavior-specific red/green evidence and the resulting change. | Choose one TDD discipline; justify standalone utility without repeating Superpowers' loop. |
| `gzs-cross-platform-python` | Python changes touch an actual supported OS/filesystem/process seam. | Identified assumption, bounded repair and platform-specific evidence/limits. | A risk-driven implementation/review complement; no blanket all-platform ceremony. |
| `gzs-quality-gate` | A required verification checkpoint needs the project's checks executed and evidenced. | Results for the actual candidate and applicable dimensions. | High priority: distinguish running the owner's checks from owning completion/approval or rerunning fresh evidence. |
| `gzs-change-review` | A bounded change needs independent defect/regression scrutiny. | Prioritized reachable findings, reviewed scope and residual risk. | Strong existing owner boundary; distinguish from intent fulfillment and automated checks. |
| `gzs-intent-audit` | Delivered behavior may not fulfill its authoritative specification or acceptance claims. | Observed fulfillment/correction findings routed to their existing owner. | High priority: distinguish a user-visible fulfillment check from another generic/spec-compliance review. |
| `gzs-tech-debt-review` | Maintenance planning needs an evidenced debt inventory and priorities. | Bounded findings, consequences and concrete fix routes. | Distinguish broad maintenance prioritization from defects in the current diff or a specific architecture question. |
| `gzs-pythonic-pattern-detect` | A bounded Python surface may contain avoidable pattern machinery. | Concrete candidates with behavioral/architectural rationale. | Candidate discovery for a maintenance decision; no class-name-driven rewrites or automatic implementation. |
| `gzs-pythonic-pattern-apply` | One candidate and refactor target are authorized. | A simpler implementation with before/after behavioral evidence. | Strong existing implementation-owner/return boundary; avoid duplicating its plan or lifecycle state. |
| `gzs-update-dependencies` | Project-managed dependencies/tools need maintenance, or an explicit freshness check. | Applied/verified scoped migration, or read-only findings when explicitly requested. | Verify current 0.5.0 action authority and handback to the active implementation/maintenance owner. |
| `gzs-repository-hygiene` | Workspace, packaging or generated/control surfaces show concrete drift. | Scoped hygiene findings and authorized repairs with evidence. | Keep cleanup bounded; do not turn every task into a repository-wide cleanup pass. |
| `gzs-git-sync` | An authorized remote save point is needed. | Validated commit, safe push and verified local/remote alignment. | Maintain branch/owner controls and the 1.1.0 release-authority checkpoint without treating every save as publication. |
| `gzs-release` | A project needs version advice, a candidate or authorized publication. | The requested release decision/deliverable and remote verification when publishing. | Preserve project/Backplane release ownership and the actual publication boundary. |
| `gzs-session-handoff` | Work must continue across an actual session/agent boundary. | A durable, resumable state record using the existing owner's artifact where available. | Strong existing continuity role; no competing backlog/handoff or new authority. |

## Priority review findings

### 1. Review assurance roles together first

The highest-value first pass is `gzs-plan-audit`, `gzs-intent-audit`,
`gzs-change-review` and `gzs-quality-gate`. Their distinct questions should be
clear to an adopter:

- Plan audit: does the proposed work cover the authorized intent and scope?
- Intent audit: does the delivered behavior fulfill the agreed intent?
- Change review: what reachable defects or regressions does this change contain?
- Quality gate: what do the project's required executable checks demonstrate?

The [plan-audit activation description](../../skills/gzs-plan-audit/SKILL.md)
includes leaving plan mode and starting a planned change; its workflow produces
a PASS/FAIL verdict. It lacks an explicit active-workflow ownership/return
section. That combination needs review before treating it as a default extra
gate inside an already-approved Superpowers plan.

[Intent audit](../../skills/gzs-intent-audit/SKILL.md) correctly routes incomplete
delivery back to existing intent, but does not explicitly describe how its
findings feed an active owner's spec-compliance/acceptance stage. Its distinct
user-visible observation is valuable; the review should make the incremental
question and the condition for skipping equivalent work explicit.

[Quality gate](../../skills/gzs-quality-gate/SKILL.md) already discovers project
commands and resolves applicability. Its pre-handoff/pre-merge/pre-release
activation and final full-sequence instruction need an explicit composition
review with existing verification ownership and reusable current evidence.
Preserve unconditional project requirements; do not solve duplication by
weakening a required gate.

[Change review](../../skills/gzs-change-review/SKILL.md#precedence-and-scope)
is a useful existing model: it preserves the owner's reviewer roles and
verdicts, distinguishes intent audit, and rejects redundant full-gate execution.
Review this cluster jointly, then make bounded individual corrections where
evidence warrants them. Do not turn the four skills into four required reviews.

### 2. Resolve overlapping development disciplines by selecting one owner

[Root-cause debugging](../../skills/gzs-root-cause-debugging/SKILL.md) and
[test-driven change](../../skills/gzs-test-driven-change/SKILL.md) already retain
active project controls. Both overlap directly with established Superpowers
disciplines. Review their useful standalone cases and the explicit skip/delegate
case alongside Superpowers before deciding whether either needs revised scope.
Their presence should not create a second debugging or test-first sequence.
Overlap alone is insufficient evidence to remove a skill; lack of a distinct
useful contribution would justify considering a merge or deprecation.

### 3. Review delivery and continuity as handoffs

Review Git sync, release and session handoff together around the artifact and
authority crossing each boundary. A successful test run, committed change,
remote save point, prepared candidate and verified publication are different
outcomes. Backplane/project release and handoff mechanisms remain their owners.
Keep the strong existing continuity behavior and test composition rather than
adding another mandatory chain.

### 4. Align the queue with current contract evidence

The review queue still described dependency-update's 0.4.1 initial review while
0.5.0 has changed direct-invocation authority. Git-sync's original accepted
1.0.0 baseline also does not by itself qualify the later 1.1.0 release checkpoint.
Keep historical evidence and accepted decisions, but identify which current
contract additions still need native behavioral evidence. Router 0.6.0 already
records that distinction from its earlier orientation-only trials.

### 5. Keep enabling and specialist roles proportionate

Setup, context maintenance, portability, risk/debt/architecture analysis and the
Pythonic refactor pair address legitimate needs at multiple points in a
development effort. They do not each need a dedicated chronological stage.
Their role review should name the concrete trigger, bounded result and return
to an owner, with a case where invoking them would add no value. Avoid expanding
these skills merely to fill an empty lifecycle diagram.

## Required questions for the focused reviews

For each skill establish:

1. Which user/project need warrants invoking it now, and when should it be skipped?
2. What existing inputs/authority does it consume?
3. What concrete result does it produce, and what demonstrates completion?
4. Which workflow owns the surrounding stage and receives that result?
5. With Superpowers absent, what bounded work can the skill independently supply?
6. With Superpowers/project ownership present, is it delegated work, a distinct
   complementary check, or an unnecessary duplicate?
7. Does a realistic scenario demonstrate the claimed value and preserve the
   owner, scope, approval and continuation boundaries?

Use the answers to keep, clarify, narrow, merge or deprecate a skill. Do not
preselect a blanket rewrite or removal outcome. Direct skill invocation and
router-mediated use both need the same ownership contract. Model execution
requires separate behavioral evidence; a role table or structural test cannot
substitute for it.

## Outcome and limits

This review accounts for all twenty published interfaces and recommends the
assurance cluster as the next bounded review. It adds lifecycle contribution
to the review criteria and reconciles stale evidence labels. It changes no
skill body, activation, version, runtime, installation or lifecycle behavior.
It is repository documentation only and selects no new pending bundle/skill
version. The review itself grants no commit, push or publication authority.
Individual dispositions and behavioral
qualification remain with the focused reviews.
