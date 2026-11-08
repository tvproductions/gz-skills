# uv_build migration evidence

Observed November 8, 2026 on Windows, managed CPython 3.14.10 and uv 0.13.7.
Source is the uncommitted migration over `50e2de11861995f81454dbbed256e0901dd0e9f0`.
The maintainer explicitly requested “Hatchling → uv_build.” No commit, push,
release, plugin refresh or existing-consumer update is part of this request.

## Scope and policy

GitHub's latest published release was rechecked as v0.10.0, neither draft nor
prerelease. Pending 0.10.1 corrects the publisher's packaging-policy debt while
preserving public CLI, snapshot/update, lock and skill contracts. The bundle's
five metadata/runtime mirrors and uv-generated lock advance together. Skill
trees and independent versions are unchanged; both marketplace refs remain
v0.10.0. Next minor 0.11.0 remains unselected.

Starter main was rechecked at `a483e382146c6082e590e31494c07d1812645014`, unchanged
from the preceding review. Reviewed engineering alignment, versioning and
changelog support uv_build for pure Python and installed artifact verification.
This is a scoped policy correction, not formal starter adoption or a complete
engineering-conformance claim.

The [implementation plan](../superpowers/plans/2026-11-08-uv-build-migration.md)
implements the [roadmap acceptance](../roadmap.md#uv_build-migration-acceptance).
`uv_build>=0.13.7,<0.14` uses the documented bounded backend family; the manager
requirement remains minimum-only `uv>=0.13.5`. Actual builds use uv's bundled
0.13.7 backend. No runtime dependency is added.

## Resource layout decision

[Astral documents wheel data mappings](https://docs.astral.sh/uv/reference/settings/#build-backend_data)
but recommends module-local resources for ordinary small data. The canonical
root skill tree and native plugin paths rule out moving authored resources.
Use the supported `purelib = "skills"` mapping: wheel data installs the `gzs-*`
directories beside `gz_skills`. Distribution file records determine membership,
so unrelated adjacent directories do not enter the catalog. Missing manifests
produce a clear error. Editable installs still read root `skills/`.

This applicability decision avoids symlinks, generated authored mirrors and
custom build hooks. Internal archive paths change; supported user-facing
behavior does not. Revisit the data-layout choice if uv_build adds native
resource remapping or another distribution needs overlapping skill paths.
Maintainer/repository packaging owns that review; no alternate-backend exception
is retained.

## Verification

- New installed-discovery tests first failed against the old resource lookup;
  the full suite now covers owned-only discovery, absent records and missing
  manifests, plus existing install/update and PEP 610 Git-provenance cases.
- `uv run --locked python -m unittest discover -s tests -v`: 32 tests pass,
  including repository links, skill identities/prompts, floor/activation-policy
  contracts, version mirrors, setup and OpenCode adapter checks.
- All twenty `uvx --from skills-ref agentskills.exe validate <skill>` checks
  pass; validator reports 0.1.1. Activation descriptions are unchanged, and
  the existing explicit/implicit policy and router checks pass.
- Isolated release-comparable Ruff 0.17.3 check/format and ty 0.0.95 checks pass.
  Early checks used installed Ruff 0.16.2/ty 0.0.69; those are preliminary only.
- Two `uv build --no-sources --out-dir <first|second>` builds have equal
  SHA-256 digests for both wheel and sdist. A direct `--wheel` build matches
  the wheel built from the sdist. The final checker prints the actual digests;
  local artifacts live under ignored `dist/uv-build-migration/`.
- `uv run --locked python scripts/check_package.py --artifacts
  dist/uv-build-migration` verifies twenty skills and all 44 resource bytes in
  wheel, sdist and installed catalog. It excludes caches, virtual environments
  and unrelated generated dependencies from archives.
- The checker creates a fresh uv environment outside the checkout and runs
  installed imports and entry point, version/list, all-skill install, status,
  update/apply, and refusal to overwrite a locally edited skill. Wheel locks
  retain canonical `skills/<name>` paths, repository, snapshot hashes and the
  honest `package:0.10.1` source identity. Existing unit tests preserve the
  PEP 610 immutable Git-commit path; this is not a new tagged-install receipt.
- The checker replaces the wheel with an editable installation through
  `uv pip install --python <temporary-environment> --editable <checkout>` and
  probes it through `uv run --no-project` from outside the checkout: all twenty
  canonical skill directories and 44 resource bytes match. `git diff --check`
  passes.
- Independent read-only review found no concrete defects. Its test rerun was
  blocked by sandbox temp/cache ACLs; it supplies review evidence, not a second
  passing execution. Main-agent checks ran successfully with filesystem access
  for uv caches and disposable directories.

## Limits

This verifies the Windows candidate, not Linux/macOS execution or publication.
Native managed-plugin trees are unchanged; native tagged channel installs and
release-commit validation belong to a separately authorized release. No hosted
quality CI is configured. No global tool or installed consumer is upgraded.
