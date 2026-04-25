# Transactional Email

Transactional emails exist for utility. They confirm an action, deliver a credential, or notify of a system event. They are *not* marketing emails wearing a uniform. The single biggest failure mode in this category is treating transactional sends as a chance to upsell — it tanks deliverability, dilutes the user's trust in your auth flow, and in some jurisdictions creates compliance issues (CAN-SPAM, GDPR-PECR) by mixing transactional and marketing content under the wrong consent basis.

Every's transactional emails should feel like the system itself talking: brief, accurate, and bored.

## When to invoke

- When writing login links, magic links, or password reset emails
- When writing email verification, payment confirmations, or receipts
- When drafting subscription start, cancel, or renewal notices
- When writing payment failure notifications, plan-change confirmations, or security alerts
- When writing trial-status notifications for any Every product (Cora, Spiral, Sparkle, Monologue)
- When the email is triggered by a specific user action or system event and exists for utility or confirmation rather than marketing
- When the brief mentions "login link," "magic link," "password reset," "verification email," "receipt," "payment confirmation," "trial ending," "subscription canceled," "transactional," "system email," "noreply," "auth email," or "billing email"

## Audience model

The recipient just clicked a button or had something happen to their account and is now waiting for this email to do exactly one thing. They will spend 2-5 seconds on it. They will be irritated by anything that is not the thing they came for.

Write to that person. Plain, fast, no fanfare.

## Voice — house rules for transactional

Different from editorial / marketing voice. Tighter, more functional, fewer flourishes.

- **Brutal brevity.** Most transactional emails should be under 50 words. Auth emails should be under 30.
- **Subject = the thing inside.** Literally describe what the email contains. "Your login link." "Receipt for your Every annual subscription." "Your Sparkle trial ends in 3 days." Never tease.
- **One thing per email.** One action, one credential, one notification. Never two.
- **No marketing inside auth or billing.** Cross-sells, "while you're here..." links, social-follow CTAs, and product recommendations do not belong in pure transactional sends. (See "Soft transactional" section below for the narrow exception.)
- **Plain-text version must work standalone.** Many users read transactional emails in plain-text mode (security tools, screen readers, etc.). The body must be intelligible without HTML.
- **No "Hi [First Name]" if you don't have a first name.** Either personalize correctly or don't at all. "Hey," with no name is fine.

## Sender address conventions

| Email type | From address |
|---|---|
| Authentication (login, password, verification) | `noreply@every.to` |
| Billing (receipts, subscription state changes) | `billing@every.to` or `noreply@every.to` |
| Product transactional (trial state, app notifications) | `[product]@every.to` (e.g., `sparkle@every.to`, `cora@every.to`) |
| Security alerts | `security@every.to` |

Reply-to: usually unset for `noreply@`. For product transactional from named team members on activation flows, reply-to should route to a real human (Yash, Naveen, etc., as Every already does for Sparkle and Monologue).

## The auth email (login link / magic link / password reset)

The most common transactional email Every sends. Strict skeleton.

**Subject:** "Your login link" / "Reset your password" / "Verify your email address"

**Body:** Brief. Greeting ("Hey,"), one sentence naming what the link does, the button, the fallback URL, link expiration notice. That's it. Word count: ~25-35.

**Rules:**
- Always include the fallback URL. Some email clients break button rendering.
- Always include link expiration. Security and trust signal.
- Never include marketing links or social icons in auth emails.
- Greeting is "Hey," with no name. Auth emails go out before the user has even confirmed their identity in some flows.
- Sign-off is omitted or simply "—Every" if needed for branding.

## The receipt / payment confirmation

**Subject:** "Receipt for your Every annual subscription" / "Payment received: $200.00 to Every"

**Body skeleton:**

1. Greeting ("Hi Douglas,")
2. One-line confirmation of what was paid for. ("Thanks for your annual Every subscription.")
3. Itemized receipt block: amount, payment method (last 4 digits), transaction date, invoice number.
4. One link to manage subscription / view all invoices.
5. Sign-off ("—The Every team")

Length: 60-90 words.

**Rules:**
- Receipts are documentation. Treat them like documentation. People save these for taxes and expense reports.
- Include all the line items a finance team would need without having to log in.
- One link only — to the billing page. No editorial links, no product cross-sells.
- Always state the payment method (last 4 digits) and transaction date.

