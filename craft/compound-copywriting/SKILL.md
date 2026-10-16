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

## Use the smallest execution path

For a small, fully briefed source-to-destination copy request, use this default sequence:

1. Read the supplied source and the narrow brand or channel rule already governing it.
2. Inspect only the requested destination and nearby formatting.
3. Draft the requested copy, write it, and verify the edited area once.
4. Deliver the result before doing any optional compounding work.

Skip interviews, concept development, broad workspace searches, benchmark research,
multi-tab inventories, reviewer panels, and repeated readbacks when they cannot change
the requested copy. Do not delay a usable draft to validate context the user already
provided. Expand the workflow only for a missing fact or decision that would materially
change the copy, a write or permission failure, or a request that changes document
structure. If the workflow expands, state the reason in one sentence and continue.

## Explicit constraints and existing approval

Carry forward the user’s explicit word bans until they revoke them. A later appearance
in a draft, quote, or source does not revoke a ban. Check generated copy and editorial
suggestions against these constraints before delivery; do not infer universal bans from
a single rejected sentence. For Douglas’s Every work, load the current constraints in
`../../brand-voice/every-master/references/editorial-constraints.json`.

Existing explicit authorization to apply changes takes precedence over a default
review-first interview. Preserve its scope; do not ask the user to approve it again.
Approval to edit a draft does not authorize sending or publishing it.

## Establish the copy brief

Before drafting, resolve from supplied sources and maintained context:

1. Business objective, reader, current belief, and intended response.
2. Offer, single promise, mechanism, proof, and material objection when the copy asks
   the reader to buy, install, subscribe, apply, or take another commercial action.
3. Product truth, approved claims, positioning, and voice authority.
4. Canonical copy, protected language, and sections outside the edit scope.
5. Copy job, channel, format, destination, any appropriate CTA, and final approver.
6. The review criterion for the piece and, when compounding applies, the next comparable
   artifact.

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
| Earn attention and cultural relevance | Always-on social, timely commentary, humor, editorial observation | `craft/copywriting-wieden` |
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

### Enforce the revision contract

Before revising human-edited or rejected copy, run this compact gate in the working
notes. Keep it subordinate to the requested deliverable.

1. **Recover the current version.** Match the artifact and section, not merely the most
   recent attachment. Use the latest human edit as the baseline. If that full version is
   unavailable, apply explicit corrections to the latest recoverable draft; state the
   limitation only when it affects delivery. Do not claim an unrelated edit snapshot
   contains the missing version.
2. **Record what changed.** Keep protected language, removed content, rejected approaches,
   format preferences, and the current section's job in the project-local copy contract.
   Retire superseded requirements when the user changes the brief. Acknowledging feedback
   in chat is not a substitute for applying it to the next artifact.
3. **Honor exclusions.** A source can verify a fact without authorizing its inclusion.
   Keep user-cut content out of subsequent revisions of the same artifact unless the
   user reopens it. A request to rewrite, strengthen, or shorten does not reset those
   decisions. Do not turn a local deletion into a universal ban on the fact or format.
4. **Fix the rejected decision.** For a structural rejection, name the failed argument,
   evidence selection, or section job before drafting. Change that decision rather than
   paraphrasing the same inventory. Preserve unaffected approved material. After two
   revisions fail for the same reason, diagnose the missed constraint before generating
   again; do not make the user repeat feedback already available.
5. **Check the delta before delivery.** Compare against the baseline and explicit cuts.
   Check restored content, protected wording, format, length, repeated evidence, and
   whether the requested structural change occurred. Use mechanical checks for literal
   exclusions when useful; they do not establish persuasive quality. Keep the comparison
   internal unless the user asks for it.

For evidence-led copy, distinguish business performance, attributed conversions, product
use, reach, and measured customer outcomes. Keep dates and denominators attached to the
claims they qualify. Do not infer causation from aggregate growth or add explanatory
sentences that merely restate a metric. Apply confidentiality labels from explicit user
direction or an established source restriction, not simply because a source is internal.

Reading a skill is preparation, not evidence that its checks ran. Report only the review,
verification, and transfer actually performed. Exercise the revision cases in
`evals/cases.json` when changing this gate.

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

For email work, read `references/email-learning.md` before drafting, revising a
reminder, producing audience variants, or applying human edits to the next email.
Apply its concept, hook, story, selective-economy, proof-rotation, lifecycle, platform,
visual, and authorship rules. Keep the segment, lifecycle state, offer, and intended
action visible throughout review. Before delivery, run the manual checks in
`evals/email-edit-regressions.json`; do not confuse checklist completion with a named
editorial tool run, human approval, or measured conversion improvement.

For a campaign-wide final edit or conversion audit, use
[`Email Final Pass`](../email-final-pass/SKILL.md). Review the whole campaign,
current context, reviewer notes, Kit results, and assets; return no more than 10
recommendations. When changes are not already authorized, interview the user about
each category before applying them. Review-only requests do not authorize even obvious
fixes; explicit authorization from the user, including prior turns, still governs. Keep accepted email craft in Compound Copywriting, not Compound Writing.

