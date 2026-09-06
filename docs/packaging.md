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
tree therefore uses `agents/openai.yaml` for Codex policy.

The `v0.2.0` Claude package deliberately ships that canonical Agent Skills tree
unchanged. It does not build a Claude-specific transformed copy. Explicit-only
intent remains part of each affected skill's activation description and
authority boundary, while Codex additionally enforces its invocation policy
through `agents/openai.yaml`. This is a documented 0.x harness limitation, not
permission for an implicitly selected skill to perform a remote mutation.

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
uvx --from git+https://github.com/tvproductions/gz-skills.git@v0.2.0 `
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

Every publication requires a clean, validated release commit, synchronized
bundle manifests, reproducible artifacts with recorded SHA-256 values, and an
immutable Git tag. The repository is licensed under the
[MIT License](../LICENSE).

The one-by-one skill review and behavioral evidence in
[`docs/review/README.md`](review/README.md) gate the stable `1.0.0` release.
They remain intentionally in progress during the 0.x development series.
