# Every Skills — Dependency Architecture

Every skill loads `foundation/marketing-os` as its root dependency.
Additional dependencies are listed below, grouped by category.

---

## Skill file structure

Every SKILL.md in this repo follows the same structure. Deviations are bugs, not style choices.

```
# [Title]

[One or two prose paragraphs introducing what this skill does and when it matters.
No YAML frontmatter. The file starts with the heading.]

## When to invoke

- [Bullet list of trigger conditions, situations, and trigger phrases.]
- [Phrase matching goes here — not in a description: field or frontmatter.]

## [Body sections specific to this skill]

[Content varies by skill type: audience model, voice rules, structural anatomy,
reference file descriptions, orchestration logic, cadence, etc. Section names and
count are not fixed — use whatever sections the skill needs.]

## Dependencies

- `skill/path` (loaded dynamically or always)
- `skill/path/{relevant brand}` (loaded dynamically)

## Quick checklist

[Checkbox list as the operational close. This section is last.]

- [ ] Item one
- [ ] Item two
```

**What this repo does not use:**
- YAML frontmatter (`---` blocks with `name:`, `description:`, etc.)
- A `description:` field for trigger phrases — those live under `## When to invoke`
- A fixed set of body section names — body sections are skill-specific

**Section ordering rules:**
- `## When to invoke` is always near the top, directly after the intro paragraph
- `## Dependencies` is always near the bottom, before the checklist
- `## Quick checklist` is always last

---

## Foundation

    foundation/marketing-os
      (no dependencies — this is the root)
      Enforces knowledge boundaries:
        - reusable operating doctrine in skills
        - durable, ruled brand and product canon in positioning and voice
        - current project facts outside the repository
        - optional cases under docs/cases, never loaded by default

## Brand Voice

All brand-voice skills load:
  - foundation/marketing-os (the voice OS)

    brand-voice/every-master
    brand-voice/cora
    brand-voice/spiral
    brand-voice/monologue
    brand-voice/plus-one
    brand-voice/proof
    brand-voice/sparkle

## Positioning

All positioning skills load:
  - foundation/marketing-os
  - marketing-science/archetyping
  - marketing-science/research

    positioning/every-master
    positioning/cora
    positioning/spiral
    positioning/monologue
    positioning/plus-one
    positioning/proof
    positioning/sparkle

## Strategy

    strategy/compound-marketing
      - foundation/marketing-os
      - foundation/marketing-os/references/golden-path.md
      - foundation/marketing-os/references/collaboration.md
      - foundation/marketing-os/references/knowledge-boundaries.md
      - foundation/marketing-os/references/learning-loop.md (when evidence may compound)
      - strategy/program-brief, marketing/gtm, or strategy/one-pager
        (selected dynamically after strategy approval)
      - craft/editing and marketing-science/measurement (during closeout)
      Carries one governed decision record from context through strategy, market action,
      and learning. Optional pod guidance is subordinate to this path.

    strategy/compound-brand
      - foundation/marketing-os
      - marketing-science/research
      - marketing-science/archetyping
      - marketing-science/brand-equity
      - craft/verbal-identity
      - craft/art-direction
      Orchestrates gated phases:
        1. Strategic foundation
        2. Brand character
        3. Optional equity modeling
        4. Verbal identity
        5. Art direction

    strategy/messaging-architecture
      - foundation/marketing-os
      - positioning/{relevant product}
      - brand-voice/{relevant product}

    strategy/one-pager
      - foundation/marketing-os
      - positioning/{source brand}
      - brand-voice/{source brand}

    strategy/program-brief
      - foundation/marketing-os
      - marketing-science/measurement
      - positioning/{relevant brand}

    strategy/marketing-pod
      - foundation/marketing-os
      - foundation/marketing-os/references/collaboration.md
      - foundation/marketing-os/references/knowledge-boundaries.md
      - strategy/program-brief or strategy/compound-brand (selected dynamically)
      - launches/launch-brief (L/XL only) and marketing/gtm
      - marketing-science/research
      - marketing-science/measurement
      - launches/claims-clearance
      - positioning/{relevant brand}, brand-voice/{relevant brand}, and assigned craft skills
      Orchestrates role-bounded agent waves while Douglas remains the manager.
      Workers never delegate, and pod maturity is measured by accepted work and review burden.

## Marketing

    marketing/gtm
      - foundation/marketing-os
      - positioning/every-master
      - marketing-science/archetyping
      - marketing-science/research
      - marketing-science/measurement
      - craft/editing
      - launches/launch-brief and launches/canonical-process.md (L/XL only)
      - launches/claims-clearance
      Canonical GTM entry for flagship, standard, scoped-revision, drumbeat, and social modes.

## Craft

### Core craft (not channel-specific)

    craft/verbal-identity
      - foundation/marketing-os
      - strategy/compound-brand
      - marketing-science/archetyping
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}

    craft/art-direction
      - foundation/marketing-os
      - strategy/compound-brand
      - craft/verbal-identity
      - marketing-science/research
      - marketing-science/archetyping
      - marketing-science/brand-equity (only for explicit equity evaluation)
      - positioning/{relevant brand}
      - brand-voice/{relevant brand}

    craft/copywriting
      - foundation/marketing-os
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}

    craft/compound-copywriting
      - foundation/marketing-os
      - craft/copywriting
      - craft/editing
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}
      - the relevant channel skill
      Orchestrates Write → Judge → Learn → Test → Repeat. Human edits become bounded
      project instructions immediately and durable doctrine only after a fresh transfer
      test and the Marketing OS promotion gate.

    craft/editing
      - foundation/marketing-os
      - brand-voice/{relevant brand}

    craft/naming
      - foundation/marketing-os
      - marketing-science/archetyping
      - brand-voice/{relevant brand}

