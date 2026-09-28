# Heavy Python profile and Pythonic skills: session handoff

Observed 2026-09-28 00:57 UTC in `gz-skills` on `main` at
`d4a5565db7b312f082ee044f102893733b464898`. A fresh fetch showed
`HEAD...origin/main` at `0/0` before this save point. The worktree contained
the profile and skill changes described below, unstaged. This handoff is part
of that pending save point; recheck Git state when resuming.

## Resume point

Continue from the [adopting-project design](../proposals/lightweight-sdd-ecosystem.md)
and [heavy Python environment standard](../guides/heavy-python-environment.md).
The latest result is a reviewed normal Python 3.13.x and XPPython3-oriented
3.12.x development profile, setup and dependency-update reconciliation of its
minimum tools, and two portable Pythonic pattern skills. First verify this
handoff's commit reached `origin/main`, then inspect the SP-BP agent's actual
Python migration status before planning integrated adoption. A successful
next step would show a Python SP-BP core and an adopting-project pilot using
the selected heavy profile without duplicating project lifecycle state.

## Settled user decisions

- Heavy Python adopters use the common development assortment in the
  [environment standard](../guides/heavy-python-environment.md). Both initial
  setup and later `gzs-update-dependencies` runs add missing required
  development dependencies and refresh stale pins, groups, locks, and CI.
  The project's justified exceptions, host compatibility, and gate remain
  project-owned. The exact development patch belongs in `.python-version`;
  `requires-python` states tested package compatibility.
- Ordinary Python uses the latest supported 3.13.x patch; code loaded by or
  shared with XPPython3 uses the latest supported 3.12.x patch and is verified
  against the real host. Pydantic is an optional approved runtime package in
  the ordinary profile and excluded by policy from the XPPython3 profile.
- `uv_build` is the preferred pure-Python backend after wheel, sdist, entry
  point, and resource parity are proved. PyInstaller applies when shipping an
  executable. Cosmic Ray belongs to the development assortment, with selected
  mutation targets rather than a universal score.
- The [Pythonic detection](../../skills/gzs-pythonic-pattern-detect/SKILL.md)
  and [application](../../skills/gzs-pythonic-pattern-apply/SKILL.md) curations
  join the existing hexagonal audit. Detection is read-only; application
  handles one authorized refactor with unchanged before/after behavior
  evidence. gzkit's scanner, archive, chores, and receipts remain local.
- The broader SP/SP-BP/MPAS architecture and Python-only SP-BP core decisions
  remain in the [design proposal](../proposals/lightweight-sdd-ecosystem.md)
  and the [earlier handoff](20260927T232837Z-python-sdd-ecosystem.md).

## Completed here

- Updated [`gzs-project-setup`](../../skills/gzs-project-setup/SKILL.md) to
  guide and reconcile the minimum profile after heavy selection; updated
  [`gzs-update-dependencies`](../../skills/gzs-update-dependencies/SKILL.md)
  to add missing profile dependencies during a later refresh.
- Added the two Pythonic skill trees at version `0.1.0`, routed them through
  [`gzs-router`](../../skills/gzs-router/SKILL.md), and listed them in the
  Claude manifest and README. [Provenance](../origins.md) records the gzkit
  source revision. Bundle `0.6.0` remains a candidate, not a released tag.
- Recorded the [cross-repository inventory](../research/python-install-profile-evidence-2026-09-27.md)
  and distinguished the later user-supplied gzkit upgrade snapshot from the
  locally inspected checkout.
- The final gate before creating this handoff passed: 28 Python tests (including
  two OpenCode adapter tests), all 19 Agent Skills validations,
  `uv lock --check`, `uv build`, and `claude plugin validate . --strict`.
  The exact `0.6.0` wheel and sdist contain both new skills. Run the final
  staged-diff and worktree checks during git-sync.

## Follow-on actions and open loops

1. Verify the pushed commit, ahead/behind counts, and clean worktree. This
   session's explicit git-sync authorization covers this repository's current
   save point; it does not create a release tag or publish a plugin channel.
2. In gzkit's own repository, reconcile its `gz-deps-upgrade` instruction to
   leave `.python-version` at `3.13` with the agreed exact-patch policy. Its
   workflow also needs to compare against the adopted minimum profile. No
   gzkit files were changed here.
3. Check the separate SP-BP agent's branch, ADR, plan, and worktree. The user
   requires a Python project; an earlier Go implementation was reported but
   its current migration state is not verified from this repository.
4. Curate the four attributed MPAS skills and their upstream maintenance chore
   as planned in the design proposal. Then pilot first-use setup, dependency
   reconciliation, and the integrated SP/SP-BP flow in an adopting project.
5. Keep release work separate. `0.6.0` requires an immutable tag and the
   channel-specific validation, installation, and publication evidence in
   [packaging contracts](../packaging.md) before claiming availability.
