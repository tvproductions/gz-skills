---
id: ADR-0001
title: Standalone architectural decision procedure
revision: 1
state: Current
decision_date: 2026-11-15
revision_date: 2026-11-15
approved_by: "project maintainer in this conversation"
approved_revision: 1
approval_ref: "#approval-evidence"
---

# ADR-0001 edition 1: standalone architectural decision procedure

Current decision. Separate explicit architectural approval is preserved below;
implementation and qualification are separate.

## Scope and context

The starter's approved cross-component contract requires gz-skills to supply a portable ADR procedure/template. Its exact-combination decision does not select
this publisher's internal ownership/interface. gz-skills owns standalone horizontal disciplines; active consumer workflows own ordering, gates, state and
release/handoff authority. This choice concerns where reusable decision handling lives, what it depends on and how it composes with existing owners.

The user directed completion of the approved release prerequisites and delegated
how to do that. The proposed approach below is the agent's recommendation;
that direction does not approve this identified ADR edition or the owning design.
See the [owning design](../superpowers/specs/2026-11-15-architectural-decisions-design.md) for exact
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

## Decision and rationale

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

## Approval evidence

See the [actual approval capture](approvals/ADR-0001-001-approval.md) and exact
[preserved reviewed proposal](approvals/ADR-0001-001-reviewed.txt), SHA-256
`807749ec03853e673b4f2f431cf3c5b277615fedf9dd552016d98b655e72d7ff`. The separate explicit human response approves edition 1;
metadata and content hashes do not create approval.

## Edition history

Edition 1, November 15, 2026: original proposal separately approved by the
project maintainer in this conversation. Administrative capture creates this
Current record while preserving the reviewed bytes and actual interaction.
No material architectural replacement or retrospective approval is asserted.
