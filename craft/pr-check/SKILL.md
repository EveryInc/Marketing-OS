# PR Check

The pre-send gate for anything going to press — pitches, press releases, embargoed
materials, founder quotes. Sits to PR what ai-check sits to copy: nothing reaches a
journalist's inbox without passing it. A bad pitch doesn't just fail; it burns the
outlet for the next launch.

## When to invoke

- A press pitch, release, one-pager, or embargo package is drafted and about to send
- "Check this pitch," "is this ready to send to [journalist/outlet]"
- A launch's PR plan reaches its send dates (Week 7–8)
- Reviewing founder quotes or spokesperson materials before external use

## The checks, in order

1. **Named human, verified beat.** The pitch targets a specific journalist. Live-check
   (search, cited) what they've actually covered in the last ~90 days — a pitch to
   someone who left the beat, or the outlet, is the most common self-burn. No blast
   templates, ever (craft/press-comms rule).
2. **The angle passes the outlet's lens, not ours.** State in one line why *their*
   reader cares. If the only answer is our launch date, there's no story yet — say so
   rather than softening the pitch into shipping.
3. **Why-now holds.** The newsworthiness test from the launch narrative: what changed in
   the world that makes this a story this week? "We shipped" is not a why-now.
4. **Claims cleared.** Every stat, customer count, price, and named customer in the
   materials appears in the launch's claims-clearance table as CLEARED. Journalists
   fact-check; an UNVERIFIED claim in a pitch is a credibility grenade.
5. **Quote hygiene.** Attributed quotes approved in writing by the person quoted.
   Testimonials carry logged permission.
6. **Embargo/exclusive logic is coherent.** One exclusive per story; embargo time zone
   stated; no outlet offered something already given to another. Check the send list
   against itself.
7. **Mechanics.** Subject line + first sentence carry the whole pitch (they're all that
   gets read). Under ~150 words to the ask. Assets linked, never attached. ai-check and
   every-style pass on the text itself.

## Output

A pass/fix verdict per check, in order, with the failing text quoted and the fix
proposed — never a silent rewrite. A pitch failing checks 2 or 3 gets a "don't send"
verdict with the reason; that verdict is the skill working, not failing.

## Dependencies

- `foundation/marketing-os`
- `craft/press-comms` (the pitch-writing skill this gates)
- `launches/claims-clearance` (clearance table in)
- `brand-voice/{relevant brand}` (dynamically)
- `organization/ai-check` · `organization/every-style` equivalents (mandatory text passes)

## Quick checklist

- [ ] Journalist named; beat live-verified with a cited source
- [ ] Angle stated in the outlet's terms; why-now survives the "we shipped" test
- [ ] Every claim CLEARED; every quote permissioned in writing
- [ ] Exclusive/embargo logic checked across the full send list
- [ ] Subject + first line do the work; under ~150 words; links not attachments
- [ ] Verdict delivered per check — including "don't send" when earned
