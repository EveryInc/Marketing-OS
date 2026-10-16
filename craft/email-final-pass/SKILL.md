---
name: email-final-pass
description: Audit an entire Every email campaign before final edits. Review current strategy, Notion and Slack decisions, reviewer comments, Kit performance, copy, cadence, and assets; return no more than 10 recommendations and interview Douglas before applying approved changes.
---

# Email Final Pass

Make the campaign more persuasive, useful, and likely to convert. Review the whole
recipient experience before polishing individual sentences. Keep recommendations
short, professional, specific, and candid about uncertainty.

Use for a campaign-wide final pass, launch email review, or conversion audit. For
a single line edit, use Compound Copywriting without this full workflow.

## Approval rule

**Review → up to 10 recommendations → interview → approved edits → verification.**

This review-first sequence applies when changes are not yet authorized. An explicit
user instruction to apply changes, including approval from an earlier turn, is sufficient
for that scope. Do not repeat an interview or request the same approval again.

Without that authorization, do not edit the campaign, add comments, generate replacement assets, change Kit,
or alter send schedules during review. This rule also applies to obvious fixes
and reviewer requests. For proposed changes outside existing authorization, interview about each kind of
change before applying it. Reading a comment is not permission to implement it.

## 1. Load the working rules

- Use Every Marketing OS to locate the current strategy, brand, product, audience,
  and campaign sources. Read its required core and task-specific references.
- Read Compound Copywriting, its `../compound-copywriting/references/email-learning.md`, the applicable
  email voice patterns, and `../compound-copywriting/evals/email-edit-regressions.json`. Load its headline
  and copywriting references when proposing new language.
- Use Compound Engineering's `ce-work` knowledge-work guidance for source checks,
  bounded execution, and verification. The plan here is review-only until approval;
  do not initiate a code pipeline, commit, or publishing workflow.
- Apply Every Style and AI Check to recommendations and proposed copy. The user's
  latest instructions and approved language take precedence over general advice.

If a dependency is unavailable, name the gap and use the available rules. Do not
claim a tool, review, or benchmark ran merely because its instructions were read.

## 2. Recover the current campaign

Identify the canonical document and exact tab or section. Read every email,
audience rule, trigger, send date, asset, and reviewer thread in scope. Inspect
human edits and previous versions where available; protect deliberate cuts,
approved subjects, humor, and the user's formatting.

Search relevant Notion and Slack material for current decisions, meeting notes,
launch workbacks, product facts, pricing, customer language, and better workflow
examples. Follow links to the underlying discussion. Favor current owner decisions
over an older draft; flag unresolved conflicts instead of choosing silently.

Track all reviewer comments, particularly Brandon's when he is a reviewer:
already satisfied, proposed change, disagreement requiring a decision, or missing
information. Do not overlook a comment because it is inconvenient. Keep comments
intact throughout the work, including after implementation.

Keep source links, versions, the campaign inventory, and comment coverage in the
project's working record. Campaign-specific facts do not belong in this skill.

## 3. Establish what converts for Every

Read [the review method](references/review-method.md) in full before research.
Inspect Kit read-only through available tools or the authenticated interface.
Review comparable strong, typical, and weak sends, actual sent copy, A/B variants,
recipient segments, reporting windows, and scheduled broadcasts and sequences.

Define the intended action for each audience: paid subscription, installation,
first completed job, or continued use. Read attributed outcomes when available.
Compare delivered counts, unique clicks, conversions, and unsubscribes. Treat open
rates as a diagnostic; an open-rate winner is not a subscription winner.

Explain patterns with specific examples: which headline, promise, story, CTA,
offer, or asset performed better, for whom, on which metric, in which test.
Historical comparisons suggest a hypothesis; a controlled test supports a stronger
claim. Do not invent results, assume causation, or call external examples proven.

If Kit data is unavailable, request the smallest useful export and continue the
source and copy review. Mark performance claims as unmeasured. Check current
primary-source guidance on testing and email design; study competitive emails for
creative approaches, without treating inclusion in a gallery as conversion data.
Use Jev if available for comparison or research, never as a substitute for results.

## 4. Review the campaign as a whole

Check these before making sentence-level changes:

- **Strategy and audience:** Does the campaign explain the product's distinctive
  benefit early enough? Does each send offer a fresh reason to act? Do existing
  users and paid members get suitable content and CTAs? Does the offer match the
  website, sales language, and current product decisions?
- **Sequence and timing:** What will a recipient receive across this campaign,
  editorial broadcasts, education sends, and onboarding? Check entry rules,
  suppressions, exits after conversion, overlaps, and time zones. Recommend a
  specific spacing change only after inspecting that combined experience.
- **Copy:** Does the subject earn attention and match the body? Do preview text
  and the opening add something? Is the benefit clear, the language specific,
  and the next step easy? Follow the current brief for CTA placement. Cut padding
  and repetition without removing ideas, personality, or necessary context.
- **Examples:** Check variety across the emails a person will receive. Prefer
  consequential, relevant workflows over filler. Identify the request, action,
  and result. Keep a proposed workflow distinct from a completed customer story.
- **Assets:** Inspect the assets themselves and the current brand design source.
  Choose a demo, miniature guide, finished output, testimonial, or no image to
  serve the email's purpose. Check mobile reading, animation pace, first-frame
  fallback, load size, contrast, alt text, and CTA visibility. Asset variety is
  useful when it improves the experience; it is not a quota.

For a recommended asset change, specify the format, content, placement, and
reason. Reuse an existing asset when it fits. Recommend production separately;
do not create or replace it during review.

## 5. Challenge each recommendation

Before retaining a change, answer privately:

1. Why should this change help the intended reader take the intended action?
2. What is the strongest argument for keeping the current version?
3. What assumption could make the recommendation wrong? What result would change
   the recommendation?

Steelman both options. Also examine the weakest link in your own reasoning; do
not substitute a deliberately weak objection for a serious check. Remove changes
based only on personal preference, generic rules, or restoring rejected copy.

Use **high**, **medium**, or **low** confidence. High means the evidence supports
the specific recommendation; it does not guarantee a future conversion lift.
For untested copy or design choices, state the hypothesis and propose a practical
test when audience size, timing, and instrumentation allow it.

## 6. Deliver no more than 10 recommendations

Start with a brief verdict. Then give a numbered list, highest impact first.
Each item names the affected email or segment, the exact change, why it matters,
a linked source or test, and confidence. Include proposed language when useful.
For test recommendations, name the two alternatives and the deciding metric.

Use this compact pattern:

> 1. Change [specific thing] in [email/segment]. [Proposed edit or asset direction.]
>    Why: [reader benefit and supporting evidence]. Confidence: [level; uncertainty].

Group related changes so the list stays within 10. Do not pad the list to 10 or
bury a material problem to meet the limit. Add one short source-coverage line
stating what was reviewed, any missing data, and unresolved reviewer questions.
Avoid a second list of disguised recommendations or a long audit appendix.

## 7. Interview before applying

Discuss one category at a time, starting with the largest consequence: audience
and cadence, promise and offer, subjects and hooks, examples, or assets. Use only
the categories the recommendations need.

For each category, show the relevant recommendation numbers and proposed changes.
Ask Douglas to approve, adjust, or keep the current version. Wait for his answer.
Track approval by recommendation and scope. Approval of one category does not
approve the others; general praise does not authorize edits. If he requests a new
direction, revise the proposal and confirm it before implementation.

## 8. Apply and verify approved changes

After the interview, apply only the agreed changes to the agreed document.
Re-read the current version first. If intervening edits materially change the
proposal, bring the difference back to Douglas. Keep a recoverable before-state.

Preserve native formatting, reviewer comments, audience metadata, links, and
unrelated sections. Do not delete or resolve comments. Approval to edit the
document does not authorize publishing, Kit changes, scheduling, or sending.
Asset creation requires approval of its brief as well as the production action.

Re-read the result and compare it with the approved scope. Inspect rendered
formatting when available. Verify links, offer terms, segment variants, assets,
and the retained comments. Report what changed and why, what stayed unchanged,
and anything still blocked. Do not claim improved conversion before measurement.

Capture accepted, reusable email craft and later test results in **Compound
Copywriting's email section**, not Compound Writing. Keep campaign facts in the
campaign record. Check [the regression cases](evals/cases.json) when changing this
skill's review, evidence, or approval rules.
