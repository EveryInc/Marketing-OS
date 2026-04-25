# Churned User Email

This skill produces win-back emails for two distinct lapsed-user populations, which behave differently and require different treatment:

1. **Paid cancellation churn.** They had a paid subscription. They canceled. They may still be on the free list, or fully unsubscribed.
2. **Free engagement churn.** They're on the list, never paid, and haven't opened anything in 60-90+ days.

The skill encodes Every's voice applied to evidence-based win-back patterns. Industry baseline: average win-back campaigns recover ~26% of churned subscribers, recovered subscribers tend to be worth roughly 2x newly acquired ones, and 2-5 email laddered sequences outperform single sends. The standard "we miss you 😢" template is banned.

## When to invoke

- When reaching out to paid subscribers who have canceled their subscription
- When re-engaging free subscribers who haven't opened in 60-90+ days
- When building a win-back sequence triggered by a meaningful product change
- When a feature or product launch creates a natural re-engagement moment
- When the brief mentions "win back," "winback," "churn," "churned," "re-engage," "reactivation," "canceled," "lapsed," "inactive," "stopped opening," or "come back"
- When correcting a brief that uses "we miss you" as the proposed opener

## Audience model

A churned user is someone who *already heard your pitch and walked away*. The first job of a win-back is to acknowledge that without flinching, then say something *new* — ideally that something has changed since they left.

Mental model: write to a former colleague who said the company wasn't right for them. You wouldn't beg. You wouldn't pretend the breakup didn't happen. You'd send them an interesting update if there was one, or quietly leave them alone.

## The cardinal rule of win-back

**Lead with what changed.** Not with what you miss, not with a discount, not with a feature dump.

If nothing has changed since they left, don't send a win-back email. Send the editorial newsletter and let them re-discover Every organically. The win-back has to earn the second look.

