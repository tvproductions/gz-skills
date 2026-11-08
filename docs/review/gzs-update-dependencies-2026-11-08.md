# Dependency update contract review — November 8, 2026

Current outcome: **initial review complete; keep corrected candidate 0.4.1**.
The initial finding is closed by static inspection of the authorized correction.
Native behavioral evidence remains required for stable-contract acceptance.
The user's portability clarification requires no named orchestrator relationship
or prerequisite. Candidate 0.4.1 removes that special case and explicitly works
standalone; an existing project workflow retains its own controls when present.
The initial diagnosis and walkthroughs below describe released 0.4.0 and are
preserved as history; the final candidate assessment records the correction.

## Final candidate assessment

Reviewed all three packaged files: `SKILL.md`, `agents/openai.yaml` and
`references/inventory.md`. The candidate tree hash from the installer's
`load_catalog` is
`a58b574e58072502514067d8eb1d0e7df6005ea88524150d75b05cd0c571f14a`.
The comparison base remains released skill 0.4.0 in v0.9.0; candidate changes
are its patch version, the standalone/general precedence paragraph, and removal
of the named orchestrator special case. Metadata and inventory are unchanged.

Disposition: **keep**, with no remaining blocking finding in this initial
static review. Do not incubate, remove or promote the skill to 1.0.0. The
correction closes the documented contract omission, not an observed execution
failure. Native behavior has not been certified.

| Initial-review requirement | Completed evidence |
| --- | --- |
| Product disposition | Keep corrected candidate 0.4.1; finding closed by the candidate diff and complete reread. |
| Invocation decision | Retain user/model invocation; Codex policy is implicit, and the OpenCode adapter also permits autoinvocation. Default mode remains read-only. |
| Positive and negative triggers | Examples and exclusions are recorded under Contract, activation and provenance; no activation-description change is needed. |
| Portable invariant and adapter points | Inventory, authority, owning-tool resolution and project gates are recorded below; no orchestrator dependency or integration path is required. |
| Side effects, authorization and stops | Freshness mode leaves dependency state unchanged; updates require scoped authority; absent approval stops gated mutations in either mode; failure and publication boundaries remain intact. |
| Baseline and behavioral scenarios | Thirteen analytical baseline/skill walkthroughs are recorded below. They are scenario design and static evidence, not native-agent trials. |
| Completion evidence | Candidate tree identity, finding disposition, version rationale and repository validation are recorded here. Stable acceptance has a separate, explicit remaining matrix. |

Correction recheck: a standalone repository needs no profile, project wrapper,
orchestrator or marker directory to use manifest/registry discovery. A project
with an already-active workflow keeps its existing controls. With approval
absent, the opening paragraph now explicitly stops before a gated mutation;
inventory may continue when independently permitted. A freshness-only request
still stops before steps 5–9. No parallel state, approval process or orchestrator
installation is introduced. These are manual candidate walkthroughs.

The initial dependency-update review is complete. Its next action is the native
stable-contract evidence task, not another initial-review pass.

## Completion validation — November 8, 2026

All commands below completed with exit 0 on the corrected candidate tree:

- `uv run --locked python -m unittest discover -s tests -v`: 29 tests passed,
  including skill identity/prompt agreement, relative links, version mirrors,
  removed-surface rejection and the existing setup exclusion.
- For every canonical skill directory,
  `uvx --from skills-ref agentskills.exe validate <directory>`: all 20 passed.
- `uv build`: wheel and sdist for candidate 0.10.0 built successfully.
- `uvx ruff check --config pyproject.toml src tests`: passed.
- `uvx ruff format --config pyproject.toml --check src tests`: all seven files
  already formatted.
- `uvx ty check --project .`: passed. The isolated ty installation warns that
  its stale `pyvenv.cfg` home prevents navigation to stdlib implementations;
  this is a local tool-environment warning, not a type-check failure. Repairing
  an unrelated global tool installation is outside this review.

Activation descriptions were inspected for intended and unintended triggers;
the dependency-update examples and exclusions are recorded below. No native
agent sessions, dependency upgrades, cross-harness stable acceptance or hosted
CI execution are claimed. No commit, push, tag or release was performed.

## Maintainer boundary clarification and history

The maintainer clarified that this ecosystem is a lightweight alternative/cousin
to gzkit and is not designed to interoperate with it. Standalone behavior and
general respect for a project's existing controls do not imply integration.
The setup exclusion guard remains intentional. Historical extraction provenance
is retained; active integration paths are removed in pending bundle 0.10.0.

