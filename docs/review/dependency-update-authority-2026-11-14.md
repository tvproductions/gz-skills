# Dependency-update authority correction

November 14, 2026. Correct released `gzs-update-dependencies` 0.4.1 to candidate
0.4.2 within pending bundle 0.10.2.

## Report and causal boundary

The maintainer supplied an adopting agent's report that the skill's sentence
“Do not infer an upgrade request from this skill's invocation alone; if no mode
is established, review first” overrode update instructions recorded in a handoff.
The agent also reported stopping while the user was correcting its workflow.
The quoted instruction is present in released 0.4.1. The complete adopter session
and worktree were not supplied, so this review establishes the instruction
ambiguity and reported outcome, not an independently reproduced native failure.

The mode section did not explicitly carry established user authority through
handoffs or recognize a project binding that selects update mode for invocation.
Its update examples omitted maintenance requests, and its default UI prompt
emphasized review or an explicitly requested update without naming existing
authority. The general project-precedence paragraph was insufficient to prevent
the reported fallback. The correction makes mode resolution precede defaults,
preserves explicit review requests, and treats workflow corrections as steering
unless the user changes or stops the authorized task. A handoff records authority;
it does not manufacture it or override a later instruction.

Where policy authorizes a newer family migration, complete the required scoped
integration and verification instead of treating an old pin as permanent policy.
Runtime/host requirements, actual compatibility constraints, project approvals,
scope and failure reporting remain controlling. The correction imposes no starter
policy on unrelated consumers and introduces no new lifecycle, helper or settings
contract.

## Static acceptance cases

These are analytical reviews of the resulting instructions, not native-agent
execution or proof of a completed adopter migration.

| Context | Required result |
| --- | --- |
| User requests an update and invokes the skill | Complete scoped steps 1–9 and verification; do not stop at a recommendation or ask again to apply. |
| Handoff records an authorized uv-managed update | Carry that request forward using the project's manager; skill invocation does not reset the mode. |
| User corrects the update procedure while it is underway | Incorporate the correction and continue within existing scope unless the user stops or changes the task. |
| Applicable policy selects updates for bare invocation | Use update mode under that binding; preserve separately required approvals. |
| Bare invocation without a request, established authority or project binding | Review only; leave dependency state unchanged. |
| Explicit freshness check or no-changes request, even under an update-default policy | Review only; do not install, synchronize or regenerate locks. |
| Earlier recommendation without update authority | Do not apply it solely because it was recommended. |
| Project authorizes migration across dependency/tool families | Review breaking changes, adapt affected integration and verify; an old pin alone does not justify deferral. |
| Project retains a runtime/host family or requires separate approval | Preserve that constraint and stop only the dependent gated work. |
| User stops or narrows the update | Follow the revised instruction; prior authority does not override it. |
| Package-only scope, disabled plugin or unrelated machine tools | Preserve the scope and disabled state; no broader installation or publication follows. |

Activation remains unchanged: dependency checks and maintenance requests apply;
license audits, unrelated global-tool maintenance and release publication are
outside this task. All catalog activation descriptions were reviewed for intended
and unintended triggers; this patch changes no descriptions or invocation policy.

## Release scope and source check

The local immutable v0.10.1 tag resolves to release commit
`4c836e3db6d43c495863a2090daaea56585a6ea9`; its dependency skill is 0.4.1.
The existing [gate-applicability correction](gate-applicability-2026-11-13.md)
already selected pending bundle 0.10.2. Both corrections restore existing
user/project-authority commitments, so the complete pending scope remains a
compatible patch. Retain all existing version mirrors at 0.10.2 and advance only
this skill to 0.4.2. No new major PRD is required. Publication, consumer
propagation, broad dependency migration and catalog stable acceptance are excluded.

Reviewed the clean local canonical starter checkout at
`77bce3bdeb77c5679cb6eed3e569a2b32a412df1`, the same revision recorded in the
November 13 policy review. Inputs: `docs/versioning.md`, `CHANGELOG.md`,
`docs/baseline-policy.md`, and its dependency-maintenance handoff
`docs/handoffs/2026-11-08-adr-practice-save-point.md`. Its unreleased 0.10.0
candidate explicitly binds maintenance and bare invocation to completed migration
for its adopters while preserving the portable default for unrelated consumers.
Honor an applicable consumer binding; do not embed that starter's update default
or runtime policy in the portable skill. This is no claim of complete companion
conformance or an installed starter upgrade. The remote main identity could not
be rechecked: `git ls-remote` failed because github.com could not be resolved.
Current remote alignment remains unverified; no policy exception is asserted.

## Verification

Observed with uv 0.13.6 and managed Python 3.14.10:

| Check | Result |
| --- | --- |
| `uv run --locked python -m unittest discover -s tests -v` | Exit 0; 32 tests passed, including name/directory agreement, prompts, relative links, version mirrors and installer protections. |
| `uvx --offline --from skills-ref agentskills validate <directory>` for every canonical skill | Exit 0 for all 20 skills. |
| `uvx --offline ruff check .` / `uvx --offline ruff format --check .` | Exit 0; all 76 Python files already formatted. |
| `uvx --offline ty check` | Exit 0. |
| `uv build --offline --out-dir dist/authority-correction/first` | Exit 0; candidate 0.10.2 wheel and sdist built. |
| Two `uv build --offline --no-sources` builds plus a direct wheel | Exit 0; reproducible wheel/sdist and identical direct wheel. |
| `UV_OFFLINE=true uv run --locked python scripts/check_package.py --artifacts dist/authority-correction` | Exit 0; 20 skills and 44 resources match archives and installed resources; isolated wheel/editable CLI, snapshot provenance and local-edit protection passed. |
| `git diff --check` | Exit 0. |

The first package-check attempt reached editable installation, then failed
resolving the build backend because PyPI DNS was unavailable. Rerunning with
uv offline mode used the cached backend and completed the entire check; no check
or threshold was bypassed. The auxiliary skill-creator `quick_validate.py`
returned 1 because its allowed-key list rejects the existing `compatibility`
frontmatter field. The repository's Agent Skills reference validator accepts all
20 skills including that unchanged field. No shared validator or valid skill
metadata was modified to satisfy this auxiliary mismatch.

These results establish instruction/package integrity, not native-agent behavior.
No wording-matching tests were added: they would not demonstrate that a model
carries authority through a handoff. Native behavioral qualification and an
observed upgrade in the reported adopter remain unverified. No adopter files,
installed caches, commits, pushes, tags or releases are changed by this correction.
