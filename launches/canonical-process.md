# The Every Launch Process — Canonical Reference

**Version 1.3 · July 6, 2026 · Ruled by Douglas (Head of Marketing / ECD)**

This file is the single source of truth for Every's flagship launch process. Every skill
in `launches/` that generates calendars, burn-downs, briefs, scaffolds, or gates derives
from this file and only this file. The rendered Commons page and the Notion process doc
are views of this canon; when they disagree with this file, this file wins and they get
updated, not the other way around.

**v1.1 supersedes** the v1.0 reference embedded in the original launch-calendar skill.
Material corrections are listed in the changelog at the bottom. Do not generate from v1.0.

## Scope and tiers

This process covers **flagship (XL) and large (L) launches** — a new or majorly
repositioned product needing new (or refreshed) branding and a new website. Smaller
tiers are separate skills in this directory (`feature-launch`, `improvement-launch`)
and do not use this spine. If asked to compress this process for a smaller launch,
don't improvise: route to the right tier or ask Douglas.

An **L launch** (e.g., Cora 2.0) may enter the spine mid-flight — brand refreshed rather
than built, copy partially approved. The spine still applies; completed phases are marked
done with evidence, never skipped silently, and the remaining calendar is a work-back
from launch day starting at the first incomplete phase.

## The rules

1. **Gates for approval.** Douglas is a required yes at every gate (ruled Jul 4 2026).
   **Brandon owns all studio projects, with the GM of that product as co-ruler** — the
   two of them approve together at every gate, alongside the named product stakeholders.
   **Dan approves at three gates: the foundation brief, the final website design, and
   Launch Week.** Austin approves at the foundation brief and the final website design.
   Dan and Austin checks are unchanged for L/XL; for S or M launches they may be
   lightened — route those tiers to their own skills.
2. **GTM runs in a separate workstream with check-ins.** Marketing and Growth stay read
   in and aligned. Two formal convergence points: kickoff (positioning/customer) and
   pre-build (site approach, launch video assets/brief). Never a marketing approval of
   the GTM plan.
3. **A gate not met means the next phase does not start.** A red light at the brand book
   presentation buys one more round, then re-present.
4. **The Notion Calendar and burn-down list exist from Week 1,** approved with the GMs,
   Brandon, and Austin — never stood up in Launch Week.
5. **Naming adds a week.** At least one week to finalize, realistically two; positioning
   and customer work run in parallel. Douglas solo; GM/Brandon and Dan approve. Any live
   AI product on a candidate name disqualifies it; every availability claim requires a
   live search cited inline; "unverified" is not a status.

## The eight-week spine

| Weeks | Phase | Gate at the end |
|---|---|---|
| (N1–N2) | Naming, only if needed | Name approved: GM/Brandon, Dan |
| 1 | Foundation | Brief approved: Douglas, Brandon, stakeholders, **Dan**, Austin |
| 2–4 | Brand build, three parallel tracks | Red / green: Douglas, Brandon, stakeholders |
| 5 | Codex/Claude bridge → brainstorm → wireframes → motion | Wireframes signed (stakeholders + Douglas); Austin sign-off #2; pricing targeted here |
| 5–6 | Full site design | Ships to builder within two weeks of green light |
| 6–7 | Build + QA; GTM plan locks one week before launch | Site staged |
| 8 | Launch Week, all hands, daily standups | Final design approved: Douglas, Brandon, stakeholders, **Dan**, Austin; pricing hard-locked Monday |
| Post | Retro + sustain | — |

### Work-back math

Work back from launch day with real date arithmetic (a script, never mental math).
Week 8's Monday is the pricing hard lock — on the calendar unconditionally.
Week k Monday = Week 8 Monday − (8 − k) × 7 days. Naming weeks precede Week 1.
Gates land on the Friday of their gate week, labeled "(proposed)" until scheduled.
Show red-light slack (one–two weeks between green light and ship-to-build) explicitly —
never hide slack to make a tight date look achievable. If the date is closer than the
spine allows, lead with that.

### The early-week collision rule

If launch day falls on a **Monday or Tuesday**, the pricing hard lock and the
daily-standup runway collapse into launch day. Default handling: shift the all-hands
window to the **five business days ending on launch day**, with the pricing hard lock at
its start (the Monday of the prior week). **Ruled by Douglas, Jul 4 2026** — apply
without a pending flag.

## Phase checklists (the burn-down source)