What counts as "what changed":
- A new product or product capability that addresses what they cited as missing
- A new editorial thread that's substantially different from what was being published when they left
- A pricing change (lower, simpler, or a new tier that fits a use case theirs didn't)
- A partnership or perk that materially expands what membership includes
- A platform-level shift that makes Every's coverage newly relevant (model release, regulatory event, etc.)

If the brief asking for a win-back doesn't include a "what changed" element, push back on the brief before drafting. The skill should refuse to write empty win-back copy.

## Segment the win-back by exit reason

If you have exit-survey data (which Every should be capturing on cancellation), segment the sequence by reason. Generic win-backs convert at <5%. Reason-matched win-backs convert in the 15-30% range.

| Exit reason | Lead with | Don't lead with |
|---|---|---|
| Price | New tier, lower price point, lifetime option, annual discount | A feature list |
| Not enough value / didn't use it | New products unlocked, easier on-ramps, "here's how members actually use it" | Generic discount |
| Missing feature | The feature, now built | "We've grown so much" |
| Wrong fit / not relevant anymore | The new editorial thread, a pivot in coverage area | A "we miss you" |
| Bug or experience problem | The fix, named explicitly | An apology paragraph |
| No reason given / didn't fill out survey | A genuinely new thing (product, tier, editorial) | Default to "we miss you" template |

If you don't have the data: send a multi-email sequence that varies the angle across emails so different reasons land for different recipients.

## Voice — house rules adapted for win-back

Same Every house voice (see current-subscriber skill for the foundation). Specific adjustments:

- **No emotional appeals.** Banned: "We miss you," "It's been too long," "Our inbox isn't the same," "You belong here." All of this is the LinkedIn breakup-letter genre. Every does not write this way.
- **Acknowledge the gap factually.** "It's been a few months since you've opened one of our sends" is fine. "We noticed your subscription ended in March" is fine. State, don't emote.
- **No reproach.** Don't make the reader feel guilty for leaving. This isn't a guilt economy.
- **Brief is better.** Win-back emails should be *shorter* than acquisition emails, not longer. The reader's attention is already on a spectrum from neutral to negative.
- **One ask.** Never stack a win-back ask with a survey ask with a "follow us on social" ask. Pick the highest-leverage single action.

## The 4-email standard sequence (paid cancellation)

Four emails, spaced over 21-28 days. Adjust to 2-3 if the cancellation reason was "no longer needed" — those people respond worse to longer sequences.

### Email 1: The "What Changed" send (Day 3 after cancellation)

The lead. State the gap factually. Lead with the substantive change.

**Subject:** A specific, true claim about the change. Not a tease.
- Good: "Spiral now writes in your voice — without the prompt"
- Good: "A new $99 individual tier"
- Good: "You asked for a longer archive. It's here."
- Bad: "We miss you"
- Bad: "Come back!"
- Bad: "It's been a while..."

**Body skeleton:**
1. Greeting. ("Hi Douglas,")
2. One sentence of factual acknowledgment. ("Your subscription ended a few weeks ago.")
3. *What changed* — the substantive update, in one paragraph.
4. Why it matters for someone with their use case (if known) or for the general member.
5. Single CTA — usually back to the article/product page that demonstrates the change. Not "Resubscribe."
6. Sign-off, no urgency.

Length: 100-180 words.

### Email 2: The proof send (Day 10)

If they didn't open or didn't act on email 1, send proof. Real users, real outcomes, real numbers.

**Subject:**
- "How [named member] uses [the new thing]"
- "200+ members now run their writing through Spiral"
- "Three weeks of Vibe Checks since you left"

**Body skeleton:**
1. Greeting.
2. *Concrete usage data or named-user story* — one paragraph. Specifics matter ("Mike Krieger, CPO at Anthropic, says..." beats "members love this").
3. Optional: a 2-3 line pull from a recent paid-only piece, with a "you can read this if you come back" framing.
4. Single CTA.
5. Sign-off.

Length: 120-180 words.

### Email 3: The offer send (Day 17, only if relevant)

Skip this email if the cancellation reason wasn't price. If it was, this is the moment.

**Subject:** Direct, terms-forward.
- "Annual at $149 (your old price was $200)"
- "A welcome-back month at $1"
- "Lifetime access for $499 — through Friday"

**Body skeleton:**
1. Greeting.
2. *Acknowledge the price thing*. ("You mentioned price when you canceled.") If you don't have that data, don't fake it — write the offer directly.
3. *State the offer* — specific number, specific terms, specific deadline.
4. Brief reminder of what they get for it. Two-three lines max.
5. CTA.
6. Sign-off.

Length: 80-130 words. The offer should do the work.

**Important:** the offer must have a real deadline and the deadline must be honored. Fake countdown timers and "extending for one more day" emails destroy trust faster than the original cancellation.

### Email 4: The permission send (Day 28)

The "we'll stop emailing you" closer. This sounds like a loss but is actually one of the highest-converting emails in any win-back sequence — and it cleans the list of people who genuinely don't want to hear from you.

**Subject:**
- "Should we stop emailing?"
- "One quick yes-or-no"
- "Last note from Every"

**Body skeleton:**
1. Greeting.
2. *Honest framing*. "We've sent a few emails since you canceled and haven't heard back. We don't want to keep emailing if you're not interested."
3. *Two clear paths* — either reactivate (one link) or unsubscribe (one link) or stay subscribed to free-tier editorial only (one link).
4. Sign-off.

Length: 60-100 words. This is the shortest email in the sequence. Brevity reads as respect.

## The 2-email engagement-winback (free, dormant)

For free subscribers who haven't opened in 60-90 days. They never paid, so the stakes are different — the goal is either re-engagement or hygiene.

### Email 1: The strongest piece (Day 60 of inactivity)

Send the single best editorial Every has published in the last 90 days, with a brief framing line at top.

**Subject:** The piece's actual subject line, possibly with a "[ICYMI]" prefix if appropriate.

**Body:** A 2-3 line lead-in noting that this is one of the most-read pieces this quarter, then the article tease and link as if it were a normal newsletter shell.

Length: 100-150 words.

### Email 2: The permission send (Day 90)

Same as Email 4 in the paid sequence above. "Should we stop emailing?"

## Length budget

| Email type | Word count target |
|---|---|
| Email 1: What Changed | 100-180 |
| Email 2: Proof | 120-180 |
| Email 3: Offer | 80-130 |
| Email 4: Permission | 60-100 |
| Free dormant: Best piece | 100-150 |

## Worked example: Email 1 (What Changed) for a paid canceler

**Context:** Member canceled annual subscription 3 weeks ago. Cited "didn't use the AI tools enough" in exit survey. Since then, Every has launched Monologue Notes, which addresses the no-product-stickiness complaint by linking voice memos directly into agent workflows.

**Subject:** Monologue Notes turns voice memos into agent context

> Hi Douglas,
>
> Your Every subscription ended a few weeks ago. We thought you'd want to know about something we shipped since.
>
> Monologue Notes records meetings, calls, and voice memos and turns them into searchable context for your AI agents — the missing layer between thinking out loud and getting an agent to act on what you said. It's the kind of tool that becomes useful the moment you start using it for the second time.
>
> If part of why you stepped away was that the AI tools didn't fit naturally into your workflow, this one might.
>
> `--→Try Monologue Notes`
>
> —The Every team

**Why this works:**
- Acknowledges the cancellation factually. No emotional charge.
- Leads with the new product, named, with one-sentence positioning.
- Connects directly to the cited exit reason ("if part of why you stepped away...") without being heavy-handed about it.
- Single CTA goes to the *product*, not to the resubscribe page. The product is the case for resubscription.
- 110 words.

## Worked example: Email 4 (Permission send)

**Subject:** Should we stop emailing?

> Hi Douglas,
>
> We've sent a few emails since your subscription ended and haven't heard back. We don't want to keep showing up in your inbox if you'd rather not hear from us.
>
> Three options:
>
> * `--→Resubscribe` if you'd like to come back.
> * `--→Stay on the free list` if you want to keep getting our daily editorial but not paid content.
> * `--→Unsubscribe` if you'd rather not hear from us at all. We won't be offended.
>
> —The Every team

**Why this works:**
- Three clear paths, no manipulation. The unsubscribe option is presented as legitimate.
- "We won't be offended" deflates the manipulation that win-back emails usually try to weaponize.
- Brief. The reader makes one decision and moves on.
- 80 words.

## Anti-patterns — never do these

1. **The "we miss you" subject line.** Banned in every variation: "We miss you," "It's been a while," "Did we lose you?", "Where'd you go?", anything with a sad face emoji. This is the genre marker of bad win-back. Every doesn't write this way.

2. **Generic discounts as the lead.** A 10% off email to a churned subscriber who canceled because they didn't find the product useful is insulting. The discount lands only when price was the actual exit reason.

3. **Guilt or reproach.** "We've been working hard on..." "After all we've built together..." Cut.

4. **Stacked pitches.** Don't send a win-back that pitches the product, the camp, the podcast, the community, and the discount in one email. Pick one angle per email; spread across the sequence.

5. **Fake personalization.** "Dear [first_name], we noticed *you specifically* haven't been around..." If the personalization is shallow, drop it. "Hi Douglas, your subscription ended in March" is real personalization. "We've been thinking about *you* lately, Douglas" is fake.

6. **Indefinite sequences.** Win-back is a finite thing. Four emails for paid cancellations, two for free dormants. Then stop. People who don't respond after a permission send should have their hygiene status updated and be removed from active marketing.

7. **The "extension" trick.** "Our offer was supposed to end yesterday but we're extending it just for you!" Nobody believes this. It signals desperation and trains future skepticism.

8. **No real deadline on offers.** Either the offer has a real end date (and is honored), or there's no deadline and no urgency framing. Pick one.

9. **Re-pitching the original product unchanged.** If literally nothing has changed since they left, don't send a win-back. The whole point is the change.

10. **Treating canceled-paid the same as never-paid.** These are different audiences with different exit emotions. Don't merge them in one sequence.

## Operational notes

- **Trigger timing:** Day 3 after cancellation is ideal for Email 1. Earlier feels stalker-y, later loses warmth. Free engagement winback fires at 60 days inactive.
- **Suppression rules:** Anyone who has explicitly unsubscribed should never receive win-back. Anyone who's resubscribed mid-sequence should immediately exit the sequence. Anyone who responds to email 1 or 2 with reactivation should not receive emails 3 or 4.
- **Sender:** From `hello@every.to` for editorial-led win-backs. Consider `dan@every.to` for the highest-stakes version (premium tier cancellations) — but only if the body genuinely warrants founder voice.
- **Measurement:** Win-back rate (reactivations / canceled cohort) is the headline metric. Secondary: revenue from reactivations, time-to-reactivation, and unsubscribe rate of email 4 (high unsubscribe on the permission send is *good* — the list gets cleaner).

## Dependencies

- `foundation/marketing-os`
- `brand-voice/{relevant brand}` (loaded dynamically)
- `positioning/{relevant brand}` (loaded dynamically)
- `craft/copywriting`
- `craft/editing`

## Quick checklist before sending to review

- [ ] There is a *real, specific* "what changed" element this email is communicating
- [ ] No "we miss you" or sad-emoji opener
- [ ] Acknowledgment of the gap is factual, not emotional
- [ ] Discount/offer is only present if price was the exit reason (or if this is Email 3 for unknown-reason segment)
- [ ] One CTA per email
- [ ] Length is at or below the budget for this email's role in the sequence
- [ ] Sequence has a defined end (no indefinite re-engagement)
- [ ] Permission send is included in the plan, with three honest paths
