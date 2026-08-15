Start with a read-only inventory of contributor records, portrait sources, existing
components, dimensions, variants, fields, and exceptions. Normalize every record to a
full identifying name; the two Dans cannot share an automation key. Use semantic fields
such as `Name`, `Role`, `Quote`, and `Portrait`, plus predictable output names.

Test one contributor before batching. Verify identity against the source record separately
from crop and appearance. Define default crop behavior and named per-person overrides for
unusual aspect ratios. After production, compare the expected and actual contributor lists,
inspect component linkage and fields, then render every output and review crops, type,
overflow, and spacing visually.
