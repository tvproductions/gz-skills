# Python environment authority for adopting projects

The consuming project owns its runtime, tool assortment, package choices and
verification gates. gz-skills discovers and applies that authority; it does not
maintain a competing Python standard. This guide replaces the former ordinary
3.13/XPPython3 profile and shared tool assortment. Historical receipts retain
what they actually tested.

## Resolve authority before environment choices

1. Read the project's governing instructions and adopted policy. If a starter
   is adopted, identify its recorded version/revision and applicable baseline.
   Read that source before selecting a family or calling a difference drift.
2. Record the authority, selected runtime family, exact execution pin, package
   support range, host constraints and gate/tool requirements separately.
   `.python-version`, `pyproject.toml` and the actual environment supply distinct
   evidence; a stored pin cannot override the governing policy.
3. Reconcile explicit local exceptions through their recorded owner and evidence.
   A mode choice does not adopt a starter or prove integrated readiness.
4. If authority is missing, unavailable or contradictory, report the dependent
   decision UNKNOWN and obtain the missing source/decision. Do not treat an
   inaccessible starter as a policy gap that library defaults may fill. Continue
   independent inventory or settings work without inventing a runtime policy.

The maintainer's [starter baseline](https://github.com/tvproductions/gz-skills-first-starter/blob/main/docs/baseline-policy.md)
is the authority where that starter governs a project. Read the project's
reviewed adopted revision, not an assumed latest value from this guide.
Unrelated consumers retain their own approved policy. This repository's own
Python choice is recorded in AGENTS and its [source binding](../release-policy.md),
not exported as a portable skill requirement.

## Apply the selected policy

- Preserve the approved family, supported range, additional packages, sources,
  retired tools, settings and explicit profile. Refresh the authorized patch
  within that family; family migration needs its own reviewed scope.
- Reconcile only the project's required tools. No library-owned default list,
  analyzer selection, Pydantic permission/exclusion or packaging preference can
  override it. Selecting heavy does not authorize unrelated installation.
- Keep actual manager provenance separate from CI's tested selection and its
  compatibility requirement. Enforce only the matching/version rules that the
  governing project declares. A supported manager need not be the freshest one.
- Preserve the existing dependency manager and generated lock contract. Use its
  owning tooling for authorized updates; keep package/backend compatibility
  claims separate from development interpreter selection.
- Verify applicable project gates and installed artifacts. Record actual inputs,
  checks, exceptions and missing evidence; installed versions and a profile
  declaration alone do not establish readiness or freshness.

## Host-bound projects

Identify code that actually loads in, or is shared with, an embedded host.
Inspect the installed host's interpreter and packages separately. A development
pin is a discovery signal, not proof of host orientation or compatibility.
Follow the project's host-supported family and verify plugin startup in the
real host. An external development interpreter does not replace an embedded one.

## Migration from the retired defaults

Existing projects retain their approved choices. The removed fallback family,
tool assortment and package restrictions do not justify rewriting an adopter.
Projects governed by a starter follow that adopted standard; projects without
one must establish their own explicit decisions. Keep the two-field settings
schema unchanged and report unresolved authority instead of silently selecting
another baseline.