For social work, read `references/social-learning.md` before building a channel
approach, drafting a run of posts, or applying human edits to the next post. Choose the
post's job before choosing its form, allow product definitions, category explanations,
memes, demonstrations, teaching, opinions, and stories to compete on their merits, and
judge each post as well as the larger feed it joins. Before delivery, run the relevant
manual checks in `evals/social-edit-regressions.json`; passing them does not prove that a
post will travel or convert.

When the publishing account is `@every`, also read
`brand-voice/every-master/references/social-copywriting.md`. Apply its topic priorities,
two observed post shapes, repost rules, and Every-specific review gates as a brand overlay.
Do not generalize those priorities to product, founder, employee, or client accounts.

State what each slide, section, card, or message should contribute to the reader's
understanding, feeling, memory, conversation, or behavior. For sequences, also state how
the unit differs from the units beside it. If it adds no idea, amusement, usefulness,
proof, or action, cut or combine it before line editing.

- Separate the audience-facing argument from production instructions. Directions such
  as “show,” “capture,” or “preserve” belong in the asset brief unless they are the
  actual message.
- Do not invent skepticism, fear, or resistance to manufacture tension. Use the barrier
  supported by the brief or evidence.
- Keep attention, trial, and adoption distinct. A hero demonstration may earn attention
  through amazement; relevance and repeat use can enter later in the journey.
- For channel plans, define the causal strategy and desired audience movement before
  naming content buckets. Every bucket must have a clear job within that strategy.

Resolve the parts below that the copy job needs from the brief, sources, and interview
record:

- **Reader payoff:** The change, relief, pleasure, identity, amusement, understanding, or
  other response the piece should create.
- **Friction:** For action-oriented or persuasive work, the specific obstacle or objection
  keeping the reader from acting.
- **Promise and proof:** For product, claim-led, or conversion work, one proposition, the
  product fact or demonstrated behavior that earns it, and the human consequence. A
  feature inventory alone does not settle this.
- **Creative approach:** The observation, demonstration, wit, or tension that makes this
  piece worth noticing. Choose an idea before polishing sentence rhythm.
- **Action:** When the copy asks for one, the next step that fits the reader's current
  stage and the destination.

Before presenting the draft, check that the subject or opening gives the intended reader
a reason to care and the rest delivers what the opening promised. When the job relies on
a product or factual claim, make the supporting evidence easy to find. Give the piece a
point of view, useful detail, humor, or another quality a competitor could not inherit
unchanged. Cut commentary that merely explains what an example already establishes.
Preserve the detail, brand character, and terms the reader needs to decide.

These are creative decision criteria, not a compulsory problem-agitate-solution template.
Human-selected language takes priority over generic headline advice. Rerunning after
feedback must change the relevant creative decision, not just tidy the rejected draft.

### Reject weak email concepts before polishing

For acquisition and reactivation email, apply these checks before writing the body:

1. Name the reader's payoff in ordinary language. Reviewing a draft, practicing a
   prompt, or inviting a colleague is usually a step, not a reason to install.
2. Compare the proposed promise and proof with the current campaign inventory.
   A new subject or membership label does not make a repeated pitch new. Reuse
   across mutually exclusive audiences only when it is deliberate and consistent
   with the user's requested variety.
3. Identify the product-specific capability that earns the send. If a generic
   chatbot could deliver the same pitch unchanged, find stronger material.
4. Give each sentence a job: motivate, substantiate, clarify the mechanism or offer,
   contribute relevant personality, or enable the action. Cut sentences that merely
   coach the reader through an obvious review/share process or restate the moral.
5. Use human edits to distinguish useful detail from padding. Added consequences,
   concrete objects, and observed humor may justify more words. Do not optimize
   length by deleting the product's payoff or the author's personality.

Preserve the reviewed human copy. Apply the correction to the next requested unit;
do not silently rewrite the whole campaign or claim successful transfer before the
human has reviewed that fresh unit.

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
- The cited proof and claim sources the copy relies on, when it makes factual or product
  claims.
- The intended reader response and any next action the copy asks for.

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

For an explicit benchmark, requested measurement, or active learning run, load
`references/scorecard.md`. An ordinary draft or clean handoff does not require a scorecard
or a new baseline. The primary metric is material revision rounds per
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
- `foundation/marketing-os/references/collaboration.md` (substantial creative decisions)
- `foundation/marketing-os/references/learning-loop.md` (meaningful learning evidence)
- `foundation/marketing-os/references/knowledge-boundaries.md` (durable promotion)
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
- Social strategy, opening choice, memes, product explanation, feed range, and learning
  from edits → `references/social-learning.md`
- `@every` posts and employee repost copy for the Every account →
  `brand-voice/every-master/references/social-copywriting.md`
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
- [ ] Did the reader payoff and creative approach shape the draft, with friction, proof,
      and action included when the copy job needs them?
- [ ] Was one useful reviewer selected, with no imitation or default panel?
- [ ] Does the opening earn attention and the rest deliver on it without generic explanation?
- [ ] Is the human-edited version canonical?
- [ ] Did the final delta preserve user cuts and resolve the rejected decision?
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
- [ ] For social work, does each post have a reason to exist without forcing every post
      into the same opening, proof structure, product lesson, or CTA?
