# Packaging contracts

`gz-skills` has one canonical flat skill tree and three installation contracts.
Choose one contract per agent scope.

| Contract | Owner of installed files | Update mechanism | Local edits |
| --- | --- | --- | --- |
| Universal editable copy | Consumer | `npx skills update` | Allowed; reconcile before accepting upstream replacement. |
| Native managed plugin | Publisher/harness | Harness plugin manager | Unsupported in the installed cache. |
| GovZero fleet snapshot | Consumer with upstream provenance | `gz-skills update` or `propagate` | Detected by complete tree hash and blocks replacement. |

## Universal editable copy

After publication:

```powershell
npx skills@latest add tvproductions/gz-skills
```

An isolated local installation test confirmed that `skills@latest` discovers
all eleven skills and copies a selected skill into Codex's `.agents/skills`
surface.

## Native managed plugins

- [`.codex-plugin/plugin.json`](../.codex-plugin/plugin.json) exposes the flat
  canonical `skills/` directory and passes the Codex plugin validator.
- [`.claude-plugin/plugin.json`](../.claude-plugin/plugin.json) explicitly lists
  all promoted skills and its repository marketplace passes
  `claude plugin validate . --strict`.

Claude's `disable-model-invocation` frontmatter and Codex's explicit-invocation
metadata are not mutually accepted by the Codex plugin validator. The canonical
tree therefore uses `agents/openai.yaml` for Codex policy. Before the first
managed Claude release, decide whether to build a generated Claude artifact
that adds its frontmatter policy to explicit-only skills. Such an artifact must
be generated from the canonical tree and tested for drift; it must not become a
second authored copy.

## GovZero fleet snapshots

The Python distribution bundles the canonical skill trees and exposes:

```text
gz-skills list
gz-skills install
gz-skills status
gz-skills update
gz-skills propagate
```

The fleet lock records source identity, bundle path, independent skill version,
installed path, and complete tree hash. This is intentionally stricter than the
universal editable-copy contract.

## Release identity

The public bundle version is synchronized across `pyproject.toml`, the Codex
manifest, and the Claude manifest. An immutable Git tag identifies a released
catalog. Individual skill versions identify the changed subset for fleet
administration.

Publication still requires:

1. Complete the one-by-one review and behavioral evidence.
2. Select a license.
3. Create the `tvproductions/gz-skills` remote and make an initial commit.
4. Build from the clean release commit and record artifact SHA-256 values.
5. Tag the release and publish or submit the native marketplace entries.
