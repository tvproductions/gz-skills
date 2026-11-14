# Adopter workflow entry and complementary ownership

November 14, 2026. The maintainer requested guidance comparable in clarity to
Superpowers, explicitly covering gz-skills independently present and gz-skills
alongside installed Superpowers. This authorizes the router/guide/README change
and validation, not release publication or changes to existing consumers.

## Scope and version decision

Published baseline v0.11.0 resolves to
`62622aee80ce27d4a39efe3554a583b844f38876`. The existing worktree already
contains the separately authorized completed dependency maintenance and direct
update-invocation correction, recorded in its
[receipt](../evidence/2026-11-14-dependency-maintenance.md). Preserve that work.

Expand the selected finite 0.12.0 outcome to reliable task initiation/completion:
teach adopter workflows and enter an authorized task through its owner.
Router 0.5.1 → 0.6.0 changes its recommendation-only boundary; this requires a
minor during 0.x. Existing bundle candidate 0.12.0 already covers that increment
alongside dependency skill 0.5.0 and current-tool maintenance. Keep all bundle
mirrors/lock at 0.12.0 and marketplace refs at published v0.11.0. No major PRD,
stable promotion, installer/schema change or new mandatory plugin is involved.

Included: router body, activation description and UI prompt; one packaged
workflow reference; prominent human-facing guidance; provenance, review and
scope reconciliation. Rename the existing implicit-invocation test to reflect
that routing is no longer categorically read-only; retain its assertions.
Do not add wording-matching tests or call static examples model certification.

Excluded: new lifecycle state, settings migration, automatic session-start
hooks, native adapter behavior changes, Superpowers/Backplane repository edits,
template bootstrap, managed-cache edits, consumer upgrades and publication.
The [heavy ecosystem proposal](../proposals/lightweight-sdd-ecosystem.md)
retains its unresolved first-use, schema and compatibility proof work.

## Reviewed sources and decisions

