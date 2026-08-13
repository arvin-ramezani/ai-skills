# Content Architecture Deliverable

Use these schemas for provisional and final outputs. Omit irrelevant fields rather than filling them with generic text.

## Contents

1. Status and evidence
2. Executive content strategy
3. Market and localization strategy
4. Information architecture
5. Journey map
6. Page architecture
7. SEO architecture
8. Mobile content strategy
9. UX Design Input
10. Quality gate

## 1. Status and evidence

Start with:

- Status: `Provisional` or `Final`
- Scope and version/date
- Confirmed inputs
- Assumptions and hypotheses
- Decisions made
- Critical unknowns or contradictions
- Research completed and research required

Do not label the architecture final while critical unknowns remain.

## 2. Executive content strategy

Define concisely:

- Primary and secondary markets
- Primary user and secondary segments
- Core problem and desired outcome
- Core value proposition and positioning
- Differentiation
- Primary and secondary conversions
- Messaging pillars
- Brand voice and editorial principles
- Content exclusions or guardrails
- Success signals and measurement dependencies

## 3. Market and localization strategy

Use one row per significant dimension:

| Dimension | Iran / Persian | International / English | Relationship | Evidence or rationale |
| --- | --- | --- | --- | --- |
| Audience | | | Shared / localized / market-specific | |
| Positioning | | | | |
| Value proposition | | | | |
| Terminology | | | | |
| Proof and trust | | | | |
| Objections | | | | |
| CTA and conversion | | | | |
| SEO intent | | | | |
| Support/transaction context | | | | |

State the chosen architecture model: `Shared`, `Localized`, or `Market-specific`.

## 4. Information architecture

Provide:

- Sitemap or page inventory
- Primary and secondary navigation
- Footer or utility navigation when relevant
- Content groups and parent-child relationships
- Entry pages and destination pages
- Cross-links and contextual pathways
- Authenticated versus public boundaries when relevant

For exact page mappings, use a table:

| ID | Page | Purpose | Audience | Primary intent | Conversion role | Parent / entry | Locale behavior |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use a compact Mermaid flow only when three or more branches or dependent steps are materially clearer than a table.

## 5. Journey map

For each primary journey:

| Stage | User question or task | Entry/context | Required content | Trust or objection | CTA/next step | Failure or exit path |
| --- | --- | --- | --- | --- | --- | --- |

Distinguish journeys by segment or market when they materially diverge.

## 6. Page architecture

Create one block per major page.

### `[Page name]`

| Field | Decision |
| --- | --- |
| Purpose | |
| Primary audience | |
| Main user question | |
| Search intent | |
| Business goal | |
| Primary CTA | |
| Secondary CTA | |
| Key message | |
| Proof/trust | |
| Objections | |
| SEO role/topic | |
| Internal links | |
| Iran/Persian | |
| International/English | |
| Dependencies/unknowns | |

Then define ordered sections:

| Order | Section | Job to be done | Required content | Priority | Mobile treatment | Locale behavior |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | Critical / Important / Supporting / Optional | Keep / compress / disclose / move / remove | Shared / translated / rewritten / market-specific / omitted |

Do not prescribe component type, visual styling, animation, or layout unless a content constraint requires it.

## 7. SEO architecture

| Page/topic | Market/language | Intent | Primary topic direction | Semantic support | Internal links | Metadata direction | Evidence status |
| --- | --- | --- | --- | --- | --- | --- | --- |

Also define:

- Topic clusters and content gaps
- Page overlap or cannibalization risks
- URL direction and localization requirements
- Structured-data opportunities as recommendations, not guarantees
- Research requirements for unavailable metrics

## 8. Mobile content strategy

Define by page or journey:

- First-screen user understanding
- First-screen proof or trust
- Primary CTA visibility and commitment level
- Content moved higher or lower
- Content compressed or progressively disclosed
- Content removable without decision loss
- Long Persian label and mixed-direction risks
- Slow-connection or device constraints only when evidenced

## 9. UX Design Input

End with a standalone handoff that the UX/UI process can consume directly:

### Users and journeys

- Primary user priorities
- Primary tasks and decision sequence
- Entry, success, failure, and recovery paths

### Hierarchy

- Page hierarchy
- Section hierarchy
- Content priorities
- CTA hierarchy
- Trust hierarchy

### Constraints

- Mobile priorities
- Persian/RTL and mixed-direction constraints
- Localization and market divergence
- SEO and internal-link constraints
- Accessibility-sensitive content
- Required content dependencies and unresolved decisions

### UX freedom

- Content order that must remain fixed
- Content that may be grouped, collapsed, or rearranged
- Optional material that may be removed
- Visual and interaction decisions intentionally left to UX/UI

## 10. Quality gate

Report each as `Pass`, `Needs validation`, or `Blocked`:

- Market and audience definition
- Evidence/assumption separation
- Positioning and conversion logic
- Sitemap and journey coherence
- Page and section justification
- Persian-native content decisions
- International/localization model
- SEO architecture
- Mobile hierarchy
- UX handoff completeness

List only material unresolved risks after the gate.
