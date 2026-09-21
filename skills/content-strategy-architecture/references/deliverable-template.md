# Website Content Architecture Deliverable

Use only the sections needed by the project. Omit irrelevant fields instead of generating filler.

## Contents

1. Status and decision basis
2. Executive content strategy
3. Market and localization model
4. Sitemap and navigation
5. Decision journeys
6. Page architecture
7. SEO architecture
8. Mobile priorities
9. Visual communication requirements
10. UX/UI handoff
11. Quality gate

## 1. Status and decision basis

Start with:

- Status: `Provisional` or `Final`
- Scope, version, and date
- Canonical product context: location, accountable owner, version/date, and applicable surfaces
- Surface-ownership map for mixed public and functional products
- Confirmed facts and supplied evidence
- Research findings with citations
- Assumptions and hypotheses
- Decisions and rationale
- Critical unknowns or contradictions
- Research or validation still required

Do not label the architecture final while critical unknowns remain.

### Traceability IDs

When the work continues into UX, screen specifications, or implementation checks, assign stable IDs such as `PAGE-###`, `SEC-###`, and `REQ-###`. Preserve an ID across revisions unless the underlying decision is replaced; mark retired IDs instead of silently reusing them.

## 2. Executive content strategy

Define concisely:

- Primary and secondary markets
- Primary audience and meaningful secondary segments
- Core problem, desired outcome, and decision context
- Positioning and value proposition
- Differentiation and prohibited claims
- Primary and secondary conversions
- Messaging pillars
- Brand voice and editorial rules
- Trust and proof strategy
- Content exclusions and governance constraints
- Success signals and measurement dependencies

## 3. Market and localization model

Choose `Shared`, `Localized`, or `Market-specific`, then justify the choice.

| Dimension | Primary market/language | Secondary market/language | Relationship | Evidence or rationale |
| --- | --- | --- | --- | --- |
| Audience | | | Shared / localized / market-specific | |
| Positioning | | | | |
| Terminology | | | | |
| Proof and trust | | | | |
| Objections | | | | |
| Conversion | | | | |
| Search intent | | | | |
| Support/transaction context | | | | |

Classify content as `Shared`, `Translated`, `Rewritten`, `Market-specific`, or `Omitted` where locale behavior matters.

## 4. Sitemap and navigation

Provide only the relevant artifacts:

- Page inventory or sitemap
- Primary, secondary, utility, and footer navigation
- Parent-child and cross-link relationships
- Entry pages and decision destinations
- Public versus authenticated boundaries

| ID | Page | Purpose | Audience | Primary intent | Conversion role | Parent/entry | Locale behavior |
| --- | --- | --- | --- | --- | --- | --- | --- |

Use Mermaid only when branching relationships are materially clearer than a table.

## 5. Decision journeys

| Stage | User question | Entry/context | Required content | Proof or objection | Next action | Exit/failure path |
| --- | --- | --- | --- | --- | --- | --- |

Separate journeys only when audience, market, or offer differences change the decision path.

## 6. Page architecture

Create one block per major page.

### `[PAGE-### — Page name]`

| Field | Decision |
| --- | --- |
| ID | PAGE-### |
| Purpose | |
| Primary audience | |
| Main user question | |
| Search intent | |
| Business goal | |
| Primary conversion | |
| Secondary conversion | |
| Key message | |
| Required proof/trust | |
| Objections | |
| SEO role/topic | |
| Internal links | |
| Locale behavior | |
| Dependencies/unknowns | |

Then define ordered sections:

| ID | Order | Section | Communication job | Required content | Priority | Mobile treatment | Locale behavior |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SEC-### | 1 | | | | Critical / Important / Supporting / Optional | Keep / compress / disclose / move / remove | Shared / translated / rewritten / market-specific / omitted |

Do not prescribe component type, visual styling, animation, or exact layout unless a content constraint makes it necessary.

## 7. SEO architecture

| Page/topic | Market/language | Intent | Topic direction | Semantic support | Internal links | Metadata direction | Evidence status |
| --- | --- | --- | --- | --- | --- | --- | --- |

Also define relevant topic clusters, gaps, overlap risks, URL/localization direction, structured-data opportunities, and research requirements. Do not invent quantitative metrics.

## 8. Mobile priorities

Define by page or journey:

- First-screen understanding
- First-screen proof or trust
- Primary action visibility and commitment level
- Content moved higher or lower
- Content compressed or progressively disclosed
- Content removable without decision loss
- Long Persian label and mixed-direction risks
- Slow-connection or device constraints only when evidenced

## 9. Visual communication requirements

Include both justified opportunities and significant no-asset decisions.

| Area | Communication need | Text sufficient? | Potential asset category | Evidence/source required | Text-only fallback | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| | Understand / demonstrate / prove / compare / explain / orient | Yes / No / Uncertain | Screenshot / diagram / data view / comparison / photograph / video / none | | | Critical / Important / Supporting / Optional |

For each non-text opportunity, state why it could materially improve comprehension or trust. Do not specify aesthetics, composition, exact placement, dimensions, or final asset choice.

## 10. UX/UI handoff

End with a standalone handoff.

### Users and decisions

- Primary audience priorities
- Decision sequence and content questions
- Entry, conversion, exit, and failure contexts

### Fixed content decisions

- Page and section hierarchy
- Content, conversion, trust, and SEO priorities
- Required terminology and locale behavior
- Mandatory dependencies and proof
- Canonical product-context reference and material decision/requirement IDs

### Visual communication brief

- Communication needs and potential asset categories
- Required source material or evidence
- Areas where text is sufficient or no asset is recommended
- Confirmation that final asset and presentation decisions remain downstream

### Constraints

- Mobile priorities
- Persian/RTL and mixed-direction constraints
- Localization and market divergence
- Accessibility-sensitive content
- Dependencies, unknowns, and validation work
- Conflicts escalated to the canonical-context owner and their resolution status

### Downstream freedom

- Content order that must remain fixed
- Content that may be grouped, collapsed, or rearranged
- Optional material that may be removed
- Visual and interaction decisions intentionally delegated

### Next-stage ownership

- `ux-flow-designer`: detailed flows, states, validation, recovery, and interaction behavior
- Visual/UI specialist: visual direction, layout, components, asset selection, and design system
- Engineering: implementation architecture and instrumentation

## 11. Quality gate

Report each as `Pass`, `Needs validation`, or `Blocked`:

- Scope, audience, evidence, and conversion definition
- Positioning and message hierarchy
- Sitemap, navigation, and journey coherence
- Page and section justification
- Trust and proof requirements
- Persian-native and localization decisions
- SEO architecture
- Mobile hierarchy
- Visual communication assessment
- UX/UI handoff completeness
- Ownership-boundary compliance
- Canonical-context and traceability compliance when applicable

List only material unresolved risks.
