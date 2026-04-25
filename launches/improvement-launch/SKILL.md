# Improvement Launch

Orchestrates a launch for a product improvement — the lightest launch tier. For small
quality-of-life updates that warrant external communication but don't rise to the level
of a new feature.

## When to invoke

- When shipping a meaningful improvement to an existing product
- When the update warrants external communication but isn't a new feature
- When coordinating a multi-channel announcement for a product refinement

## Launch narrative

At improvement tier, the launch narrative is a required upstream input but it is not a
standalone document. It is a short orienting paragraph — written before any channel asset
is drafted — that explains why this improvement matters now and how it connects to the
product's established story.

The surrounding product narrative already exists. The improvement narrative does not
rebuild it; it situates the change within it. The question it answers: why does this
matter to the people already using this product? The answer should be legible from the
user's experience, not from the engineering decision. Write the narrative first. Every
channel asset drafts from it.

## References

### references/cadence.md
Pre-launch sequencing, launch day choreography, and post-launch follow-through for
improvement tier. Compressed relative to feature and new-product launches; fewer assets,
shorter lead time, tighter coordination window.

### references/pre-launch-checklist.md
What must be true before an improvement launch can proceed. Asset readiness, message
alignment, distribution readiness, internal alignment, and the final go/no-go checkpoint.

## Reference routing

| Task type | Load |
|---|---|
| Timing, sequencing, and day-of choreography | `references/cadence.md` |
| Pre-launch readiness check | `references/pre-launch-checklist.md` |

## Dependencies

- `foundation/marketing-os`
- `positioning/{relevant product}` (loaded dynamically)
- `brand-voice/{relevant product}` (loaded dynamically)
- `strategy/messaging-architecture`

## Orchestrated craft skills

An improvement launch coordinates the following channel skills:

- `craft/email/current-subscriber`
- `craft/email/paid-user`
- `craft/social/linkedin-post`
- `craft/social/x-post`
