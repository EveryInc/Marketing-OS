# Launch Email Flows

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