Git history establishes when the conflicting implementation/guidance appeared:

- `6880a96` (2026-08-23), the initial repository commit, added the `.gzkit/skills`
  installation destination and permitted discovered `gz` commands in AGENTS.md.
- `21579a5` (2026-09-06) explicitly allowed gzkit to invoke or wrap portable skills.
- `135d5b4` (2026-09-27) added the dependency-update `.gzkit/` workflow special case.

These observations come from `git log -S` and `git blame HEAD`, not evidence of
an approved interoperability objective or a tested integration. The implemented
model was file placement plus command/workflow delegation; this review found no
end-to-end acceptance record for it. Later profile setup rejects `.gzkit/`
projects, so the named install surface also conflicted with that exclusion.
The maintainer's clarification supersedes the integration wording.

Initial decision: **revise before stable acceptance**. Retain the skill and its
user/model-invoked activation. Reviewed `gzs-update-dependencies` 0.4.0 in
published bundle v0.9.0, commit
`3f76c9eef816bba45a99ed3bff746eb61a5cf50d`. Its complete packaged tree is
unchanged at review HEAD `0683b1650ad789d92f3673efe70253727fafab7d`.
That initial pass was a contract review, not a dependency refresh or release
authorization; the subsequent correction follows the maintainer clarification.

## Initial finding — closed in candidate 0.4.1

**Medium: general project-workflow precedence is incomplete.** The update-mode
clause (SKILL.md lines 32–35) treats an upgrade request as authorization for
steps 1–9. The explicit workflow-yield instruction at lines 92–93 applies to
repositories using `.gzkit/`, within the heavy Python section. A non-gzkit
project can also have an active maintenance workflow requiring an independent
review or approval between target selection and manifest mutation. The skill
does not explicitly retain that workflow's sequencing, approvals, locks,
receipts or completion authority before progressing to step 5.

This is a documented composition-contract omission, not an observed bypass.
Step 1 requires reading agent guidance, and lines 125–129 preserve project
mutation scope and binding constraints; these already support respecting a
clearly stated prohibition. They do not explicitly establish the broader
lifecycle boundary required by AGENTS.md's one-way composition rule and the
roadmap's shared architecture. The same class of omission was corrected in
Git Sync; its opening precedence paragraph supplies a working local analogue.

Correction direction: replace the named special case with a general precedence
clause covering both modes, independently of language, profile or orchestrator.
The skill must remain usable without any project workflow or orchestrator.
Preserve existing project controls, stop before a gated mutation when its
required approval is absent, and report only the dependency task's results.
Do not create parallel lifecycle state or declare the containing workflow
complete. Confirm this boundary with native execution before stable acceptance.

No additional defect survived this bounded static review. In particular, the
0.9.0 removal of library-owned Python defaults is intentional and is not a
regression to reverse.

## Contract, activation and provenance

