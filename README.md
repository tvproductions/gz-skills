# gz-skills

`gz-skills` is the canonical library for portable GovZero agent skills:
workflows that should behave consistently across projects without belonging to
one project's architecture, runtime, vendor, or agent harness.

The first catalog contains eleven workflows distilled primarily from `gzkit`, with
corroborating implementations from other `tvproductions` repositories:

- `gz-agent-context-diet`
- `gz-cross-platform-python`
- `gz-git-sync`
- `gz-intent-audit`
- `gz-plan-audit`
- `gz-quality-gate`
- `gz-repository-hygiene`
- `gz-session-handoff`
- `gz-skill-router`
- `gz-tech-debt-review`
- `gz-update-dependencies`

The extraction evidence and the broader review are in
[`docs/origins.md`](docs/origins.md) and
[`docs/catalog-audit-2026-08-23.md`](docs/catalog-audit-2026-08-23.md).
The packaging comparison with Superpowers and Matt Pocock is in
[`docs/research/skills-library-packaging-methodology.md`](docs/research/skills-library-packaging-methodology.md).
The preserved raw-name summary and user-owned candidate ledger are under
[`docs/inventory/`](docs/inventory/), and the one-by-one review queue is
[`docs/review/README.md`](docs/review/README.md).

## Boundary

This repository owns reusable workflow intent, completion criteria, safety
invariants, optional references, and deterministic helpers that travel with a
skill. It does not own a consuming project's commands, quality policy, branch
policy, or generated harness mirrors.

- `gzkit` continues to own `gz` commands, governance events, attestation, and
  control-surface synchronization.
- A consuming project owns its `AGENTS.md`, verification commands, and any local
  adaptation of a skill.
- `.agents/skills`, `.claude/skills`, `.codex/skills`, `.github/skills`, and
  `.gzkit/skills` are installation surfaces, not authored copies here.

## Install

Choose one installation contract for a given agent scope. Installing the same
skill through more than one channel creates duplicate discovery. See
[`docs/packaging.md`](docs/packaging.md) for ownership, update, and publication
details.

### Editable universal install

After the repository is published, use the same open installer as Matt Pocock's
skills:

```powershell
npx skills@latest add tvproductions/gz-skills
```

The installer discovers all eleven skills and lets the user select skills,
scope, and supported agents. The resulting copies belong to the consumer and
update only when the consumer runs `npx skills update`.

Preview the local checkout without installing:

```powershell
npx skills@latest add . --list
```

### Managed plugins

The repository contains native Codex and Claude plugin manifests over the same
canonical `skills/` tree. The Codex manifest is ready for marketplace packaging.
After publication, Claude Code can use the repository marketplace fallback:

```text
/plugin marketplace add tvproductions/gz-skills
/plugin install gz-skills@gz-skills
```

A managed plugin is a read-only subscription to the released bundle. Do not
edit its installed cache; update it through the harness's plugin manager.

### GovZero fleet administration

The Python CLI is the advanced path for pinned snapshots, local-edit detection,
and controlled propagation across a repository collection.

List the catalog:

```powershell
uv run gz-skills list
```

Install selected skills into a project's standard agent surface:

```powershell
uv run gz-skills install `
  --project C:\path\to\project `
  --surface agents `
  gz-git-sync gz-quality-gate
```

Use `--all` for the complete catalog. Other supported surfaces are `claude`,
`codex`, `github`, and `gzkit`; `--target` accepts an exact skills directory.

After this repository is published, the fleet command can run without a local
checkout:

```powershell
uvx --from git+https://github.com/tvproductions/gz-skills.git `
  gz-skills install --project C:\path\to\project gz-git-sync
```

Every install writes a consumer-owned `gz-skills.lock.json` with the source
identity, independent skill version, complete tree hash, and installed path.

## Update and propagate

Preview one consumer:

```powershell
uv run gz-skills update --lock C:\path\to\project\gz-skills.lock.json
```

Apply safe updates:

```powershell
uv run gz-skills update `
  --lock C:\path\to\project\gz-skills.lock.json `
  --apply
```

Preview or apply every consumer below a repository collection:

```powershell
uv run gz-skills propagate C:\Users\Jeff\source\repos
uv run gz-skills propagate C:\Users\Jeff\source\repos --apply
```

An update replaces only an installed tree that still matches its prior lock.
Missing or locally edited copies block propagation and require reconciliation;
they are never silently overwritten. See
[`docs/provenance.md`](docs/provenance.md) for the full contract.

## Layout

```text
gz-skills/
|-- skills/                 # canonical Agent Skills
|-- src/gz_skills/          # installer and propagation CLI
|-- scripts/                # maintainer inventory tooling
|-- schemas/                # consumer lock contract
|-- docs/                   # provenance and extraction evidence
`-- tests/
```

## Admission rule

A workflow belongs here when its project-independent invariant is clear and a
real implementation demonstrates it. Repetition across projects is strong
evidence, but a mature `gzkit` workflow may qualify when the portable core can
be separated cleanly from GovZero runtime behavior.

Project commands and policy stay behind the consuming project's documented
seams. A tool wrapper, domain workflow, or harness-specific integration does not
become portable merely because several projects copied it.

## Validate

```powershell
uv run python -m unittest discover -s tests -v

Get-ChildItem .\skills -Directory | ForEach-Object {
    uvx --from skills-ref agentskills.exe validate $_.FullName
}

uv build
```
