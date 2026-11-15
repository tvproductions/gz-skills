---
name: gzs-architectural-decisions
description: Use when consequential architecture choices arise during design or implementation, when reviewing alignment with approved decisions, or when creating, amending, replacing or recovering an ADR. Routine edits already covered by approved decisions and general architecture explanations do not require this workflow.
metadata:
  govzero-version: "0.1.0"
  govzero-portability: "portable"
  govzero-origin: "gz-skills"
---

# GovZero Architectural Decisions

Make consequential choices visible before dependent work. Preserve the consuming
project's authority and use this discipline inside its existing workflow.

## Discovery and fallback

Read project instructions, the selected architectural-decision policy, actual
collection, applicable decisions and approval evidence. Resolve source revision,
local adaptations and active workflow. An immutable source link or a
provenance-bound local copy can supply policy; use the selected available form.
Surface applicable local/source conflicts instead of silently selecting a winner.
Missing policy, workflow or reviewed approval content limits affected claims;
continue independent authorized work. Never install tooling to make records usable.

Use project tools where available and readable records as the floor. Map suitable
existing conventions to the semantics in the [template](references/adr-template.md);
preserve legacy records and document any actual migration crossover. Do not impose
this publisher's language, branch, tooling or release policy, require another
plugin, or create a second lifecycle, index, ledger or approval service.

## At design, execution and review

1. Identify consequential ownership, interface, dependency, persistence, recovery,
   trust, deployment or operational choices. Reuse and cite applicable approved
   decisions with their identity, edition and constraints. Routine covered work
   needs no new ADR. Handle human-initiated ADR requests through the same discipline.
2. For a new or conflicting choice, explain scope, credible alternatives,
   rationale, consequences and important uncertainty. Recover available evidence;
   distinguish facts from assumptions. Weak justification needs a focused
   supplement or explicit human ruling, not fabricated certainty.
3. Prepare an identified proposed edition using the template. Keep drafts with
   design material, without authoritative state or filled approval fields.
   Present the actual content for separate explicit architectural approval.
   Design, plan, tests, release assent, deadlines and vague “looks good” do not
   approve an ADR. Verify that the human response identifies this decision and
   edition and that the reviewed content matches; wrong-edition approval fails.
4. Pause only dependent work until approval is evidenced. Continue independent
   authorized tasks. When a choice emerges mid-implementation, stop at that
   boundary, surface its impact and obtain approval before continuing it.
5. Preserve actual approval and reviewed bytes before administrative capture.
   Record human identity, date, source context and durable response/content
   references, or an honest transcript with reviewed bytes/hash. A hash establishes
   content identity, never human approval. Explain administrative metadata changes;
   do not retroactively claim that later text was reviewed. Then resume authorized
   dependent work and verify its behavior against the approved constraints.
6. Review implementation alignment explicitly, even when tests are green.
   Report drift and correct it or obtain a separately approved replacement.
   ADR approval grants no additional migration, deployment or publication authority;
   continue already-authorized local work without asking for those unrelated acts.

## Evolve records honestly

Read the template's edition rules before amending or replacing a record.
Editorial changes advance edition, date and filename while preserving identity,
decision date, approval and prior history. Material replacement needs a new
identity and separate approval; retirement needs explicit authority and a reason.
Never overwrite historical approval, infer backdated decisions, or silently
rename a legacy collection. Keep observed, inferred and unknown backfill content
separate and seek missing approval now. Requirements, plans, evidence, product
versions and ADR editions evolve independently.

## Completion evidence

Report the applicable policy/source and decision identity/edition, actual approval
reference, authorized continuation and alignment result. State unresolved choices,
conflicts and unavailable evidence precisely. Configuration, installed files and
manual source loading do not prove fresh-session native discovery or qualification.
