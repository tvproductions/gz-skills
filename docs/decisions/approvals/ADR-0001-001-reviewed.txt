---
id: ADR-0001
title: Standalone architectural decision procedure
revision: 1
state:
decision_date:
revision_date:
approved_by:
approved_revision:
approval_ref:
---

# ADR-0001 edition 1: standalone architectural decision procedure

DRAFT PROPOSAL. This is not an authoritative Current/Retired decision. Approval fields are intentionally unfilled. No architectural approval is recorded.

## Scope and context

The starter's approved cross-component contract requires gz-skills to supply a portable ADR procedure/template. Its exact-combination decision does not select
this publisher's internal ownership/interface. gz-skills owns standalone horizontal disciplines; active consumer workflows own ordering, gates, state and
release/handoff authority. This choice concerns where reusable decision handling lives, what it depends on and how it composes with existing owners.

The user directed completion of the approved release prerequisites and delegated
how to do that. The proposed approach below is the agent's recommendation;
that direction does not approve this identified ADR edition or the owning design.
See the [owning design](../2026-11-15-architectural-decisions-design.md) for exact
source identities, deliverables, finite scope and behavioral acceptance.

## Credible alternatives

1. **Focused supporting skill with template and existing router integration.**
   Provides one readable procedure, independent use and a narrow composition seam;
   adds a public skill contract requiring independent review/versioning.
2. **Router-owned procedure/template.** Avoids a new catalog member, but ties
   decision authoring and review to routing and expands its responsibilities.
3. **CLI/schema or approval-state service.** Could support deterministic checks,
   but requires runtime/state authority, maintenance and migration without an
   evidenced need for this increment. It risks duplicating consumer lifecycle.

## Proposed decision and rationale

Publish a language/tool-neutral `gzs-architectural-decisions` supporting primitive
with a self-contained template in its canonical skill tree. Route through the
existing router and project instructions at design, execution and review.
Discover the consumer's governing policy, decisions, approval evidence and active
workflow. Map suitable existing conventions; do not replace them wholesale.

Keep decision content/approval provenance with the decision or its durable
references. Preserve reviewed editions and independent record evolution. Reuse
applicable approvals; obtain separate explicit approval for new/material choices
before dependent work. Continue independent authorized work and return control
to its owner. Human approval is evidenced by the actual interaction, never created by metadata, indexing, checks or a lifecycle transition.

Introduce no CLI dependency, approval service, ledger, new lifecycle or starter
runtime requirement. A consumer can use the primitive without SP, Backplane,
starter tooling or this repository's Python development environment. Existing
project policy retains authority and its actual mutation permissions.

## Consequences and confirmation

The contribution adds one independently versioned skill and extends routing;
canonical resources can use existing package/install contracts. Consumer binding
and real agent qualification remain necessary: source/configuration presence is
insufficient. Editorial and material changes require different history handling;
missing approval history remains an explicit gap rather than invented state.

Confirm with the complete B01-B16 shared matrix, gz-skills binding stop/continue
controls and genuine approved/reused internal use followed by alignment review.
Run structural/package/native channel gates separately. Other publishers own
their bindings/internal-use evidence; do not infer combined-stack qualification.

## Approval evidence and history

Pending: separate explicit human approval naming ADR-0001 edition 1 and the exact
reviewed proposal content. Preserve these reviewed bytes/hash before adding
administrative approval fields; record actual source context, date and identity.
Approval of the design, plan or release does not fill this gap. Do not implement
dependent work or move this proposal into authoritative Current state meanwhile.
The initial proposal is authored for review on November 15, 2026; this is no
historical decision or approval date. No amendment or retirement is recorded.
