# Campaign Tracker

One dashboard page that answers: what does a paying customer cost, by message and
channel, and what do we do about it. Live before the first ad runs.

## Build it with the Compound Engineering loop

Use the Compound Engineering plugin where the host has it.

1. **Plan (`ce-plan`).** Input: the locked inputs, the test design, the tracking
   preflight, and the list of data sources that exist today. Output: which numbers the
   page shows, where each comes from, how often it refreshes, and what is manual.
2. **Work (`ce-work`).** Build the page as a shareable dashboard (in Claude, a dashboard
   artifact). Use live queries where a connector exists and dated uploads where one
   does not. Follow the brand's design system; do not invent colors or type.
3. **Review (`ce-code-review`).** Check every figure against its source by hand for at
   least one ad. Check the arithmetic. Check that immature cohorts are not shown as
   final.
4. **Compound (`ce-compound`).** Record what broke and what the next tracker should do
   differently. Bring transferable fixes back to this file.

If the plugin is not available, keep the same four steps by hand.

## What the page shows

Top to bottom:

1. **The deciding number.** Cost per paying customer on the deciding day, overall,
   against the ceiling and the stop line. Next to it: paying customers, spend, and the
   date the next cohort matures.
2. **Decision table.** One row per message and per channel: spend, signups, paying
   customers, cost per paying customer, first-year revenue per unit spent, and the call
   (scale, change, stop, or still maturing).
3. **The chain.** Per message: cost to be seen, click rate, landing page conversion,
   paid conversion. Shows which link is weak.
4. **Budget.** Spent and remaining by stage, with the release rule and whether it has
   been met.
5. **Customer quality.** Plan mix, and cancels among acquired customers.
6. **Holdout,** if one runs: both groups, the gap, and the chance band.
7. **Tracking health.** Share of signups with a known source, bot filter status, date
   of the last test purchase, and data freshness per source.

## Rules for the page

- Every number shows its source and its date.
- Company records decide. Platform-reported figures appear only in the chain and are
  labeled as the platform's.
- Cohorts younger than the deciding day are marked as maturing, with early figures
  shown separately.
- Attributed, assisted, and incremental results are never added together.
- A missing number is shown as missing with the reason, not as zero.
- The page states the definition of a paying customer at the top.