### Email

All email skills load:
  - foundation/marketing-os
  - brand-voice/{relevant brand}
  - positioning/{relevant brand}
  - craft/copywriting
  - craft/editing

    craft/email/current-subscriber
    craft/email/paid-user
    craft/email/churned-user
    craft/email/prospect
    craft/email/transactional

### Social

All social skills load:
  - foundation/marketing-os
  - brand-voice/{relevant brand}
  - positioning/{relevant brand}
  - craft/copywriting
  - craft/editing

    craft/social/linkedin-post
    craft/social/x-post
    craft/social/threads-post
    craft/social/bluesky-post
    craft/social/instagram-post
    craft/social/substack-note

### Web

All web skills load:
  - foundation/marketing-os
  - brand-voice/{relevant brand}
  - positioning/{relevant brand}
  - craft/copywriting
  - craft/editing

    craft/web/landing-page
    craft/web/product-page
    craft/web/homepage
    craft/web/blog-post

### Press

    craft/press-comms
    craft/pr-check
      - craft/press-comms
      - launches/claims-clearance
      - foundation/marketing-os
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}
      - craft/copywriting
      - craft/editing

### Long-form

All long-form skills load:
  - foundation/marketing-os
  - brand-voice/{relevant brand}
  - positioning/{relevant brand}
  - craft/copywriting
  - craft/editing

    craft/long-form/byline
    craft/long-form/thought-leadership

## Launches

All launch skills load:
  - foundation/marketing-os
  - positioning/{relevant product}
  - brand-voice/{relevant product}
  - strategy/messaging-architecture

Each tier orchestrates a specific set of craft skills:

    launches/improvement-launch
      Orchestrates:
        - craft/email/current-subscriber
        - craft/email/paid-user
        - craft/social/linkedin-post
        - craft/social/x-post

    launches/feature-launch
      Orchestrates:
        - craft/email/current-subscriber
        - craft/email/paid-user
        - craft/email/churned-user
        - craft/social/linkedin-post
        - craft/social/x-post
        - craft/social/threads-post
        - craft/web/product-page

    launches/new-product-launch
      Orchestrates:
        - marketing/gtm
        - craft/email/current-subscriber
        - craft/email/paid-user
        - craft/email/churned-user
        - craft/email/prospect
        - craft/social/linkedin-post
        - craft/social/x-post
        - craft/social/threads-post
        - craft/social/bluesky-post
        - craft/social/instagram-post
        - craft/web/landing-page
        - craft/web/product-page
        - craft/press-comms
        - craft/long-form/byline
        - craft/long-form/thought-leadership


    launches/marketing-launch-workflow
      Douglas's end-to-end execution layer. Sits on top of the three tier
      skills and adds the actual deliverable sequence, web copy workflow,
      design brief flow, and approval process.
      Additional dependencies:
        - launches/improvement-launch
        - launches/feature-launch
        - launches/new-product-launch
      Orchestrates all craft skills from the tier skills above, plus:
        - craft/web/homepage
        - craft/web/landing-page
      References:
        - references/workback-templates.md
        - references/deliverable-templates.md
        - references/web-copy-workflow.md

### Launch Architecture Skillset (L/XL flagship process)

All generate from launches/canonical-process.md — the single versioned source for the
flagship process. When the canon and a skill disagree, the canon wins and the skill
gets fixed.

    launches/canonical-process.md
      (reference, not a skill — the ruled process, versioned with a changelog)

    launches/launch-calendar
      - launches/canonical-process.md (always)
      (the date engine: work-back, collision rule, meeting schedule, burn-down seeds)

    launches/notion-launch-scaffold
      - launches/canonical-process.md (always)
      - launches/launch-calendar (dates in)
      - launches/launch-brief (Week 1 content in)

    launches/launch-brief
      - launches/canonical-process.md (always)
      - marketing-science/archetyping
      - marketing-science/research
      - positioning/{relevant product}

    launches/codex-gut-check
      - launches/canonical-process.md (always)
      - positioning/every-master
      - positioning/{relevant product}
      - brand-voice/{relevant product}
      - marketing-science/archetyping

    launches/claims-clearance
      - launches/canonical-process.md (always)

    launches/wireframe-from-copy
      - launches/canonical-process.md (always)
      - brand-voice/{relevant product}
      - launches/claims-clearance (receives the flag inventory)

    launches/launch-email-flows
      - launches/canonical-process.md (always)
      - brand-voice/{relevant product}
      - launches/claims-clearance (clearance table in)

## Marketing Science

    marketing-science/research
      - foundation/marketing-os

    marketing-science/archetyping
      - foundation/marketing-os

    marketing-science/brand-equity
      - foundation/marketing-os
      (theoretical skill, anchored in Aaker/Keller/etc.)

    marketing-science/messaging
      - foundation/marketing-os
      - strategy/messaging-architecture (cross-referenced: the message house /
        audience-proposition matrix upstream — the audience-section schema
        operationalizes the per-target section format, it does not duplicate it)
      - marketing-science/research (project evidence, competitive audits, and
        synthesis methodology it draws proof from)
      (the audience-section schema and project evidence-bank standard)

    marketing-science/measurement
      - foundation/marketing-os
      - marketing-science/brand-equity
      (subscriber acquisition, cohorts, fame, authority, decision gates, and
      compounding from results)

## Non-dependency: Project Cases

`docs/cases/` is never part of the dependency graph. A case may preserve necessary
historical evidence, but no `SKILL.md` may load it by default or treat it as current
project guidance.
