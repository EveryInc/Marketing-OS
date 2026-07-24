# Launch Email Flows

**Skill version 1.2 · July 24, 2026**

Generates the launch email set for an Every product launch as four audience flows, each
with its own job. The product, voice, offer, segments, and timing come from the current
GTM plan.

## When to invoke

- "Write the launch emails for [product]"
- The burn-down's email tasks come due (canon: emails derive from the Messaging Doc and
  route through Kate's review gate before send)
- The GTM plan's email sequencing is locked and drafts are needed

## The four flows

1. **Paid subscribers** — insiders. They already pay; the job is pride of membership plus
   the new capability. Bundle framing, not a sales pitch.
2. **Free subscribers** — the conversion flow. The job is the offer: what changed, why it
   matters to them, and the single CTA. Sequence it relative to the paid send in the GTM
   plan.
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

## Voice and structure

1. **Benefit stacks are bullets, not prose.** Any email listing three or more
   membership benefits renders them as a bulleted list — including founder-voiced
   emails. Prose carries the one idea the email exists to say; the stack is always
   scannable.
2. **Identity framing over transaction framing.** Address the reader as the member they
   nearly are, not the cart they abandoned.
3. **Restate the headline value after an itemized list.** Close the list with the
   aggregate value the offer creates.
4. **Show real price anchoring directly.** When a cleared promotional price is live,
   show the list price beside it instead of explaining the change in prose.
5. **Objection emails end with Every's opinion.** Present the honest evidence, then take
   a position. Neutrality reads as absence.
6. **Constraints get a reason.** State a real limitation with its reason, away from the
   CTA, instead of hiding it.
7. **Reassure existing paying customers first.** An upsell to a paid segment opens by
   stating what does and does not change about the current membership.
8. **Rolling-benefit promises name the cost.** If future additions are included without
   another charge, say so. If that fact is not cleared, do not imply it.
9. **Use the full brand or product name on first mention.**
10. **Team proof points carry titles and concrete workflows.**
11. **Subjects lead with the asset or value.** Pull a cleared number forward only when
    it materially sharpens the offer.
12. **Cut insider flattery.** One honest line of standing is enough.

### Urgency calibration (supersedes the blanket "no fake urgency" line)

- Unchanged: no invented countdowns, no code-scarcity numbers.
- New: at sequence exit only, real-mechanism urgency is allowed — the early-bird
  price step and the fact that this is the final email ("Last note," "Final
  chance"). Any urgency claim whose mechanism is not real (e.g. a "spot" that
  does not actually expire) goes through claims-clearance before send.

### Lifecycle mapping

- Keep retention, upsell, acquisition, abandonment, and post-purchase emails as separate
  jobs. Do not make one send serve two lifecycle states.
- Keep the CTA consistent within each flow.
- The lifecycle owner defines triggers, suppression, cadence, and exit conditions from
  current data. This skill does not inherit timing from an earlier campaign.

## Changelog

- **v1.2 — July 24, 2026.** Removed project-specific copy, prices, sequences, and
  lifecycle assumptions. Retained only reusable voice, structure, urgency, and
  lifecycle rules.
- **v1.1 — July 7, 2026.** Added voice, structure, urgency, and lifecycle rules from
  approved launch-email edits.
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
