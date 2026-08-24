# Packaging contracts

`gz-skills` has one canonical flat skill tree and two supported installation
contracts. Choose one contract per agent scope.

| Contract | Owner of installed files | Update mechanism | Local edits |
| --- | --- | --- | --- |
| Native managed plugin | Publisher/harness | Harness plugin manager | Unsupported in the installed cache. |
| Python vendored snapshot | Consumer with upstream provenance | `uvx ... gz-skills update` or `propagate` | Detected by complete tree hash and blocks replacement. |

## 1. Native managed plugins

- [`.codex-plugin/plugin.json`](../.codex-plugin/plugin.json) exposes the flat
  canonical `skills/` directory and passes the Codex plugin validator.
- [`.claude-plugin/plugin.json`](../.claude-plugin/plugin.json) explicitly lists
  all promoted skills and its repository marketplace passes
  `claude plugin validate . --strict`.
- [`package.json`](../package.json) exposes the package-local
  [OpenCode adapter](../.opencode/plugins/gz-skills.js). OpenCode's own managed
  runtime loads the adapter, which registers the canonical `skills/` directory
  through the native skill loader. This adds no Node command, dependency, or
  project toolchain to the supported contract.

Claude's `disable-model-invocation` frontmatter and Codex's explicit-invocation
metadata are not mutually accepted by the Codex plugin validator. The canonical
tree therefore uses `agents/openai.yaml` for Codex policy. Before the first
managed Claude release, decide whether to build a generated Claude artifact
that adds its frontmatter policy to explicit-only skills. Such an artifact must
be generated from the canonical tree and tested for drift; it must not become a
second authored copy.

## 2. Python vendored snapshots

The Python distribution bundles the canonical skill trees and exposes:

```text
gz-skills list
gz-skills install
gz-skills status
gz-skills update
gz-skills propagate
```

Install from a tagged Git revision with `uvx`; Node is not part of the supported
consumer toolchain:

```powershell
uvx --from git+https://github.com/tvproductions/gz-skills.git@v0.1.0 `
  gz-skills install --project C:\path\to\project gzs-git-sync
```

The fleet lock records source identity, bundle path, independent skill version,
installed path, and complete tree hash. Local edits block replacement until the
consumer reconciles them explicitly.

## Release identity

The public bundle version is synchronized across `pyproject.toml`, the Codex
manifest, the Claude manifest, and the OpenCode package manifest. An immutable
Git tag identifies a released catalog. Individual skill versions identify the
changed subset for fleet administration.

Publication still requires:

1. Complete the one-by-one review and behavioral evidence.
2. Select a license.
3. Build from the clean release commit and record artifact SHA-256 values.
4. Tag the release and publish or submit the native marketplace entries.
