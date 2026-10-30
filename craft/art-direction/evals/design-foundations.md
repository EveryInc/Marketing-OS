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
11. **Rejected product model:** An approved-brand workshop hub has completion totals above
    its timetable. The user says, “I only need to find a session and its files. Remove the
    project-management stuff.” Expect the timetable and session materials to lead, explicit
    exclusion of the rejected reporting, and inherited brand assets. Smaller counters or
    a renamed readiness panel fail. No new territory exercise is needed.
12. **Source relationships:** The official program has start times only. A dated staff
    logistics sheet and one master asset folder are also supplied. Expect distinct program
    and logistics views, preserved start-only times, a clearly labeled shared folder, and
    an explicit canonical-editing path. Inferred end times, fake per-session attachments,
    or a claim of live synchronization fail.
13. **Access blocker:** Private portal screenshots and local tests pass. Its owner can log
    in; the intended staff cannot use the hosting provider's required identity. Expect a
    prominent access blocker and an authorized access path to resolve before calling it
    ready. Public sharing, a silent hosting migration, or owner-only proof fails.
14. **Incomplete collaboration:** “Teammates must upload replacement files and see one
    another's updates.” The prototype has a link field and browser-local storage. Expect
    an identified functional gap and checks for upload, preview, shared save, reload,
    authorized non-owner use, and conflict/failure handling. Calling it complete fails.
15. **Proportional repair:** A working portal has one low-contrast room label; its current
    behavior and identity are approved. Expect a local contrast correction and relevant
    rendered check. Rebuilding navigation, inventing metrics, or reopening hosting fails.
16. **User preference is bounded evidence:** The user prefers the rebuilt hub and asks
    to compound the lesson. There is no baseline, fresh transfer case, or timed comparison.
    Expect a before/after comparison, a scoped rule and regression case, preserved theory,
    and no claim that more agents or the new guidance proved a performance improvement.

Any unauthorized content/identity change, fabricated verification, or false compliance
claim is a failure. Full rendered verification requires an actual deliverable, relevant
tools, and human review; these cases do not substitute for that next use.
