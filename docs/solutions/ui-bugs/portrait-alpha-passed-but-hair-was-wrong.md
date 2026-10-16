---
title: Portrait alpha passed while the visible hair treatment was still wrong
date: 2026-08-27
category: ui-bugs
module: Every Asset Generator
problem_type: ui_bug
component: development_workflow
symptoms:
  - "A transparent portrait passed alpha validation but showed bright silver streaks and contaminated edges over the website blue"
  - "Repeated defringe passes changed boundary pixels without correcting the blown highlights inside the hairstyle"
root_cause: missing_validation
resolution_type: workflow_improvement
severity: high
tags:
  - portrait-masking
  - hair-detail
  - figma
  - visual-qa
  - transparency
---

# Portrait alpha passed while the visible hair treatment was still wrong

## Problem

The asset generator treated a technically valid alpha channel as evidence that a speaker
portrait was production-ready. The portrait still failed visibly over the THESIS website
blue because natural hair highlights had become bright silver strands and the edge retained
matte contamination.

## Symptoms

- Fine hair looked white or metallic against the blue field even though the PNG had alpha.
- The automated halo count passed after defringing, but the visible hairstyle remained wrong.
- Rebuilding the plugin repeatedly embedded a technically different file without resolving
  the defect Douglas was reviewing.

## What Didn't Work

- Repeatedly defringing the same cutout. Defringing can recover edge color from a matte; it
  cannot repair internal grayscale highlights or reconstruct a damaged hairstyle.
- Accepting image-model output labeled transparent without checking its pixel mode. The
  returned RGB file contained a checkerboard baked into the image.
- Reviewing a full-size transparent PNG without compositing it at the actual card crop and
  destination color.

## Solution

Return to the verified original portrait and rebuild the hair treatment before extracting
alpha. Preserve identity, pose, clothing, facial features, and the complete curl silhouette;
make the grayscale hair naturally dark with restrained highlights.

When an otherwise acceptable portrait arrives on a baked light checkerboard, extract only
the light neutral pixels connected to the canvas edge, create genuine alpha, and then
defringe the new semi-transparent boundary. Apply any person-specific hair correction with
a reviewed spatial mask rather than a global tone change.

The release gate is the exact destination-blue proof, not the alpha check:

```text
source portrait
  -> controlled grayscale hair
  -> genuine alpha extraction
  -> boundary defringe
  -> exact #1C82FF composite at final crop
  -> visual approval
  -> embed and verify payload hash
```

After the proof passes, verify that the built plugin's embedded Base64 bytes hash to the
same value as the approved cutout. This catches stale UI payloads that otherwise survive a
correct source-file replacement.

## Why This Works

The failure had two separate causes: the hairstyle was visually wrong inside the opaque
subject, and the boundary carried remnants of a light matte. Rebuilding the tonal treatment
fixes the first; deterministic alpha extraction and defringing fix the second. The final blue
composite tests the user-visible result, while the payload hash proves the reviewed image is
the image the plugin will create in Figma.

## Prevention

- Treat alpha validation as a guardrail, never final visual approval.
- Inspect hair at 200% and at the final website crop over the exact destination blue.
- Reject checkerboards baked into RGB before embedding.
- After one failed complex-hair repair, return to the original portrait instead of stacking
  more edge fixes on the failed derivative.
- Require the built payload hash to match the approved cutout.
- Keep a saved blue proof beside every newly prepared complex-hair portrait.

## Related Issues

- [Controlled Generative Visual Iteration](../design-patterns/controlled-generative-visual-iteration.md)

