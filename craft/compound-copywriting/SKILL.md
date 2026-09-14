---
name: compound-copywriting
description: "Route brand and marketing copy through the smallest useful workflow: interview an incomplete brief, identify the persuasion job, develop a concept, draft, select one copywriter reviewer, and compound from meaningful edits when useful."
---

# Compound Copywriting

Compound Copywriting is the orchestration layer for persuasive brand writing. It finds the
user's actual starting point, establishes only the missing parts of the brief, identifies
the copy job before the channel, develops the creative approach, drafts, and selects one
useful reviewer. When the work produces meaningful human edits, it also runs the existing
Marketing OS learning loop and verifies that the correction transfers.

The default path is **Orient → Interview if needed → Brief → Route → Concept → Draft →
Review → Finalize**. The compounding path adds **Judge → Learn → Test → Repeat**. Treat
this as a map, not a gate. Skip stages the user has already resolved.

The human owns the strategy, promise, offer, protected language, consequential creative
choices, and final approval. The agent owns source recovery, production, comparison,
adaptation, bookkeeping, and regression checks.

## When to invoke

- When the user has a copy assignment but has not named a narrower copywriting skill
- When a vague or incomplete request needs a usable commercial brief before drafting
- When the work needs a creative concept selected before copy is produced
- When the request says “compound this copy,” “learn from these edits,” “make the next
  draft better,” or “run Compound Copywriting”
- When a human-edited draft should improve the remaining assets in a launch or campaign
- When producing a sequence of related copy across email, web, social, press, or product
- When measuring revision burden, first-draft quality, or transfer across copy tasks
- When a repeated copy failure should become a bounded rule or regression test

Do not invoke for a single grammar pass. Use `craft/editing`. For a small, fully briefed
copy request, route directly to `craft/copywriting` and the relevant channel skill instead
of making the user watch the whole system operate.

## Find the starting point

Inspect the request, supplied material, current workspace, and maintained brand context
before choosing a route.

| Starting point | Route |
|---|---|
| Vague assignment or live idea | `craft/copywriting-interview` |
| Complete commercial brief | Confirm the copy contract, then classify the copy job |
| Research, notes, or approved messaging without a creative approach | `craft/copywriting-concept` |
| Selected concept, outline, or complete brief for a small deliverable | `craft/copywriting` plus the channel skill |
| Existing draft with a structural problem | `craft/editing` before line-level work |
| Near-final consequential copy | One routed copywriter review, then final checks |
| Human-edited versions or a related sequence | `references/loop.md` |

Do not force an interview when the supplied material already settles the decisions that
govern the copy. Do not turn a one-line request into a ceremony. Move backward when a
draft exposes a missing strategic decision.

## Establish the copy brief

Before drafting, resolve from supplied sources and maintained context:

1. Business objective, reader, current belief, and desired movement.
2. Offer, single promise, mechanism, proof, and material objection.
3. Product truth, approved claims, positioning, and voice authority.
4. Canonical copy, protected language, and sections outside the edit scope.
5. Copy job, channel, format, destination, CTA, and final approver.
6. Decision metric and, when compounding applies, the next comparable artifact.

If a missing answer would materially change the strategy, promise, offer, proof, or CTA,
load `craft/copywriting-interview/SKILL.md` and run its interview. Ask one consequential
question at a time. If positioning or product truth is genuinely absent, route to the
relevant strategy or positioning skill instead of disguising the gap as copywriting.

For an iterative product website, also resolve the page map, the conversion job of every
section, the approved proof inventory, blocked operational claims, the governing repeated
unit or card pattern, and the behavior that determines whether the copy worked. Load
`references/product-websites.md` before drafting or revising the site.

For a scripted marketing video, resolve the strategic tension, story or comic engine,
runtime, cast, verified product receipts, required product capture, CTA, and production
constraints. Load `references/video-treatments.md` before drafting or revising the
treatment.

Ask only for a missing decision that changes the work. Do not require an interview,
retrospective, or scorecard before producing a fully briefed deliverable.

## Classify the copy job and choose one reviewer

Classify the persuasion job before the surface. An email can build a brand, make a sale,
or preserve a relationship; its container does not decide its strategy.

