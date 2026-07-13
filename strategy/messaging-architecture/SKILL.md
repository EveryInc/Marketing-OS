# Messaging Architecture

Builds the foundational messaging document that a brand or launch operates from. A
messaging architecture translates positioning into a structured hierarchy of messages —
from tagline through value propositions through proof points — that every downstream
channel and craft skill can draw on.

This is the bridge between strategy and execution. Positioning says what the brand stands
for; messaging architecture says what we actually say about it, to whom, and in what order
of priority.

> Cross-reference: when writing an actual audience-facing messaging doc, the canonical
> per-target section format — WHO · PAIN · MOTIVATION · HOW WE SOLVE IT · THE COMPETITION ·
> WHY US · WHERE — lives in `marketing-science/messaging/references/audience-section-schema.md`.
> It operationalizes the audience-proposition matrix below at the section level; it does not
> replace it.

## System

Messaging architecture is composed of four reference files:

### references/message-house.md
The structure we use — the message house format that organizes top-level narrative,
pillars, supporting messages, and proof points into a single, navigable document.

### references/audience-proposition-matrix.md
How we map messages to audiences. Different audiences need different emphasis — this
matrix governs which propositions lead for which audience segments.

### references/pillar-development.md
How we develop messaging pillars — the 3-5 core themes that a brand's messaging
organizes around. Covers pillar identification, prioritization, and substantiation.

### references/channel-cascade.md
How top-level messages cascade to channel. The same pillar expressed as a headline, a
LinkedIn post, a product page section, and an email subject line. Governs translation
from architecture to execution.

## When to invoke

- When creating a messaging framework for a product launch
- When aligning cross-functional teams on what to say and how to say it
- When a launch skill needs messaging scaffolding before channel execution
- When building a message house for a new or repositioned brand
- When cascading a messaging framework into channel-specific deliverables

## Reference routing

| Task type | Load |
|---|---|
| Building the message house structure | `references/message-house.md` |
| Mapping messages to audience segments | `references/audience-proposition-matrix.md` |
| Developing or refining messaging pillars | `references/pillar-development.md` |
| Translating architecture to channel execution | `references/channel-cascade.md` |

## Dependencies

- `foundation/marketing-os`
- `positioning/{relevant product}` (loaded dynamically)
- `brand-voice/{relevant product}` (loaded dynamically)

## Status

Reference skeletons are in place. Message house structure and pillar development will be
populated first; audience-proposition matrix and channel cascade will follow.
