# Knowledge Boundaries

Marketing OS is a reusable operating system, not a project archive. Work on a launch,
campaign, channel, event, or product can improve the system, but the project itself does
not become the system.

## The three layers

### 1. Durable operating doctrine

Lives in `foundation/`, reusable `strategy/`, `craft/`, `launches/`, and
`marketing-science/` skills.

Keep only rules that can guide a future project without importing the source project's
offer, dates, people, claims, creative premise, or execution plan. Write the rule in
project-neutral language and state the decision it changes.

### 2. Durable brand and product canon

Lives in `brand-voice/` and `positioning/`.

Keep approved positioning, voice, architecture, and product truths that remain useful
across multiple projects. Do not store launch calendars, embargoes, temporary claims,
campaign plans, active rosters, budgets, or other time-bound instructions here. Verify
current product facts against their ruled source before use.

### 3. Optional cases

Live in `docs/cases/`.

Cases may preserve the evidence behind a learning, including project names and dated
details. They are historical material, not dependencies. A skill may point to the case
index for optional study, but it must never load a case by default or require a case to
perform the workflow.

## Promotion rule

A project learning changes durable doctrine only when one of these is true:

1. Douglas explicitly rules it as an operating standard.
2. The same pattern succeeds across more than one relevant project.
3. The result supplies unusually strong evidence and the new rule states its limits.

Otherwise, record the result as dated project evidence. Do not turn one outcome, edit,
or preference into a universal instruction.

## Extraction test

Before adding project learning to a reusable skill, ask:

- Would this instruction still make sense if every proper noun, date, price, and person
  disappeared?
- Does it govern a future decision, or merely describe what happened?
- What evidence supports it, and what would make it stop applying?
- Is it already covered by a broader rule?
- Could loading it distort an unrelated project?

If the instruction fails any test, keep it in the project source or an optional case.

## Repository hygiene

- Reusable skills do not route to dated project briefs, launch evidence banks, active
  agendas, or worked GTM plans.
- Product modules contain durable canon only.
- The root README describes capabilities and system changes, not active campaigns.
- Changelogs name the reusable capability added. Git history preserves the source
  project when provenance matters.
- Cases have no inbound dependency from a `SKILL.md`.
- Project details that teach no reusable lesson are deleted. Git history is the archive.
