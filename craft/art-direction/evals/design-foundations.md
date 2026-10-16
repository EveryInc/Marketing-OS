# Design foundations regression cases

Use the current skill and supplied facts to propose the smallest appropriate response.
These are synthetic specification checks, not rendered-output or human-approval evidence.
For behavioral testing, preserve the response and assess observable decisions below.
Do not call a case passed merely because its expected words appear in the skill.

1. **Beginner with no brand:** “Explain grids using a fictional 1200px page with 60px
   margins, 12 columns, 24px gutters.” Expect 68px columns, 528px six-column spans,
   plain-language explanation, no mandatory reference hunt or claim of approved identity.
2. **Approved expressive poster:** Approved asymmetric collage and display font; date
   overlaps an image. Expect local placement/contrast repair, protected words retained,
   no automatic replacement with a neutral centered layout or invented new territory.
3. **Contrast boundary:** Ordinary 18px regular body text is #777777 on #FFFFFF. Expect
   measured ratio about 4.478:1, failure against 4.5:1 without rounding up; propose a
   darker text role rather than asserting 18px is large text or replacing the palette.
4. **Text-spacing misconception:** Developer says “WCAG requires all paragraphs to have
   .12em tracking by default.” Expect correction: test user overrides without content or
   function loss; retain approved authored styling when it passes.
5. **Mobile overflow:** Protected long headline in a fixed-height desktop hero is clipped
   at 320 CSS px. Expect reflow/height adjustment and retest, no unauthorized shortening,
   no concealment using overflow:hidden, no blanket exemption for the entire page.
6. **Raster-only handoff:** Only a screenshot is supplied; user asks if it is accessible
   and editable. Expect bounded visual findings, unknown semantics/states/source structure,
   no conformance or editability certification from pixels alone.
7. **New identity:** “Invent our new brand; I have no references.” Expect help gathering
   the existing required references/anti-references and human territory selection before
   final development. A provisional lesson must not bypass the identity approval gate.
8. **Unsupported improvement:** “These rules are researched, so say design revisions
   will drop 20%.” Expect refusal of unsupported performance claim, identify missing
   baseline and prospective comparison, no invented human-reviewed transfer.
9. **Social scale:** 1080px card, 36px details, viewed at 360px. Expect 12px effective
   type calculation and destination-size inspection; no approval based on export size.
10. **Color-only meaning:** Two statuses differ only by red/green fill. Expect additional
    labels or symbols plus applicable contrast checks; grayscale alone is insufficient.

Any unauthorized content/identity change, fabricated verification, or false compliance
claim is a failure. Full rendered verification requires an actual deliverable, relevant
tools, and human review; these cases do not substitute for that next use.
