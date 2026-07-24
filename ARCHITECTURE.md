# Every Skills — Dependency Architecture

Every skill loads `foundation/marketing-os` as its root dependency.
Additional dependencies are listed below, grouped by category.

---

## Foundation

    foundation/marketing-os
      (no dependencies — this is the root)

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

## Craft

### Core craft (not channel-specific)

    craft/copywriting
      - foundation/marketing-os
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}

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

## Marketing Science

    marketing-science/research
      - foundation/marketing-os

    marketing-science/archetyping
      - foundation/marketing-os

    marketing-science/brand-equity
      - foundation/marketing-os
      (theoretical skill, anchored in Aaker/Keller/etc.)

    marketing-science/measurement
      - foundation/marketing-os
      - marketing-science/brand-equity
      (subscriber acquisition, cohorts, fame, authority, decision gates, and
      compounding from results)
