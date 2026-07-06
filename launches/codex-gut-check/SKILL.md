# Codex Gut-Check

The Week 5 bridge between locked brand and website work. Feeds the full strategy doc and
the Every master brand into a fresh model pass to pressure-test positioning and copy
before anything gets wireframed or designed. The point is adversarial: a reader with no
sunk cost in the strategy, told to find where it fails, before the website inherits it.

## When to invoke

- Week 5 of any L/XL launch, before the website brainstorm
- "Run the Codex check / Claude check / gut-check on [product] positioning or copy"
- Web copy exists in draft and the team is about to wireframe from it
- Canon checklist item: "gut-check positioning, inform high-conversion site copy, check
  customer alignment, brainstorm CTA and prompt copy against competitors"

## Inputs (all required — refuse to run on partial context)

1. The launch's full strategy/positioning doc (or brand doc containing it)
2. Every master brand positioning and archetypes (`positioning/every-master`,
   `marketing-science/archetyping`)
3. The competitive set with live citations (`competitive-audit` output — if stale by more
   than ~4 weeks, re-verify the claims that the copy leans on)
4. The current web copy draft, whatever round it's at

## Outputs

1. **Positioning verdict** — confirm or challenge, with the specific passages that earn
   the verdict. "Strongest" and "clear" only with evidence; a challenge names what a
   named competitor already owns or contradicts.
2. **Copy pressure-test** — where the draft contradicts the strategy doc, the voice
   rules, or itself (headline tensions, duplicate blocks, truncated bodies, banned
   terms). Cite doc-internal locations. Every unverified stat, quote, logo, or price
   found here is handed to `claims-clearance` as an opening inventory.
3. **CTA and prompt-copy candidates** — tested against what named competitors actually
   run (cited), not against generic SaaS patterns.
4. **Customer alignment check** — does the copy speak to the Week 1 customer profile and
   archetypes, section by section, or has it drifted to a different reader?

## Rules

- Findings cite their location (section, line, source). No unearned superlatives.
- Disagreement with the strategy is the job — deliver the challenge plainly and let
  Douglas rule. The check is advisory; the human ruling is final.
- The output feeds copy R-next and the wireframe; it is not itself copy. Never rewrite
  the draft wholesale inside the check.

## Dependencies

- `foundation/marketing-os`
- `launches/canonical-process.md` (Week 5 definition, epistemic rules)
- `positioning/every-master` · `positioning/{product}` (loaded dynamically)
- `brand-voice/{product}` (loaded dynamically)
- `marketing-science/archetyping`
- `launches/competitive-audit` output as input

## Quick checklist

- [ ] All four inputs present; refused otherwise
- [ ] Verdict cites passages; challenges name competitors with sources
- [ ] Copy contradictions located precisely (the Cora pattern: hero-line tension,
      duplicate feature blocks, truncated bodies)
- [ ] Unverified claims inventoried and handed to claims-clearance
- [ ] CTA/prompt candidates tested against cited competitor reality
- [ ] Delivered as findings for ruling, not as a rewrite
