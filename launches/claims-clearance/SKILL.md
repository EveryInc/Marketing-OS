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

## Worked clearance log — All Access / Builder Pack (2026-07-07)

The live claim inventory for the All Access / Builder Pack launch, seeded from Douglas's
R002 edit diff and verified against the Notion sources (Goodie Bag Partner Tracker, the
All Access / Builder Pack CS Readiness Source of Truth, and the Builder Pack redemption
help page). None of these is cleared unless marked otherwise; OPEN and CONFLICT items are
resolved by their owners (Growth/Product, Yash, Brandon, Douglas) before send, and nothing
is marked CLEARED beyond what this log states.

| Claim | Where it appears | Status | Notes |
|---|---|---|---|
| "90% discount" | Abandonment E3, E4; page-view E1 | OPEN | Math: $450 vs $7,000+ ≈ 93.6% off, so "90%+" is conservative — but the aggregate $7,000+ itself must stay cleared for this to hold |
| "Save 15% today" | Abandonment E4 early-bird bracket | OPEN | $450 vs $525 = 14.3%; "15%" rounds up. Rule whether rounding up is acceptable or use "over 14%"/"$75" |
| Builder Pack "replenishes with a year's worth of new credits" on renewal | Annual Reminder | OPEN | New product claim; confirm with Yash/partners that offers renew annually |
| "$550 All Access fee" | Annual Reminder | **CONFLICT** | Contradicts ruled $525 list (Douglas, 7/7). Correct to $525 or re-rule |
| Pro-rated upgrade ("pro-rated based on whatever you've paid so far this year") | Member email; Dan version | OPEN | Reverses 7/6 ruling that upgrade math was out. If intentional, Yash confirms the billing mechanic |
| "Several [partners] already in the pipeline" | Abandonment E2 | OPEN | Confirm at least two signed-but-unannounced partners exist at send time |
| "You're about to lose your spot" | Abandonment E4 subject | OPEN | No expiring-spot mechanism verified; either a mechanism exists or subject changes |
| **"$7,000+" / "10 tools" / ChatGPT Business as headliner** | Every email in the set | **OPEN — LAUNCH-CRITICAL** | Tracker (7/7): OpenAI Offer Ready = NO, language not approved, redemption unconfirmed. Verified math from tracker values: pack = $6,004 without OpenAI, $7,124 with. If OpenAI isn't confirmed by the July 13 content freeze, every value claim in the set needs a re-cut |
| Welcome Email: "There's no rush on the rest — offers stay available to you while your membership is active" | Welcome Email | **CONFLICT** | Contradicts CS policy anchor: codes are first-come-first-served and can run out ("codes running out does not create refund entitlement"). Soften to "claim the rest whenever you're ready — offers are live now" or add "while codes last" |
| AgentMail redemption code | Help article + CS SoT say EVERY6MONTHS; Partner Tracker says EVERY6 | **CONFLICT** | Confirm which code is provisioned before beta (July 8) |
| Framer code EVERYXFRAMER; Cursor unique codes | Help article (live); emails reference offers | OPEN | Tracker (7/7): both marked "Tested and working: Not working (screenshot attached)." Fix flows before beta or show a holding state |
| Anthropic offer value | ~$100 (help article) vs $200 (master doc) vs $300 (old card) | **RESOLVED → $100** | Tracker (canonical per CS SoT): Value = $100, "1 month of Claude Max 5x." Reconcile master doc and card to $100 |
| Early-bird window duration | Multiple {{brackets}} | OPEN | Yash: "will circle back" (doc comment, 7/7) |
| Launch series video links | Welcome email | OPEN | Douglas comment to Yash: "link to videos" |

Also record as CLEARED (Douglas ruling by edit, 7/7, plus CS SoT policy anchors): Builder Pack partner itemization (9 launch partners per tracker; OpenAI pending), $525 list / $450 early bird, annual-only + fraud-mitigation rationale, "no refunds" language retired from customer-facing **email** (help center Article 4 still states the public no-refund position — that split is intentional), FCFS is true and may be stated in help content without quantities (internal ~3,000/partner figure never publishes).

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
