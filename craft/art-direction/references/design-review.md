# Design review and correction

Use with the relevant sections of `design-foundations.md`. Keep the review proportional:
a caption repair does not need an identity audit. Inspect the actual artifact; without
a render, return a specification review and mark visual checks pending.

## Review in priority order

1. **Fidelity:** Is the approved message, offer, identity, and evidence intact? Check
   source against output. Missing wording or a substituted font is not cosmetic.
2. **Comprehension:** What draws attention first? Does that match the intended message?
   Is the relationship between message, evidence, and action clear?
3. **Reading and access:** Check text size at destination scale, applicable contrast,
   grouping, crop, overflow, and interactive states. List untested requirements.
4. **System:** Check shared edges, spacing roles, type roles, color roles, and intentional
   exceptions. Preserve approved expressive choices.
5. **Finish:** Check awkward wrapping, optical spacing, image resolution, export dimensions,
   clipping, font substitution, and consistency across the requested surfaces.

Fix the highest-impact problem, render again, and inspect the same condition. Do not
generate endless variants. After two unsuccessful repair passes, describe the remaining
failure and the decision or resource needed. Do not publish automatically.

## Symptom → diagnosis → smallest useful change

| Symptom | Inspect | First correction to try |
|---|---|---|
| Everything shouts | Multiple equally strong elements | Select one first read; reduce competing emphasis |
| Page feels scattered | Inconsistent edges and unrelated gaps | Establish shared alignment and group related items |
| Looks bland despite neat spacing | Missing concept or distinctive feature | Preserve structure; return the unresolved expressive choice to the owner |
| Dense copy is hard to follow | Measure, leading, paragraph rhythm | Adjust text width and spacing before changing fonts |
| Heading belongs to wrong paragraph | Space above versus below | Move heading closer to the section it introduces |
| Color works in swatches but fails on page | Adjacent backgrounds, proportions, opacity | Test the actual pair and adjust its role or placement |
| Desktop works, mobile fails | Fixed widths, reordered evidence, scaled-down text | Reflow and recrop while preserving content order |
| Chart looks elegant but tells nothing | Missing units, labels, evidence or scale | Restore meaning; never invent data to fill the design |
| Interface looks polished but the user still cannot do the job | Requested task, source relationships, complete action, intended account access | Repair the task structure or blocked action before another cosmetic pass; use `task-first-interfaces.md` |

## Short teaching examples

**Launch page:** A fictional approved headline, paragraph, screenshot, and action are
centered in four unrelated widths. Keep the words. Establish one text edge, constrain
reading width, give the screenshot enough size to show its evidence, and align the action
with the text. On mobile, stack in the intended reading order. Explain how shared edges
reduce competing starts; don't claim a conversion lift without a test.

**Social card:** A 1080px export uses 36px type for essential details. At a 360px display
width that becomes roughly 12px. Inspect at that size. Recompose with larger essential
details and fewer competing elements; ask before shortening protected wording. Export
resolution and displayed reading size are different checks.

**Deck:** A slide contains eight equal-size boxes of evidence. Identify the principal
point, create a dominant evidence area, and group the remaining support. If all detail
must remain, use another slide or an approved appendix rather than shrinking the text.
Do not label a layout successful until inspected at audience viewing size.

## Handoff and learning

Report: intended first read; most consequential correction; what was checked and at what
size/state; remaining failures or unknowns; editable source and rendered output references.
Classify findings as **blocking defect**, **recommended refinement**, or **unverified**.
A blocker cannot be averaged away by good scores elsewhere.

For interactive tools, report visual, functional, and audience-access checks separately.
Test the intended account role; owner access or a local test identity does not establish
deployed teammate access. A core blocked action belongs in the opening handoff, even if
the design is approved. Keep privacy intact while resolving access requirements.

When a human correction warrants learning, use the shared compound workflow. Keep a
small project-local record: before/after references, observed defect, correction and
rationale, applicability boundary, reviewer/date, material revision rounds, and next
authorized comparable surface. Do not store private designs in the reusable skill.

For the next comparable assignment, track **material correction rounds to human approval**
as the primary craft metric. A round is one consolidated review that requires a substantive
visual change; count rounds consistently. Track production defects and identity fidelity
as guardrails. Missing baselines stay missing. This research addition is not evidence of
reduced revisions. Apply a correction on fresh authorized work and record human review
before claiming transfer; use the shared proof standard before claiming improvement.