Checked canonical `obra/superpowers` main at
`22f0b463e7a5e579904dd6211a520321035526f7`; read its
[basic workflow](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/README.md#the-basic-workflow)
and [entry skill](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md).
Lessons adopted: explain progression from task through result, select the owning
process before implementation, make transitions/completion visible, and teach
the agent how to use its installed skills. Superpowers retains its development
methodology. The new GovZero prose describes original task-routing and
complementary ownership; it does not copy a Superpowers skill implementation.

Rechecked canonical starter remote main and clean local source at
`1c633f869ad3757961a4f734b0203eb558aaf718`. Versioning, baseline and
verification policy are unchanged from reviewed
`0d60d0dc6b6a4a695135a9e1bbcc4e7830171dd2`; the later changelog records
starter adoption of published gz-skills 0.11.0. Preserve the existing policy
binding, prospective major PRD rule and scope-based verification. This is not
formal template adoption or a companion-conformance claim.

The router stays usable independently. Superpowers presence is capability
evidence, not a profile selector, permission grant or proof of active workflow
ownership. When its installed process applies, it owns the development sequence;
GovZero supplies distinct supporting disciplines and returns results to that
owner. Existing project/Backplane authority takes precedence in either case.
Action questions enter the destination; advice questions return a recommendation.

## Scenario acceptance review

These are instruction walkthroughs against the resulting body, guide and
destination contracts, not independent model runs. The historical 0.5.1 native
orientation evidence does not qualify the new action boundary.

| Scenario | Required routing and observable completion |
| --- | --- |
| gz-skills only: fix an unexplained bug | Enter root-cause debugging, implement the requested fix and verify the affected behavior; no Superpowers installation or advice-only stop. |
| gz-skills only: implement a feature | Use ordinary project development with useful standalone disciplines; deliver behavior/evidence without inventing a required design/backlog system. |
| Superpowers available: start a feature | Load the installed applicable entry/process guidance; let it own development and approvals, using GovZero only for distinct supporting needs. |
| Superpowers debugging already underway | Resume the same owner; do not restart diagnosis with a second generic debugger. |
| Superpowers active: dependency migration needed | Run dependency maintenance within the active stage, return changes/evidence and continue the original task; no separate lifecycle. |
| Review already completed for unchanged work | Reuse relevant evidence; add a distinct audit only when needed/requested rather than repeating equivalent review/gates. |
| Backplane owns tracking/release/handoff | Feed the existing owner and artifacts; create no parallel backlog, release state or handoff. |
| Superpowers absent or unavailable | Distinguish actual absence/unknown state; proceed with independent authorized work without installing another plugin. |
| Superpowers installed without a profile choice | Do not infer lite/heavy, approved architecture, Backplane availability or integrated readiness. |
| “Which skill reviews a diff?” | Recommend only, with observed syntax/discovery; do not review the repository or fix anything. |
| “Review this diff” | Execute bounded review through its owner; report findings without taking unauthorized corrective/publication actions. |
| “Check dependencies without changes” | Read-only freshness assessment despite action-capable routing and dependency skill defaults. |
| Direct dependency-update invocation | Complete scoped maintenance/verification without a second go-ahead or a version-table stop. |
| Router invoked without a task or established outcome | Establish the desired outcome; choose no arbitrary mutating workflow. |
| Implement/fix request without Git/publication authority | Complete and verify the local result; no automatic commit, push, tag or release. |
| Explicit Git sync with pending version | Follow the destination's publication-authority checkpoint; a routing decision alone grants no release authority. |
| Existing project approval blocks a stage | Preserve the dependent approval and continue independent authorized work; do not bypass or invent another permission round. |
| Unsupported harness syntax or hidden explicit-only skill | Discover the native mechanism or report the limitation; do not invent a universal command or declare the skill absent without evidence. |
| Translate ordinary prose without an engineering/catalog question | Router is not needed; do the unrelated task without workflow/bootstrap mutations. |

Walkthrough outcome: the two installation cases, action/advice separation,
destination authorization and owner continuity are explicitly covered. This
changes the router's prior contract by design; orientation remains available.
No global instruction, hook or plugin dependency is silently installed.

## Verification and limits

Observed on macOS with uv 0.13.8, managed Python 3.14.10, project Ruff 0.17.5
and ty 0.0.104:

| Check | Result |
| --- | --- |
| `uv run --locked python -m unittest discover -s tests -v` | All 32 tests passed; metadata, names/prompts, relative links, version agreement, installer protections and native JavaScript adapter registration included. |
| `uv run --locked agentskills validate <directory>` for every canonical skill | All twenty passed, including the changed router and packaged-reference link. |
| All catalog activation descriptions | Reviewed positive/negative triggers; router selects engineering workflow entry, advice remains read-only, unrelated tasks and optional plugins retain their scope. |
| `uv run --locked ruff check .`, `ruff format --check .`, `ty check` | All passed through the locked project tools. |
| `uv lock --check`, `git diff --check` | Passed; no dependency or schema churn from this extension. |
| Strict native Claude plugin and marketplace validators | Both passed; optional directory ICON_MISSING remains nonblocking. |
| Codex 0.169.0 disposable local marketplace install | Candidate 0.12.0 installed; all twenty skills/45 resources match canonical bytes, and the router's relative workflow-guide path resolves inside the installed plugin. |
| Two `uv build --no-sources` builds and a direct `--wheel` | Reproducible wheel/sdist and identical direct wheel. |
| `uv run --locked python scripts/check_package.py --artifacts dist/adopter-workflows-0.12.0` | Passed all twenty skills/45 resources, isolated installed CLI/catalog, snapshot provenance, update/local-edit protection and external editable lookup. |

The packaged reference adds the catalog's forty-fifth resource without changing
installer behavior. Native installation used only disposable configuration beneath
`/tmp/gz-skills-adopter-workflows.i2IR92`; no consumer plugin or project was
upgraded. The prior maintenance's vulnerability/outdated evidence remains
applicable because this extension changes no dependencies. The auxiliary
skill-creator validator retains its known allowlist mismatch for the existing
standard `compatibility` key; the authoritative Agent Skills validator passes.
No metadata was removed or validator weakened to accommodate that mismatch.

The final documentation closeout repeats link/contract checks; final archives
under `dist/adopter-workflows-0.12.0-final` verify the finalized source after
recording these observations. Artifacts are local candidate outputs, not a
release. The entire selected 0.12.0 scope remains uncommitted/unpublished.
No hosted quality CI is configured.

Native automatic selection, task continuation across real model/harness
sessions, and combined heavy readiness remain unqualified. The guide clearly
distinguishes these from files being registered, candidate installation and
structural/package validation. These are outstanding qualification dimensions,
not evidence of a shipped automatic bootstrap or stable contract acceptance.
