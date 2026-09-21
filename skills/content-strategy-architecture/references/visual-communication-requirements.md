# Visual Communication Requirements

Use this reference to decide whether non-text content could materially improve communication. Identify needs and opportunities; do not perform visual direction or final asset selection.

## Evaluate the communication problem

For each relevant page or section:

1. State what the user must understand, believe, compare, verify, remember, or orient around.
2. Decide whether text can communicate it sufficiently.
3. Identify whether non-text content could materially reduce ambiguity, cognitive load, or unsupported claims.
4. State what source material or evidence would be required.
5. Define a text-only fallback or explain why one is not viable.
6. Assign a content priority rather than a production priority.

## Use justified opportunity categories

| Need | Potential category | Typical evidence requirement |
| --- | --- | --- |
| Demonstrate real product behavior | Current product screenshot or short demonstration | Verified build, representative data, permission to expose content |
| Explain a process or relationship | Diagram or annotated sequence | Approved workflow, terminology, and exception rules |
| Compare meaningful alternatives | Comparison table, chart, or side-by-side evidence | Comparable criteria and validated source data |
| Prove a result or capability | Real result, artifact, data view, or case evidence | Traceable customer/product evidence and consent |
| Establish physical context or authenticity | Photograph or video | Real subject, usage rights, and accurate caption context |
| Orient within a complex offering | Map, taxonomy view, or overview diagram | Stable structure and approved labels |

Treat each as a candidate. The downstream design agent may choose another medium or no asset.

## Prefer no asset when

- Text is already clear and concise.
- An image would be decorative rather than informative.
- No trustworthy source material exists.
- A generic stock image would weaken credibility.
- The visual would duplicate adjacent content without reducing effort.
- Mobile, performance, accessibility, or maintenance costs exceed the communication benefit.
- The concept is unstable and would make the asset quickly inaccurate.

## Record requirements

| Area | Communication need | Text sufficient? | Potential asset category | Evidence/source required | Text-only fallback | Priority |
| --- | --- | --- | --- | --- | --- | --- |

Use `None recommended` when a deliberate no-asset decision is important to preserve.

## Preserve the ownership boundary

Do not finalize:

- Visual aesthetic or art direction
- Photography versus illustration treatment
- Color, composition, crop, or exact placement
- Dimensions, responsive rendition, or banner design
- Final asset selection, production, or approval

Pass communication requirements, evidence dependencies, and constraints to downstream UX/UI. Allow that stage to reject or replace any candidate asset while still satisfying the underlying communication need.

## Add accessibility and integrity constraints

- Require meaningful text alternatives for informative assets.
- Avoid putting essential copy only inside images.
- Require captions, transcripts, or data tables when the medium needs them.
- Flag mixed-direction labels and localization needs in screenshots or diagrams.
- Do not fabricate product screens, customer evidence, data, testimonials, certifications, or results.
- Mark redaction, permission, freshness, and version dependencies explicitly.
