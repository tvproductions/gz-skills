# Python policy alignment — November 7, 2026

The maintainer directed fixing alignment across the starter, gz-skills and
SP-BP, then explicitly reaffirmed: ordinary projects use Python 3.14; code bound
to X-Plane/XPPython3 uses the supported 3.12 exception. The starter owns its
adopter standard; each companion establishes its own project binding. Portable
skills consume the governing project's standards rather than owning duplicates.

## Source and starting state

- Canonical starter reviewed at `4f8bb09633655473cd6aab9e1ddc60963c487bb1`:
  `docs/baseline-policy.md`, `docs/engineering/python.md`, `docs/versioning.md`,
  `docs/gz-skills-python.md`, AGENTS and CHANGELOG. Python family policy is
  unchanged by its minimum-only uv change.
- Canonical gz-skills starts clean at
  `9a7970208207d68cc4a04eff7c3d39bcea664463`. A new standalone source checkout
  was created; installed caches and the copy inside another consumer are read-only.
- SP-BP independently selected 3.14 on October 25 and refreshed its exact patch
  to 3.14.10 October 31. This correction does not bootstrap the starter into it.

## Demonstrated gap and correction

Five baseline cases were reviewed against released setup 0.3.1, dependency-update
0.3.0 and their guide. Explicit adopted 3.14, host-bound 3.12 and unrelated
consumer 3.11 policies already took precedence. The clear failure was an
ungoverned heavy project: setup recommended 3.13 and a fixed tool assortment;
update would reconcile that assortment as a standard. Unavailable adopted policy
also left an ambiguity between UNKNOWN and an open choice. No observed override
of an available explicit policy is claimed.

Retire the competing family/tool/package defaults. Resolve the project's adopted
source and exceptions first; missing, inaccessible or contradictory authority
remains UNKNOWN. Preserve existing working policy, unrelated consumer choices,
mode settings schema and host-verification boundaries. This is a conditional
recipe for resolving authority, not an extra lifecycle or maintenance skill.

The publisher's own project is ordinary Python. Set its family to
`>=3.14,<3.15`, exact managed development patch to 3.14.10 and executable uv
minimum to `>=0.13.5` without an upper bound. CPython's official `v3.14.*` stable
tag inventory was checked with gh; 3.14.10 is the latest stable patch in that
family observed at this review. The deliberate 3.14 family is not inferred from
an installed interpreter. uv regenerates the project lock; no dependencies are
added. Python 3.14's unittest behavior and existing stdlib APIs are tested on
the actual runtime; no new API or modernization mechanism is needed for this
instruction/configuration correction.

## Pending contract versions and migration

Prepare bundle 0.9.0, synchronizing Python/Codex/Claude/OpenCode metadata and the
source version fallback. Setup and dependency-update advance to 0.4.0. Removing
a previously supplied fallback contract and raising/narrowing the Python CLI
support range require a minor during 0.x; this is not a patch-only claim.
Existing marketplace refs and tagged installation examples keep published
0.8.3. No release, tag or consumer installation follows.

Existing consumers retain adopted choices. The standalone setup helper's 3.11+
execution compatibility is separate from this publisher's Python CLI support
range. XPPython3-loaded code still uses its own supported host environment;
installing this publisher's Python CLI inside that host is not required.

The packaging backend/resource layout is unchanged in this Python-policy scope.
This receipt does not claim full starter/Astral conformance, backend migration,
new native-host acceptance or complete dependency freshness. Those are separate
existing applicability/verification work, not waived by passing this correction.

## Observed verification

Before editing, all 28 tests passed on the original managed 3.13.15. After the
metadata/pin/lock change, all 28 pass on actual managed 3.14.10. Ruff 0.17.3
check/format and ty 0.0.95 pass. Explicit pyproject targets prevent inherited
unrelated settings from choosing another contract. Ruff's Python 3.14 formatter
removes exception-tuple parentheses in the publisher's core; the actual 3.14
tests cover the code. Portable helper files retain byte-identical source and
py311 formatter targets rather than inheriting new publisher-only syntax.
The initial generic Ruff invocation exposed shebang/executable checks from
outside repository-owned configuration; the explicit reviewed project selection
matches the governing starter routine families and is not an exception to them.

All 20 authored skill directories pass `agentskills validate` through isolated
skills-ref tooling. Every skill identity, metadata prompt and relative reference
also passes the existing repository contract tests. Both changed frontmatter
versions and all bundle identities agree with the pending candidate. The uv lock
check passes; no transitive/runtime dependency was added.

`uv build --no-sources` builds sdist then wheel. Zip/tar inspection verifies all
44 canonical skill resources byte-for-byte in both artifacts and exactly 20
skill entry points in the wheel. From outside source, an isolated tool invocation
of that wheel on managed 3.14.10 lists all 20 skills, including both corrected
0.4.0 contracts. uv refuses installation on 3.13.15 with the declared 3.14-only
requirement. The first catalog-output probe assumed JSON; the CLI emits text,
so the corrected assertion parses its actual public rows instead. No CLI format
change was introduced to satisfy the probe.

The five-case baseline/green instruction review preserves available starter,
XPPython3-host and unrelated-consumer policies, while the unavailable/no-policy
cases now remain UNKNOWN. These are fresh read-only scenario sessions, not paid
native-host acceptance or a statistical evaluation of every future invocation.

No native plugin installation, user settings change, consumer update, commit,
push, release or immutable tag mutation occurred. Package-tool download caches
and disposable wheel invocation are distinct from native plugin activation.

## Committed authority reconciliation for authorized sync

The maintainer subsequently authorized ordinary Git synchronization of this
correction. The reviewed starter authority is now committed and verified on
origin/main at `a483e382146c6082e590e31494c07d1812645014`. This reconciles the earlier working-tree review to an
immutable source; its runtime/ownership declarations are unchanged from the
accepted correction. Preserve published 0.8.3 refs and installed copies. This
candidate remains unreleased; no tag or plugin propagation is authorized.
Local tests, schema/resource and isolated-artifact results above remain the
applicable scope. This repository has no configured quality CI; report remote
arrival separately from unavailable exact-commit hosted quality evidence.
