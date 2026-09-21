# Product Information Architecture Deliverable

Use only the sections needed by the product. Omit irrelevant fields rather than generating boilerplate.

## Contents

1. Status and decision basis
2. Product, users, and scope
3. Terminology and concepts
4. Information objects and relationships
5. Capability organization
6. Navigation architecture
7. Lists, details, and findability
8. Roles and visibility
9. Content, localization, and RTL
10. Visual communication requirements
11. UX design handoff
12. Quality gate

## 1. Status and decision basis

- Status: `Provisional` or `Final`
- Scope, version, and date
- Confirmed facts and supplied evidence
- Research findings with source, date, and confidence
- Assumptions and hypotheses
- Recommendations awaiting decision
- Decisions and rationale
- Critical unknowns or contradictions
- Validation still required

Do not label the architecture final while critical product meaning remains unresolved.

## 2. Product, users, and scope

Define:

- Product purpose and boundaries
- In-scope and excluded capabilities
- Platforms and operating contexts
- Roles and primary goals
- High-frequency, high-risk, or high-value tasks
- Current pain points and workarounds
- Accessibility, device, density, and regulatory constraints
- Existing UX, design-system, and engineering dependencies

| Role | Goal | Primary tasks | Frequency/risk | Information needed | Evidence status |
| --- | --- | --- | --- | --- | --- |

## 3. Terminology and concepts

| Concept | Preferred user-facing term | Definition | Synonyms/current labels | Avoid | Role/locale variance | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

Flag collisions where one term represents multiple concepts or multiple terms represent the same concept.

## 4. Information objects and relationships

| Object | User purpose | Primary identifier | Recognition attributes | Status/lifecycle | Relationships | Sensitive/conditional information |
| --- | --- | --- | --- | --- | --- | --- |

Describe relationships in user-facing language. Use a compact diagram only when cardinality or branching is materially clearer visually. Label implementation details as engineering dependencies rather than IA decisions.

## 5. Capability organization

| Capability group | User purpose | Included capabilities | Primary roles | Related objects | Boundary/rationale |
| --- | --- | --- | --- | --- | --- |

Group by user purpose, not current code modules or database ownership.

## 6. Navigation architecture

Define global, local, contextual, utility, and cross-object navigation where relevant.

| ID | Item/destination | Navigation layer | User purpose | Eligible roles | Parent/context | Entry points | Naming rationale |
| --- | --- | --- | --- | --- | --- | --- | --- |

Also document:

- Default landing destinations by role when required
- Cross-object pathways
- Context preservation requirements
- Recent, pinned, or saved destinations when justified
- Public/authenticated or workspace/account boundaries
- Terms that must remain aligned across navigation and objects

Do not prescribe menus, tabs, drawers, breadcrumbs, or other components unless a constraint requires one.

## 7. Lists, details, and findability

### Collection/list architecture

| Collection | User decision | Primary identifier | Scan/compare information | Search scope | Filters/facets | Sort/group | Saved/recent needs | Empty/no-result content |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Detail architecture

| Object | Summary priority | Decision-critical information | Relationships to surface | Activity/history | Role-dependent content | Deeper destinations |
| --- | --- | --- | --- | --- | --- | --- |

### Cross-product findability

Define search entry points, searchable objects and attributes, result disambiguation, scope switching, partial/restricted result language, and terminology/synonym needs at the architectural level.

## 8. Roles and visibility

| Information/capability | Role | Visible? | Reason/user need | Required explanation | Policy dependency | Unknown |
| --- | --- | --- | --- | --- | --- | --- |

Treat this as a UX and product requirement. Do not claim to define or implement authorization policy.

## 9. Content, localization, and RTL

Define:

- Labels, names, descriptions, help, empty states, warnings, confirmations, and error-message categories
- Glossary and terminology governance
- Locale-sensitive dates, times, numbers, currency, units, identifiers, and addresses
- Shared, translated, rewritten, locale-specific, and omitted content
- Long-label, mixed-direction, truncation, table, chart, and sequence risks
- User-generated versus system-generated content behavior

## 10. Visual communication requirements

Include justified opportunities and meaningful no-asset decisions.

| Product area/object | Communication need | Text/data sufficient? | Potential visual category | Source/evidence required | Accessible fallback | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| | Understand / compare / monitor / verify / orient | Yes / No / Uncertain | Diagram / map / timeline / chart / screenshot / annotated example / none | | | Critical / Important / Supporting / Optional |

Do not define aesthetics, chart styling, exact placement, dimensions, or final asset choice.

## 11. UX design handoff

End with a standalone handoff.

### Fixed IA decisions

- Roles, goals, concepts, terminology, and scope
- Object and relationship model
- Capability groups and navigation layers
- List, detail, search, filter, sort, and grouping requirements
- Role visibility and locale constraints

### Content requirements

- Required labels and microcopy categories
- Empty, no-result, restricted, partial-data, warning, and help content
- Terminology governance and localization requirements

### Visual communication brief

- Communication needs and potential visual categories
- Live-data, source-material, evidence, permission, and freshness dependencies
- Areas where text/data is sufficient or no visual is recommended
- Confirmation that final visual decisions remain downstream

### Dependencies and unknowns

- Policy, domain, research, engineering, analytics, or legal dependencies
- Assumptions and validation tasks
- Contradictions requiring owner decisions

### Downstream freedom

- Information priorities that must be preserved
- Groupings or sequences open to UX exploration
- Component and layout decisions intentionally delegated

### Next-stage ownership

- `ux-flow-designer`: flows, states, permissions interactions, validation, failures, recovery, save/resume, and acceptance criteria
- Visual/UI specialist: layout, components, visual direction, asset selection, and design system
- Engineering: services, data models, APIs, authorization enforcement, search implementation, analytics events, and performance

## 12. Quality gate

Report each as `Pass`, `Needs validation`, or `Blocked`:

- Scope and role definition
- Evidence/assumption separation
- Terminology coherence
- Object and relationship model
- Capability grouping
- Navigation and findability
- List and detail information priorities
- Role visibility requirements
- Localization, Persian, and RTL handling
- Visual communication assessment
- UX handoff completeness
- Ownership-boundary compliance

List only material unresolved risks.
