# Pre-implementation gate applicability correction

November 13, 2026. Decision: correct `gzs-git-sync` 1.0.1 and
`gzs-quality-gate` 0.1.2 without changing project-owned authority or invocation.
Candidate skill versions are 1.0.2 and 0.1.3; bundle candidate is 0.10.2.

## Report and observed cause

The maintainer reported repeated Git-sync stops in a planning project because
unittest discovered zero tests and returned 5. Read-only inspection of the local
GZYoke checkout confirmed the reported mechanism: `AGENTS.md` calls its current
zero-test run a bootstrap check and defers runtime implementation, but
`.pre-commit-config.yaml` runs `uv run --locked python -m unittest discover -v`
unconditionally with `always_run: true`. Its `docs/research/verification.md`
records that failure, successful other checks and seven unpublished paths.
This is observed project configuration and recorded evidence, not a fresh
execution of the consuming project's gate or a claim about its current remote.

The portable instructions said to run required gates and stop on unresolvable
failure, but supplied no procedure for deciding whether a behavioral test
dimension existed yet. Quality gate likewise lacked the distinction between
inapplicable verification and failed required verification. The resulting
bootstrap mismatch repeatedly became a request for a bypass or fabricated tests.

The correction resolves applicability before execution, requires complete-tree
inspection and permits only project-authorized configuration repair. A failed
aggregate still needs a genuine correction and successful rerun; it cannot be
relabeled green. An explicit unconditional test requirement remains controlling.
For the reported adopter, a skill upgrade alone cannot change the installed
hook: the owning project must reconcile its hook, CI and governing scope.

## Static acceptance cases

These are analytical instruction reviews, not native model execution results.

| Case | Required result under both corrected skills |
| --- | --- |
| Planning-only tree; policy permits pre-implementation validation; no executable behavior or test assets | Report behavioral tests not applicable with evidence; run checks for actual artifacts and continue if all required checks succeed. |
| Runner is scaffolded but never required by project policy | Its presence alone does not impose behavioral tests or require creating implementation. |
| Hook unconditionally runs an empty suite despite permitted planning scope; repair authorized | Correct the project-owned applicability condition and relevant hook/CI/guidance, then rerun the complete gate with hooks enabled. |
| Same mismatch; ordinary sync authorization only, with explicit unconditional test requirement | Identify the exact owning policy conflict and bounded correction; preserve that requirement rather than silently overriding it. |
| Documentation-only diff in a repository with an existing implementation | Run required implementation tests; changed file type does not waive them. |
| Executable helper exists in an otherwise planning repository | Investigate applicable helper tests; a planning label does not excuse implemented behavior. |
| Tests exist but wrong discovery scope finds none | Repair discovery where authorized; do not classify the suite as inapplicable. |
| Import/discovery error or failing test | Preserve the failure and fix within scope or stop; do not convert a numeric status to success. |
| Runner exits successfully after finding zero tests | Inspect count and scope anyway; exit 0 alone does not prove testing or inapplicability. |
| Implementation or test assets are later added | A project-owned applicability condition must enforce tests automatically; a permanent allow-empty switch or manual phase label is insufficient. |
| Aggregate previously failed | Record the failed attempt; require corrected aggregate execution before claiming pass. |
| Proposed workaround uses dummy tests, hook skipping or blanket exit suppression | Reject the workaround; preserve meaningful tests, hooks and thresholds. |

The Git-sync activation description and explicit-only metadata are unchanged:
commit/push requests trigger it; review-only and local-only requests do not.
Quality gate remains applicable to full-verification requests without becoming
a feature implementation or release workflow. No scripts or cross-skill
dependencies were added; each skill remains independently usable.

## Release classification and authority check

Baseline: published v0.10.1, release commit
`4c836e3db6d43c495863a2090daaea56585a6ea9`, confirmed through the local immutable
tag and GitHub's latest-release response on November 13. Existing pending skill
changes were absent before this correction. Pending 0.10.2 contains only this
bounded defect correction and its evidence/version bookkeeping. Completion is
the case review plus the repository's validation sequence. Publication,
consumer upgrades, starter hook implementation and catalog-wide stable review
are excluded. No snapshot, installer, settings or authorization contract changes.

The canonical starter's current main was checked via GitHub and matched the
clean local checkout at `77bce3bdeb77c5679cb6eed3e569a2b32a412df1`.
Reviewed inputs: `docs/versioning.md`, `CHANGELOG.md`,
`docs/baseline-policy.md` and `docs/engineering/python.md`. The starter is a
development 0.10.0 candidate above published 0.9.0; this is not an installed
template upgrade. Its patch classification permits compatible corrections to
existing commitments and preserves consumer policy authority. Its unittest
and pre-commit selection supplies no portable permission to suppress failures.
The pending ADR and dependency-migration directions are separate companion
work; this bounded correction claims neither delivery nor full conformance.
No exception to required gates is introduced. Future source/adopter repair
must resolve that project's own governing policy and propagation requirements.

## Verification limits

Repository checks and a disposable runner probe are recorded below.
Structural checks prove packaging/instruction integrity, not model
behavior or successful synchronization in the reported adopter. Historical
Git-sync native acceptance remains historical; this scenario has not been added
to its native behavioral certification. No installed plugin cache, starter
checkout or adopting-project file is changed by this patch.

Observed locally with uv 0.13.6 and managed Python 3.14.10:

| Check | Observed result |
| --- | --- |
| `uv run --locked python -m unittest discover -s tests -v` | Exit 0; all 32 tests passed, including name/directory agreement, prompts, relative links, manifests and installer protection. |
| `uvx --from skills-ref agentskills validate <skill-directory>` for every canonical skill | All twenty directories valid. |
| Activation description review across the catalog | Unchanged triggers; no new implicit sync/publication authority or unwanted planning-to-implementation activation. |
| `uvx ruff check .` / `uvx ruff format --check .` | Exit 0; Ruff 0.17.3, 75 Python files already formatted. |
| `uvx ty check` | Exit 0; ty 0.0.93. This records the executing tool, not a latest-stable claim. |
| `uv build` | Exit 0; candidate 0.10.2 wheel and source archive built. |
| `git diff --check` | Exit 0. |

A standard-library probe executed through `uv run --locked python` created an
isolated temporary documentation tree. Its runner was
`uv run --no-project --python 3.14.10 python -m unittest discover -v`:

1. No tests: zero discovered, exit 5.
2. Add a real charter-content assertion under a non-package `tests/` directory:
   default discovery still found zero tests, exit 5.
3. Add `-s tests` to discovery: the assertion ran and passed, exit 0.
4. Change the charter to violate the assertion: one failing test, exit 1.

Both legitimate absence and misconfigured discovery therefore produced the
reported empty-suite status on this runtime. This directly supports diagnosing
scope/counts rather than treating status 5 as either universal failure or
universal success. The probe checked documentation content in disposable files;
no placeholder tests or product implementation were added to any repository.
It demonstrates runner behavior, not execution of a new project-owned gate or
native agent compliance with the corrected prose.
