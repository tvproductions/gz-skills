# Published development dependencies

Status: proposed; implementation deferred on November 14, 2026 while the
maintainer makes most needed changes from the starter repository. The maintainer
requested a handoff and Git save point, not design approval or implementation.
This document grants no publication authority. This is repository development
tooling, not a new skill runtime. See the
[session handoff](../../handoffs/20261114T204924Z-starter-first-dogfooding.md).

## Intent and boundary

Develop gz-skills using its released skills and released Python installer, with
Superpowers governing development. The maintainer selected both published
products for dogfooding and required the starter's strict Astral discipline.

Skills remain independently usable. Their existing packaged Python helpers stay
in their skill directories. The `gz-skills` CLI installs, inspects and updates
snapshots; no skill acquires a runtime dependency on that CLI. Canonical authored
skills remain exclusively under `skills/`. Do not install skill mirrors here or
bootstrap the starter bundle. Backplane adoption remains outside this change.

## Approach

Use the native managed gz-skills plugin at the published v0.12.0 tag and native
Superpowers v7.0.2. Commit project Codex configuration with explicit marketplace
refs and enablement, preserving unrelated user choices and disabled starter
copies. Record immutable resolved commits and verify actual fresh-process skill
discovery. A current conversation's previously supplied catalog is not proof of
a refreshed host.

Use a separate non-distributed uv development project under `dev/published/`
with its own generated lock and ignored environment. Its development group pins
`govzero-skills` from the immutable published Git revision; the checkout's root
environment continues testing the candidate package. This separate resolution
prevents the candidate package from substituting for its own released dependency.
Keep shared Ruff/ty settings in the repository root, with no competing analyzer
configuration. Honor the managed exact Python pin in both environments.

Alternatives considered: a root self-dependency cannot resolve both revisions
of the same distribution; an unrecorded global CLI or repeated ad hoc uvx runs
would not provide the requested project-owned locked development dependency.
Vendoring the skills here would violate the canonical-tree boundary. The
maintainer chose dogfooding both products; the independent uv resolution is an
implementation proposal.

## Release maintenance

Keep development pins on the latest successfully published and accepted release,
including while authoring the next candidate. After publication and tagged
channel acceptance, advance this repository's published-plugin and CLI pins,
regenerate the development lock, and verify native discovery plus installed CLI
origin/catalog and disposable install/status/update behavior. The promotion is
a development-only follow-up; it must not alter the immutable release tag or
require the next unpublished version to install itself. Other consumer
propagation remains separately authorized.

## Strict Astral reconciliation

Review starter `1c633f869ad3757961a4f734b0203eb558aaf718`, including its
Astral alignment/acceptance, Python, baseline and verification policies. Record
every A01–A18 result with evidence or a reasoned applicability decision. Reconcile
missing applicable routine hooks/CI and pinned on-demand tools, preserving the
routine four-check contract and keeping deeper analysis outside routine hooks
and CI. Verify tool/runtime freshness, effective configuration, exact sync,
installed artifacts and the independent published consumer. Record demonstrated
compatibility gaps with ownership and revisit conditions; never infer complete
acceptance from configuration. Hosted CI requires an observed run after an
authorized push; until then report that evidence as unperformed.

## Completion and next work

Document reproducible setup/check/promotion commands, immutable inputs, rollback
and observed results. Preserve existing lifecycle-review documents. No packaged
skill behavior change is part of this tooling change. Once tooling acceptance is
established, use the published assurance skills under Superpowers to evaluate
plan audit, intent audit, change review and quality gate in standalone use,
active Superpowers work and reuse of already-completed checks. Any resulting
skill corrections receive a separate bounded plan, behavioral evidence and
versions derived from the last published release.
