# Marketing / GTM

Turn messy launch context into a strategic master plan and, when needed, a separate social brief. Lead with the argument and intended behavior. Add execution only after the strategy is clear.

## When to invoke

- When building or revising a GTM strategy, launch plan, launch backbone, or campaign sequence
- When producing a dated drumbeat, production plan, or concise social brief
- When applying a scoped revision to an existing GTM artifact

## Load the system

Read:

1. `../../foundation/marketing-os/SKILL.md`
2. `../../foundation/marketing-os/references/method.md`
3. `../../foundation/marketing-os/references/collaboration.md`
4. `../../positioning/every-master/SKILL.md`
5. `../../marketing-science/archetyping/references/every-audiences.md`
6. `../../craft/editing/SKILL.md`
7. `../../craft/editing/references/compound-from-edits.md`

For an existing collaborative document, also read `../../foundation/marketing-os/references/native-document-editing.md`. Apply `every-style` and `ai-check` to final prose.

## Establish authority

Identify the sources that own:

- Product or event facts.
- Strategic decisions.
- Canonical copy.
- Structural precedent.
- Dates, people, pricing, and publication plans.
- Approval.

Search the supplied Notion, Slack, Drive, meeting, and editorial sources before asking for information that can be found. Cite current sources. Label conflicts and unknowns.

When this work comes from `strategy/compound-marketing`, inherit the approved decision
record before drafting. Record its version, locked decision IDs, protected-language IDs,
and open questions in the GTM artifact. Do not reinterpret those decisions from the
underlying source pile.

## Interview before a long draft

Confirm these decisions when the materials do not settle them:

- What is launching?
- What is the primary action?
- What should each audience think, feel, or do?
- What story or language is protected?
- What is the launch window?
- Who can lock facts and strategy?

Ask one to three high-value questions at a time. Continue when the answers already exist.

## Lock the strategy

Write these elements before building a calendar:

1. **Goal:** State the future condition and audience behavior.
2. **Story:** Name the tension, the company's position, and why the launch follows.
3. **Campaign concept:** Define the mechanism that creates attention and participation.
4. **Launch backbone:** Explain how the story moves through company voices, credible participants, the public, and the offer.

Use the user's chosen language exactly. Keep protected sections unchanged during scoped edits.

Before polishing the prose, separate the strategic jobs:

- **Audience and tension:** Who needs this, and what is stopping them?
- **Category and outcome:** What is the product, and what changes because it exists?
- **Mechanism:** How does the product create that outcome?
- **Reason to believe:** Why can Every credibly deliver it?
- **Proof:** What specific request, action, and result show it happening?

Make each sentence and section do one job. Do not collapse the product promise,
positioning, hero UVP, supporting UVPs, mechanism, and reason to believe into one
paragraph. Name the customer and the first champion separately when they differ. Lock one
hero UVP; use the others as supporting stories rather than competing headlines.

Treat the one-line strategy and positioning statement as decision tools, not website copy.
Do not move into pricing, metrics, calendars, or channel tactics while the product story is
still being settled unless the user makes one of those the current decision.

## Write proof at production specificity

Every product example must name:

1. The request.
2. The action the product took.
3. The result.

Explain causal links an unfamiliar reader could not infer. Retrieve the missing detail
from Slack, Notion, Drive, or the governing source before writing. Never replace a specific
field, error, file, fix, artifact, or outcome with mystery language.

Do not use “real” as a credibility word. Replace it with the exact claim: shipped,
published, corrected, approved, customer-facing, live, verified, or another concrete fact.
If the evidence is incomplete, mark the gap instead of inventing intrigue.

## Build the master GTM plan

Use the relevant parts of this order:

1. Decision-record version and inherited decision IDs, when supplied.
2. Launch facts and primary action.
3. Goal and audience behavior.
4. Story.
5. Campaign concept.
6. Launch backbone.
7. Launch production.
8. Launch sequence.
9. Dated drumbeat.
10. Social brief link.
11. Copy and design surfaces.
12. Open questions and sources.

Right-size the document. Keep measurement to one compact success definition unless the user requests a measurement plan. Do not invent targets.

For a dated drumbeat:

- Use calendar days, including weekends.
- Distinguish confirmed dates from proposed workback dates. Label derived dates as proposed.
- Run strategic lanes simultaneously when the campaign requires it.
- Give each day a new argument, participant, proof point, program detail, or reason to act.
- Match editorial moments only when the actual article, speaker, or contributor argument supports the connection.
- Use `N/A` when no credible connection exists.
- Name owners and dependencies only when they help the team ship.
- Keep undecided pricing, talent, channel, and publishing choices under open questions.

Read `references/document-architecture.md` for the detailed format.

## Build the social brief separately

Default to three jobs:

1. State the story social must tell.
2. Name the actions and behavior social should elicit.
3. List concrete ideas to discuss.

Keep it short. Do not repeat the GTM plan or turn the brief into a channel manual unless the user asks for one. Include real examples when they sharpen an idea. For events, make desire, participation, and application behavior explicit.

## Verify before delivery

- Check every date, name, title, quote, speaker status, contributor statement, editorial item, price, and link against an authoritative source.
- Distinguish a locked decision from a missing production value. For example, pricing can be approved while the exact display price is still absent from the source packet.
- Quote the actual statement when claiming a thematic match.
- Mark approval dependencies explicitly.
- Preserve unresolved questions.
- Compare the final artifact with every inherited locked decision and protected phrase.
  Restore drift or record the human-approved replacement in the decision ledger.
- Remove generic language, repeated strategy, and unsupported specificity.
- Avoid “room,” “who belongs in the room,” and related event-marketing shorthand.

Use `references/edit-deltas.md` for the durable lessons behind these rules.

## Revise with a scoped diff

When the user identifies a section boundary:

1. Fetch the latest document.
2. Record the protected prefix and suffix.
3. Replace only the authorized section.
4. Re-fetch the document.
5. Compare protected content exactly.

Treat the user's edited version as canonical. Learn from the delta before drafting again.
When the user rejects an edit, restore their wording immediately and carry that decision
through the authorized scope. Preserve parentheticals, fragments, provocations, and rough
one-two-punch rhythms when they carry the idea or voice; tighten the connective prose
around them.

Compress only after the strategy and canonical language are stable. Cut repetition,
throat-clearing, and process detail. Do not cut a unique idea, mechanism, proof point,
owner, creative detail, or unresolved decision.

## Evaluate

Use `evals/cases.json` and `evals/rubric.md`. Run `scripts/check_output.py` for deterministic checks. The skill passes only when it clears the score threshold with zero hard failures.

## Dependencies

- `foundation/marketing-os`
- `positioning/every-master`
- `marketing-science/archetyping`
- `marketing-science/measurement`
- `strategy/program-brief`
- `craft/editing`

## Quick checklist

- [ ] Authority and source roles are explicit
- [ ] Ambiguous strategic questions were resolved before the long draft
- [ ] Goal, story, concept, and launch backbone precede the calendar
- [ ] The artifact names its inherited decision-record version and preserves its locked IDs
- [ ] Dates, people, claims, prices, and links are verified or clearly marked open
- [ ] Positioning separates audience, category, outcome, mechanism, and reason to believe
- [ ] Every proof point names the request, action, and result
- [ ] User-edited language and voice-bearing details remain canonical
- [ ] Measurement names a primary decision metric and decision date
- [ ] Scoped revisions preserved protected content exactly
- [ ] The relevant evaluation and deterministic checks passed
