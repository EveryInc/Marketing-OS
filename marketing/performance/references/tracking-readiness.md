# Tracking Readiness

Run this before any money moves. Each line is pass, fail, or not checked, with who
confirmed it.

## Preflight

- [ ] Every ad has its own tagged link or code, from one naming scheme
      (channel, stage, message, version).
- [ ] The source is saved on the customer record at signup and survives until payment.
- [ ] A test purchase through a tagged link shows the right source on the paid record.
- [ ] The platform receives the events it needs (signup, trial, payment), sent from the
      server as well as the browser where the platform supports it.
- [ ] Bot and duplicate signups are filtered before counting.
- [ ] The share of signups with no known source is measured, and is low enough that the
      test can be read. If not, fix it or narrow the test.
- [ ] Spend is recorded by ad and by day, from the platform's export.
- [ ] Ads to new people exclude existing customers and the existing list.
- [ ] A "how did you hear about us" answer exists for paths tracking will miss.
- [ ] Data is current. A snapshot is labeled with its date and never read as today's.

## If a line fails

Say what the test can no longer answer. Then choose: fix it before launch, cut the part
of the test that depends on it, or go ahead and label the affected results unreadable.
Do not launch and hope.
