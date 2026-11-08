# Release 0.10.0 and Astral alignment handoff

Observed: November 8, 2026, 15:45:12 UTC.
Workspace: `U:/repos/agents/gz-skills`; branch `main`; remote `origin` at
`https://github.com/tvproductions/gz-skills.git`.

## Resume point

Release 0.10.0 is published and verified. The latest work records the maintainer's
strict Astral/uv alignment preference and adds the Hatchling-to-`uv_build`
migration as [backlog item 2](../roadmap.md#uv_build-migration-acceptance), with
explicit package-behavior acceptance criteria. The backend has not been migrated.

First permissible action: inspect Git status, current HEAD and the roadmap,
then read the migration criteria and current package/resource lookup. Expect
a clean main containing the documentation commit that introduced this handoff,
descending from `497dcde5032e6a098a51b3e623427686feb6ad08`. Locate that commit
with `git log -1 --format=fuller -- docs/handoffs/20261108T154512Z-astral-alignment-and-release.md`;
do not assume the observed base remains the tip.

The next concrete maintenance candidate is the backend migration. Read-only
inspection should establish how the canonical root `skills/` tree can be packaged
with `uv_build` while preserving installed resource access and CLI behavior.
Implementation is backlogged, not authorized by this handoff. Continue when the
maintainer requests that work; stop before unrequested migration, plugin updates,
another release or consumer propagation. No demonstrated migration blocker or
approved permanent Hatchling exception has been recorded.

## Git scope and authorization

At capture, HEAD was `497dcde5032e6a098a51b3e623427686feb6ad08`; main aligned
with origin/main after fetch. Four intended documentation changes were present:
`AGENTS.md`, `CHANGELOG.md`, `docs/release-policy.md`, and `docs/roadmap.md`.
Nothing was staged and no unrelated work was observed. This fresh handoff is the
fifth file in the save point. The user explicitly requested “create fresh handoff
and git sync,” authorizing ordinary validation, commit and push of this unit.
The final save-point SHA and remote alignment are reported by the sync operation;
this document does not predict its own commit identity.

All changes in this save point are repository guidance/backlog/continuity text.
No skill tree, dependency, backend or published version changes. Bundle metadata
remains 0.10.0; the next minor number is 0.11.0 with scope unselected. Classify
any later implementation against the actual published baseline and complete
pending scope rather than incrementing a version for each task.

## Settled maintainer decisions

- gz-skills is a separate lightweight alternative/cousin to gzkit, with no
  designed interoperability. Historical source provenance is not integration.
  Keep the setup guard against mixing the ecosystems; do not reintroduce the
  removed installer surface or named integration paths.
- Apply strict Astral/uv alignment to this repository. `uv_build` is the preferred
  pure-Python backend; existing Hatchling is migration debt. A different backend
  needs a concrete requirement, evidence, maintainer approval, owner and dated
  revisit. Previous narrow release deferrals are not continuing waivers.
- Migration preserves supported package behavior: canonical skill resources,
  resource lookup, imports/CLI, install/update safety and lock provenance, editable
  installation, source-independent builds and reproducibility. It need not produce
  the same archive bytes as Hatchling. The roadmap owns the detailed criteria.
- These are repository-development decisions, not a new universal backend/tool
  mandate for unrelated consumers of portable skills. No formal starter bootstrap
  or gzkit integration follows.

The [policy binding](../release-policy.md#astraluv-alignment-clarification--november-8-2026)
records the November 8 clarification and reviewed starter source
`a483e382146c6082e590e31494c07d1812645014`. The canonical
`docs/engineering/astral-alignment.md` at that revision selects `uv_build` for
pure Python and permits another backend only for a concrete need. Recheck the
source at the next scoped policy/tooling change; do not claim full conformance.

## Completed release and review

- [Published v0.10.0](https://github.com/tvproductions/gz-skills/releases/tag/v0.10.0)
  is neither draft nor prerelease. Release commit:
  `f49c765831fecfbd058aaf7893206cda3ff1890a`; annotated tag object:
  `1f4a48c038b3a64eba3de86f6d24ecadef94c4a2`. Do not move or recreate it.
- The [release receipt](../evidence/2026-11-08-0.10.0-release.md) records clean-commit
  gates, two reproducible builds, all 44 resource comparisons, downloaded asset
  checksums and tagged Codex/Claude/OpenCode/uvx checks. No existing consumer was
  upgraded. Native loading is proved; model behavioral certification is separate.
- The [dependency-update initial review](../review/gzs-update-dependencies-2026-11-08.md)
  is complete: keep corrected 0.4.1, initial finding closed by static inspection.
  Native baseline/behavioral execution remains pending for stable acceptance.
  Do not reopen the initial review merely because a new session begins, and do
  not describe stable acceptance as complete.
- The [review queue](../review/README.md) and roadmap own remaining work. No issue
  or PR was created for this migration; the GitHub issue snapshot in the roadmap
  remains explicitly dated, not current tracker evidence.

## Read-only freshness observations

Checked November 8 using official package metadata, CPython tags and release
records. No pins, environments, plugin installs or dependency files were changed
by that review; recommendations are not verified upgrades:

- Python 3.14.10 is the latest observed patch in the approved 3.14 family; uv
  0.13.7 and the release build's Hatchling 1.33.0 match observed latest versions.
  Python 3.15.2 is outside the selected family and does not authorize migration.
- Release validation used Ruff 0.17.3 and ty 0.0.95. Newer
  [Ruff 0.17.4](https://github.com/astral-sh/ruff/releases/tag/0.17.4) and
  [ty 0.0.99](https://github.com/astral-sh/ty/releases/tag/0.0.99) are candidates
  for separately authorized compatibility checks; ty remains beta.
- `skills-ref` latest was 0.1.1; its documented invocation is unpinned and the
  previous validation's exact resolved version was not recorded. Build-tool
  transitive versions are also unrecorded: no complete freshness certification.
- The skill invocation supplied to this session still loaded bundle 0.9.0 / skill
  0.4.0 from its managed cache, although bundle 0.10.0 / skill 0.4.1 is published.
  That is invocation evidence, not a complete inventory of installed plugins.
  Refresh only through the native manager under explicit update authority;
  do not edit managed caches or assume a released update is installed.
- Ignored `.opencode` dependency files are harness-generated state, excluded from
  the supported publisher toolchain/package. Do not turn this into a Node
  dependency-update task. There are no declared Python runtime dependencies.

## Verification and local-only artifacts

Before this handoff, the four documentation changes passed all twelve repository
contract tests (including links, names/prompts and version agreement), all twenty
Agent Skills validators and `git diff --check`. The requested save point will
run the README's complete test/specification/build sequence including this file
before committing. Observe those results in the sync response; prior release
checks do not prove a later working tree passed. No hosted quality CI is configured.

Release preview artifacts, final local artifacts and disposable native-check
directories are local-only. Authoritative digests and outcomes are in the release
receipt and published assets; a successor need not recover temporary paths or
reuse the discarded preparation snapshot. The release's nonblocking optional
directory-icon/helper-alias warnings and corrected fixture attempts remain in
the receipt. No credentials or server passwords belong in handoff evidence.

Suggested next-session skills: dependency-update for an explicitly scoped tool
refresh, quality-gate for verification, and release only for a separately
requested release increment. Use the roadmap's migration acceptance as the
scope authority when the maintainer selects that work.
