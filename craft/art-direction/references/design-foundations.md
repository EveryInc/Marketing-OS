# Design foundations

Practical support for someone who cannot yet name why a layout fails. Read the sections
needed for the task. Research checked October 16, 2026; sources and limits appear below.
The numerical starting points are workflow defaults, not scientific optima or brand rules.

## Start with the communication

Before choosing a font, name the audience, surface, viewing conditions, first thing to
notice, next thing to understand, and desired action (if any). Find approved copy and
visual rules. Ask only about missing choices that would change the output. For teaching,
use a labeled fictional example instead of inventing product claims.

Separate three kinds of instruction:

- **Requirements:** approved content, identity, accessibility target, format and delivery
  constraints. Surface conflicts rather than silently violating them.
- **Defaults:** useful starting points when the system is silent. Adjust for content,
  typeface, language, device, and viewing distance.
- **Expression:** intentional asymmetry, density, surprise, texture, or unusual scale
  that serves the concept. Preserve it while repairing avoidable reading problems.

## 1. Hierarchy: choose what gets noticed first

Hierarchy is the order in which information attracts attention. Assign roles before
styles: primary message, supporting evidence, action, and metadata. Give the main message
or defining image a clear advantage in scale, placement, contrast, or surrounding space.
Do not make every element compete using bold type, bright color, and a box.

Start with three visibly distinct levels on a simple asset. This is a working limit,
not a ban on complex editorial systems. Importance need not equal font size: an isolated
small label can carry more emphasis than a large muted block. Inspect the whole surface.
Use a thumbnail to check dominant shapes, then read at destination size. A thumbnail
cannot prove body text is readable. [S1]

**Repair:** If the logo, headline, illustration, and button all compete, select the
intended first read and reduce competing emphasis before adding more decoration.

## 2. Grids: give elements shared edges

A grid is a set of alignment guides. Margins separate content from the canvas edge;
columns divide usable width; gutters separate columns. Start with the smallest grid
that fits the content: one column for a narrow reading surface, two for a comparison,
more subdivisions when different spans must align. A 12-column web grid is an option,
not a requirement. IBM's 2x system demonstrates another coherent approach. [S2, S3]

For equal columns: `column width = (canvas width − 2 × margin − (columns − 1) × gutter) / columns`.
A block spanning n columns includes the n−1 internal gutters. Align headline, text,
images, and captions to deliberate shared edges; avoid independent floating offsets.

**Worked geometry (fictional):** On a 1200px-wide canvas with 60px side margins,
12 columns and 24px gutters, each column is 68px. A six-column block is 528px.
Two such blocks plus their 24px gap fill the 1080px content width. On a 390px viewport
with 20px margins, stack the blocks at 350px; do not shrink the desktop composition.
These are example dimensions, not a preset for every site.

Breaking the grid works when enough alignment remains to make the exception visible.
An image may bleed outside the text margin while headings and captions retain their
shared edge. Preserve an approved exception; do not normalize it reflexively.

## 3. Space: show what belongs together

Nearby objects tend to read as a group. Put a caption closer to its image than to the
next image; put a heading closer to its following paragraph than the preceding section.
Give separate groups more space than the elements within them. [S1, S4]

Choose a small spacing scale where none exists: for digital layouts, 4, 8, 12, 16, 24,
32, 48, 64px is a workable starting set. Use named roles such as inline-gap, group-gap,
and section-gap. Don't force every optical adjustment onto a mathematical increment.
Empty space directs attention; dense work can also be excellent if grouping stays clear.

**Repair:** Before adding divider lines or cards, try correcting spacing and alignment.
If content does not fit, reflow or expand the surface. Do not shrink essential type or
remove protected wording just to preserve a box. Propose copy edits separately.

## 4. Typography: build roles before choosing more fonts

A typeface is the letterform design; weight is its thickness; leading is line spacing;
tracking is spacing across letters; measure is the length of a text line.

Inherit licensed, available brand fonts. If none exist, a single family with useful
weights is a good provisional starting point. A second family should have a distinct
role, such as expressive headlines with a quieter reading face. Extra families cannot
repair weak hierarchy. Do not silently replace a missing approved font.

For an English-language web reading surface, try body text at 16–18 CSS px, line height
around 1.5, and roughly 45–75 characters per line. Inspect the chosen font and audience;
this is a starting range, not a WCAG minimum. USWDS and Butterick offer differing ranges,
which is a reason to test the composition rather than treat one number as law. [S4, S5]

Define role tokens: display, section-heading, body, caption, label. A provisional scale
might use 40/44, 28/34, 18/27, and 14/20 (size/line height in CSS px). Adapt display type
for smaller screens. Captions remain essential information, not permission for faint text.
Use weight, size, and space consistently; avoid almost-identical heading levels.

Default to flush-start paragraphs for the writing direction. Center short headings when
the composition calls for it, not long reading blocks. Avoid stretched or fake-bold type.
Check awkward wraps, stranded final words, clipped accents, numeral alignment, and actual
font loading. A manual line break that helps one width may fail at another.

## 5. Color: assign jobs and test relationships

Hue is the color family; saturation is its intensity; lightness describes light versus
dark appearance. Equal apparent lightness is not guaranteed by matching numeric values
in different color models. Color appearance changes with adjacent colors. Review colors
in the intended proportions and backgrounds, not only as isolated swatches. [S6]

Define roles first: canvas, surface, primary text, secondary text, accent/action, and
status colors when needed. An initial neutral base plus one accent reduces unplanned
competition; it is not a restriction on an expressive approved palette. Reserve the
strongest accent for a specific purpose. Reusing an error color decoratively can confuse
meaning. Never assume blue means trust or red means urgency across audiences.

