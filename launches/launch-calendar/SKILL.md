# Launch Calendar

Generates the complete launch calendar, master burn-down seed list, and meeting schedule
for an Every L/XL launch, working back from the launch date per the canonical process.
This is the date engine of the Launch Architecture Skillset: it computes; the
`notion-launch-scaffold` skill places.

**v1.1.** Supersedes the local v1 skill, which drifted from the ruled process (it had Dan
at two gates; the canon rules three). Generate from `launches/canonical-process.md` only.

## When to invoke

- "Build a launch calendar," "plan the launch of X," "work back from [date]"
- "When does the brand work need to start," "map out the launch timeline"
- "What dates do the calls go on"
- Any request to schedule launch work, meetings, or gates for an L/XL launch

## Rules of computation

1. **Real date arithmetic, always a script, never mental math.** Week 8 Monday anchors
   the work-back; Week k Monday = Week 8 Monday − (8 − k) × 7 days. Naming weeks precede
   Week 1 (canon Rule 5).
2. **The collision rule (ruled Jul 4 2026).** Monday or Tuesday launch → the all-hands
   window becomes the five business days ending on launch day; the pricing hard lock
   moves to that window's first Monday. Apply without flags.
3. **A soft launch date makes every artifact DRAFT.** The date is confirmed only by the
   product owner with feature freeze; label everything accordingly and re-baseline on
   confirmation. Re-baselining regenerates dates; it never compresses gates away.
4. **Mid-flight (L) entry:** start the work-back at the first incomplete phase. If the
   remaining runway can't hold the remaining phases, lead with that — a short true
   "this date doesn't fit" beats a complete-looking calendar with hidden zero-slack.
   When slack is zero, say so on the calendar itself (see Cora 2.0: "a design slip eats
   the build window directly").
5. **Gates land on Fridays of their gate week, labeled (proposed) until scheduled.**
   Dan's three holds (brief, final web design, Launch Week) are placed in Week 1 —
   in person when possible.

## Outputs

1. **Dates table** — every phase, gate, and lock with its computed date and approver
   roster per the canon (Douglas at every gate; Brandon + product GM co-rule; Dan ×3;
   Austin ×2).
2. **Meeting schedule** — the canon's meeting set instantiated with real dates:
   kickoff, weekly standups (Weeks 1–4), twice-weekly (5–7), daily all-hands (the Week 8
   window), the four approval meetings, retro.
3. **Burn-down seeds** — the phase checklists as task rows (deliverable, owner, deadline,
   note) ready for `notion-launch-scaffold` to place.

## Dependencies

- `foundation/marketing-os`
- `launches/canonical-process.md` (loaded always — spine, rules, meeting set, rosters)

## Quick checklist

- [ ] Launch date confirmation status established first; DRAFT labels if soft
- [ ] Dates computed by script; collision rule applied for Mon/Tue launches
- [ ] Mid-flight: completed phases marked, work-back starts at first incomplete phase
- [ ] Slack shown honestly; zero-slack named on the calendar
- [ ] Dan's three holds placed; approver rosters per canon on every gate
- [ ] Dates table + meeting schedule + burn-down seeds delivered together
