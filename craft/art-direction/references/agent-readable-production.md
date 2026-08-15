# Agent-Readable Visual Production

Use this reference when an approved identity becomes a component library, template system,
batch of assets, or automated workflow.

## Labeling is infrastructure

An agent reads a design file through names, hierarchy, properties, geometry, and rendered
evidence. Labels are part of the interface.

- Use stable, descriptive component and frame names.
- Use full names when short names collide. `Dan Shipper` and `Dan Frommer` are safer than
  two layers named `Dan`.
- Name source portraits and images by identity, subject, and role, not `IMG_1042` or
  `Rectangle 87`.
- Use consistent field labels such as `Name`, `Quote`, `Byline`, and `Portrait`.
- Name variants by meaningful state or format, not visual accident.
- Preserve a clear distinction between canonical components, instances, experiments, and
  final exports.

Good labeling helps people as much as agents. It reduces mistaken identity, makes reviews
legible, and allows another operator to resume the work without reconstructing the file.

## Inventory before mutation

Before changing the file, inventory:

- Existing components, variants, instances, and duplicates
- Variables, styles, fonts, and unresolved or missing dependencies
- Source images and their aspect ratios
- Canonical examples and known-good outputs
- Required export dimensions and formats
- Identity fields and content fields
- Auto-layout, clipping, overflow, and responsive behavior

Count the actual state. A user's estimate is orientation, not a database query. Report
material discrepancies before scaling the change.

## Resolve missing assets deliberately

Treat a missing portrait or image as an implicit production dependency when the requested
deliverable clearly requires it. Search in this order:

1. The canonical Figma file and approved component library
2. Supplied project folders and named internal asset repositories
3. Current authoritative public sources associated with the person or organization
4. The open web when the authoritative sources do not provide a usable asset

Use the person's full name, organization, and role to disambiguate the search. Preserve
the source URL or file provenance. Before final use, verify identity, recency, resolution,
promotional suitability, and rights. Ask the human when any of those remain uncertain.

Background removal, reframing, and texture adaptation still require visual review. A
technically clean cutout can alter a face, remove meaningful details, or introduce a false
sense of authority around an unverified source.

## Assign tool ownership

Choose the production architecture based on fidelity and reliability:

### Figma-native

Use when the connected tools can preserve fonts, variables, component properties, and
export behavior. Keep the source and output inside the canonical design system.

### Hybrid

Use when Figma reliably owns layout, components, variables, and portrait geometry but an
external renderer is more dependable for custom typography, data binding, or batch export.
Document what crosses the boundary and how the final asset returns to the source system.

### Human-finished

Use when a small judgment-heavy correction, such as an unusual portrait crop or optical
alignment, takes seconds for a human and would require a fragile automation detour. This is
an intentional part of the workflow, not concealed failure.

## Separate the skill from the execution engine

A reusable creative skill owns the decisions: choose the approved template, gather and
validate inputs, find missing assets, apply content and crop rules, run QA, and escalate
judgment calls.

A Figma plugin or renderer owns repeatable execution: clone the canonical frame, bind the
portrait, write local fonts, preserve editable layers, apply stable names, and place the
output correctly. Keep the input contract independent of the execution tool so the same
skill can route to Figma-native, hybrid, or human-finished production.

## Protect layout behavior

Visual absence and structural absence are different. Removing or hiding a child can cause
auto-layout to collapse. When the layout must remain, preserve the object's geometry and
change visibility in a way that does not reflow the parent. Verify the rendered result.

Test overflow, clipping, and text length against the actual output environment. If a quote
or title needs a size reduction, use a documented rule before ad hoc manual exceptions.

## Separate identity from appearance

A card can look correct while containing the wrong person, source image, byline, variable,
or component reference. Verify identity fields independently from rendered appearance.

For each generated item, check:

- Expected identity and source asset
- Component and variant reference
- Frame dimensions
- Image crop and focal point
- Text content and font
- Overflow, clipping, and spacing
- Export path, filename, and format

## Review in two passes

### Structural pass

Inspect names, hierarchy, properties, variables, dimensions, component references, content,
and export configuration.

### Visual pass

Render or export the result and inspect it at the intended size. Use browser or image proof
when needed. Compare every exception, including the hard cases.

Independent review can expose failures that successful tool execution misses. A debugging
or review workflow is especially useful after the first automation pass because packaging,
dependencies, and invisible output errors may not appear in the final image.

## Learn from corrections

Classify each correction:

- **System rule:** Update the component, template, naming convention, or generator.
- **Content rule:** Update length, field, or identity handling.
- **Asset exception:** Record a focal point or crop override for this source.
- **Taste exception:** Leave the human decision explicit when it should not generalize.

The useful benchmark is not whether the first run eliminates every manual touch. Measure
setup time, number of outputs, number and severity of corrections, human finishing time,
and performance of the next clean run. The workflow compounds only when corrections alter
future behavior.
