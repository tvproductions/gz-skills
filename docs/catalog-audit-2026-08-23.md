# Portable skill catalog audit

Date: 2026-08-23

## Result

The initial portable GovZero catalog contains eleven skills. Nine additional
skills were extracted after the two motivating examples, `gzs-git-sync` and
`gzs-update-dependencies`.

| Portable skill | Primary mature source | Why it crosses projects |
| --- | --- | --- |
| `gzs-agent-context-diet` | `gzkit/gz-context-diet` | Persistent agent context needs periodic evidence-based pruning in any repository. |
| `gzs-cross-platform-python` | `airlineops/cross-platform` | Python path, process, encoding, and shell assumptions recur independently of domain. |
| `gzs-git-sync` | `gzkit/git-sync` | A guarded, verified save-and-publish workflow is repository-independent. |
| `gzs-intent-audit` | `gzkit/gz-intent-trace` | Intent can be traced through decisions, code, tests, and docs in any project. |
| `gzs-plan-audit` | `gzkit/gz-plan-audit` | Plans need checking against current repository evidence before execution. |
| `gzs-quality-gate` | `gzkit/gz-check` | Every repository has authoritative checks even though the commands differ. |
| `gzs-repository-hygiene` | `gzkit/gz-tidy` | Safe cleanup and artifact classification are broadly useful. |
| `gzs-session-handoff` | `gzkit/gz-session-handoff` | Durable state transfer is independent of language, domain, and harness. |
| `gzs-router` | `gzkit/gz-skill-router` | A curator reduces the human cognitive load of choosing among explicit skills. |
| `gzs-tech-debt-review` | `gzkit/gz-tech-debt-review` | Evidence-based maintainability review is general engineering work. |
| `gzs-update-dependencies` | `gzkit/gz-deps-upgrade` | Dependency and toolchain refreshes share one invariant across ecosystems. |

`gzkit` was treated as the principal authority because it is the most mature
implementation. Other user-owned repositories were used to corroborate
recurrence and identify which details were local rather than copied blindly.

## Inventory scope

The inventory script scanned `C:\Users\Jeff\source\repos` recursively while
excluding Git metadata, dependency directories, virtual environments, and this
new repository. It found:

- 1,010 installed or authored skill directories;
- 198 unique declared skill names;
- 21 Git repository roots, representing 18 distinct project directory names,
  with at least one skill.

Copies in generated harness surfaces were grouped by declared skill name and
content hash. Counts therefore describe the search space, not 1,010 independent
ideas. The committed snapshot under `docs/inventory/` is authoritative; an
earlier preliminary count of 1,024 included one additional 14-skill external
Superpowers installation that was no longer present when the snapshot was
preserved.

## Ownership classification

The audit can distinguish the major sources mechanically rather than by naming
style alone:

- Matt Pocock skills are identified by the checked-in `skills-lock.json`
  records whose source is `mattpocock/skills`.
- Superpowers skills are identified from the local `superpowers` source and
  matching stock skill families copied into consumer repositories.
- GovZero candidates come from `tvproductions` repositories and are confirmed
  against their Git history, source path, and repository role. An ambiguous or
  untracked skill is not assumed to be user-authored.

No Matt Pocock or Superpowers skill was copied into this catalog. Similarity to
an external skill was treated as a reason to narrow or exclude a candidate, not
as evidence of ownership.

## User-owned work intentionally not extracted

### GovZero runtime and governance lifecycle

The `gz-adr-*`, `gz-obpi-*`, `gz-arb`, `gz-state`, `gz-status`, `gz-validate`,
`gz-agent-sync`, `gz-init`, `gz-constitute`, `gz-chore-runner`, and related
skills remain in `gzkit`. They are reusable inside a GovZero-governed project,
but they depend on GovZero state, receipts, event vocabularies, or commands and
therefore do not satisfy “regardless of project.”

### Domain workflows

AirlineOps fleet, demand, forecasting, placement, and dataset audits; X-Plane
build, backlog, artifact, flight-data, geometry, and simulator workflows; and
course exercise workflows remain with their domains. Their quality is not in
question—their objective is simply not general.

### Thin command aliases

Skills such as `format`, `lint`, `test`, `cov`, `docs-proof`, and similar
project command wrappers were not copied one-for-one. Their useful invariant is
represented by `gzs-quality-gate`; the exact commands remain consumer policy.

### Vendor or harness integrations

`ghi-*`, pull-request closeout, GitHub issue filing, and harness synchronization
skills are user-authored in places but fail the vendor-neutral criterion. They
remain valid local or vendor-specific skills.

## Borderline candidates for review

These are substantial user-owned workflows, but this pass leaves them at their
source until a cleaner portable seam is proven:

| Candidate | Why deferred |
| --- | --- |
| `gz-design` | Strong workflow, but currently coupled to GovZero decisions and overlaps external brainstorming/design skills. |
| `gz-flighttest` | Mature evidence-driven validation, but the current campaign and substrate model is GovZero-specific. |
| `gz-health-audit` | Broad objective, but its layers, chores, and governance evidence assume `gzkit`. |
| `gz-pythonic-pattern-detect` / `apply` | General to Python, but current corpus, receipts, and apply protocol are `gzkit` machinery. |
| `gz-competitor-radar` | Potentially portable research cadence, but current routing and records are governance-specific. |
| `gz-cli-audit` | Broadly useful for CLI projects, but not broad across projects and currently assumes a specific documentation contract. |

These are the best candidates for a second review. They should be extracted
only after deciding whether “broadly applicable” means every software project
or permits narrower catalogs such as Python projects and CLI projects.

## Distribution decision

The central-repository approach is sound with one important constraint: the
repository is the single authored source, while consumers receive immutable,
locked snapshots. Consumers should not track a floating branch or silently
overwrite local changes.

The included `gz-skills` CLI implements that model. It can install one or all
skills, report status, update a consumer, or propagate updates across a
repository collection. A complete skill-tree hash blocks updates when a local
copy has diverged, forcing an explicit keep, discard, or upstream-extraction
decision.
