# gz-skills agent guidance

Build this repository as the canonical, vendor-neutral library of portable
GovZero skills.

## Source and boundary

- Author skills only under `skills/<skill-name>/`.
- Keep project-specific commands, paths, versions, branch names, and governance
  ceremonies in the consuming project.
- Preserve the invariant and completion criteria shared by proven project
  implementations.
- Treat `.agents/skills`, `.claude/skills`, `.github/skills`, and `.gzkit/skills`
  as consumer installation surfaces. Do not add generated mirrors here.
- Keep `gzkit` runtime behavior in `gzkit`; a portable skill may use a documented
  `gz` command when present but must state a safe discovery or fallback path.

## Skill contract

- Follow the open Agent Skills directory and frontmatter specification.
- Prefix public skill names with `gzs-` to identify the `gz-skills` release
  contract and avoid collisions with project-local `gz-*` skills.
- Apply `gzs-` to the skill directory, frontmatter `name`, and invocation token.
  Keep headings and UI display names human-readable; prefer the established
  `GovZero ...` labels rather than exposing a raw identifier as display copy.
- Keep each skill focused on one user goal.
- Put branch-specific detail in `references/` and deterministic repeated logic in
  `scripts/` only after real usage proves it useful.
- Store GovZero-specific string metadata under `metadata` keys prefixed with
  `govzero-`.
- Use `agents/openai.yaml` only for OpenAI UI metadata or invocation policy; the
  workflow must remain usable when a harness ignores that file.
- Remote-mutating skills default to explicit invocation where the harness
  supports it.

## Versioning and provenance

- Follow Semantic Versioning 2.0.0 for both the bundle and each skill. Versions
  advance from released state; an unreleased correction may amend its pending
  version, but never decrement or reuse a published version.
- Keep the bundle version synchronized across `pyproject.toml`,
  `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and `package.json`.
  Use major for an incompatible installer, lock, or bundle contract; minor for
  backward-compatible catalog or installer capability; and patch for compatible
  fixes or packaging and metadata corrections.
- Version each skill independently with `metadata.govzero-version`. Use major
  for an incompatible invocation, workflow, safety, or authorization change;
  minor for backward-compatible new capability or expanded scope; and patch for
  compatible fixes, clarifications, activation metadata, prompts, or packaged
  supporting-resource changes. Repository-only tests and documentation do not
  change a skill version.
- Record every user-visible bundle or skill change under `Unreleased` in
  `CHANGELOG.md`. At release, rename that section to the released bundle version
  and ISO date, then create a fresh `Unreleased` section.
- Consumers install immutable snapshots and record the fields defined by
  `schemas/skill-lock.schema.json`.
- An updater may replace an installed skill only when its current hash still
  matches the prior lock. Treat a mismatch as a local modification and stop for
  reconciliation.
- Support exactly two consumer channels: native managed Codex, Claude Code, and
  OpenCode plugins, then Python `uvx` snapshots when repository vendoring is
  required. Keep Node tooling outside the supported install and update contract;
  OpenCode owns the runtime for its bundled adapter.

## Validation

Before handoff:

1. Validate every `skills/*/SKILL.md` against the Agent Skills specification.
2. Confirm the frontmatter name matches its parent directory.
3. Confirm every relative file link resolves.
4. Confirm each `agents/openai.yaml` default prompt names its skill explicitly.
5. Review activation descriptions for both intended and unintended triggers.

Preserve user changes. Do not commit or push unless explicitly requested.