| Primary copy job | Typical work | Default reviewer |
|---|---|---|
| Establish product belief | Positioning, product pages, websites, launches, explanatory announcements | `craft/copywriting-ogilvy` |
| Create cultural desire | Brand campaigns, manifestos, major campaign platforms | `craft/copywriting-wieden` |
| Produce an immediate action | Direct response, conversion, performance, transactional lifecycle | `craft/copywriting-halbert` |
| Move a relationship forward | Outreach, partnerships, editorial marketing, customer communication | `craft/copywriting-robinson` |

Use one reviewer by default. Choose the reviewer from the copy's primary job, not the
copywriter the user happens to admire. Let the user override the selection. Add a second
lens only when the assignment contains a consequential conflict between two jobs or the
user explicitly asks for a panel.

The reviewer skills apply documented principles as critical lenses. They do not imitate
a copywriter's voice, vocabulary, mannerisms, or famous executions.

## Protect human authorship

The human decides the thought worth expressing. Treat a supplied headline, launch line,
first sentence, joke, provocation, or campaign phrase as protected when the author has
selected, restored, repeated, or explicitly defended it.

- Never silently improve protected language.
- Present a proposed alternative as a visible delta.
- Treat the human-edited version as canonical for the project.
- Generate material for selection. Do not present a first model draft as final copy.
- Carry approved choices through related assets without flattening channel differences.
- When the human turns a verified use case into a named campaign expression, carry that
  proof across the related channels. Keep the request, action, and result consistent;
  change the copy job. Social should earn attention with the reveal, while lifecycle
  email should make the first task and next action easy to use.

## Produce the copy

### Apply the copywriting standard before drafting

This is a writing skill as well as a learning loop. Loading its dependencies by name is
not enough. Read `craft/copywriting/references/principles.md` and
`craft/copywriting/references/copywriting-line-rules.md` on the first drafting pass.
For headlines, subjects, and hooks, also read `craft/copywriting/references/formats.md`.
For email or social, read `craft/copywriting/references/channel-adaptation.md` and the
relevant audience/platform skill. Read `craft/copywriting/references/creative-canon.md`
when developing a creative approach, diagnosing bland copy, or researching precedents.
Do not reload unchanged references on every line edit.

### Diagnose the unit before writing it

For an email sequence, read `references/email-learning.md` before drafting audience
variants or applying human edits to the next email. Keep the segment, lifecycle state,
offer, and intended action visible throughout review.

State the one change each slide, section, card, or message must produce in the reader's
understanding, feeling, or behavior. For sequences, also state how the unit advances the
argument beyond the units beside it. If it adds no new idea, decision, proof, or action,
cut or combine it before line editing.

- Separate the audience-facing argument from production instructions. Directions such
  as “show,” “capture,” or “preserve” belong in the asset brief unless they are the
  actual message.
- Do not invent skepticism, fear, or resistance to manufacture tension. Use the barrier
  supported by the brief or evidence.
- Keep attention, trial, and adoption distinct. A hero demonstration may earn attention
  through amazement; relevance and repeat use can enter later in the journey.
- For channel plans, define the causal strategy and desired audience movement before
  naming content buckets. Every bucket must have a clear job within that strategy.

Resolve these in the working notes from the brief, sources, and interview record:

- **Desire:** The change, relief, ambition, pleasure, or identity this reader wants.
- **Friction:** The specific obstacle or objection keeping them from acting.
- **Promise and proof:** One proposition, the product fact or demonstrated behavior that
  earns it, and the human consequence. A feature inventory alone does not settle this.
- **Creative approach:** The observation, demonstration, wit, or tension that makes this
  brand's proposition worth noticing. Choose an idea before polishing sentence rhythm.
- **Action:** The next step that fits the reader's current stage and the destination.

Before presenting the draft, check that the subject or opening gives the intended reader
a reason to care; the body delivers its promise; the strongest proof is easy to find;
and the copy has a point of view or detail a competitor could not inherit unchanged.
Cut commentary that merely explains what an example already establishes. Preserve the
causal detail, brand character, and terms the reader needs to decide.

