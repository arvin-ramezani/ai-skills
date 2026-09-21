# Product Information Model

Use this reference to translate user goals and domain meaning into concepts, objects, relationships, capability groups, navigation, and findability requirements.

## Build a user-facing glossary

For each concept, define the preferred term, plain-language meaning, synonyms, current labels, prohibited labels, locale differences, and evidence. Resolve:

- One term used for multiple concepts
- Multiple terms used for one concept
- Backend terms exposed without user meaning
- Role-specific terms that could cause cross-role confusion
- Status names that mix lifecycle, outcome, and system state

Do not rename stable domain terms merely for novelty.

## Model information objects

An information object is something users recognize, find, inspect, compare, relate, or act on. It is not automatically a database table.

For each object, identify:

- User purpose
- Primary identifier and disambiguating attributes
- Ownership or responsibility
- Status and lifecycle concepts
- Related objects
- Activity, history, or provenance users need
- Sensitive, restricted, unavailable, or derived information
- Role and locale differences

Distinguish:

- Object identity from display name
- Current status from historical activity
- Ownership from access permission
- Relationship from containment
- User-facing concept from implementation entity

## Describe relationships

Use user language such as `belongs to`, `contains`, `associated with`, `generated from`, `assigned to`, or `supersedes`. Record direction and multiplicity only when they affect comprehension or navigation.

Do not infer database cardinality, foreign keys, or service ownership. Flag them as engineering questions if necessary.

## Organize capabilities

Group capabilities by the user's purpose and mental model. Test each proposed group:

- Does the label predict what users will find?
- Does the group serve one coherent purpose?
- Can an item belong in more than one place through contextual access without duplicating its canonical meaning?
- Is the group stable as features evolve?
- Does it mirror an internal team or code module without helping users?

Separate canonical ownership from multiple valid entry points.

## Design navigation layers

| Layer | Purpose |
| --- | --- |
| Global | Move among major product purposes or workspaces |
| Local | Move within one capability area or object context |
| Contextual | Reach information or actions related to the current object/task |
| Utility | Access account, help, notifications, settings, or system-wide tools |
| Cross-object | Follow meaningful relationships between objects |

Define destinations and relationships, not component patterns.

## Architect lists and details

For a collection, define the decision users make, recognition fields, scan/compare priorities, status/risk signals, search scope, filters, sort/group requirements, and empty/no-result content.

For a detail view, define summary priority, decision-critical information, related objects, activity/history, sensitive or role-dependent content, and deeper destinations.

Avoid exhaustive field catalogs unless every field changes user comprehension. Hand exact screen composition to UX.

## Specify findability

Consider:

- Known-item versus exploratory finding
- Global versus scoped search
- Searchable objects and attributes
- Synonyms, abbreviations, codes, and localized terms
- Result disambiguation
- Filters/facets versus sorting/grouping
- Recent, pinned, or saved views
- Restricted, partial, missing, empty, and no-result states
- Cross-object navigation and return context

State requirements and rationale; do not design the search index, query language, database, or persistence model.

## Map roles and visibility

Record what each role needs to see, why, and what explanation is required when information is hidden, partial, or restricted. Distinguish:

- Product requirement
- Policy dependency
- UX explanation requirement
- Engineering enforcement responsibility

Never infer that visibility in a design constitutes authorization.
