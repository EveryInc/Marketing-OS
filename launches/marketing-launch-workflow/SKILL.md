# Marketing Launch Workflow

Douglas's end-to-end marketing launch system for Every products. Built from actual
launches (Monologue Shortcuts, Monologue website redesign, EveryCon, Cora 2.0) — not
theory. Covers the full sequence from launch decision through post-launch retro:
calendar entry, positioning brief, web copy, creative brief, deliverables list, social
briefs, email copy, asset drill-down, approvals, and go-live.

This skill is the marketing-specific execution layer. It sits on top of the three
existing launch tier skills (improvement, feature, new-product) and adds the actual
deliverable sequence, web copy workflow, design brief flow, and approval process that
marketing runs for every launch.

## When to invoke

- When Douglas says "we need to launch X" or asks for launch planning help
- When a new product, website, or feature needs marketing support
- When building a workback calendar or deliverables list for a launch
- When someone asks Douglas's team to prepare launch materials
- When coordinating social briefs, email copy, or web copy for a launch

## Tier classification

Ask Douglas or infer from context. The tier determines which phases are required.

| Tier | What it is | Lead time | Example |
|---|---|---|---|
| Feature update | New capability in an existing product | 2–4 weeks | Monologue Shortcuts, Plus One new model |
| Website / Rebrand | New or redesigned product site, positioning shift | 4–8 weeks | Monologue website redesign, Cora 2.0 website |
| New product | Net-new product launch or major initiative | 8–12 weeks | EveryCon, new Every website |

### Tier-specific scope

**Feature update** — Required phases: 1, 6, 7, 9, 10. Optional: 2 (if positioning
changes), 8 (if assets are needed). Skip: 3, 4, 5.

**Website / Rebrand** — All ten phases required.

**New product** — All ten phases, plus launch narrative (from
`launches/new-product-launch`), press strategy (if applicable), and multi-wave marketing
campaign with workback dates.

## The ten-phase sequence

Every launch follows this order. Earlier phases must complete before later ones start.
Each phase produces a concrete deliverable.

### Phase 1: Calendar & Timeline

**Deliverable:** Notion calendar entry + Creative Deliverables Timeline entry

1. Set the launch date.
2. Add to the Every Calendar in Notion.
3. Add to the Creative Deliverables Timeline.
4. Work back from the launch date to set phase deadlines.
5. For multi-product or conference launches, build a full workback with phase dates.

### Phase 2: Positioning Brief

**Deliverable:** Google Doc — Positioning & Research Brief (one to two pages each section)

This is upstream of everything. No copy, no design, no assets until positioning is
locked.

The brief has four sections:

1. **Positioning one-pager** — positioning statement, category language, core promise,
   target audience, product moments, competitive differentiation, guardrails.
2. **Research one-pager** — customer profile backed by evidence (Notion, testimonials,
   social proof), competitive landscape, market dynamics, breakthrough strategy.
3. **Best-practice copy flow** — what claims go where on the page (hero through closing
   CTA), benchmarked against Linear, Notion, Superhuman, Raycast.
4. **Current site audit** (for redesigns) — section-by-section analysis of the existing
   site against the positioning brief.

Source material: the product's Notion workspace (especially landing page redesign pages
and customer evidence sub-pages), `foundation/marketing-os`, competitor websites, and
existing testimonials.

Post the brief for review before proceeding to Phase 3.

### Phase 3: Web Copy

**Deliverable:** Google Doc — Web copy recommendations and/or draft copy per page

Only starts after the positioning brief is reviewed.

The web copy workflow follows a specific pattern:

1. Douglas provides headline direction (e.g., "THINK OUT LOUD").
2. Push back with variants organized by approach (transformation, wordplay, imperative,
   personality), grounded in conversion best practices and the competitive scan.
3. Douglas refines live in a rapid-fire thread.
4. Push again with the positioning doc as reference.
5. Final copy lands in a Google Doc or Notion.

Rules: always reference the positioning brief (Douglas will ask). Never fall into
category traps the positioning doc warns against. No pseudo-profound sentences. Provide
variants organized by approach, not a flat list. Know what competitors say and do not
accidentally write their copy.

### Phase 4: Creative Brief

**Deliverable:** Google Doc or Notion page — Creative brief for the design team

Bridges positioning to design. Contains: what we're making, objective, positioning,
target audience, competitive context, customer evidence, tone and voice, technical
constraints, reference/inspiration, team, timeline, and approval chain.

### Phase 5: Deliverables List

