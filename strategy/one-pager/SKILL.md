# One-Pager

Compresses extensive brand docs, strategies, positioning frameworks, or plans into a
decision-ready page. The one-pager is a second layer, never a replacement for the full
strategy. Every word earns its place, but unique strategic and creative information
survives compression.

Different audiences need different one-pagers. An executive one-pager emphasizes strategic
rationale and outcomes. A team one-pager emphasizes operational clarity. An external
one-pager emphasizes the brand story.

## System

One-pager is composed of three reference files:

### references/compression-methodology.md
How we compress — the methodology for reducing a 20-page positioning doc or strategy
deck into a single page without losing structural integrity or strategic coherence.

### references/information-hierarchy.md
How we prioritize information on the page — what leads, what supports, what gets cut.
The hierarchy governs the reading experience and ensures the most important content
lands first.

### references/formats.md
The one-pager format variants — executive (for leadership and board), team (for internal
alignment), and external (for partners, press, or sales). Each variant has a different
structure and emphasis.

### references/executive-gtm-strategy.md
How to turn deep product, brand, audience, messaging, and launch context into a concise
executive GTM decision document. Load this for beta or launch strategy, messaging
architecture, first successful use, creator seeding, launch gates, or multi-source GTM
synthesis.

## When to invoke

- When a stakeholder needs a concise brand or product overview
- When onboarding a new team member or partner on a brand
- When distilling a full positioning framework into an executive-facing artifact
- When preparing a strategic summary for a board, investor, or partner meeting
- When a brand doc or strategy is complete and needs a compressed reference version
- When leadership needs to review a strategy in 10 to 15 minutes

When invoked from Compound Marketing, read `../compound-marketing/references/handoff-contract.md`
and the supplied `handoff.json` before compressing. Preserve the decision-record version
and digest, governed IDs, protected language, unresolved questions, owner, and record
paths in the governed source or companion sidecar. Do not print the governance block on
the external one-pager.

## Reference routing

| Task type | Load |
|---|---|
| Compressing a longer document into one page | `references/compression-methodology.md` |
| Deciding what to prioritize on the page | `references/information-hierarchy.md` |
| Choosing the right format for the audience | `references/formats.md` |
| Building an executive GTM, beta, or launch decision document | `references/executive-gtm-strategy.md` |

## Dependencies

- `foundation/marketing-os`
- `positioning/{source brand}` (loaded dynamically)
- `brand-voice/{source brand}` (loaded dynamically)

## Quick checklist

- Does the page lead with the decision or argument?
- Can leadership understand it in 10 to 15 minutes?
- Does it preserve the source's distinctive idea, mechanism, audience, and evidence?
- For GTM work, are first successful use, locked decisions, experiments, launch proof,
  and open questions distinct?
- Are ownership, measurement, asks, and budget visible when relevant?
- Does the full strategy remain available as the source of truth?
- When routed from Compound Marketing, does the governed source retain the complete handoff sidecar?
