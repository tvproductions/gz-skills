# Dependency maintenance and direct-invocation correction

November 14, 2026. The maintainer corrected an unwanted review-only stop and
explicitly directed completed updates: the imperative skill invocation must
request action without another go-ahead. Complete maintenance and correct the
canonical skill/default prompt and repository binding. Commit, push, release and
existing managed-plugin propagation are not part of this request.

## Scope and policy

Published baseline v0.11.0 resolves to
`62622aee80ce27d4a39efe3554a583b844f38876`; initial worktree was clean at
`55e146abccb73d67c25baa60ee6c0c2d403aa84f`. Select pending bundle 0.12.0
and dependency-update skill 0.5.0 from released 0.4.2: changing direct invocation
from review fallback to completed updates changes the authorization contract
and requires a minor in the 0.x series. The same bundle covers existing-tool
refresh and locked project ownership. No major PRD or stable promotion applies.

Canonical starter remote main and clean local source match
`0d60d0dc6b6a4a695135a9e1bbcc4e7830171dd2`. Reviewed baseline maintenance,
Python, Astral alignment, verification, versioning and changelog guidance. Adopt
the maintainer's explicit completed-maintenance direction in this repository and
in the portable invocation contract; preserve consumer-owned constraints and
explicit review requests. This is not formal starter/heavy-profile adoption.
Retain Python 3.14.10 / >=3.14,<3.15 and minimum-only uv >=0.13.5 support.

Finite outcome: complete the existing Python tool refresh, lock reproducible
development verification and fix direct invocation. Exclude new tool assortments,
application refactoring, unrelated global/native apps, managed-plugin cache edits,
registry publication and consumer migration. Marketplace refs stay at v0.11.0.

## Observed failure and acceptance

The actual preceding turn stopped at a freshness table after a direct invocation,
using installed bundle 0.8.3's skill 0.3.0 fallback. Released canonical skill
0.4.2 already honored prior authority but still defaulted an otherwise bare
invocation to review. Merely upgrading that installed copy would not satisfy the
new direct-invocation requirement. Correct the authored tree, not its cache.

Static acceptance of the resulting instructions:

| Request | Required behavior |
| --- | --- |
| Direct invocation alone | Complete scoped updates and verification; no second go-ahead. |
| Update/maintain request or authorized handoff | Carry authority forward and finish; corrections steer continuing work. |
| Explicit freshness/check/no-changes request with invocation | Read only; do not resolve the ambiguity by changing dependencies. |
| Skill automatically selected during an unrelated task | Follow the surrounding task; relevance alone grants no update scope. |
| Concrete project approval/host/runtime restriction | Preserve it and report the dependent blocker; continue independent authorized work. |
| Older installed fallback in this repository | The local AGENTS binding selects completed maintenance. |

This matrix is instruction review, not native behavioral certification. The
current maintenance exercises actual tooling effects, not every future agent's
interpretation. No wording-matching tests are added.

## Inventory and live targets