## The subscription state change (canceled / paused / plan changed)

**Subject:** "Your Every subscription has been canceled" / "Your plan changed to Annual"

**Body skeleton:**

1. Greeting.
2. *State the change factually.* "Your Every annual subscription was canceled on April 25, 2026."
3. *State what it means practically.* "You'll continue to have full access until your current period ends on April 25, 2027. After that, your account will move to the free tier."
4. *State what the user can do.* "If you canceled by mistake or change your mind, you can resubscribe in your account settings at any time."
5. Sign-off.

Length: 70-110 words.

**Rules:**
- Cancellation confirmations are NOT win-back emails. The user just canceled. Respect that. Win-back belongs to a separate flow that fires days later (see the churned-user skill).
- Do not editorialize. "We're sorry to see you go" is acceptable as a brief courtesy line; "We hope you'll reconsider!" is not.
- The factual end-of-access date must be stated explicitly.

## The payment failure / dunning notification

**Subject:** "We couldn't process your payment for Every"

**Body skeleton:**

1. Greeting.
2. *State the issue.* "Your payment of $200.00 for Every annual subscription was declined by your card issuer on April 25."
3. *State the consequence.* "Your subscription is currently in a grace period. We'll retry the payment in 3 days. If it fails again, your subscription will move to the free tier on May 7."
4. *State the action.* `--→Update payment method`
5. Brief sign-off.

Length: 80-120 words.

**Rules:**
- Tone is matter-of-fact. The user didn't necessarily do anything wrong (expired card, fraud hold, etc.) — don't make them feel they did.
- Always state the retry schedule and the consequence date.
- One CTA: update payment method.

## The trial state notification (3 days remaining / today is the last day / trial ended)

**Subject:** "Your Sparkle trial ends in 3 days" / "Your Sparkle trial ended today"

**Body skeleton:**

1. Greeting.
2. *State the timing.* "Your 15-day Sparkle trial ends on April 28."
3. *State what happens at trial end.* "After that, you'll be charged $10/month unless you cancel. You can cancel anytime in the app."
4. Optional: one short value reinforcement line ("In the past 15 days, Sparkle organized 1,247 files for you.") — this is the soft-transactional moment described below.
5. CTA: `--→Manage subscription`
6. Sign-off.

Length: 80-130 words.

## Soft transactional — the narrow exception

Some transactional emails sit at the boundary of utility and marketing. Examples:
- Trial-ending emails (a chance to convert or downgrade)
- Activation emails ("you just signed up — here's how to get started")
- Welcome emails immediately post-purchase ("you made it Sparkle ✨")

These can include *one* light value reinforcement or one optional cross-link, but the email's primary job is still confirmation/utility. The marketing element should be no more than 15-20% of the body.

Reference: Every's actual "You made it Sparkle ✨" email is a model of soft transactional — Yash welcomes, explains what Sparkle is doing in the background, lists 4 utility points the user needs to know, and offers a reply-to-this-email contact. The sole "marketing" beat is a link to FAQ. The primary job remains *informing the user about the state of their account*.

In those cases:
- Sender can be a named human (`yash@every.to`) instead of `noreply@`
- Greeting can include the name
- One short founder/GM intro is allowed ("I'm Yash, the GM of Sparkle.")
- Reply-to should route to that human

But the email is still *not a marketing email*. The user just took an action and the email is responding to it.

## Length budget

| Email type | Word count target |
|---|---|
| Login / magic link / password reset | 20-35 |
| Email verification | 25-40 |
| Payment receipt | 60-90 |
| Subscription state change | 70-110 |
| Payment failure / dunning | 80-120 |
| Trial state notification | 80-130 |
| Soft transactional (welcome/activation) | 150-250 |
| Security alert (new device login) | 60-90 |

## Worked example: Login link (Every's actual format)

**Subject:** Your login link

> Hey,
>
> Here is your link to log in to Every.
>
> `--→Log in`
>
> If you can't click the button, you can copy and paste the following link into your browser:
> https://every.to/verify?hash=...
>
> —Every

