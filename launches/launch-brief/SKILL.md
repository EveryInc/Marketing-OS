# Launch Brief

Generates the Week 1 foundation brief for an L/XL launch — the document every gate,
calendar, and channel asset hangs on. The brief is the launch's constitution: if it's
wrong, everything downstream inherits the error, which is why it carries the heaviest
approval roster in the process.

## When to invoke

- Week 1 of any L/XL launch ("write the launch brief for [product]")
- A launch is being stood up and no brief exists
- Re-baselining after a meaningful product change (canon edge rule 1 — a pure calendar
  slip does not reopen the brief)

## The brief's anatomy (canon Week 1, in order)

1. **Launch date + feature freeze** — confirmed by the product owner or the entire brief
   is marked DRAFT on its face.
2. **Subscriber lens** — can all our subscribers use it? (Monologue and Cora pass; Para
   didn't.) A "no" here is a strategy conversation, not a footnote.
3. **Customer profile** — one core psychographic or professional target, sub-targets
   allowed, laddering to one–two archetypes (Builder, Operator, Seeker, Executive).
   Feeling-first archetype analysis per `marketing-science/archetyping`, not projection.
4. **Why / success / how** — why we're doing this, what defines success, how we drive it.
5. **Dream tweet and dream headline** — written out verbatim. These are the retro's
   scoring rubric; vague versions make the retro unscoreable.
6. **Positioning and story** — what we made, why we made it, who it's for. For net-new
   products, the why-now / why-us / why-this narrative discipline from
   `launches/new-product-launch` applies.
7. **Competitive picture** — the `competitive-audit` summary, source-linked.
8. **Pricing owner named** — Brandon + the product GM (canon ruling); target lock at the
   wireframe gate, hard lock Monday of the Launch Week window.
9. **Roster** — collected for this launch, never inherited; canon rosters offered as
   examples only.
10. **Approval record** — Douglas, Brandon + GM (co-rule), stakeholders, Dan, Austin;
    with dates. An unapproved brief blocks Week 2 (canon Rule 3).

## Rules

- Facts the model cannot know (dates, freezes, rosters, product truths) are collected
  from the humans who own them and attributed; gaps are marked OPEN, never filled with
  plausible text.
- The brief states its own confirmation status at the top.
- Length discipline: the brief is read at a gate meeting — pages, not a deck.

## Dependencies

- `foundation/marketing-os`
- `launches/canonical-process.md` (Week 1 checklist, rosters, epistemic rules)
- `marketing-science/archetyping` · `marketing-science/research`
- `positioning/every-master` · `positioning/{product}` (dynamically)
- `launches/competitive-audit` output as input
- `launches/new-product-launch` (narrative discipline, for net-new products)

## Quick checklist

- [ ] Date + freeze confirmation status stated on the face of the doc
- [ ] Subscriber lens answered, escalated if "no"
- [ ] Customer profile laddered to archetypes, feeling-first
- [ ] Dream tweet + dream headline verbatim (the retro rubric)
- [ ] Competitive claims source-linked
- [ ] Pricing owner named per the Brandon + GM ruling
- [ ] Roster collected fresh; OPEN items marked, not filled
- [ ] Approval record present: Douglas, Brandon + GM, stakeholders, Dan, Austin
