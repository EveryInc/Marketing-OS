# Copywriting

Every's general copywriting skill. Writes original marketing copy grounded in whichever
brand-voice and positioning are loaded dynamically at invocation. This is the workhorse
craft skill — channel-specific skills (launch-email, linkedin-post, etc.) handle format,
but copywriting handles the fundamentals of writing well for brands.

The principles here synthesize the creative canon (Ogilvy, Bernbach, Wieden, and others
from marketing-os) into operational writing guidance. The skill adapts to format and
channel but the core craft is consistent.

## System

Copywriting is composed of four reference files:

### references/principles.md
The copywriting principles we hold — synthesized from the creative canon in marketing-os.
The non-negotiable standards for how Every writes.

### references/formats.md
Format guidance — long vs. short, headline vs. body, manifesto vs. product copy. How
format shapes the writing, and how to choose the right format for the job.

### references/channel-adaptation.md
How copy changes by channel. The same message written for email, LinkedIn, X, web, and
press operates differently. This reference governs those adaptations.

### references/antipatterns.md
What not to do. AI tropes, cliché, LinkedIn-voice, hollow superlatives, and the specific
failure modes that make marketing copy generic or untrustworthy.

## When to invoke

- When drafting net-new copy for any brand or product
- When a channel-specific skill isn't the right fit (multi-format, unusual deliverable)
- When writing copy that spans multiple channels or formats
- When a draft needs to be written from scratch rather than edited
- When the task is "write this" rather than "fix this" (editing) or "name this" (naming)

## Reference routing

| Task type | Load |
|---|---|
| Core writing standards and principles | `references/principles.md` |
| Choosing or adapting to a format | `references/formats.md` |
| Adapting copy across channels | `references/channel-adaptation.md` |
| Reviewing for failure modes | `references/antipatterns.md` |

## Dependencies

- `foundation/marketing-os`
- `brand-voice/{relevant brand}` (loaded dynamically)
- `positioning/{relevant brand}` (loaded dynamically)

## Status

Reference skeletons are in place. Principles and antipatterns will be populated first;
format and channel guidance will follow.
