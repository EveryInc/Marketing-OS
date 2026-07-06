# Claims Clearance

The pre-ship verification gate for every launch surface. Inventories every factual claim
on every asset — stats, quotes, logos, prices, availability statements, competitor
comparisons — and clears, flags, or blocks each one. Built from the July 2026 Cora 2.0
pass, where one careful read of the web copy found an unsourced hero stat, unpermissioned
logos, and a price that contradicted the strategy doc in the same file.

## When to invoke

- Week 8 of every L/XL launch, before anything ships (canon Week 8 checklist item)
- Any copy round review ("check the claims in this," "is this stat sourced")
- `codex-gut-check` hands over its unverified-claims inventory
- A price, stat, quote, or logo appears in any draft headed for a public surface

## The clearance categories

Every claim lands in exactly one:

- **CLEARED** — source cited inline (live link or named document + date), or permission
  logged (who granted, when, in writing where).
- **CONFLICTED** — two launch surfaces disagree (the Cora pattern: strategy doc says
  $20/mo, web copy says $15/mo). Conflicts block both surfaces until the owner rules —
  for pricing, that's Brandon + the product GM.
- **UNVERIFIED** — no source. Unverified is not a status that ships; the claim is cut or
  cleared, never softened into shipping ("many users say…" is the tell for laundering an
  unverified stat).
- **PENDING PERMISSION** — logos, testimonial quotes, named-person or named-company
  references awaiting a written yes. No logo ships without one.

## The sweep

1. Inventory every surface in the burn-down: site, emails, social assets, video
   end-cards, pricing page, press materials, changelog.
2. Extract every claim — numbers, superlatives, comparisons, names, logos, prices,
   availability ("works with X," "the only Y that Z").
3. Check each the same way. No sampling. If the sweep runs out of room, name what wasn't
   covered rather than implying it passed.
4. Cross-surface consistency pass: the same fact must read identically everywhere
   (price, plan names, trial length, stat wording).
5. Deliver the clearance table (claim · surface · category · source/owner · action) and
   a plain block list of what cannot ship as-is.

## Rules

- The bar for "verified" is fixed before the sweep and doesn't move; narrowing a
  definition to keep a claim alive is the tell for rationalizing.
- Comparative claims about competitors require a live check dated within the launch
  window (`competitive-audit` refresh), not memory.
- Clearance is recorded in the burn-down task's note, so the gate is auditable at the
  final design approval.

## Dependencies

- `foundation/marketing-os`
- `launches/canonical-process.md` (epistemic rules, Week 8 placement, pricing ruling)
- `launches/competitive-audit` (live re-verification of comparative claims)

## Quick checklist

- [ ] Every surface inventoried; every claim extracted
- [ ] Each claim in exactly one category; same check for every item
- [ ] Conflicts routed to their owner (pricing → Brandon + GM)
- [ ] Unverified claims cut or cleared — never reworded into shipping
- [ ] Permissions logged: who, when, where in writing
- [ ] Cross-surface consistency pass done
- [ ] Clearance table + block list delivered; uncovered items named
