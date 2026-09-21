# gz-skills

`gz-skills` is the canonical library for portable GovZero agent skills:
workflows that should behave consistently across projects without belonging to
one project's architecture, runtime, vendor, or agent harness.

The catalog contains sixteen workflows distilled primarily from `gzkit`, with
corroborating implementations from other `tvproductions` repositories:

- `gzs-agent-context-diet`
- `gzs-change-review`
- `gzs-cross-platform-python`
- `gzs-dependency-risk-audit`
- `gzs-git-sync`
- `gzs-hexagonal-architecture-audit`
- `gzs-intent-audit`
- `gzs-plan-audit`
- `gzs-quality-gate`
- `gzs-repository-hygiene`
- `gzs-root-cause-debugging`
- `gzs-router`
- `gzs-session-handoff`
- `gzs-tech-debt-review`
- `gzs-test-driven-change`
- `gzs-update-dependencies`

The extraction evidence and the broader review are in
[`docs/origins.md`](docs/origins.md) and
[`docs/catalog-audit-2026-08-23.md`](docs/catalog-audit-2026-08-23.md).
The packaging comparison with Superpowers and Matt Pocock is in
[`docs/research/skills-library-packaging-methodology.md`](docs/research/skills-library-packaging-methodology.md).
The preserved raw-name summary and user-owned candidate ledger are under
[`docs/inventory/`](docs/inventory/), and the one-by-one review queue is
[`docs/review/README.md`](docs/review/README.md).
Release-facing changes are maintained in [`CHANGELOG.md`](CHANGELOG.md).
The latest immutable bundle release is `v0.5.0`; `v0.2.0` was the first. The
catalog remains in the SemVer 0.x development series while the one-by-one
behavioral review matures toward 1.0.0.

## Latest catalog expansion

The `0.3.0` release promotes `gzs-change-review`,
`gzs-dependency-risk-audit`, and `gzs-test-driven-change`. They remain
horizontal disciplines beneath project-owned workflows, not replacements for
`gzkit` lifecycle orchestration. Their contracts, boundaries, and promotion
record are described in [`docs/roadmap.md`](docs/roadmap.md).

## Boundary

This repository owns reusable workflow intent, completion criteria, safety
invariants, optional references, and deterministic helpers that travel with a
skill. It does not own a consuming project's commands, quality policy, branch
policy, or generated harness mirrors.

The `gzs-` prefix identifies skills whose canonical source and release contract
belong to this repository. Project-local skills use a project or domain prefix;
third-party skills retain their upstream names.

- `gzkit` continues to own `gz` commands, governance events, attestation, and
  control-surface synchronization.
- `gz-skills` owns portable horizontal disciplines that remain useful without
  `gzkit`; it does not provide a competing project lifecycle.
- An active project-owned workflow takes precedence. It may compose a `gzs-*`
  primitive, but the primitive must not bypass its stages, gates, state, locks,
  receipts, or human decisions.
- A consuming project owns its `AGENTS.md`, verification commands, and any local
  adaptation of a skill.
- `.agents/skills`, `.claude/skills`, `.codex/skills`, `.github/skills`, and
  `.gzkit/skills` are installation surfaces, not authored copies here.

## Install

Choose one of the two supported contracts for a given agent scope. Installing
the same skill through both creates duplicate discovery. See
[`docs/packaging.md`](docs/packaging.md) for ownership, version decisions,
and publication gates.

### 1. Native managed plugins (preferred)

The repository contains native Codex, Claude Code, and OpenCode plugin adapters
over the same canonical `skills/` tree.

- Codex can install the released bundle from this repository marketplace:

  ```text
  codex plugin marketplace add tvproductions/gz-skills@v0.5.0
  codex plugin add gz-skills@gz-skills
  ```

  A listing in the universal public Plugins Directory requires separate review
  and publication.

- Claude Code can use the repository marketplace, whose plugin source is pinned
  to the latest released Git tag:

  ```text
  /plugin marketplace add tvproductions/gz-skills
  /plugin install gz-skills@gz-skills
  ```

