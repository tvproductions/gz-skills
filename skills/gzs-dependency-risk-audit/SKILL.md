---
name: gzs-dependency-risk-audit
description: Assess a project's direct and transitive dependency risks using manifests, lockfiles, authoritative advisories, compatibility constraints, maintenance signals, licenses, provenance, and actual repository usage. Use for dependency-risk, supply-chain, vulnerability, abandonment, or license audits; not for automatically upgrading packages or performing a general security review.
compatibility: Uses local dependency metadata and, when available, current authoritative registry, advisory, license, and maintainer sources; offline results must remain explicitly limited.
metadata:
  govzero-version: "0.1.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Dependency-Risk Audit

Turn dependency evidence into a prioritized retention, mitigation, replacement,
or upgrade decision. This is a read-first audit: do not change versions, remove
packages, create exceptions, publish findings, or open issues unless separately
authorized.

## Precedence and scope

1. Read repository policy and any active security, maintenance, or release
   workflow. Keep that workflow in control of thresholds, exceptions,
   remediation deadlines, state, gates, and attestations.
2. Resolve the requested project or component scope. Inventory every owning
   manifest, lockfile, workspace definition, runtime and package-manager pin,
   package source, vendored dependency, container base, CI action, generated
   dependency surface, and available SBOM within it.
3. Record the audit time and evidence access. Current risk claims require live
   sources; an offline audit may establish local exposure and identify evidence
   to fetch, but cannot claim that dependencies are currently safe.

## Evidence workflow

1. Build the resolved dependency graph with each component's selected version,
   source, integrity or signature data when present, direct or transitive
   status, owning manifest, and dependency path. Preserve ecosystem-specific
   semantics instead of flattening incompatible lock or advisory models.
2. Determine actual exposure. Locate where the project imports, executes,
   bundles, distributes, loads at build time, or grants privilege to each
   relevant dependency. Separate reachable production behavior from test-only,
   development-only, optional, or unused paths.
3. Query the package manager and official registry first, then maintainer
   security and support notices, authoritative ecosystem or vulnerability
   databases, and license texts. Use secondary aggregators only to discover
   leads or corroborate evidence. Record source URLs or identifiers, retrieval
   times, affected ranges, fixed versions, and source limitations.
4. Evaluate only risk classes supported by available evidence:

   - known vulnerabilities and project-context exploitability;
   - end-of-support, abandonment, or maintenance-capacity concerns;
   - license incompatibility with the project's distribution and use;
   - provenance, integrity, dependency-confusion, typosquatting, or unexpected
     package-source concerns;
   - install-time behavior, runtime privilege, and sensitive data or network
     access;
   - maintainer concentration, transitive duplication, and upgrades blocked by
     runtime, platform, or peer constraints.

5. Reconcile evidence rather than counting alerts. Preserve advisory identity
   and status; do not report a withdrawn advisory as active. When sources
   conflict, state the disagreement, prefer the source closest to the affected
   package and ecosystem, and lower confidence until the affected range and
   status can be resolved.
6. Protect private dependency information. Do not send private package names,
   versions, source URLs, or graphs to public services without authorization.
   Use approved private registries or local evidence and mark external status
   unavailable where necessary.
7. Treat an incomplete transitive graph, unresolved package identity, missing
   integrity data, unreachable registry, or unavailable advisory source as a
   coverage limitation. Never translate missing evidence into "no risk."

## Prioritization and output

Rank findings by credible project consequence, reachability, privilege,
affected deployment, availability of a fix, and confidence—not by advisory
score or package age alone. For each retained finding report the dependency and
path, affected surface, evidence and date, consequence, feasible response,
confidence, and urgency. Distinguish actions such as upgrade, constrain,
replace, isolate, remove, accept temporarily, or investigate.

End with the inventoried ecosystems and surfaces, coverage gaps, conflicts or
withdrawals, finding counts by severity, and the smallest useful next decision.
Recommend `gzs-update-dependencies` only when an authorized upgrade is the
chosen response; do not claim the containing security or release workflow is
complete.
