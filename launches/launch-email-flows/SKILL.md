# Launch Email Flows

**Skill version 1.1 · July 7, 2026**

Generates the launch email set for an Every product launch as four audience flows, each
with its own job. The pattern consolidated across Spiral 4.0 (active / churned /
subscriber) and Cora 2.0 (paid subs / free subs): the flows are stable; the product, the
voice, and the offer are the variables.

## When to invoke

- "Write the launch emails for [product]"
- The burn-down's email tasks come due (canon: emails derive from the Messaging Doc and
  route through Kate's review gate before send)
- The GTM plan's email sequencing is locked and drafts are needed

## The four flows

1. **Paid subscribers** — insiders. They already pay; the job is pride of membership plus
   the new capability. Bundle framing, not a sales pitch.
2. **Free subscribers** — the conversion flow. The job is the offer: what changed, why it
   matters to them, the single CTA. Sequenced relative to the paid send per the GTM plan
   (All Access precedent: all-subs followed ~two days after).
3. **Churned product users** — the win-back. Leads with what specifically changed since
   they left; never pretends they didn't leave. Only runs when the product has a churned
   cohort worth addressing (a 2.0 does; a net-new product doesn't).
4. **Prospects / never-tried** — runs only if the GTM plan includes an acquisition list;
   otherwise skipped, and the skip is stated rather than silently absorbed.

## Rules

- **Every email derives from the Messaging Doc** — hed, proof points, enemy framing. If
  the Messaging Doc doesn't exist yet, that's the blocker to report, not a gap to
  improvise around.
- **Kate's review gate is mandatory** for every launch send; the burn-down's "Email
  reviews with Kate" task is the gate's record.
- **`ai-check` and `every-style` run on every draft.** Non-negotiable.
- **Claims discipline:** any stat, price, or availability claim in an email must already
  be CLEARED by `claims-clearance` — emails ship last and inherit the clearance table,
  they don't re-litigate it.
- **One CTA per email.** Subject lines drafted in threes for selection, never sent as a
  triple.
- Segment boundaries are checked with whoever owns the list (a churned-user email to an
  active user is a trust injury); send timing belongs to the GTM plan, not this skill.
- **Reminder / last-call send:** the canon's Week-8 reminder-sends item (a Day 2–3
  last-call/ICYMI email to non-openers, plus a Discord nudge) is part of the launch email
  set — an owned, GTM-sequenced task through Kate's gate, not an afterthought. See
  `launches/canonical-process.md` (Week 8).

## Learnings: All Access / Builder Pack (Douglas edit diff, 2026-07-07)

Rules below were expressed by Douglas's line edits to the All Access email flows and
generalize beyond that launch. Facts and claims arising from the same diff live in
claims-clearance and canon, not here.

### Voice and structure

1. **Benefit stacks are bullets, not prose.** Any email listing three or more
   membership benefits renders them as a bulleted list — including founder-voiced
   emails. Prose carries the one idea the email exists to say; the stack is always
   scannable.
2. **One locked announcement opening across segments.** Launch announcements share a
   single opening formula: reader motive → our practice → the handoff. All Access
   canonical form: "You read Every because you want to stay on top of AI. We stay on
   top of AI by building with it, daily. Today we're handing you the full stack."
   Adjust pronouns for founder voice; do not restructure per segment.
3. **Builder sign-offs.** Closings carry the brand motif: "Let's build." / "Keep
   building." / "Let's keep building." One per email, placed after the CTA or the
   reply invitation.
4. **Identity framing over transaction framing.** Address the reader as the member
   they nearly are, not the cart they abandoned: "You're almost an Every All Access
   member" — never "you stopped short at checkout."
5. **Restate the headline value after any itemized list.** Close every line-by-line
   of offers with the aggregate: "That's over $7,000 in AI credits included."
6. **Strikethrough price anchoring.** When early-bird pricing is live, show list
   price struck through beside the live price (~~$525~~ $450) instead of prose
   ("before it rises to...").
