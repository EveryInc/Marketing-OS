---
name: x-post
description: Draft brand posts and threads for X with a distinct idea, platform-fit proof, and an action matched to the post's job.
---

# Social — X Post

Writes posts for X (Twitter) for launches, engagement, and brand presence.

## When to invoke

- When drafting an X post or thread for a launch or announcement
- When a launch skill orchestrates channel execution and needs the X deliverable
- When writing standalone X content or threads for a brand

## Dependencies

- `foundation/marketing-os`
- `brand-voice/{relevant brand}` (loaded dynamically)
- `positioning/{relevant brand}` (loaded dynamically)
- `craft/copywriting`
- `craft/editing`

Brand is resolved dynamically based on what invokes this skill.

## Pre-draft viability gate

Before writing or revising a post, recover the current campaign state: publishing
account, approved language, adjacent posts, the post's job, intended action, destination,
and available media. Then make a clear **keep / reframe / kill** judgment on the underlying
idea. A content bucket organizes the calendar after an idea earns its place; it is not a
premise worth publishing by itself.

For an idea that survives, settle these points before line editing:

1. Who the post is for, what they believe now, and the one belief, feeling, or action the
   post should create.
2. The specific moment, fact, joke, or argument that gives a reader a reason to care.
3. The exact role of the media: deliver the joke, demonstrate the result, or supply proof.
4. The verified names, handles, product facts, integrations, links, and, for a product
   demonstration, the request, action, and result.
5. Whether the post needs a CTA. When conversion is the job, confirm the destination and
   build the next step into the post instead of appending it after review.

Do not rescue a weak premise with cadence, parallel examples, a generic question, or a
polished closing line. One strong moment usually beats a roundup of weaker moments. The
post must make sense without an unexplained reply, carousel, or asset; the media should
make the same idea more vivid.

When collaborating one post at a time, lead with the strategic verdict, then provide one
recommended post and its media direction. Do not produce a menu of rewrites unless the
user asks for alternatives.

## Channel-specific notes

- Read `craft/compound-copywriting/references/social-learning.md` before drafting a
  related run of posts or carrying human edits into the next post. Run the relevant
  manual checks in `craft/compound-copywriting/evals/social-edit-regressions.json`
  before delivery.
- Read `craft/copywriting/references/channel-adaptation.md` for social and measurement,
  and `craft/copywriting/references/formats.md` for hooks.
- Establish the intended account and format. Verify its current length and media limits;
  do not assume every post has the same cap or that longer means more effective.
- A post should carry one intelligible idea, proof, or observation. Use a thread when
  progression earns it, with each part contributing rather than repeating the opener.
- Preserve the brand's voice and supplied language. Do not compress away the detail that
  lets a new reader understand the claim.
- For an action-oriented post, deliver value in the post and make the next step clear.
  For brand or discussion work, do not force a sales CTA or manufacture engagement bait.
- When effort compression is the emotional proof, name the human steps the job normally
  requires before revealing the shorter agent path. Use steps inherent to the task; do
  not invent a company's former process.
- Adjacent posts may use the same proof only when they do different jobs. A proof post
  dramatizes the result. A follow-up teaching post gives the input, exact prompt,
  guardrails, review step, and finished output.
- When public copy names a teammate with an active public handle, verify and tag the
  handle. The tag strengthens attribution and gives the post a natural distribution
  path. Never guess a handle. Do not tag the account publishing the post; use the product
  or company name in the copy instead.