The portable invariant is a complete, scoped inventory with authoritative
version evidence, policy-preserving updates when authorized, owning-tool lock
regeneration, project verification and honest constrained/unknown reporting.
Projects own release families, package managers, intentional pins, adopted
standards, exceptions, gates, host compatibility and mutation authority.
The manifest/registry fallback permits useful work without an upgrade wrapper;
offline operation establishes inventory and constraints without inventing
latest versions. The extraction sources and retained invariant in
[origins](../origins.md#gzs-update-dependencies) remain applicable.

Keep implicit invocation enabled: the skill supports read-only freshness
assessment and selects that mode when invocation alone establishes no update
authority. Positive triggers include “check dependency freshness,” “which pins
are outdated?” and “upgrade this project's dependencies within its approved
families.” Negative triggers include “audit dependency licenses,” “debug this
failing test,” “update every tool installed on my computer,” and “publish this
release.” Route those goals to their owning discipline; a dependency mention
alone does not authorize updates, deployment or publication.

The inventory reference protects locally modified vendored skills and managed
plugin caches, keeps deferred components disabled, and requires request or
workflow authority for commit, push and publication. An installed or selected
plugin revision is distinct from tested discovery and integration readiness.

## Scenario walkthroughs

Method: one reviewer traced the complete skill body, inventory reference and
OpenAI metadata against repository guidance, provenance, the released diff and
the accepted Git Sync boundary. The baseline column describes ordinary review
reasoning without this skill. These are analytical comparisons, not fresh
no-skill/with-skill agent runs, registry queries or executed upgrades.

| Scenario | No-skill baseline | With-skill contract walkthrough |
| --- | --- | --- |
| Invocation without an update request | Establish whether assessment or mutation is wanted. | Review first; no manifest, lock, environment or plugin mutation. |
| “Check freshness; do not update” | Inventory and research without changing state. | Steps 1–4 only; targets remain untested unless isolated verification was separately authorized. |
| Authorized update with a project wrapper | Read wrapper policy before resolving versions. | Prefer the documented wrapper; preserve families and regenerate locks through their owner. |
| No wrapper, multiple ecosystems | Discover actual manifests and managers. | Inventory reference covers each evidenced ecosystem; classify excluded surfaces explicitly. |
| Registry unavailable | Report current constraints and unknown target status. | Offline fallback permits inventory but prevents a fully-current claim. |
| Heavy selected, no governing standard available | Do not invent a baseline. | Report UNKNOWN and continue independent inventory; no fallback family/tool list. |
| Consumer explicitly supports Python 3.11 | Preserve consumer policy. | Read its authority; this publisher's Python 3.14 pin supplies no consumer mandate. |
| Host-bound Python 3.12, newer development interpreter | Verify the real loading boundary separately. | Preserve host family and report missing host verification; development execution proves no host readiness. |
| Minimum-only manager range and a newer compatible installed patch | Separate manager compatibility from the tested pin. | Do not require an exact CI-patch match absent governing policy. |
| Required development tool missing, approved extra package present | Reconcile requirements without replacing declarations. | Update mode adds required tools in their owning group and preserves approved additions/exceptions. |
| Vendored skill modified locally; plugin deferred | Preserve local edits and disabled state. | Require reviewed reconciliation; do not replace the snapshot, edit cache files or enable deferred plugins. |
| Resolver or verification failure | Preserve recoverable work and report failure. | No hand-edited lock, weakened gate or fully-current claim; identify the unresolved constraint. |
| Non-gzkit workflow requires approval before mutation | Inventory is permitted; mutation waits for approval. | General guidance supports obeying the prohibition, but lifecycle precedence is not explicit. Retain the finding above; actual bypass is untested. |

## Acceptance limits and next action

This pass establishes the static contract review, activation decision,
provenance check and scenario design. It does not establish native inference,
tool execution, update success, improvement over baseline, or complete
cross-harness acceptance. The November 7 policy-alignment record provides prior
bounded policy scenarios; it is not a replacement for this skill's full
stable-contract behavior matrix.

The precedence correction is now applied; next collect sanitized native-session
evidence with disposable repositories. Cover review-only/default invocation,
successful authorized update, intentional constraints, missing/unavailable
authority, offline evidence, overlapping user edits, failed resolution/gates,
locally modified snapshots and absent project approval. Include negative
activation and a no-skill baseline. Observe actual skill loads and commands,
before/after file and environment state, owning-tool lock stability, gate
results, preserved unrelated work and final claims. Keep external package
targets fixed or record exact authoritative responses so changing registries
do not obscure the comparison. Exercise supported harnesses and retain failed
fixture/permission attempts as limitations rather than successful runs.

## Release accounting

Published baseline is bundle 0.9.0 and skill 0.4.0. The initial review changed
only documentation. Following the user's clarification, the selected pending
scope is the standalone/vendor-neutral correction, removal of the gzkit install
surface and integration examples, and review records: bundle 0.10.0 and skill
0.4.1. The skill correction is compatible; removal of the supported installer
option requires a minor during 0.x. No invocation or authority is expanded. All four bundle
version mirrors and the source fallback advance together; uv regenerates lock
metadata. Marketplace refs retain published v0.9.0. No new major PRD is required
for this pre-1.0 minor. Stable reviews and ecosystem integration proposals are
excluded from this release scope. Published identities remain unchanged.

Manual correction checks: the current skill has no named orchestrator or marker
directory check. With no project workflow it proceeds through the existing
discovery fallback; with an active workflow it preserves that workflow's controls
in either mode and stops before an unapproved gated mutation. Freshness mode
still prohibits dependency-state mutation. These are text walkthroughs, not
native-session acceptance results. The remaining acceptance gate is the native
behavioral matrix above plus the repository's structural/package checks.

Remaining stable reviews, heavy integration, MPAS adaptations and the baseline
proposal remain outside this bounded review. No stable promotion or publication
readiness is claimed.