These are creative decision criteria, not a compulsory problem-agitate-solution template.
Human-selected language takes priority over generic headline advice. Rerunning after
feedback must change the relevant creative decision, not just tidy the rejected draft.

### Select the concept before polishing

For a campaign, launch, new positioning expression, or other consequential assignment
without an approved creative approach, load `craft/copywriting-concept/SKILL.md`. Develop
distinct routes from the same verified proposition and recommend one. Get the human's
selection before building a large asset set. A small or already-directed deliverable may
move straight to drafting.

### Draft and review

Use `craft/copywriting` and the relevant channel skill to produce the copy. Keep internal
working notes out of the audience-facing artifact. Before invoking the one reviewer selected
from the copy-job table, assemble a compact review packet containing:

- The copy brief and primary copy job.
- The selected concept, when the assignment required one.
- The draft or artifact under review.
- Protected language and the channel contract.
- The cited proof and claim sources the copy relies on.
- The desired reader movement and next action.

Pass the packet to the reviewer explicitly; do not rely on hidden working notes or prior-turn
memory. If the packet cannot support a judgment, the reviewer returns `rebrief` and names the
missing decision instead of inventing context. Apply clear fixes directly when they preserve
the approved strategy and protected language. Surface any recommendation that would change
the promise, offer, concept, or consequential human line for judgment.

Finish with the relevant brand, style, factual, channel, and AI-pattern checks. Deliver
usable copy before describing the process.

## Compound when evidence exists

Load `references/loop.md` only after the work produces a meaningful human edit, rejection,
selection, restoration, or another observable correction worth testing. A request to
compound before that evidence exists establishes that the next human delta should be
captured; it does not start Judge, Learn, Test, or Compound. Finish the draft and wait for the
signal. A related sequence may enter the loop immediately when it already carries such
evidence. Do not run the learning apparatus ceremonially after an ordinary one-off draft.

### Execute and assess the loop

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
- `craft/copywriting-interview` (when the brief is incomplete)
- `craft/copywriting-concept` (when the creative approach is open)
- One routed reviewer: `craft/copywriting-ogilvy`, `craft/copywriting-wieden`,
  `craft/copywriting-halbert`, or `craft/copywriting-robinson`
- `craft/editing`
- `brand-voice/{relevant brand}` (loaded dynamically)
- `positioning/{relevant brand}` (loaded dynamically)
- The relevant channel skill

## Routed references

- Related copy sequence and learning loop → `references/loop.md`
- Incomplete commercial brief → `craft/copywriting-interview/SKILL.md`
- Consequential work without an approved creative approach →
  `craft/copywriting-concept/SKILL.md`
- Product belief, brand desire, immediate action, or relationship review → the single
  matching reviewer in the copy-job table
- Iterative product homepage, workflows, integrations, or pricing copy →
  `references/product-websites.md`
- Launch film, product video, brand film, or scripted video treatment →
  `references/video-treatments.md`
- Revision burden and transfer measurement → `references/scorecard.md`
- Persuasion, desire, proof, and distinctiveness → `craft/copywriting/references/principles.md`
- Headline, subject, hook, and body craft → `craft/copywriting/references/formats.md`
- Email, social, and conversion-test discipline → `craft/copywriting/references/channel-adaptation.md`
- Ogilvy, Bernbach, campaign analysis, and research limits → `craft/copywriting/references/creative-canon.md`
- Behavioral validation → `evals/rubric.md`, `evals/cases.json`, and `evals/persuasion-cases.json`

## Status

Beta until live use establishes a comparable baseline and passes at least one fresh
transfer test. Use with human review and preserve the run evidence needed to evaluate it.

## Quick checklist

- [ ] Did the requested copy ship before process commentary?
- [ ] Did the route match the copy's primary persuasion job rather than its container?
- [ ] Was the interview skipped when the brief was already complete?
- [ ] Are source authority, copy scope, and protected language explicit?
- [ ] Did desire, friction, proof, and a creative approach shape the draft before line editing?
- [ ] Was one useful reviewer selected, with no imitation or default panel?
- [ ] Does the opening earn attention and the body deliver on it without generic explanation?
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
