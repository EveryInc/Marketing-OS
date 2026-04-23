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

## Craft

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

    craft/launch-email
      - foundation/marketing-os
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}
      - launches/{parent launch skill} (when invoked inside a launch)

    craft/linkedin-post
      - foundation/marketing-os
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}
      - launches/{parent launch skill} (when invoked inside a launch)

    craft/x-post
      - foundation/marketing-os
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}
      - launches/{parent launch skill} (when invoked inside a launch)

    craft/website-copy
      - foundation/marketing-os
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}
      - launches/{parent launch skill} (when invoked inside a launch)

    craft/press-comms
      - foundation/marketing-os
      - brand-voice/{relevant brand}
      - positioning/{relevant brand}
      - launches/{parent launch skill} (when invoked inside a launch)

## Launches

All launch skills load:
  - foundation/marketing-os
  - positioning/{relevant product}
  - brand-voice/{relevant product}
  - strategy/messaging-architecture
  - craft/launch-email
  - craft/linkedin-post
  - craft/x-post
  - craft/website-copy
  - craft/press-comms

    launches/improvement-launch
    launches/feature-launch
    launches/new-product-launch

## Marketing Science

    marketing-science/research
      - foundation/marketing-os

    marketing-science/archetyping
      - foundation/marketing-os

    marketing-science/brand-equity
      - foundation/marketing-os
      (theoretical skill, anchored in Aaker/Keller/etc.)
