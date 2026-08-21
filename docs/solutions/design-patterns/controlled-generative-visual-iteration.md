---
module: craft/art-direction
date: 2026-08-15
problem_type: design_pattern
component: development_workflow
severity: medium
applies_when:
  - "Turning approved copy into wireframes or designed surfaces"
  - "Iterating on generated visual concepts in Figma or Flora"
  - "Adapting visual references without copying them literally"
  - "Defining motion from reference frames or multi-stage transformations"
  - "Producing editable design artifacts that also require rendered visual QA"
related_components:
  - documentation
  - tooling
tags:
  - generative-visuals
  - visual-iteration
  - figma
  - flora
  - wireframes
  - reference-abstraction
  - motion
  - visual-qa
---

# Controlled Generative Visual Iteration

## Context

The art-direction system already required canonical-file inspection, human-supplied
references, representative proofs, and separate structural and visual verification. It
did not define how to keep copy, source frames, reference roles, generation settings, and
motion endpoints controlled from one iteration to the next.

That gap produced several recurring failures: helpful copy invented during wireframing;
flattened PDFs presented as editable design handoffs; many references averaged into generic
work; conspicuous objects copied literally; several visual variables changed in one pass;
and motion applied to the wrong connected source or allowed exact wordmarks to drift.

## Guidance

1. Freeze approved content as a locked manifest, including exact text, explicit omissions,
   placeholders, annotations, order, source round, and date.
2. Lock the canonical editable surface by file, page, frame or node, component state,
   dimensions, and revision. Preview the connected source before generation.
3. Give one primary reference authority over composition and, when needed, one secondary
   reference authority over a bounded treatment.
4. Translate each reference into invariants, allowed variables, and forbidden literal
   shortcuts before prompting.
5. Generate one real-content surface, critique the visible result, branch from the
   strongest output, and change one declared variable while holding other inputs fixed.
6. For precise motion, use exact first and last frames. Split multi-stage transformations
   at an approved shared frame, or use deterministic tooling when text and coordinates may
   not drift.
7. Treat editability and rendered fidelity as separate acceptance gates. Flattened output
   may prove appearance, but it does not replace native layers, constraints, components,
   variables, or prototype behavior.

The canonical production protocol lives in
[`craft/art-direction/references/agent-readable-production.md`](../../../craft/art-direction/references/agent-readable-production.md).
Reference translation lives in
[`craft/art-direction/references/reference-doctrine.md`](../../../craft/art-direction/references/reference-doctrine.md),
and the copy-to-layout entry point lives in
[`launches/wireframe-from-copy/SKILL.md`](../../../launches/wireframe-from-copy/SKILL.md).

## Why This Matters

A broad prompt can produce an attractive result while changing copy, composition, source
identity, palette, and motion subject at once. The team then cannot tell which decision
caused the improvement. Controlled branches turn iteration into evidence: each output
answers one question, preserves what already works, and leaves a useful parent for the next
decision.

The workflow also protects downstream production. Locked manifests prevent copy drift.
Reference grammar discourages literal imitation. Source audits prevent the wrong object
from moving. Exact endpoint frames protect brand transformations. Editable handoffs keep
design authority with the next operator.

## When to Apply

- Moving approved copy into a wireframe, layout, or design file
- Using a generative canvas to explore composition, treatment, or motion
- Translating artistic or historical references into a new visual system
- Comparing palette, crop, texture, lighting, or motion options
- Moving a review artifact into Figma for continued design production
- Correcting a promising result without losing its strongest decisions

## Examples

Instead of asking a generator to “make this more premium, dynamic, and editorial,” branch
from the strongest poster and state: preserve the composition, crop, type scale, content,
and seed; change only the warm metallic treatment to the approved cool palette.

Instead of prompting from a complete historical poster, record the vertical hierarchy,
dense supporting information, and ceremonial framing as invariants; allow the subject,
material, and palette to change; forbid the literal bust, scalloped border, and faux-aged
paper.

For a `ME` to `WE` to `Every` transformation, use exact `ME` and `WE` frames for the first
stage, then reuse that approved `WE` frame as the exact start of the second stage. Verify
the animated source immediately before each run.

## Related

- [`craft/art-direction/SKILL.md`](../../../craft/art-direction/SKILL.md)
- [`foundation/marketing-os/references/native-document-editing.md`](../../../foundation/marketing-os/references/native-document-editing.md)
- [`launches/canonical-process.md`](../../../launches/canonical-process.md)
