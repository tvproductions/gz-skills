# Architectural decision template and edition rules

Use the consuming project's selected policy and suitable conventions first.
Map equivalent fields explicitly; these defaults apply to a new collection.
This is a readable record, not a required parser/schema or additional workflow.

## Identity and state

- Start a new collection at `ADR-0001`. Stable identity is `ADR-[0-9]{4,}`.
  Allocate an unused identity; never recycle it or equate it with a release.
- Name editions `ADR-[0-9]{4,}-[0-9]{3,}-<slug>.md`, starting at edition 001.
  Widths four and three are minimums: edition 999 advances to 1000, decision
  9999 to 10000. Do not cap, renumber or rename the collection at overflow.
  The slug grammar is `[a-z0-9-]+`; use a readable kebab-case title.
- Authoritative records use `Current` or `Retired`. Keep an unapproved proposal
  with design material; leave state and approval fields blank and label it a
  proposal in prose. `Proposed` may describe its review status, not authoritative
  state. Follow an existing consumer's equivalent semantic mapping where suitable.
- Preserve prior editions and exact reviewed content in existing history or
  immutable references. No index, registry, separate receipt file or ledger is
  required. Existing project mechanisms can carry evidence.

## Proposed edition

Replace placeholders with actual content. Leave unknown approval values empty;
remove explanatory comments when adapting into the project's record format.

```yaml
id: ADR-0001
title: <decision title>
revision: 1
state:
decision_date:
revision_date: <actual edition date, YYYY-MM-DD>
approved_by:
approved_revision:
approval_ref:
```

# <Decision title> — proposal, edition 1

## Scope and context

State the affected boundary, need, constraints and relevant approved decisions.
Separate observed evidence, inference and unknowns. Reference governing
requirements/designs without treating their approval as ADR approval.

## Alternatives

Compare credible options, including retaining the present design where relevant.
Describe their tradeoffs and evidence limitations without constructing a straw man.

## Decision and rationale

State the proposed choice precisely and why it addresses the context. Identify
consequential uncertainty and the focused evidence or human ruling still needed.

## Consequences

Describe benefits, costs, risks, compatibility and operational implications.
Separate architectural approval from authorization to perform external operations.

## Confirmation (optional)

Describe how implementation alignment can be checked and when to revisit.

## Approval evidence

Before acceptance, retain exact proposed/reviewed bytes or an immutable content
reference. Preserve the actual explicit response, human identity, date and source
context with a durable interaction reference or honest transcript. Tie it to this
identity and edition and the reviewed content. A checksum alone proves no approval.
Explain the subsequent administrative transition: fill actual approval metadata,
set Current, and preserve the reviewed proposal. Do not claim these administrative
edits or later explanatory additions were in the original reviewed bytes.

## Amendment history

Record each actual edition/date, change type and approval relationship. Never
invent historical dates or responses. Link preserved prior content as appropriate.

## Editorial amendment

An editorial clarification preserves the approved choice. Increment `revision`,
update `revision_date` and advance the edition filename, including 999 -> 1000.
Keep the stable `id`, original `decision_date`, `approved_by`, `approved_revision`
and `approval_ref`. Preserve the prior edition/content and record the edit and
its nonmaterial nature in amendment history. Do not rewrite approval to pretend
the human reviewed the new editorial edition. No architectural reapproval is
required for a genuinely editorial change.

## Material replacement and retirement

A material change receives a new stable identity and separately approved edition.
Explain its relationship to the prior decision. Obtain explicit authority to
retire the old record; new-choice approval alone must not be inflated to retirement
or operational permission. Retain the old identity/history/approval, mark it
Retired through a recorded new edition, and record actual date, reason and
replacement identity where applicable. Do not overwrite it with the new choice.

## Backfill and independent evolution

Label a retrospective record honestly. Describe what is observed now, what is
inferred and what remains unknown; never reconstruct fictional approval or dates.
Obtain missing architectural approval now before dependent work. Product versions,
requirements, plans and evidence may change without changing an approved decision,
and editorial editions may change without a new product version. Reassess the
actual architectural impact rather than forcing synchronized numbers or records.
