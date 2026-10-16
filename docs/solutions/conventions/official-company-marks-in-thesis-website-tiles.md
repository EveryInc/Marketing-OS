---
title: Official company marks are required assets for THESIS website tiles
date: 2026-08-27
category: conventions
module: Every Asset Generator
problem_type: convention
component: development_workflow
severity: high
applies_when:
  - "Creating or rebuilding a THESIS 2027 speaker website tile"
  - "Adding a new speaker record to the Every Asset Generator"
tags:
  - company-wordmark
  - logo-provenance
  - thesis-2027
  - figma
  - website-tiles
---

# Official company marks are required assets for THESIS website tiles

## Context

A speaker website tile replaced the canonical company mark with typed company text. The
words were correct, but the asset was visually and semantically wrong: a company name set in
Founders Grotesk is not that company's wordmark.

## Guidance

Company-mark acquisition is part of THESIS speaker-asset production. For every website tile,
automatically retrieve the current official wordmark or logomark from the company's own
brand kit or website. An existing approved mark in the Thesis Figma file or live Every site
is the next-best source. Do not use logo aggregators, search-result thumbnails, screenshots,
or recreated typography.

Normalize the mark to a transparent black PNG when needed, embed it in the plugin build, and
attach it to the speaker record as an image payload. The Figma builder must create an image
node, preserve the mark's aspect ratio with `FIT`, and insert it above the speaker title in
the canonical metadata stack.

```js
{
  name: "Speaker Name",
  company: "Company",
  title: "Founder",
  websiteCompanyLogoBase64: OFFICIAL_COMPANY_WORDMARK_BASE64
}
```

The default behavior is strict: a missing official mark stops website-tile generation with
an actionable error. Typed company text is permitted only as an explicit, company-specific
exception approved by Douglas; it is never an automatic fallback.

## Why This Matters

The website panel is a branded editorial object, and the company mark carries identity that
plain text cannot reproduce. Automatic sourcing removes a recurring manual dependency while
the strict runtime guard prevents the generator from quietly completing an incorrect tile.

## When to Apply

- Every new THESIS speaker request, because the complete speaker set includes a website tile
- Any website-tile repair that changes the company, title, or metadata stack
- Any batch whose legacy records still rely on typed company-name fallbacks

## Examples

Wrong: delete the source logo group, create a text layer containing `Polsia`, and place it
above `Founder`.

Correct: download Polsia's current official black wordmark from its website, convert it to a
transparent PNG, embed it in the plugin, create an image node named
`Website company logo — official asset`, and validate that the node appears above `Founder`.

## Related

- [Controlled Generative Visual Iteration](../design-patterns/controlled-generative-visual-iteration.md)

