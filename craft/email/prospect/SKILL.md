---
name: prospect-email
description: Draft cold or warm prospect email around relevant audience motivation, verified proof, and one appropriate next action.
---

# Email — Prospect

Writes emails to prospects who haven't yet subscribed — cold outreach, partnership pitches, and acquisition communications.

## When to invoke

- When reaching prospects outside the existing subscriber base
- When a new-product launch needs cold or warm acquisition email
- When building outreach sequences for partnerships or co-marketing

## Dependencies

- `foundation/marketing-os`
- `brand-voice/{relevant brand}` (loaded dynamically)
- `positioning/{relevant brand}` (loaded dynamically)
- `craft/copywriting`
- `craft/editing`

Brand is resolved dynamically based on what invokes this skill.

## Write the email

Read `craft/copywriting/references/principles.md`, `formats.md`, and
`channel-adaptation.md` before the first draft. Resolve whether the contact is cold,
introduced, a partner, or an opted-in prospect; do not assume familiarity or invent a
relationship. For personal outreach on behalf of Every, also use the installed
`marketing-outreach-emails` skill.

- Establish the reader's relevant situation and reason to care early. A cold reader
  needs more orientation than someone who requested product news.
- Make subject and preview earn an appropriate open, then pay off their promise in the
  body. The subject cannot establish success by itself.
- Give the proposition one concrete proof point, with enough context to understand what
  happened and why it matters. Identify internal demonstrations as internal.
- Choose the smallest useful next action for the relationship and offer: a reply,
  introduction, demonstration, or trial. Do not force every prospect into the same ask.
- Personalize using relevant, sourced context. Avoid invented familiarity, false reply
  subjects, decorative flattery, and a list of facts about the recipient with no bearing
  on the proposition.
- State material trial, price, eligibility, and follow-up conditions. Resolve objections
  with facts rather than invented urgency or promises.
- Keep one primary action. Remove paragraphs that restate proof, repeat the invitation,
  or explain a benefit the reader already understands.

## Sequences and measurement

Use the approved entry, timing, suppression, and exit conditions. A subsequent email
should introduce relevant proof or address an unfinished decision. Stop the sequence when
its goal is met or the recipient opts out; a generic cadence is not authority to send.

Define success through the intended response, such as qualified replies or activations,
with the eligible or delivered denominator and measurement window. Use opens and raw
clicks cautiously as diagnostics. Apply the testing rules in channel adaptation.

Deliver a reviewable draft. Drafting does not authorize sending, scheduling, or publishing.
