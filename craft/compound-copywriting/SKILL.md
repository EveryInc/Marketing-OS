# Compound Copywriting

Turn human judgment into better future copy. This skill orchestrates copywriting,
editing, and the Marketing OS learning loop across a sequence of related deliverables.
It produces the requested copy first, learns from meaningful edits without overfitting,
and verifies that the learning transfers to a fresh piece of work.

The operating loop is **Write → Judge → Learn → Test → Repeat**. The human owns the
point of view, protected language, consequential creative choices, and final approval.
The agent owns source control, production volume, comparison, adaptation, bookkeeping,
and regression checks.

## When to invoke

- When the request says “compound this copy,” “learn from these edits,” “make the next
  draft better,” or “run Compound Copywriting”
- When a human-edited draft should improve the remaining assets in a launch or campaign
- When producing a sequence of related copy across email, web, social, press, or product
- When measuring revision burden, first-draft quality, or transfer across copy tasks
- When a repeated copy failure should become a bounded rule or regression test

Do not invoke for a single grammar pass with no requested learning. Use `craft/editing`.
Do not invoke for net-new copy when no iterative sequence or learning goal exists. Use
`craft/copywriting` and the relevant channel skill.

## Establish the copy contract

Before drafting, resolve from supplied sources:

1. The audience, intended behavior, and job of the copy.
2. Product truth, approved claims, positioning, and voice authority.
3. Canonical copy, protected language, and sections outside the edit scope.
4. Format, channel, destination, and final approver.
5. The next comparable artifact that can test transfer.

For an iterative product website, also resolve the page map, the conversion job of every
section, the approved proof inventory, blocked operational claims, the governing repeated
unit or card pattern, and the behavior that determines whether the copy worked. Load
`references/product-websites.md` before drafting or revising the site.

For a scripted marketing video, resolve the strategic tension, story or comic engine,
runtime, cast, verified product receipts, required product capture, CTA, and production
constraints. Load `references/video-treatments.md` before drafting or revising the
treatment.

Ask only for a missing decision that changes the work. Do not require a retrospective or
scorecard interview before producing the deliverable.

## Protect human authorship

The human decides the thought worth expressing. Treat a supplied headline, launch line,
first sentence, joke, provocation, or campaign phrase as protected when the author has
selected, restored, repeated, or explicitly defended it.

- Never silently improve protected language.
- Present a proposed alternative as a visible delta.
- Treat the human-edited version as canonical for the project.
- Generate material for selection. Do not present a first model draft as final copy.
- Carry approved choices through related assets without flattening channel differences.

## Run the loop

Load `references/loop.md` and execute the six stages:

1. **Frame:** Lock authority, copy job, protected language, and measurement baseline.
2. **Write:** Produce verified, channel-fit material and flag weak lines before review.
3. **Judge:** Preserve both versions and classify the meaningful human delta.
4. **Learn:** Turn the delta into a project-local carry-forward instruction immediately.
5. **Test:** Apply that instruction to a fresh comparable artifact and record the result.
6. **Compound:** Promote only the smallest transferable rule that clears the Marketing OS
   learning gate; otherwise keep it with the project.

The original edited artifact demonstrates correction. The fresh artifact demonstrates
transfer. Do not claim that the system learned until the transfer check passes.

For product websites, treat the current human-edited document as canonical for copy,
structure, formatting, and protected language. Governing GTM, positioning, product,
security, pricing, and integration sources still own factual truth. Recover approved
language before generating, map one conversion job to each section, and allocate verified
receipts across the page before polishing any line. Do not solve a missing proof point with
generic copy, an unrelated logo row, or a repeated example.

## Use two learning speeds

### Project-local learning

Apply a clear correction immediately to the remaining assets in the same campaign,
product, audience, or channel family. This improves current work without declaring a
universal rule.

### Durable system learning

Load `foundation/marketing-os/references/learning-loop.md` and
`foundation/marketing-os/references/knowledge-boundaries.md`. Promote only an explicit
ruling, a pattern supported by two independent tasks, credible causal evidence, or a
factual correction. Update the narrowest authority:

- Brand-specific language or behavior → `brand-voice/{brand}`
- Durable product or audience truth → `positioning/{brand}`
- General line craft → `craft/copywriting`
- Editing and delta interpretation → `craft/editing`
- Channel behavior → the relevant channel skill
- Repeatable failure → the narrowest relevant evaluation

Never store the project’s full draft, private source material, or temporary campaign
language as reusable doctrine.

## Measure the run

Load `references/scorecard.md`. The primary metric is material revision rounds per
approved artifact. Record time to approval, protected-language survival, hard failures,
human quality score, and whether the next-task transfer check passed.

Compare only reasonably similar work. If no baseline exists, mark the run as the baseline.
Never infer improvement from one polished final artifact or from time estimates reconstructed
after the fact.

## Output contract

Deliver the requested copy in its usable form. Keep process detail subordinate. When a
meaningful edit occurred, add only what the task needs:

- A three- to seven-item delta map.
- The project-local carry-forward instruction.
- The scorecard fields that can be derived from the work.
- The fresh task or artifact that will verify transfer.
- A learning candidate only when the trigger and boundary tests pass.

If no transferable learning exists, finish the copy and say nothing ceremonial about
compounding.

## Dependencies

- `foundation/marketing-os`
- `foundation/marketing-os/references/collaboration.md`
- `foundation/marketing-os/references/learning-loop.md`
- `foundation/marketing-os/references/knowledge-boundaries.md`
- `craft/copywriting`
- `craft/editing`
- `brand-voice/{relevant brand}` (loaded dynamically)
- `positioning/{relevant brand}` (loaded dynamically)
- The relevant channel skill

## Routed references

- Related copy sequence and learning loop → `references/loop.md`
- Iterative product homepage, workflows, integrations, or pricing copy →
  `references/product-websites.md`
- Launch film, product video, brand film, or scripted video treatment →
  `references/video-treatments.md`
- Revision burden and transfer measurement → `references/scorecard.md`

## Status

Beta until live use establishes a comparable baseline and passes at least one fresh
transfer test. Use with human review and preserve the run evidence needed to evaluate it.

## Quick checklist

- [ ] Did the requested copy ship before process commentary?
- [ ] Are source authority, copy scope, and protected language explicit?
- [ ] Is the human-edited version canonical?
- [ ] Did the delta become a bounded project-local instruction?
- [ ] Did a fresh artifact test transfer?
- [ ] Are revision rounds and hard failures measured honestly?
- [ ] Did durable promotion clear the learning and knowledge-boundary gates?
- [ ] For a product website, does every section have a distinct conversion job and an
      approved proof source?
- [ ] Do repeated units follow the human-edited exemplar in copy role, field order, count,
      and native formatting?
- [ ] For a video treatment, are story, spoken copy, visible action, product proof, and
      runtime independently judgeable?