**Why this works:**
- Subject names the contents literally.
- 28 words. Reader gets credential, takes action, closes the email.
- Fallback URL handles broken-rendering cases.
- No marketing. No cross-sells. No social icons.

## Worked example: Subscription canceled

**Subject:** Your Every subscription has been canceled

> Hi Douglas,
>
> Your Every annual subscription was canceled on April 25, 2026.
>
> You'll continue to have full access until April 25, 2027. After that, your account will move to the free tier — you'll still receive our daily editorial newsletter, just without paid features (camps, archive, AI tools, private community).
>
> If this was a mistake or you change your mind, you can resubscribe in your account settings.
>
> `--→Manage subscription`
>
> —The Every team

**Why this works:**
- Factual confirmation in the first sentence.
- Specific dates throughout. The user knows exactly what they have and when they lose it.
- Soft acknowledgment that the user keeps the editorial — not framed as a guilt trip, just a fact.
- One CTA, no win-back pressure.
- 80 words.

## Worked example: Payment receipt

**Subject:** Receipt for your Every annual subscription

> Hi Douglas,
>
> Thanks — your Every annual subscription has been renewed.
>
> Every Annual Subscription
> $200.00
> Paid via Visa ending in 1234
> April 25, 2026
> Invoice #EVR-2026-04-25-7841
>
> `--→View all invoices`
>
> —The Every team

**Why this works:**
- Single confirmation line, then receipt block, then a link to billing history.
- Every line item a finance team needs is there.
- 50 words.

## Anti-patterns — never do these

1. **Marketing in auth emails.** Login links must be sterile. No "while you wait, check out this article" links. No social icons. No upsell banners.

2. **Tease subjects on transactional.** "You won't believe what's in your account!" — never. Subject must literally name the contents.

3. **Multi-purpose transactional.** "Your password has been reset. Also, here's our latest newsletter." No. One email, one purpose.

4. **Manufactured warmth in system emails.** "We're SO excited that you logged in!" — no. Login is a routine action. Treat it routinely.

5. **Branding the noreply.** Putting the full Every logo, footer, social links, and editorial preview in a magic link email. Auth emails should be visually minimal — header, body, fallback URL, sign-off. Nothing else.

6. **Hidden important information.** Cancellation date, retry schedule, end-of-grace-period — these must be *stated*, not buried in a footnote or a help link.

7. **Misuse of "noreply" for replyable contexts.** If the user might reasonably want to reply (billing dispute, trial question), the reply-to must route somewhere. `noreply@` is for credential and notification emails where reply doesn't make sense.

8. **Editorial-marketing creep into receipts.** Receipts are documents. Don't add "P.S. Have you read our latest essay on..." to a receipt.

9. **Inconsistent sender addresses.** Auth from `hello@every.to`, receipts from `noreply@every.to`, trial notes from `support@every.to` — confusing and bad for deliverability. Pick a convention (see sender address table above) and hold to it.

10. **The "exciting news!" subject for a routine notification.** "Exciting changes to your account!" for a passive plan change. No. State the change.

## Compliance notes (non-legal-advice baseline)

- Transactional emails generally fall outside marketing-consent requirements (CAN-SPAM, GDPR-PECR), *but only when their primary purpose is genuinely transactional*. The moment marketing content exceeds incidental volume, the email becomes promotional and requires marketing consent.
- The 15-20% guideline for soft transactional is a working rule, not a legal threshold. When in doubt, lean transactional.
- Footer should still include physical mailing address and an unsubscribe link for any email that is not pure auth. Pure auth emails (magic links, password resets) typically don't need unsubscribe.
- This is general guidance, not legal advice. For specific compliance questions, consult Every's legal counsel.

## Dependencies

- `foundation/marketing-os`
- `brand-voice/{relevant brand}` (loaded dynamically)
- `craft/copywriting`
- `craft/editing`

## Quick checklist before sending to review

- [ ] Subject literally describes the email's contents
- [ ] One purpose, one action
- [ ] Critical dates / amounts / consequences stated explicitly
- [ ] No marketing content in pure auth or billing
- [ ] Plain-text version reads correctly
- [ ] Sender address matches the email type per table above
- [ ] Length is within budget for this transactional category
- [ ] Reply-to is set correctly (real human for soft transactional, unset for pure system)