**Deliverable:** Google Doc — Asset deliverable list with owners and status

The granular breakdown of every asset needed for launch. Organized by category
(strategic/brand, site-wide components, page-specific, video/animation, social assets,
email assets, structural/UX, future/stretch). Each row: deliverable name, description,
owner, status, priority.

If someone (e.g., Brandon) has written notes or feedback, parse them into structured
deliverable rows.

### Phase 6: Social Briefs

**Deliverable:** Google Doc — One social brief per launch beat

Contents: messaging architecture (primary, secondary, tertiary angles), key proof
points, social proof table (person, role, quote, best use), asset needs table, draft
posts for each account and platform (product account, @every, founder, GM, Douglas),
posting cadence across launch day plus day two and three follow-ups, alternate copy
options, day-before tease content, and success signals.

Draft actual posts, not placeholders.

### Phase 7: Email Copy

**Deliverable:** Google Docs — One per launch beat, three options each

Load `craft/email` skills. Search Kit for existing product emails to match style.

Each option is a complete, send-ready email: subject line plus preheader, Kit greeting
tag, 250–400 words, declarative subjects, bold-label bullet features, action-verb CTA,
product-appropriate sign-off. Three options per launch, each with a different lead angle.

Do a grammar pass before delivering.

### Phase 8: Asset Drill-Down

**Deliverable:** Prioritized asset list with specs

Consolidated from social briefs and deliverables list. Each asset: description, specs
(dimensions, length), creator, deadline, where it is used.

Asset types: screen recordings, product demo videos, before/after screenshots, GIFs,
feature page screenshots, social proof walls of love, email header images.

### Phase 9: Approvals & Go-Live

**Deliverable:** Approval checklist plus scheduled sends

All copy reviewed and approved. Design assets reviewed. Kit email configured. Social
posts scheduled. Product page staged. Product team confirms stability. Support team
briefed. Go/no-go at T-2.

### Phase 10: Post-Launch

**Deliverable:** T+1 check plus T+7 retro

T+1: engagement check (email opens/clicks, social engagement, site traffic).
T+7: what worked, what did not, user response patterns. Update this skill with learnings.

## References

### references/workback-templates.md

Workback schedules for all three tiers, with actual dates from past launches. Feature
update runs T-14 through T+7. Website/rebrand runs T-42 through T+7. New product runs
T-84 through T+30. Includes the EveryCon-specific phase breakdown.

### references/deliverable-templates.md

Templates for each major deliverable: social brief, email options, positioning brief,
and deliverables list. Each template shows the exact structure and sections, ready to
populate for a new launch.

### references/web-copy-workflow.md

How web copy iteration works from headline direction through final copy. Includes the
hero copy structure, page-by-page copy flow, the subheadline workshop process, and rules
extracted from corrections on past launches.

## Reference routing

| Task type | Load |
|---|---|
| Building a workback calendar | `references/workback-templates.md` |
| Writing a social brief, email, positioning brief, or deliverables list | `references/deliverable-templates.md` |
| Iterating on web copy or hero headlines | `references/web-copy-workflow.md` |
| Tier cadence and day-of choreography | The relevant tier skill's `references/cadence.md` |
| Pre-launch readiness | The relevant tier skill's `references/pre-launch-checklist.md` |

## Dependencies

- `foundation/marketing-os`
- `positioning/{relevant product}` (loaded dynamically)
- `brand-voice/{relevant product}` (loaded dynamically)
- `launches/improvement-launch` (for feature-update tier)
- `launches/feature-launch` (for website/rebrand tier)
- `launches/new-product-launch` (for new-product tier)
- `strategy/messaging-architecture`
- `craft/email/current-subscriber`
- `craft/email/paid-user`
- `craft/social/linkedin-post`
- `craft/social/x-post`

## Quick checklist

- [ ] Classify the tier (feature update, website/rebrand, new product)
- [ ] Set the launch date with Douglas
- [ ] Add to Notion calendar and Creative Deliverables Timeline
- [ ] Propose workback schedule based on tier lead times
- [ ] Positioning brief drafted and reviewed before any copy starts
- [ ] Web copy grounded in positioning doc at every step
- [ ] Creative brief posted to design team
- [ ] Deliverables list categorized with owners and priorities
- [ ] Social briefs contain actual draft posts, not placeholders
- [ ] Email copy grammar-checked before delivery
- [ ] All deliverables produced as Google Docs (never PDFs)
- [ ] Post-launch retro completed and skill updated with learnings
