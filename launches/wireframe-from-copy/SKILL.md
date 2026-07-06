# Wireframe From Copy

Turns an approved web-copy document into an annotated lo-fi wireframe — the artifact the
Week 5 brainstorm reviews and the design team builds from. Proven on Cora 2.0 (July
2026): copy R002 in, an eleven-section grayscale wireframe out, with the copy's own
contradictions flagged inline where designers would otherwise build on top of them.

## When to invoke

- "I need a wireframe" with a copy doc in hand
- Week 5 of an L/XL launch, after the copy round the team is aligned on
- The copy exists but no page structure does ("we're approved on sections, no wireframe")

## Conventions (the deliverable's contract)

- **Grayscale is deliberate.** The wireframe specs structure; design direction belongs to
  the design lead. A styled wireframe preempts the designer and gets thrown away.
- **Copy is placed verbatim** from the source round, with the round and date stated in the
  header and footer. The wireframe never silently improves copy — improvements are flags.
- **Placeholders are typed:** solid ✕-boxes for static images/screenshots; dashed hatch
  for motion/video. Every motion placeholder is numbered as a motion-scope item so the
  motion brief can be written straight off the wireframe.
- **Every section carries an annotation bar:** number · name · the section's job in one
  line. Sections are renumbered sequentially if the source doc's numbering drifts (state
  that it was done).
- **Flags live inline where the problem lives** — an unsourced stat flags on the proof
  bar, a price conflict flags on the pricing section. Flags come from an actual careful
  read of the copy: contradictions with the strategy/messaging spine, duplicate or
  orphaned blocks, truncated bodies, banned terms, unverified claims. The flag set is
  handed to `claims-clearance` and to the copy owner for R-next.
- **Provenance footer:** source doc + round, build date, what gate it serves, who signs
  off, where the motion-scope items are.
- Output is a single HTML file; PDF export on request (wkhtmltopdf print pass, verified
  page count and text before delivery).

## Reading the copy carefully (the actual job)

The wireframe is the excuse; the careful read is the value. Before drawing anything:
check the hero against the messaging spine's ruled hero line; check every stat, logo,
quote, and price for a source; check feature sections for copy-paste artifacts; check the
doc's internal numbering; check pricing against the strategy doc in the same file. Each
finding becomes an inline flag, not a silent fix.

## Dependencies

- `foundation/marketing-os`
- `launches/canonical-process.md` (Week 5 placement, sign-off roster)
- `brand-voice/{product}` (dynamically — hero-line and banned-term checks)
- `launches/claims-clearance` (receives the flag inventory)
- `craft/*` as relevant to the copy's format

## Quick checklist

- [ ] Source round + date stated on the artifact
- [ ] Copy verbatim; improvements expressed as flags, not edits
- [ ] Static vs. motion placeholders typed; motion items numbered for the brief
- [ ] Annotation bar on every section: number, name, job
- [ ] Careful-read flags inline: spine contradictions, unsourced claims, copy artifacts
- [ ] Flag inventory handed to claims-clearance and the copy owner
- [ ] Provenance footer; PDF verified if exported
