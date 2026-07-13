# Messaging

The canonical format and evidence discipline for audience-facing messaging documents. Where
`strategy/messaging-architecture` builds the message house (top-level narrative → pillars →
proof points), this skill governs how an actual messaging doc is written per audience: the
section schema every target gets, and the verified evidence banks the claims draw from.

It is the operational layer between architecture and copy. The architecture says what the
brand's message hierarchy is; this schema says how each audience section is structured,
evidenced, and closed, so a downstream craft/copywriting pass has real material to cascade.

## When to invoke

- When writing or reviewing an audience-facing messaging document (per-persona, per-segment, or per-launch)
- When a messaging doc needs a consistent per-target section structure
- When placing or re-verifying a product's evidence bank before it goes into buyer-facing copy
- When cascading a message house into audience sections that carry proof, competition, and sample lines
- When auditing a draft against the four-bucket verification protocol before delivery

## System

Messaging is composed of reference files:

### references/audience-section-schema.md
The canonical per-target section format for messaging docs — WHO · PAIN · MOTIVATION · HOW
WE SOLVE IT · THE COMPETITION · WHY US · WHERE — plus the macro-backdrop opening and the
per-section evidence ledger that closes each section.

### references/evidence-bank-every-agent.md
The verified evidence bank for the Every Agent launch — every stat with its report,
publisher, year, and sample, dated and flagged for re-check, including the known-fabricated
stats that must never ship. Product-tagged; re-verify dates before external use.

## Reference routing

| Task type | Load |
|---|---|
| Structuring an audience section in a messaging doc | `references/audience-section-schema.md` |
| Pulling a verified stat for Every Agent copy | `references/evidence-bank-every-agent.md` |
| Sourcing/citation discipline for the whole draft | `craft/copywriting/references/messaging-doc-discipline.md` |
| The message house / pillars this schema sits under | `strategy/messaging-architecture` |

## Dependencies

- `foundation/marketing-os`
- `strategy/messaging-architecture` (cross-referenced: the message house / audience-proposition matrix upstream — the section schema operationalizes it, does not duplicate it)
- `marketing-science/research` (competitive audits, synthesis methodology, and the evidence the banks are built from)

## Quick checklist

- [ ] Every audience section follows the schema in order: WHO · PAIN · MOTIVATION · HOW WE SOLVE IT · THE COMPETITION · WHY US · WHERE
- [ ] The doc opens with the cited macro backdrop framing why the timing works
- [ ] Every PAIN and market claim carries its named study inline (report, year, sample)
- [ ] MOTIVATION claims are tagged [H] with the validation step named
- [ ] THE COMPETITION carries dated verbatims per named competitor; absence claims dated with a re-check flag
- [ ] Each section closes with a one-line evidence ledger: verified / hypothesis / pending re-check
- [ ] Stats pulled only from the evidence bank; no known-fabricated stat shipped
