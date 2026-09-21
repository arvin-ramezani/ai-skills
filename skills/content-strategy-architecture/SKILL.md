---
name: content-strategy-architecture
description: Design evidence-led content strategy and information architecture for public-facing, content-driven digital experiences, including marketing websites, SaaS websites, ecommerce storefronts, landing pages, corporate sites, content-heavy sites, and multilingual websites. Use for business and audience discovery, positioning, messaging, sitemap and navigation, page and section purpose, conversion architecture, SEO, trust, localization, Persian-native and RTL content, mobile priorities, visual communication requirements, and implementation-ready UX handoffs. Do not use for authenticated application information architecture, detailed UX flows, final visual design, or copy-only requests unless strategy or architecture is also required.
---

# Content Strategy & Architecture

Create the evidence, content decisions, and public-site architecture that downstream UX and UI design can implement without inventing product or business intent.

## Route the work

- Use this skill for public-facing marketing, commerce, editorial, and other content-led surfaces.
- Use `product-information-architecture` for functional applications such as CRM, ERP, dashboards, admin panels, and operational products.
- For a mixed product, assign each surface to one skill and define one canonical product context for shared facts, approved terminology, offer and capability names, limitations, and proof.
- Require both skill outputs to cite the canonical context by location, owner, and version/date instead of redefining shared product truth independently.
- Escalate conflicts with the canonical context to its accountable product owner. Keep affected decisions provisional until that owner resolves the conflict.
- Hand detailed task flows, states, validation, recovery, permissions behavior, and interaction logic to `ux-flow-designer`.
- Hand visual direction, aesthetics, layout, component styling, asset selection, image composition, and design-system decisions to Impeccable or another visual/UI specialist.

## Apply operating principles

- Inspect supplied sources before asking questions.
- Separate facts, research findings, assumptions, hypotheses, recommendations, decisions, contradictions, and unknowns.
- Treat audience beliefs and competitor patterns as hypotheses until supported by evidence.
- Integrate positioning, conversion, trust, SEO, localization, mobile priorities, and accessibility-sensitive content into the architecture.
- Treat Persian as a native content system rather than translated English.
- Default to the user's stated market and language. If none is stated and the context is Iranian, use `Iranian market -> Persian content -> RTL experience` as a documented working assumption, not a universal default.
- Keep copy strategy distinct from complete production copy. Write full copy only when explicitly requested or authorized.
- Identify communication needs before proposing an asset. Never assume that a page needs an image.
- Leave final visual and interaction decisions to downstream specialists.

## Load references selectively

- Read [deliverable-template.md](references/deliverable-template.md) before producing an interim or final specification.
- Read [visual-communication-requirements.md](references/visual-communication-requirements.md) whenever assessing imagery, screenshots, diagrams, comparison visuals, proof assets, or a no-image decision.
- Read [persian-content-system.md](references/persian-content-system.md) for every Persian, Iranian, bilingual Persian-English, or RTL task.
- Read [research-and-evidence.md](references/research-and-evidence.md) whenever market, audience, competitor, search, pricing, regulatory, or technology claims require external evidence.

## Establish the brief

Inspect product and business documents, current pages, analytics, research, brand guidance, content inventories, repository instructions, constraints, and prior decisions. Then determine:

1. Business model, offer, scope, and primary conversion
2. Primary audience, problem, knowledge, objections, alternatives, and decision context
3. Product capabilities, limitations, differentiation, and required proof
4. Markets, languages, locale priority, and launch boundaries
5. Existing content, evidence, gaps, constraints, and governance
6. Search goals and available first-party search data
7. Brand voice, editorial preferences, and prohibited claims
8. Mobile and accessibility-sensitive content constraints
9. Canonical product context, accountable owner, version/date, and surface-ownership map when the product includes both public and functional surfaces
10. Exact artifact the downstream UX/UI process needs

Maintain an internal decision ledger:

| State | Meaning |
| --- | --- |
| Fact | Directly supported by the user, product, analytics, or authoritative source |
| Research finding | Externally observed evidence with source, date, scope, and confidence |
| Assumption | Working input not yet verified |
| Hypothesis | Testable explanation or opportunity |
| Recommendation | Proposed direction awaiting a decision |
| Decision | Chosen direction and rationale |
| Unknown | Material missing information |
| Contradiction | Inputs that cannot both guide the architecture |

Expose only the decision-relevant parts of the ledger.

## Run bounded adaptive discovery

Do not jump to a final specification when material inputs are missing.

1. Ask one to three high-impact questions per round.
2. Ask only questions whose answers can change scope, hierarchy, positioning, conversion, localization, evidence, or handoff constraints.
3. Explain choices with brief examples or mutually exclusive options when the user lacks design vocabulary.
4. Do not repeat resolved questions or ask for information already present in supplied sources.
5. Resolve material contradictions before finalizing.
6. Stop asking when remaining uncertainty can be documented safely as assumptions, validation work, or downstream freedom.

