---
name: performance-marketing
description: Plan, run, and read a paid acquisition test that is judged on paying customers. Use for ad budgets, channel and creative tests, tracking readiness, spend rules, and the campaign tracker. Beta until one campaign has run through it.
---

# Performance Marketing

Spend money to find paying customers, and learn what one costs. This skill sits under
Compound GTM. It inherits the approved audience, offer, and prices; it does not set them.

## Status

**Beta draft.** Written while planning a first campaign. No campaign has run through it
and no rule here has been tested on results. Treat every rule as a starting position.
Do not cite this skill as evidence that a practice works. See "Finalize after the first
run" at the end.

## When to invoke

- When someone proposes an ad budget, a paid channel test, or a paid creative test
- When setting a cost target, a spend rule, or a scale, change, or stop line
- When checking whether tracking is ready before money moves
- When building or reading the campaign tracker
- When reading results at day 10, day 30, or later

Do not use it for unpaid social, PR, or lifecycle email. Those feed the same tracker but
belong to their own skills.

## Rules that hold the whole way through

1. **One number decides.** Cost per paying customer, counted in the company's own
   records at a fixed day after signup. Clicks, signups, and platform dashboards explain
   that number. They never replace it.
2. **Set the bar before looking.** Write down what counts as verified, what counts as a
   win, and the stop line before reading research or results. Do not move them after.
3. **Compare every recommendation to the ceiling.** No channel, budget, or creative idea
   goes into a plan until its likely cost per paying customer sits next to the most the
   company will pay.
4. **Say what was measured.** Clicks, recall, signups, and payments are different. A
   study of clicks is not evidence about payments.
5. **Explain each term once, in plain words.** The owner of the budget may not be a
   performance marketer. Teach as you go.
6. **A plan authorizes nothing.** Spending, launching, pausing, and changing a live
   campaign each need the named approver.

## Workflow

### 1. Lock the inputs

Inherit from the approved brief or decision record. Ask for anything missing; do not
invent it.

- What counts as a paying customer (trials, gifts, team seats: in or out)
- Offer, prices, plans, start and end dates
- Budget, who approved it, and whether it is fixed
- The return rule (for example, revenue back per unit spent) and whether it means
  revenue or profit
- First-year value of a new customer, by plan, with its source
- Who owns ads, creative, tracking, and the readout

Record conflicts between sources (two budgets, two cost targets) as open decisions. Do
not pick one silently.

### 2. Work out the ceiling and the chain

Read `references/unit-economics.md`. Produce the ceiling per plan, the most a signup can
cost at each paid rate, and how many paying customers the budget can buy at best and
worst. If the budget cannot reach the stated goal, say so first and say where the rest
has to come from.

### 3. Research with a fixed bar

Use `../../marketing-science/research/references/evidence-standard.md`. Search live each
run; platform rules, prices, and benchmarks go stale in months. Start with the company's
own history: earlier paid tests, which sources convert, which content people pay after.
Grade outside findings by how many independent sources agree and whether those sources
sell the thing they measured. Name what was not checked.

### 4. Check tracking before money moves

Run `references/tracking-readiness.md`. If a paying customer cannot be tied to the ad
that found them, the test cannot answer its question. Fix that or shrink the question.

### 5. Design the test

Read `references/test-design.md`. Decide channels, stages, messages, the event the
platform optimizes for, the holdout if there is one, and the scale, change, and stop
lines. Check feasibility: every rule must be usable in the time the budget allows.

### 6. Build the tracker

Read `references/tracker-dashboard.md`. Build one dashboard page with the Compound
Engineering loop (plan, work, review, compound). It is live before the first ad runs.

### 7. Run and read

- Weekly: move money between ads on the early signal named in the test design.
- At the early read: release or hold the next stage.
- At the deciding day: apply the scale, change, or stop line to each message and channel.
- Report cancels from acquired customers next to new paying customers.
- Label each claim attributed, assisted, or incremental, using
  `../../marketing-science/measurement/references/attribution-and-economics.md`.

### 8. Compound

Close with `../../marketing-science/measurement/references/compound-from-results.md`.
The dated result record stays with the campaign, outside this repository. Only a rule
that clears `../../foundation/marketing-os/references/knowledge-boundaries.md` changes
this skill.

## Dependencies

- `foundation/marketing-os`
- `marketing/gtm` (approved audience, offer, channels, owners)
- `marketing-science/measurement`
- `marketing-science/research`
- `craft/compound-copywriting` and `craft/art-direction` (ad concepts, when in scope)
- Compound Engineering plugin (`ce-plan`, `ce-work`, `ce-code-review`, `ce-compound`)
  for the tracker; optional if the host has no code tools

## Finalize after the first run

Remove the beta label only when all of these are true:

- One campaign ran from step 1 through a deciding-day readout using this skill.
- Each rule in "Rules that hold the whole way through" and each reference was either
  used as written, changed with a stated reason, or cut.
- The tracker spec was corrected against the dashboard that was built and used.
- At least three cases in `evals/cases.json` came from that run.
- The skill owner approved the final text.

## Quick checklist

- [ ] Paying customer defined, and the deciding day fixed
- [ ] Ceiling per plan written down with its source
- [ ] Budget's best and worst case stated against the goal
- [ ] Every channel compared to the ceiling
- [ ] Test purchase proves the source lands on the customer record
- [ ] Scale, change, and stop lines set before launch
- [ ] Every rule usable within the budget's time window
- [ ] Tracker live before the first ad
- [ ] Readout ends in a decision, with cancels shown