- OpenCode v2 can install the `v0.5.0` Git package per project. The
  earlier `v0.4.0` package uses the OpenCode v1 adapter.

  In each adopting repository, add this to its `opencode.jsonc`:

  ```jsonc
  {
    "$schema": "https://opencode.ai/config.json",
    "plugins": [
      "git+https://github.com/tvproductions/gz-skills.git#v0.5.0"
    ]
  }
  ```

  OpenCode registers the canonical `skills/` tree through its v2 skill
  transform. See [the OpenCode install guide](.opencode/INSTALL.md) for
  verification and update notes.

A managed plugin is a read-only subscription to the released bundle. Do not
edit its installed cache; update it through the harness's plugin manager.

### 2. Python vendoring and fleet administration

Use the Python CLI when a repository must carry pinned, reviewable skill
snapshots. The consumer needs `uv`, not Node.js. Install directly from an
immutable release tag:

```powershell
uvx --from git+https://github.com/tvproductions/gz-skills.git@v0.5.0 `
  gz-skills install `
  --project C:\path\to\project `
  gzs-git-sync gzs-quality-gate
```

The default `agents` surface writes to `.agents/skills`. Use `--all` for the
complete catalog. Every install writes `gz-skills.lock.json` with source
identity, independent skill version, complete tree hash, and installed path.

For development from this checkout, run the same CLI through `uv`:


```powershell
uv run gz-skills list
uv run gz-skills install `
  --project C:\path\to\project `
  gzs-git-sync gzs-quality-gate
```

Other supported surfaces are `claude`, `codex`, `github`, and `gzkit`;
`--target` accepts an exact skills directory. Prefer native plugins for Codex,
Claude Code, and OpenCode unless the repository specifically requires
checked-in snapshots.

## Update and propagate

Preview one consumer:

```powershell
uvx --from git+https://github.com/tvproductions/gz-skills.git@v0.5.0 `
  gz-skills update --lock C:\path\to\project\gz-skills.lock.json
```

Apply safe updates:

```powershell
uvx --from git+https://github.com/tvproductions/gz-skills.git@v0.5.0 `
  gz-skills update `
  --lock C:\path\to\project\gz-skills.lock.json `
  --apply
```

Preview or apply every consumer below a repository collection:

```powershell
uvx --from git+https://github.com/tvproductions/gz-skills.git@v0.5.0 `
  gz-skills propagate C:\Users\Jeff\source\repos
uvx --from git+https://github.com/tvproductions/gz-skills.git@v0.5.0 `
  gz-skills propagate C:\Users\Jeff\source\repos --apply
```

An update replaces only an installed tree that still matches its prior lock.
Select the release tag whose snapshots should become available before applying
an update.
Missing or locally edited copies block propagation and require reconciliation;
they are never silently overwritten. See
[`docs/provenance.md`](docs/provenance.md) for the full contract.

## Future public directory listings

The GitHub repository marketplace and tagged Git package above are available
now. A platform's public directory is a separate discovery channel: adding
this repository as a marketplace does not submit it for a public listing.

- **ChatGPT and Codex:** Follow the [OpenAI plugin submission process](https://developers.openai.com/plugins/deploy/submission).
  Verify the publisher identity and Apps Management access; prepare the public
  listing, support, privacy, and terms URLs; create a **Skills only** draft;
  upload the final skill bundle; add starter prompts and at least five positive
  and three negative test cases. Submit for review, then publish after approval.
  The resulting listing appears in the shared ChatGPT and Codex Plugins
  Directory. Each later directory version also requires review and publication.
- **Claude Code:** Validate the released plugin with
  `claude plugin validate . --strict`, then use the [Claude community marketplace
  submission form](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace).
  After review and catalog sync, users can discover it through `claude-community`.
  Anthropic curates `claude-plugins-official` separately; the submission form
  does not apply for that marketplace.
- **OpenCode:** The tagged Git package remains the supported install path.
  For discovery, propose it for the [OpenCode ecosystem list](https://opencode.ai/docs/ecosystem/)
  by pull request; a listing does not change the install command. Publishing
  to the `npm` registry would add a distribution channel and requires an
  explicit change to this repository's release contract before doing so.

Public listings can shorten discovery and personal plugin installation. They
do not replace pinned, reviewable copies in repositories that choose vendoring.
Track each directory's acceptance and published version separately from the
GitHub release; do not claim a listing from a submission or local install.

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

## License

`gz-skills` is available under the [MIT License](LICENSE).