If the user requests speed or a provisional draft, proceed with explicit assumptions, confidence, and validation needs. Never disguise provisional work as final.

## Research only when it changes a decision

Start from a decision question rather than a broad topic. Prefer first-party evidence, product behavior, authoritative sources, and current primary sources. Treat competitor pages as market observations, not proof of user needs.

Never invent search volume, keyword difficulty, rankings, traffic, conversion, pricing, audience preferences, or competitor behavior. Label unsupported needs as `Research required` and state the method, market, timeframe, and decision the research will inform.

## Design the architecture

Work in this order:

1. Define audience, positioning, value proposition, messaging pillars, voice, and conversion hierarchy.
2. Map primary decision journeys and the questions content must answer.
3. Create the page inventory, sitemap, navigation, and contextual pathways.
4. Assign each major page one primary purpose, audience, intent, and conversion role.
5. Order sections from user need and decision sequence, not a generic landing-page formula.
6. Assign required content, proof, objections, trust, dependencies, internal links, and locale behavior.
7. Classify content as `Critical`, `Important`, `Supporting`, or `Optional`.
8. Define mobile first-screen understanding, compression, progressive disclosure, and removable material.
9. Define SEO topics, intent, semantic relationships, URL direction, headings, metadata direction, and internal links without keyword stuffing.
10. Assess visual communication needs and record justified opportunities or explicit no-asset decisions.
11. Assign stable IDs to material pages, sections, and requirements when the work will continue into UX, screen specifications, or implementation acceptance checks.
12. Produce a standalone UX/UI handoff containing implementation-relevant decisions and clearly delegated freedoms.

For every major page, define:

- Purpose, audience, user question, business goal, and search intent
- Primary and secondary conversion actions
- Ordered sections and each section's job
- Key message, content requirements, proof, and objections
- SEO role, topic direction, and internal links
- Content priority and mobile treatment
- Locale behavior and Persian/RTL constraints when relevant
- Visual communication need, potential asset category, source/evidence requirement, priority, and text-only fallback
- Dependencies, unknowns, and validation needs

Use the schemas in [deliverable-template.md](references/deliverable-template.md). Scale the output to the project and omit irrelevant fields rather than filling them with boilerplate.

## Assess visual communication without designing it

For each relevant page or section, ask:

- What must the user understand, believe, compare, verify, or orient around?
- Can text communicate it sufficiently?
- Would a demonstration, diagram, screenshot, data view, comparison, photograph, or other non-text asset materially improve understanding or proof?
- What verified source material is required?
- Can the requirement be satisfied without an image?

Record the communication requirement and a potential asset category, not a final design. Do not decide aesthetic style, photography versus illustration treatment, color, composition, exact placement, dimensions, banner design, or final asset selection. The downstream design agent may decide that no asset is needed.

## Keep ownership boundaries explicit

Own:

- Content strategy, positioning, messaging, public-site information architecture, page/section purpose, conversion content, SEO, trust, localization, content priorities, and visual communication requirements

Do not own:

- Complete production copy unless requested
- Detailed interaction behavior, task states, validation, or recovery
- Final UI structure, layout, component choice, visual direction, or asset selection
- Software architecture, database design, authorization implementation, or analytics instrumentation design

## Pass the quality gate

Before labeling work final, verify:

- Scope, audience, market, evidence status, and primary conversion are explicit.
- Every major page and section has a defensible job.
- Positioning, trust, conversion, SEO, and localization do not contradict one another.
- Persian content is native and RTL constraints are actionable when relevant.
- Mobile priorities are explicit enough for downstream design.
- Visual opportunities are justified by communication needs; unnecessary imagery is absent.
- Every potential asset includes a source/evidence requirement and text-only fallback when relevant.
- UX/UI handoff includes fixed decisions, downstream freedoms, dependencies, unknowns, and validation needs.
- Mixed-surface work cites one canonical product context and escalates rather than silently resolving conflicts.
- Stable IDs preserve traceability into downstream artifacts when multi-stage delivery requires it.
- The skill has not absorbed detailed UX-flow or visual-design ownership.

If a critical input remains unresolved, return to discovery or label the specification `Provisional`.

## Handle copy requests

Default to copy requirements, message hierarchy, proof, tone, and acceptance criteria. When full copy is authorized, write it only after the relevant architecture is stable. Preserve intent and effect across languages rather than translating word for word.

## Communicate clearly

- Match the user's language; use Persian when the user writes Persian or requests it.
- Use natural Persian terminology and add English terms only when they improve precision.
- Explain design choices in plain language without expecting the user to supply design jargon.
- Keep outputs detailed enough for independent UX work and concise enough to remain operational.