Every item becomes a burn-down task with an owner, a deadline from the work-back, and a
note in the standard format (below).

### Week 1 — Foundation (owner: Douglas unless noted)

- Confirm launch date and feature freeze with the product owner — the whole clock hangs on this. A soft date makes every artifact DRAFT.
- Subscriber lens: can all our subscribers use it? (Monologue and Cora pass; Para didn't.)
- Customer profile: one core psychographic or professional target, sub-targets allowed, laddering to one–two archetypes (Builder, Operator, Seeker, Executive)
- Why are we doing this, what defines success, how do we drive it
- Dream tweet and dream headline
- Positioning and story: what we made, why we made it, who it's for
- Deep competitive audit — messaging, positioning, colors, pricing (`competitive-audit` skill)
- Name the pricing/offer owner — Brandon and the GM lock pricing, targeted for wireframe approval
- Naming phase if needed, per Rule 5
- Assemble the brief → approval: Douglas, Brandon, stakeholders, Dan, Austin
- Stand up the Notion Calendar entry and sectioned burn-down (`notion-launch-scaffold` skill); approve with the GMs, Brandon, and Austin
- Place Dan's three calendar holds now (brief, final web design, Launch Week) — Dan is best in person when possible
- Ping Austin — the GTM framework begins

### Weeks 2–4 — Brand build (three parallel tracks)

- Douglas + design lead write the Figma moodboard brief; hand off to the designer
- Designer builds the brand book: wordmark, brandmark, type hierarchy, colors, treatments, photography direction, illustration, logos, applications, systems
- Marketing builds the full brand doc: fleshed strategy and positioning, messaging, sample web copy R1, tone of voice, influencer/culture if relevant
- Austin builds the GTM framework and brief — a conversion strategy that makes money (solo track)
- Cadence: weekly team standup; Douglas's design standups; weekly stakeholder approval
- Two GM/engineering touchpoints on the weekly update
- End of Week 4: red light / green light presentation (Douglas, Brandon, stakeholders)

### Week 5 — Codex/Claude bridge and website definition

- Feed Codex/Claude the full strategy doc + Every master brand positioning and archetypes: gut-check positioning, inform high-conversion site copy, check customer alignment, brainstorm CTA and prompt copy against competitors (`codex-gut-check` skill)
- Finalize web copy off the pass (ai-check + every-style gates, both mandatory)
- Team brainstorm on the website — the wireframe phase; a few section mockups (`wireframe-from-copy` skill produces the annotated wireframe)
- Motion and video needs surface from the brainstorm → motion brief + deliverables list; brief the motion lead earliest possible, maximum lead time
- Team approves the list; Austin approves only launch assets (launch video yes, site-only motion no)
- Austin sign-off #2: positioning in the copy, approach to site and brand, launch video assets/brief
- Wireframe sign-off: stakeholders on product, Douglas on marketing
- Pricing locked by Brandon and the GM — targeted here; if unlocked, the build continues with pricing as WIP
- Brand locked → third GM/engineering touchpoint: hand the brand to the product designer and GM for in-product application (theirs, not marketing's)

### Weeks 5–7 — Design and build

- Design the full website; ship to the builder within two weeks of green light
- Builder builds, one–two weeks; QA owner named, definition of done agreed at handoff
- Product designer and GM apply the brand in the app, from the locked brand book
- Measurement and KPIs locked in Growth's GTM plan, metrics included — Growth owns measurement
- Austin locks the GTM plan one week before launch
- Douglas builds the Marketing Launch Calendar — including retro and sustain — into the Notion Calendar

### Week 8 — Launch Week

- Pricing locked — hard deadline: the Monday of Launch Week (see collision rule)
- Daily standups through launch day, set by Douglas — all hands
- Master burn-down is the single source of truth — if it's not on the list, it doesn't exist
- Pre-launch influencer/affiliate plan live per the GTM plan (only if the launch has one)
- Dan pulled in: tweet, video, whatever the launch needs — in person when possible
- Final website design approved: Douglas, Brandon, stakeholders, Dan, Austin
- Claims clearance pass on every launch surface (`claims-clearance` skill): every stat sourced, every logo permissioned, every price consistent — before anything ships
- Asset capture during launch — screenshots, product film, launch-day material; it's perishable
- Launch day: assets ship in sequence; live monitoring in Slack
- Reminder sends, Day 2–3: last-call/ICYMI email to non-openers and a Discord nudge,
  per the GTM plan. The second touch routinely performs on par with the first; it is a
  task with an owner, not an afterthought. Kate's gate applies to the email.

### Post-launch

- Retro — always. Scored against the Week 1 success definition: dream tweet, dream headline, metrics
- Sustain per the GTM plan and Marketing Launch Calendar — flexes by launch
- Learnings logged back into **this file**, with a changelog entry and version bump

## The Notion scaffold standard

Established July 2026 on the All Access, Every Agent, and Cora 2.0 launches. The
`notion-launch-scaffold` skill implements this; the standard lives here.

- **One calendar entry** in the Every Calendar database per launch (Type: Product Launch,
  Date = launch day). The page body is: template buttons, then section headings, then one
  linked table view per section. No untitled duplicate views.
- **Tasks live in the shared "Tasks: Launch, post, and project" database**, linked via
  the Launch relation. Rows are the tasks: deleting a row deletes the task everywhere.
  Views are windows; remove views, never rows, to change what a page shows.
- **Sections** via the shared `Section` select: Brand + Strategy · Web Design + Build ·
  GTM · Influencer + Affiliate + PR · Launch Week · Post-Launch. Launches subset as
  ruled (Cora 2.0 dropped Influencer + Affiliate + PR — social campaign lives in GTM).
- **Every task carries:** an Owner (a real person; "TBD with [name]" in the note when
  genuinely undecided — never a silent blank), a Deadline from the work-back, and a
  **Note in the All Access format**: `[Function tag] What it is. What it derives from /
  feeds. Open questions marked plainly.` Assumed owners and proposed dates are labeled
  as such in the note.
- **Section views filter on Section AND the Launch relation.** Known limitation: the
  Notion API cannot set relation filters on views (verified July 2026, three syntaxes),
  so the Launch filter is added manually in the UI per view and saved for everyone —
  the scaffold's final step is a checklist of exactly which views need it.
- Retroactively added tasks for completed work are marked with real status and evidence
  ("done per Douglas, [date]"), never fabricated as Not Started or silently Completed.

## Edge rules (rulings, not suggestions)

1. **When the timeline is pushed.** The push is called by the GM or Brandon. Meaningful
   product change: pause and hold a meeting on what's changing. Pure calendar slip: they
   tell Douglas, who pushes the date in the Notion Calendar. Brand/positioning phase:
   work continues. Web or final GTM phase: work may pause and switch if something else
   took the timeline. Re-baselining regenerates dates; it never compresses gates away.
2. **Pricing.** Brandon and the GM lock it. Target: the brainstorm/wireframe approval.
   If unlocked, the build continues with pricing as WIP. Hard deadline: the Monday of
   Launch Week, on the calendar unconditionally. Any price appearing on a launch surface
   before the lock is a claims-clearance flag.
3. **Naming.** Per Rule 5.
4. **Red light.** One more round; solve the reasons within a week if possible; budget
   one–two weeks before re-presenting. Show the slack on the calendar.
5. **Measurement.** Growth owns measurement and KPIs, locked inside the GTM plan.
   Marketing's retro scores against the Week 1 success definition.
6. **In-product brand.** The GM builds the app. Marketing connects with the GM and
   engineering twice during the brand build and once at brand lock; the product designer
   and GM incorporate the identity. Not marketing's workstream.

## The meeting set

| Meeting | When | Attendees | Required output |
|---|---|---|---|
| Launch kickoff | Week 1, day 1 | Full launch team | Calendar + burn-down stood up |
| Brief approval | End of Week 1 | Douglas, Brandon, stakeholders, Dan, Austin | Approved brief |
| Weekly team standup | Weeks 1–4 | Launch team | Updated burn-down |
| Design standups | Weeks 1–4, as Douglas sets | Douglas, design lead, designer | Design decisions |
| Stakeholder approval | Weeks 2–4, weekly | Douglas, project owner, stakeholders | Sign-off or notes |
| GM/eng touchpoints 1 & 2 | During brand build | Douglas, GM, engineering | Shared context |
| Red light / green light | End of Week 4 | Douglas, Brandon, stakeholders | Green, or scoped red round |
| Website brainstorm | Week 5 | Full team | Wireframes + motion list |
| Wireframe sign-off | Week 5 | Stakeholders, Douglas | Sign-off to design |
| GM/eng touchpoint 3 | At brand lock | Douglas, GM, product designer | Brand handed off |
| Twice-weekly standup | Weeks 5–7 | Launch team | Updated burn-down |
| Daily standup | Week 8 through launch | All hands | Burn-down burned |
| Final web design approval | Week 8 | Douglas, Brandon, stakeholders, Dan, Austin | Approved design |
| Retro | Post-launch | Douglas, Austin, team | Learnings → this file |

## Rosters (offer, never assume)

**The Every Agent (XL, Aug 18 2026):** process owner Douglas · project owner Brandon ·
stakeholders Willie, Marcus · founder Dan · GTM Austin · design lead Daniel · site build
Andrey · motion Valerio · video Douglas · in-product Ryan (product design) + GM.

**Cora 2.0 (L, Aug 4 2026, mid-flight entry):** GM/co-ruler Kieran · project owner
Brandon (per the studio-ownership ruling) · site design Daniel on a basis by Noah
(freelance) · site build Andrey probable (vs. Yash) · motion Valerio · product build
Tyler (freelance) · video Douglas.

A new launch's roster is collected, never inherited. These are examples to offer.

## Epistemic rules (non-negotiable, inherited by every launch skill)

- Fix the bar for "confirmed / verified / available" before generating and don't move it.
  A launch date is confirmed only by the product owner; a soft yes makes everything DRAFT.
- Never phrase a guess as a finding. Proposed dates, assumed owners, and inherited
  defaults are labeled as such in the artifacts themselves.
- Any claim about what exists or is available — names, domains, handles, stats, quotes,
  logos, competitor facts, prices — requires a live source cited inline or it doesn't ship.
- Lead with the real answer, including "this date doesn't work." A short true answer
  beats a complete-looking false one.
- Check every item the same way; name what wasn't covered instead of implying it passed.

## Skill registry (status as of July 4, 2026)

| Skill | Status | Role |
|---|---|---|
| launch-calendar | v1 live locally; **v1.1 in this bundle** re-grounds it in this canon | Date engine: calendar, burn-down, meetings |
| competitive-audit | Live v1 | Week 1 audit, source-linked |
| notion-launch-scaffold | **New in this bundle** | Builds the Notion standard above |
| codex-gut-check | **New in this bundle** | The Week 5 bridge |
| launch-brief | **New in this bundle** | Week 1 foundation generator |
| claims-clearance | **New in this bundle** | Pre-ship verification gate |
| wireframe-from-copy | **New in this bundle** | Copy doc → annotated lo-fi wireframe |
| launch-email-flows | **New in this bundle** | Four-flow launch email pattern |
| ai-check, every-style, every-editor | Live | Mandatory copy gates, referenced not duplicated |
| marketing-outreach-emails | Live | If outreach is in the GTM plan |

## Changelog

**v1.3 — July 6, 2026 (Douglas × Claude)**
- Added reminder sends (Day 2–3 email last-call + Discord nudge) to the Week 8
  checklist — adopted from Anukshi's event-launch pattern ("Launch + Reminder"),
  which the product-launch canon previously lacked.
- Scaffold standard implemented in the Every Calendar [Launch] template (sections,
  views, updated instructions, rebuilt Product Launch button), Jul 6.


**v1.2 — July 4, 2026 (Douglas ruling)**
- Ratified: Douglas required yes at every gate; Dan at three gates; the six-section
  structure; tier logic and mid-flight entry; the meeting set.
- New ruling: Brandon owns all studio projects with the product GM as co-ruler for
  approvals — replaces per-launch guessing at project ownership.
- Collision rule formally ruled; pending flag removed.
- Noted: Dan/Austin checks may lighten for S/M tiers (their own skills).


**v1.1 — July 4, 2026 (Douglas × Claude)**
- Corrected Dan's gates from two to three (foundation brief, final website design, Launch
  Week) — v1.0 drift against Douglas's July ruling.
- Added the Notion scaffold standard (sections, task format, view rules, API limitation).
- Added the early-week collision rule with its pending-ruling status.
- Added L-tier mid-flight entry (Cora 2.0 pattern).
- Added claims clearance to the Week 8 checklist.
- Added the Cora 2.0 roster as a second worked example.
- Consolidated three diverged copies (Commons HTML, Notion doc, launch-calendar skill
  reference) into this single file; corrected the contradictory skill-status tables.

**v1.0 — July 2026.** Original process, ruled by Douglas, encoded in the launch-calendar
skill and the Commons page.