Official PyPI metadata and Astral GitHub latest releases were checked today:
[uv 0.13.8](https://github.com/astral-sh/uv/releases/tag/0.13.8),
[uv_build 0.13.8](https://pypi.org/project/uv_build/0.13.8/),
[Ruff 0.17.5](https://github.com/astral-sh/ruff/releases/tag/0.17.5),
[ty 0.0.104](https://github.com/astral-sh/ty/releases/tag/0.0.104),
and [skills-ref 0.1.1](https://pypi.org/project/skills-ref/0.1.1/).
All targets are stable, non-yanked and declare Python support including 3.14.
Release notes describe compatible fixes; no newer stable tool family is available.
Python's [version index](https://www.python.org/doc/versions/) confirms 3.14.10
is current in the selected family; upstream 3.15.2 does not change that policy.

| Surface | Before | Selected outcome |
| --- | --- | --- |
| uv execution | 0.13.6 | 0.13.8 via supported self-update before resolution; support floor unchanged. |
| uv_build isolated backend | >=0.13.7,<0.14 | >=0.13.8,<0.14; verify actual build uses 0.13.8. |
| Ruff | Global 0.17.3 / isolated cached use | Lock and run project development 0.17.5. |
| ty | Global 0.0.93 / isolated cached use | Lock and run project development 0.0.104. |
| Agent Skills reference validator | Unpinned on-demand, cached 0.1.1 | Lock existing validation tool 0.1.1 and its transitives. |
| Python | Pin/environment 3.14.10; >=3.14,<3.15 | Retain; no runtime-family migration or modernization rewrite. |
| Published plugin refs | v0.11.0 in both marketplaces | Retain; pending bundle is not a publication. |
| Starter | Policy source SHA above, no adoption lock | Retain source binding; no starter bootstrap or companion edits. |

Runtime dependencies are empty. The JavaScript package is a harness adapter with
no Node dependencies or supported Node development toolchain. No CI action,
pre-commit configuration, container, submodule, heavy-profile settings, vendored
external binary, project plugin lock or ignored local Node dependency exists.
Git/gh, Codex, Claude Code, OpenCode and global Ruff/ty installations remain
outside this project's managed-environment refresh. The uv executable itself is
the explicitly refreshed resolver; project checks use locked development tools.
The latest baseline lock and its transitive packages will be audited and checked
for resolver stability, including any unavailable service evidence.

## Verification

Initial completed checks:

- `uv self update 0.13.8` succeeded before resolution.
- `uv add --dev ruff==0.17.5 ty==0.0.104 skills-ref==0.1.1` generated the lock
  and installed the project tools; `uv sync --locked` passed. The resolver also
  selected click 8.5.1, strictyaml 1.7.3, python-dateutil 4.0.0 and tzdata 2026.6;
  all equal current non-yanked PyPI releases and support the selected Python.
- Reviewed [dateutil's 4.0.0 and 3.0.0 release notes](https://dateutil.readthedocs.io/en/stable/changelog.html):
  Python >=3.11, removal of six, stricter ISO numeric fields and zoneinfo/tzdata
  behavior changes affect this validator-only transitive dependency. The actual
  all-skill validation checks its project use; no runtime package gains dateutil.
- `uv run --locked python -m unittest discover -s tests -v`: all 32 tests passed.
  Name/directory agreement, relative links, prompts, versions, native JavaScript
  adapter registration and installer protections are included.
- `uv run --locked ruff check .`, `uv run --locked ruff format --check .` and
  `uv run --locked ty check` passed with the newly locked project executables.
- `uv audit --locked --output-format json` succeeded: seven packages audited,
  zero known vulnerabilities or adverse statuses. uv warns that the command
  and JSON schema are experimental; no suppression or reduced threshold used.
  `uv pip list --python .venv --outdated --format json` returned `[]`.

Completed acceptance:

- All twenty `uv run --locked agentskills validate <directory>` checks passed
  using the locked validator and current transitive dependencies. Reviewed all
  twenty activation descriptions: only dependency-update discovery changes,
  prioritizing direct invocation while preserving explicit checks and unrelated
  task scope. UI prompts name their skill and the portable body owns behavior.
- Strict Claude plugin and marketplace validation passed. Native Codex 0.169.0
  parsed and installed candidate 0.12.0 through a disposable local marketplace
  containing the canonical manifest and skills under
  `/tmp/gz-skills-0120-maintenance.eZMyK4`. No existing consumer was upgraded.
- A second `uv lock --upgrade` left the lock's SHA-256 unchanged;
  `uv sync --locked` and `uv lock --check` passed. Project executables report
  Ruff 0.17.5, ty 0.0.104 and Python 3.14.10. New tooling, lock and declared
  targets agree; the seven resolved development packages are current.
- Explicit OSV batch queries for PyPI uv 0.13.8 and uv-build 0.13.8 returned
  empty advisory results, extending the seven-package development-lock audit.
  This records known advisories at the checked date, not a security guarantee.
- Two `uv build --no-sources` builds and a direct `--wheel` build passed.
  `uv run --locked python scripts/check_package.py --artifacts
  dist/maintenance-0.12.0` confirmed reproducible wheel/sdist, identical direct
  wheel, all twenty skills/44 resources, external installed CLI/catalog,
  provenance, update/local-edit protection and editable lookup.
  A verbose direct build confirms uv uses its bundled uv_build backend;
  executing uv is 0.13.8. No build-isolation bypass was used. The checker also
  exercises isolated editable installation through the declared backend.

The auxiliary skill-creator `quick_validate.py`, run via an isolated uvx PyYAML
environment, returned 1 because its allowlist rejects the existing standard
`compatibility` key. The Agent Skills reference validator accepts all twenty
canonical skills. This pre-existing auxiliary schema mismatch was not repaired
by deleting valid metadata or weakening the authoritative gate. Claude's optional
ICON_MISSING directory warning remains nonblocking and outside listing scope.

The maintenance is complete locally. Pending bundle 0.12.0 and skill 0.5.0 are
uncommitted/unpublished; published v0.11.0 and consumer caches remain immutable.
No hosted quality CI is configured. The changed activation's native model
behavior and execution on other operating systems remain unqualified; structural,
actual-tool and installed-package evidence do not assert that certification.
Final documentation-only closeout uses the repository-contract checks; final
source-independent archives are rebuilt after the evidence text is finalized.



## Subsequent authorized adopter-workflow extension

After this maintenance pass, the maintainer requested clear standalone and
Superpowers-complementary workflows. Pending bundle 0.12.0 now also includes
router 0.6.0 and its packaged guide. The 44-resource observations above describe
the earlier maintenance source; the extended catalog adds one reference.
The [workflow case review](../review/adopter-workflows-2026-11-14.md) owns final
extended-candidate scope and verification. Preserve this pass as dated evidence,
not proof of the changed router's model behavior or final archive identities.
