# uv_build release and stable-review handoff

Observed: November 8, 2026, 16:26:37 UTC.
Workspace: `U:/repos/agents/gz-skills`; branch `main`; origin:
`https://github.com/tvproductions/gz-skills.git`.

## Resume point

The Hatchling-to-uv_build migration is complete, committed and released as
v0.10.1. Publication, artifacts and all four tagged installation channels are
verified in the [release receipt](../evidence/2026-11-08-0.10.1-release.md).
This supersedes the migration-as-next-work resume point in the
[previous handoff](20261108T154512Z-astral-alignment-and-release.md).

The next recommended backlog step is native behavioral evidence for
`gzs-update-dependencies`, whose initial review is already complete. First
inspect Git status/current HEAD and the [review queue](../review/README.md), then
read the [review's acceptance limits and next action](../review/gzs-update-dependencies-2026-11-08.md#acceptance-limits-and-next-action).
Expect a clean main containing this handoff's save-point commit, descending
from `2c7cff541bfc362f7b0068a40e6890ac855073bf`. Locate its actual identity with
`git log -1 --format=fuller -- docs/handoffs/20261108T162637Z-uv-build-release-and-stable-review.md`.

The user asked what comes next and clarified the distance to 1.0; they have not
requested execution of the next review. Read-only resumption is permissible.
Stop before unrequested behavioral sessions, skill changes, another release or
consumer updates. No unfinished implementation plan or active native server
needs to be resumed.

## Completed release and current state

- [Published v0.10.1](https://github.com/tvproductions/gz-skills/releases/tag/v0.10.1)
  is neither draft nor prerelease. Release commit:
  `4c836e3db6d43c495863a2090daaea56585a6ea9`; annotated tag object:
  `722fea4b8defd97cfbe40b21ef179ca062a88a5f`. Do not move or recreate the tag.
- HEAD before this handoff was `2c7cff541bfc362f7b0068a40e6890ac855073bf`, the
  release-evidence descendant. Fresh fetch showed ahead 0 / behind 0 and a clean
  worktree. Fresh GitHub queries found no open issues or PRs. These are dated
  observations, not continuing tracker guarantees.
- The [migration receipt](../evidence/2026-11-08-uv-build-migration.md) and
  [completed plan](../superpowers/plans/2026-11-08-uv-build-migration.md) explain
  package layout and acceptance. `uv_build>=0.13.7,<0.14` packages canonical
  root `skills/` through supported wheel `purelib` data. Installed discovery
  uses distribution-owned manifests; editable installs use the checkout tree.
- The 0.10.1 patch preserves CLI, snapshot/update, lock and skill contracts.
  All twenty skill trees and independent versions are unchanged from v0.10.0.
  Both marketplace pins select v0.10.1; no existing consumer was upgraded.
- Starter main was rechecked for release at
  `a483e382146c6082e590e31494c07d1812645014`, unchanged from the policy review.
  Keep the [release-policy binding](../release-policy.md) and consumer-owned
  policy boundaries. Closing backend debt does not establish full conformance.

## Next review and the 1.0 distinction

The [roadmap](../roadmap.md#current-backlog) remains the planning authority.
Continue dependency-update's native no-skill/with-skill comparison using
disposable repositories when requested. Its reviewed candidate 0.4.1 is retained;
do not reopen the initial review or assume structural validation proves stable
acceptance. The review already lists review-only/default invocation, authorized
updates, constraints, unavailable authority, offline evidence, user edits,
resolution/gate failures, modified snapshots and missing project approval.
Record actual loads, commands, file/environment state and honest final claims.

This is the next step, **not the last requirement for bundle 1.0.0**. Stable
contract and behavioral reviews across the catalog, catalog acceptance, a newly
written 1.0 PRD defining the release scope/acceptance, and ordinary release and
channel gates remain. Individual skill versions are independent: Git sync has
stable-contract acceptance already. Quality gate is next without an initial
review; router invocation-guidance findings remain separate. Heavy integration,
MPAS adaptations and the baseline proposal become 1.0 requirements only if
included in its approved scope; they are not automatically a blanket 1.0 list.
The next minor number is 0.11.0, with scope unselected. No 1.0 scope was approved
in this conversation.

## Verification, artifacts and authorization

The release receipt records the clean-commit proof: 32 tests, twenty Agent Skills
validators, Ruff 0.17.3/ty 0.0.95, native manifest checks, reproducible builds,
44 resource comparisons, external installed/editable behavior, exact Git uvx
provenance and downloaded asset checksums. Codex 0.167.0, Claude 2.1.311 and
OpenCode 2.1.4 tagged installation/loading checks passed. Linux/macOS execution
and full model behavioral certification remain unverified; no hosted quality CI
is configured. The optional Claude directory-icon and temporary Codex helper
warnings are nonblocking and retained in evidence.

`scripts/check_package.py` is the durable package verifier. Ignored artifacts
under `dist/release-0.10.1/` and temporary native-check scopes are local-only;
published assets and the release receipt are authoritative. Owned OpenCode
servers were stopped. No credentials belong in continuity evidence.

The current request, “update handoff, git sync,” authorizes this documentation
save point, repository validation, commit and ordinary push. Before committing,
run the README test/specification/build sequence, configured Ruff/ty checks and
`git diff --check` with this file present. The sync response reports its actual
commit, fresh gate results and final remote alignment; earlier release checks
do not prove this later documentation tree passed.

Suggested next-session disciplines: session-handoff for state verification,
the existing review's behavioral matrix for authorized execution, and
quality-gate for final verification. Publication and consumer refreshes need
their own requested scope; never edit managed caches to simulate an update.
