# Preserved skill inventory

This directory preserves the evidence behind the initial GovZero extraction.
The JSON files are snapshots, not live generated mirrors.

## Snapshots

- [`skill-inventory-2026-08-23.json`](skill-inventory-2026-08-23.json) records
  all 198 unique declared names found across 1,010 skill installations, with
  projects, surfaces, descriptions, and content-variant counts.
- [`user-skill-candidates-2026-08-23.json`](user-skill-candidates-2026-08-23.json)
  records 144 candidate user-authored names from canonical GovZero and
  project-local source surfaces after separating installed Matt Pocock and
  Superpowers copies.

The candidate label establishes likely ownership, not portability. Domain,
vendor, harness, thin-wrapper, and GovZero-runtime classification still applies.

## Extracted source mappings

| Portable skill | Source names represented |
| --- | --- |
| `gz-agent-context-diet` | `gz-context-diet` |
| `gz-cross-platform-python` | `cross-platform` |
| `gz-git-sync` | `git-sync`, `gz-git-sync` |
| `gz-intent-audit` | `gz-intent-trace` |
| `gz-plan-audit` | `gz-plan-audit` |
| `gz-quality-gate` | `gz-check`, `quality-gate`, `quality-check` |
| `gz-repository-hygiene` | `gz-tidy`, `repo-hygiene`, `maintenance-qa` |
| `gz-session-handoff` | `gz-session-handoff` |
| `gz-skill-router` | `gz-skill-router` |
| `gz-tech-debt-review` | `gz-tech-debt-review` |
| `gz-update-dependencies` | `gz-deps-upgrade`, `refresh-dependencies`, `hygiene` |

See [`../origins.md`](../origins.md) for source revisions and
[`../catalog-audit-2026-08-23.md`](../catalog-audit-2026-08-23.md) for the
admission decisions.

## Reproduce a current scan

From the repository root:

```powershell
uv run python scripts/inventory_skills.py `
  C:\Users\Jeff\source\repos `
  --exclude-project gz-skills
```

A new scan describes current filesystem state. It does not replace this dated
snapshot without an explicit inventory refresh and review of the diff.