Color-wheel relationships can generate candidates; they do not guarantee quality,
readability, or brand fit. Neither a 60/30/10 allocation nor a golden-ratio palette is
a universal requirement. Test the proposed combinations with the actual content.

## 6. Contrast and access: measure the applicable requirements

For a web deliverable targeting WCAG 2.2 AA:

- Text normally needs at least **4.5:1** foreground/background contrast. Large text
  needs **3:1**: at least 18pt regular or 14pt bold (24 or approximately 18.67 CSS px).
  Logotypes and incidental text have defined exceptions; body copy does not inherit
  the logo exception. Thin fonts can still be difficult to read at a passing ratio. [S7]
- Essential component boundaries/states and graphical objects generally need **3:1**
  against adjacent colors, with criterion-specific exceptions. This is not a requirement
  for every decorative border. Button text has its own text-contrast requirement. [S8]
- Convey meaning through labels, shapes, patterns, or position as well as color. A red
  error outline alone is insufficient. Grayscale inspection is useful, but is not a
  substitute for contrast measurement or color-vision testing. [S9]

Calculate with source foreground/background colors after compositing opacity and overlays;
do not sample anti-aliased glyph edges as the text color. Do not round a failing ratio up
to the threshold. For
text on photography or gradients, inspect the backgrounds beneath the text across crops
and states; a sampled average can conceal failure. Move text, add a tested solid panel,
or adjust the pairing without replacing the whole identity. Record foreground, background,
ratio, text size/weight, state, and pass/fail. If colors cannot be measured, mark unverified.

For print, slides, and raster assets, these ratios are a useful readability reference,
not proof that the complete deliverable conforms to WCAG. Test actual viewing conditions.

## 7. Composition and imagery: keep one argument

Visual weight comes from area, contrast, detail, and position. Balance does not require
symmetry. A small dark object can counter a large pale field. Use crop and placement to
support the first read; don't add an unrelated image just to fill space.

Preserve the subject or evidence the image needs to communicate. Show the relevant
product action at a readable scale rather than a tiny full-screen screenshot. Label
illustrative mockups; never fabricate product proof. Check crop, resolution, rights,
focal point, and text collisions at each destination aspect ratio. An approved texture
or unusual image treatment can remain while the reading area becomes clearer.

## 8. Match the medium

| Surface | Starting move | Proof to inspect |
|---|---|---|
| Launch page | Clear first read, supporting proof, intended action; content-led stacking | Narrow and wide layouts; actual text and font; navigation and action states |
| Social graphic | One dominant message or image, essential identifying details | Feed-size preview and platform crop/safe area; not just the large export |
| Presentation | One principal point per slide where appropriate; evidence at useful scale | Projection or audience-size preview; dense detail moved to an appendix only with approval |
| Editorial/document | Consistent reading measure, section rhythm, captions and folios | Several consecutive pages, longest heading, image/caption associations |
| Product interface | Stable component roles, visible labels, differentiated states | Keyboard focus, errors, long content, zoom, reflow and pointer targets |

For web layouts, test vertically scrolling content at 320 CSS px equivalent width,
allowing the defined exceptions for inherently two-dimensional content. [S10]
Test user spacing overrides without content/function loss: line height 1.5 times font
size, paragraph spacing 2 times, letter spacing .12 times, word spacing .16 times.
These are override tests, **not mandatory authored styling**. [S11]
For interactive web controls, WCAG 2.2 AA specifies 24×24 CSS px targets or permitted
exceptions, including sufficient spacing. Larger comfortable targets are often preferable;
do not mislabel a 44px preference as the AA minimum. [S12]

These checks are a design subset. They do not certify complete accessibility; semantics,
keyboard behavior, alternative text, focus, and motion require appropriate implementation
testing too. Use the relevant production specialist for those checks.

## Sources and evidence boundaries

Research-backed guidance is separate from Every's identity and from measured performance.
No source below establishes that these defaults improve Every's conversion rate.

- **S1:** [NN/g, Five Principles of Visual Design](https://www.nngroup.com/articles/principles-visual-design/): hierarchy, scale, balance and grouping; practitioner guidance.
- **S2:** [IBM Design Language, 2x Grid](https://www.ibm.com/design/language/2x-grid/): coherent grid and spacing implementation; IBM's convention, not a universal rule.
- **S3:** [USWDS, Layout grid](https://designsystem.digital.gov/utilities/layout-grid/): responsive column/gutter implementation.
- **S4:** [USWDS, Typography](https://designsystem.digital.gov/components/typography/): reading measure, spacing and typesetting guidance.
- **S5:** [Matthew Butterick, Line length](https://practicaltypography.com/line-length.html): practitioner guidance; recommends 45–90 characters, not the narrower starter range used here.
- **S6:** [Albers Foundation, Interaction of Color](https://www.albersfoundation.org/alberses/teaching/interaction-of-color): perception in context, not a formula for brand color meaning.
- **S7:** [W3C, Contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- **S8:** [W3C, Non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
- **S9:** [W3C, Use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).
- **S10:** [W3C, Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
- **S11:** [W3C, Text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).
- **S12:** [W3C, Target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

W3C Understanding documents explain the linked normative criteria. Verify the current
criterion and its exceptions for a formal conformance assessment. Original worked
dimensions, recipes, and repair order here are provisional operating guidance created
for this skill, not quotations or validated experimental findings.
