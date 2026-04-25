# Feature Launch

Orchestrates a launch for a new product feature — the mid-tier launch. For meaningful
new capabilities that warrant a coordinated multi-channel campaign.

## When to invoke

- When shipping a new feature for an existing product
- When the feature is significant enough to warrant a coordinated campaign
- When coordinating a multi-channel announcement for a new capability

## Launch narrative

At feature tier, the launch narrative is a required upstream input that bridges the
feature announcement to the product's established narrative. It is shorter than
new-product launch narrative but more developed than an improvement brief — typically a
single document of one to two pages that the channel lead drafts before asset production
begins.

A new feature may expand what the product is understood to do, or confirm what it was
always understood to do better. The launch narrative specifies which of these is true and
why it matters. It answers: what tension does this feature resolve for the user, and why
is now the right moment to ship it? It does not require the full why-now/why-us/why-this
treatment of a new-product launch — the product's credibility is established — but it
does require a clear account of the user problem and why this feature addresses it well.

Every channel asset traces back to the launch narrative. If a channel asset cannot be
derived from the narrative, revise the asset before revising the narrative.

## References

### references/cadence.md
Pre-launch sequencing, launch day choreography, and post-launch follow-through for
feature tier. More extended than improvement; shorter than new-product. Typically runs
T-30 through T+14.

### references/pre-launch-checklist.md
What must be true before a feature launch can proceed. Asset readiness, message
alignment, distribution readiness, product page update, internal alignment, and the
final go/no-go checkpoint.

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

A feature launch coordinates the following channel skills:

- `craft/email/current-subscriber`
- `craft/email/paid-user`
- `craft/email/churned-user`
- `craft/social/linkedin-post`
- `craft/social/x-post`
- `craft/social/threads-post`
- `craft/web/product-page`
