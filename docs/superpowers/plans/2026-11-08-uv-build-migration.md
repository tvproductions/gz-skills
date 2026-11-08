# uv_build migration implementation plan

> **For agentic workers:** Use superpowers:executing-plans to implement this plan task by task. Preserve the user's no-commit/no-push instruction.

**Goal:** Replace Hatchling with uv_build while preserving the roadmap's package and snapshot behavior.

**Architecture:** Keep `skills/` as the sole authored skill tree. Use uv_build's supported wheel `purelib` data mapping for that tree, and distribution file records for installed catalog membership. Editable installations continue reading the checkout tree.

**Tech Stack:** Managed Python 3.14.10, uv 0.13.7, uv_build 0.13.x, unittest, Ruff, ty.

**Spec:** [Roadmap migration acceptance](../../roadmap.md#uv_build-migration-acceptance).

## Global constraints

- Preserve all twenty skills and their 44 durable resources; change no skill tree.
- Preserve entry points, install/update protection, lock schema and provenance.
- Use uv exclusively; preserve minimum-only manager requirement >=0.13.5.
- Baseline v0.10.0; pending 0.10.1 is a compatible packaging-policy correction.
- Do not publish, commit, push, change release pins or propagate consumers.

## Design decisions

uv_build has no Hatchling-style force-include remapping. Moving the canonical
tree would break repository/plugin paths; symlinks would introduce Windows
checkout requirements; generated mirrors or custom build hooks add unnecessary
build state. The supported `purelib = "skills"` mapping installs the `gzs-*`
directories next to the Python module. Although Astral normally recommends
module-local data, the canonical root-tree constraint warrants this supported
option. Read only distribution-owned skill entries, never arbitrary neighboring
packages. This is an internal layout change, not a public installation contract.

## Review focus

- Installed discovery must exclude unrelated site-packages directories.
- Missing installed resources must fail clearly rather than return an empty catalog.
- Editable discovery must use current canonical resources.
- Wheel and sdist rebuilds must preserve resource bytes and omit caches.
- External install/update must retain provenance and refuse modified snapshots.

## Task 1: Backend and installed discovery

- [x] Add installed-layout discovery tests, including unrelated and missing resources; observe failure.
- [x] Replace Hatchling configuration with uv_build >=0.13.7,<0.14, explicit module name, data mapping and resource exclusions.
- [x] Adapt `src/gz_skills/core.py` installed lookup to distribution-owned paths; preserve checkout lookup.
- [x] Replace the Hatchling-specific repository test with backend-neutral exclusion and backend checks.
- [x] Synchronize bundle mirrors and uv-generated lock to 0.10.1; record classification in changelog/roadmap.

## Task 2: Package acceptance and evidence

- [x] Run all unittest, Agent Skills specification validators, Ruff, ty and diff checks.
- [x] Build twice using `uv build --no-sources`; compare artifact hashes and all canonical resources in wheel/sdist.
- [x] Verify installed imports, CLI, all-skill install/update, lock provenance and local-edit protection outside the checkout.
- [x] Verify editable installation and a wheel built directly from the checkout.
- [x] Record policy revision, decisions, commands, results and limitations in an evidence receipt; reconcile roadmap and AGENTS debt text.

## Execution record

User authorized migration on November 8, 2026. Implementation runs in the supplied
clean checkout, with no branch, commit or push. Starter source main rechecked at
`a483e382146c6082e590e31494c07d1812645014`, unchanged from the prior policy review.
No new product/workflow decisions are needed beyond the recorded acceptance.