7. **Exclusivity phrasing.** The flagship perk is available "only with" the tier.
   Use it in modals and subject lines.
8. **Objection emails end with our opinion.** Present the honest math, then take the
   position: "Run your own math. But we think so." Neutrality reads as absence.
9. **Constraints get a reason, in the PS.** Annual-only is stated together with its
   reason ("We do this to mitigate fraud") as a postscript, not buried near the CTA.
   Do not use "no refunds" language in customer-facing emails.
10. **Reassure existing paying customers first.** Any upsell to a current paid
    segment opens by stating nothing changes about what they already have: "Nothing
    is changing about your current Every membership."
11. **Rolling-additions promises always carry "at no additional cost."** Every
    future-partner claim is paired with the cost reassurance.
12. **Full brand name on first mention.** "Every All Access," then "All Access."
13. **Team proof points carry titles.** Format: Name (Role) + concrete workflow.
    "Kieran (GM Cora) builds and ships Cora entirely with Claude Code."
14. **Subjects lead with the asset and the number, possessive preferred.** "Your
    Builder Pack, itemized" over "The Builder Pack, itemized"; "$7,000+" pulled
    forward. (Taste ruling from edits, not A/B tested.)
15. **Cut insider flattery.** No itemizing the reader's own usage back at them
    ("the archive, the software, the camps"). One clean line of standing — "among
    our most active subscribers" — is the ceiling.

### Urgency calibration (supersedes the blanket "no fake urgency" line)

- Unchanged: no invented countdowns, no code-scarcity numbers.
- New: at sequence exit only, real-mechanism urgency is allowed — the early-bird
  price step and the fact that this is the final email ("Last note," "Final
  chance"). Any urgency claim whose mechanism is not real (e.g. a "spot" that
  does not actually expire) goes through claims-clearance before send.

### Lifecycle mapping

- The renewal-window email targets **current All Access members** (retention;
  Builder Pack replenishment framing) — it is not the Member upsell email. An
  upsell-at-renewal email is a separate asset if ruled in. Trigger definitions
  belong to the lifecycle owner (Yash), not this skill.
- CTA uniformity: acquisition → "Get All Access →"; Member upsell → "Upgrade to
  All Access →"; post-purchase → "Open the Builder Pack →". One CTA per email,
  unchanged.
- Abandonment sequence shape confirmed: 4 emails (10 min / 1 day / 2 days /
  3 days, then exit). Page-view sequence: 2 emails (1 day / 3 days, then exit).

## Changelog

- **v1.1 — July 7, 2026 (Douglas × Claude).** Added the "Learnings: All Access /
  Builder Pack" section — voice/structure, urgency calibration, and lifecycle-mapping
  rules from Douglas's R002 edit diff, generalized across launches with All Access as
  the worked example. The urgency-calibration block supersedes the earlier blanket
  "no fake urgency" guidance (that rule lived in the email-drafts source doc, not in
  this skill, so there was no in-repo line to rewrite).
- **v1.0 — July 2026.** Original four-flow launch email skill (Launch Architecture
  Skillset bundle).

## Dependencies

- `foundation/marketing-os`
- `launches/canonical-process.md` (gates, sequencing authority)
- `brand-voice/{product}` + `brand-voice/every-master` (dynamically)
- `organization/ai-check` · `organization/every-style` (mandatory passes)
- `launches/claims-clearance` (clearance table in)
- Messaging Doc for the launch (input, required)

## Quick checklist

- [ ] Messaging Doc in hand — blocked and reported if not
- [ ] Four flows assessed; skipped flows stated with the reason
- [ ] Every draft: derives from messaging, one CTA, subjects in threes
- [ ] ai-check + every-style run on every draft
- [ ] Claims already cleared; none introduced fresh
- [ ] Kate gate scheduled before any send date
- [ ] Sequencing deferred to the GTM plan
- [ ] Day 2–3 reminder / last-call send planned per canon Week 8 (owned, not an afterthought)
