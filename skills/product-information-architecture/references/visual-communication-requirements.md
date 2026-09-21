# Visual Communication Requirements for Applications

Use this reference to decide whether non-text communication could materially improve application understanding. Identify needs and opportunities; do not perform visual direction or final UI design.

## Evaluate each candidate

1. State what users must understand, compare, monitor, verify, or orient around.
2. Decide whether labels, prose, values, and structural grouping are sufficient.
3. Identify whether a visual representation could materially reduce ambiguity or cognitive effort.
4. Determine whether it depends on live data, representative examples, approved workflows, or other verified sources.
5. Define an accessible text or data fallback.
6. Assign a content priority.

## Candidate categories

| Need | Potential category | Source requirement |
| --- | --- | --- |
| Understand object relationships | Relationship diagram or map | Approved concepts and relationships |
| Understand progression or history | Timeline or sequence | Valid lifecycle and event semantics |
| Compare quantities or trends | Chart or data view | Accurate data, units, timeframe, and definitions |
| Learn a complex area | Annotated screenshot or example | Current product state and representative safe data |
| Orient within a complex domain | Overview map or taxonomy view | Stable architecture and approved terminology |
| Verify operational status | Status visualization or evidence view | Trustworthy source, freshness, and failure semantics |

A visual opportunity is not a component decision. UX/UI may satisfy the need with structure, progressive disclosure, or text.

## Prefer no additional visual asset when

- Labels, values, and grouping already communicate the meaning.
- The application has no explanatory imagery need.
- The visual would decorate rather than improve a task.
- Data is unavailable, unreliable, too sparse, or misleading.
- A chart would obscure exact values users need.
- The concept changes too often to keep the asset accurate.
- Accessibility, performance, localization, privacy, or maintenance cost exceeds the benefit.

Record `None recommended` when preserving a no-asset decision matters.

## Preserve boundaries

Do not finalize:

- Visual aesthetic or art direction
- Chart type or styling unless the data relationship makes a class of representation invalid
- Photography/illustration treatment
- Color encoding, composition, exact placement, or dimensions
- Component choice, banner design, or final asset selection

Pass the communication need, semantics, evidence dependency, and fallback to downstream UX/UI.

## Protect accuracy and accessibility

- Require text alternatives, transcripts, captions, or data tables where needed.
- Never encode essential status by color alone.
- Do not fabricate screenshots, data, workflows, customers, or results.
- Mark data freshness, units, timeframe, timezone, sampling, and missing-data semantics.
- Flag privacy, permission, redaction, role visibility, and representative-data requirements.
- Flag localized screenshots, mixed-direction labels, and RTL reading-order needs.
