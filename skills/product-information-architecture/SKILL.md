---
name: product-information-architecture
description: Design evidence-led information architecture for functional software applications and complex product experiences, including CRM, ERP, SaaS apps, dashboards, admin panels, ecommerce back offices, operational tools, and multi-role products. Use for user goals and tasks, domain concepts, user-facing terminology, information objects and relationships, capability organization, global and contextual navigation, lists and detail views, findability, architectural search and filtering requirements, role-specific visibility, microcopy requirements, localization, Persian/RTL information architecture, visual communication requirements, and implementation-ready UX handoffs. Do not use for marketing-site content strategy, software or database architecture, authorization implementation, detailed UX flows, or final visual design.
---

# Product Information Architecture

Create the user-facing conceptual model, information hierarchy, navigation system, findability requirements, and handoff constraints that a downstream UX agent can turn into detailed flows and screens.

## Route the work

- Use this skill for authenticated or functional product surfaces such as CRM, ERP, dashboards, admin panels, back-office tools, and multi-role SaaS applications.
- Use `content-strategy-architecture` for public-facing marketing, ecommerce storefront, landing, corporate, editorial, and other content-led surfaces.
- For mixed products, define explicit surface ownership and one canonical product context for shared facts, approved terminology, offer and capability names, limitations, and proof.
- Require both skill outputs to cite the canonical context by location, owner, and version/date instead of redefining shared product truth independently.
- Escalate conflicts with the canonical context to its accountable product owner. Keep affected decisions provisional until that owner resolves the conflict.
- Hand detailed flows, states, validation, recovery, save/resume, edge cases, and interaction rules to `ux-flow-designer`.
- Hand visual direction, layout, component styling, asset selection, image composition, and design-system decisions to Impeccable or another visual/UI specialist.

## Apply operating principles

- Inspect supplied product, domain, user, role, workflow, support, analytics, and system material before asking questions.
- Organize information around user goals and domain meaning rather than database tables, backend services, or the current menu.
- Separate facts, evidence, assumptions, hypotheses, recommendations, decisions, contradictions, and unknowns.
- Use stable, user-facing concepts and terminology. Preserve exact machine identifiers only where users need them.
- Treat role visibility as a product requirement and handoff constraint, not an authorization implementation.
- Define search, filter, sort, grouping, and saved-view needs at the information-architecture level; do not design query engines or persistence.
- Treat Persian and RTL as information-architecture concerns, not post-design translation.
- Identify visual communication needs before proposing an asset. Many applications need no imagery beyond product data and UI itself.
- Leave detailed behavior, final UI organization, visual treatment, and engineering architecture to downstream specialists.

## Load references selectively

- Read [deliverable-template.md](references/deliverable-template.md) before producing an interim or final specification.
- Read [product-information-model.md](references/product-information-model.md) when defining domain concepts, objects, relationships, capability groups, navigation, lists/details, findability, roles, or visibility.
- Read [visual-communication-requirements.md](references/visual-communication-requirements.md) whenever assessing diagrams, maps, data visualizations, product screenshots, onboarding explanations, or a no-asset decision.
- Read [persian-product-language-and-rtl.md](references/persian-product-language-and-rtl.md) for every Persian, Iranian, bilingual Persian-English, or RTL application.
- Read [research-and-evidence.md](references/research-and-evidence.md) when information decisions depend on user research, support data, analytics, domain evidence, standards, regulation, or current product behavior.

## Establish the brief

Determine:

1. Product scope, service boundaries, platforms, and lifecycle stage
2. User roles, goals, primary tasks, frequency, risk, and decision context
3. Domain concepts, user-facing objects, vocabulary, and relationships
4. Capabilities in scope and excluded from scope
5. Current navigation, pain points, workarounds, and findability evidence
6. Role-specific information access and visibility requirements
7. Search, filtering, sorting, grouping, saved-view, and cross-object discovery needs
8. Localization, Persian/RTL, accessibility, device, and density constraints
9. Existing design-system, UX-flow, technical, regulatory, or migration constraints
10. Canonical product context, accountable owner, version/date, and surface-ownership map when the product includes both public and functional surfaces
11. Named owner and approval gate for final application UI wording
12. Exact artifact the downstream UX process needs

Maintain an internal decision ledger:

| State | Meaning |
| --- | --- |
| Fact | Directly supported by approved product material, observed behavior, or supplied evidence |
| Research finding | Observed evidence with source, date, scope, and confidence |
| Assumption | Working input not yet verified |
| Hypothesis | Testable explanation or organization opportunity |
| Recommendation | Proposed direction awaiting a decision |
| Decision | Chosen direction and rationale |
| Unknown | Material missing information |
| Contradiction | Inputs that cannot both guide the architecture |

Expose only decision-relevant ledger items.

## Run bounded adaptive discovery

Do not produce a final architecture while material product meaning is unresolved.

1. Ask one to three high-impact questions per round.
2. Ask only questions that can change scope, concepts, hierarchy, navigation, findability, visibility, terminology, localization, or handoff constraints.
3. Explain choices with concrete examples or mutually exclusive options when the user lacks IA vocabulary.
4. Do not repeat resolved questions or ask for information already present in sources.
5. Resolve contradictions between product policy, user mental models, current UI, and technical terminology.
6. Stop asking when remaining uncertainty can be documented safely as an assumption, validation task, or downstream decision.

If the user requests a provisional draft, proceed with explicit assumptions, confidence, and validation needs.

## Model product information

Work from user goals toward product structure:

1. Identify roles, goals, primary tasks, and decision points.
2. Establish the domain glossary with preferred user-facing terms, synonyms, collisions, and prohibited terms.
3. Define user-facing objects, attributes that affect recognition, and meaningful relationships.
4. Separate object identity, status, ownership, lifecycle, activity, and related records conceptually.
5. Group capabilities by user purpose rather than implementation module.
6. Design global, local, contextual, utility, and cross-object navigation.
7. Define list, detail, overview, and cross-object information priorities.
8. Define findability requirements: entry points, search scope, filters, facets, sorting, grouping, recent items, saved views, and empty/no-result guidance.
9. Map role-specific visibility and terminology differences without inventing authorization rules.
10. Assess whether visual explanations or data views could materially improve orientation, comprehension, comparison, or proof.
11. Assign stable IDs to material roles, concepts, objects, routes, and IA requirements when the work will continue into UX, screen specifications, or implementation acceptance checks.
12. Produce an implementation-ready UX handoff with fixed IA decisions, open questions, and downstream freedoms.

## Define navigation and findability

For each navigation item, object collection, or search surface, document:

- User purpose and eligible roles
- Scope and content represented
- Entry points and contextual pathways
- Relationship to global, local, contextual, and utility navigation
- Naming rationale and disambiguation needs
- Default information priorities
- Search scope and query expectations
- Filter/facet, sort, group, and saved-view requirements
- Empty, no-result, restricted, and partial-data content requirements
- Locale and RTL implications

Do not turn architectural requirements into component prescriptions. For example, require rapid switching among related records without deciding that the UI must use tabs.

## Define lists and detail views

At the architecture level, specify:

- What users must recognize, compare, scan, or decide
- Primary identifier and disambiguating attributes
- Status, ownership, recency, risk, or priority signals
- Relationships that deserve summary versus deeper access
- Information that is role-dependent, sensitive, or unavailable
- Actions whose presence affects hierarchy, without designing the interaction
- Required labels, help, empty states, warning language, and other microcopy categories

Do not prescribe database fields, API payloads, table schemas, component libraries, or exact screen layouts.

## Gate production UI wording

Define microcopy requirements and required meaning; do not leave developers to invent final labels, empty states, errors, warnings, confirmations, or help text during implementation.

- Name a `Product UI Content Owner` for the project. This may be a content designer, product owner, or an authorized writing agent whose output the product owner approves.
- Never assign the developer or implementer as Product UI Content Owner merely because no content specialist exists. Require explicit authorization and suitable accountability; otherwise mark ownership and production wording `Blocked`.
- Require final application wording to be drafted after the relevant IA and UX-flow decisions are stable.
- Record the terminology source, draft owner, approval owner, approval status, and unresolved wording dependencies in the handoff.
- Block production wording from being treated as approved when no accountable owner or approval gate exists.

## Assess visual communication without designing it

For each relevant product area or object, ask:

- What must users understand, compare, monitor, verify, or orient around?
- Can labels, prose, values, and structure communicate it sufficiently?
- Would a diagram, map, timeline, chart, screenshot, annotated example, or other non-text explanation materially improve the task?
- Is the visual derived from live product data, static source material, or evidence that must be obtained?
- What accessible text or data fallback is required?

Record communication needs and potential asset categories. Do not decide aesthetic style, chart styling, color treatment, composition, exact placement, dimensions, banner design, or final selection. Downstream UX/UI may satisfy the need without an image.

## Keep ownership boundaries explicit

Own:

- User-facing concepts and terminology
- Object and relationship model at the product-information level
- Capability grouping and navigation architecture
- Lists/details hierarchy and findability requirements
- Role-specific visibility requirements
- Content and microcopy requirements, localization, RTL, and visual communication requirements

Do not own:

- Software architecture, service boundaries, database modeling, API design, or event design
- Authorization policy implementation or permission enforcement
- Detailed flows, transitions, validation, recovery, or state machines
- Exact screen layouts, components, visual direction, or design system
- Final application UI wording unless the user explicitly authorizes drafting; approval still belongs to the named Product UI Content Owner
- Analytics event implementation

Information architecture may inform engineering architecture but never claims authority over it.

## Pass the quality gate

Before labeling work final, verify:

- Product scope, roles, tasks, concepts, evidence status, and terminology are explicit.
- User-facing objects and relationships are coherent without mirroring backend structure blindly.
- Capability groups and navigation reflect user purpose.
- Lists, details, and findability requirements support real decisions.
- Role visibility is documented without inventing enforcement logic.
- Persian/RTL and localization constraints are actionable when relevant.
- Visual opportunities are justified; applications with little or no imagery are allowed and documented.
- UX handoff includes fixed IA decisions, content requirements, boundaries, dependencies, unknowns, and validation needs.
- Mixed-surface work cites one canonical product context and escalates rather than silently resolving conflicts.
- Stable IDs preserve traceability into downstream artifacts when multi-stage delivery requires it.
- Final application wording has a named Product UI Content Owner and explicit approval gate; engineering is not the fallback copywriter.
- Detailed UX-flow, visual-design, and engineering ownership remain downstream.

If a critical concept or scope boundary remains unresolved, return to discovery or label the specification `Provisional`.

## Communicate clearly

- Match the user's language; use Persian when the user writes Persian or requests it.
- Explain IA choices in plain language without expecting the user to supply design terminology.
- Use tables for exact mappings and compact diagrams only when relationships are materially clearer visually.
- Keep the final specification detailed enough for an independent UX agent and concise enough to stay operational.
