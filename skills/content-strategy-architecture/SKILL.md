---
name: content-strategy-architecture
description: Design evidence-led content strategy, information architecture, page architecture, SEO structure, localization strategy, and implementation-ready UX handoffs before visual or interaction design. Use for Iranian or Persian/Farsi-first websites, products, apps, landing pages, SaaS, ecommerce, dashboards, bilingual Persian-English experiences, content redesigns, sitemaps, navigation, messaging hierarchy, conversion journeys, or pre-UX planning. Treat Iran, Iranian users, natural Persian, RTL, and Persian search behavior as the default primary context unless the user states otherwise. Do not use for copy-only requests unless strategy or architecture is also required.
---

# Content Strategy & Content Architecture

Create the content foundation that UX/UI design will implement. Establish strategy, evidence, structure, hierarchy, and localization decisions before drafting final copy or deciding visual presentation.

## Operating principles

- Default to `Iranian market -> Iranian users -> Persian content -> RTL experience` unless the user defines another priority.
- Treat Persian as a native content system, not as translated English.
- Treat audience beliefs as hypotheses until supported by user evidence or credible research.
- Separate confirmed facts, user assumptions, research findings, hypotheses, decisions, and unknowns.
- Integrate SEO, conversion, localization, mobile constraints, and trust into the architecture from the beginning.
- Preserve the user's desired brand taste unless it materially harms clarity, accessibility, usability, SEO, or conversion; then explain the tradeoff briefly.
- Aim for simple, modern, premium, creative, clear content. Reject empty claims, generic startup language, fake urgency, keyword stuffing, and AI-sounding prose.
- Keep content decisions separate from visual styling and interaction design.

Read [persian-content-system.md](references/persian-content-system.md) for every Persian, Iranian, bilingual, or RTL task. Read [research-and-evidence.md](references/research-and-evidence.md) whenever market, competitor, search, regulatory, pricing, or audience claims require external evidence. Read [deliverable-template.md](references/deliverable-template.md) before producing an interim or final architecture.

## Phase 1: establish the brief

Inspect all supplied sources before asking questions: product documents, existing pages, analytics, research, brand guidance, repository instructions, content inventories, and prior decisions.

Build an internal decision ledger with these states:

| State | Meaning |
| --- | --- |
| Confirmed | Directly supported by the user, product, analytics, or reliable evidence |
| Assumption | Claimed or implied but not yet verified |
| Hypothesis | A testable explanation or opportunity |
| Decision | Explicitly chosen direction and rationale |
| Unknown | Material missing information |
| Contradiction | Two inputs that cannot both guide the architecture |

Do not expose the full ledger unless useful. Use it to avoid repeated questions and accidental fact inflation.

Determine first:

1. Product and business model
2. Primary business goal and conversion
3. Primary Iranian user or explicitly chosen alternative
4. User problem, task, knowledge, objections, and current alternatives
5. Product capabilities and differentiators
6. Launch markets and language priority
7. Existing content, evidence, constraints, and UX/design-system context
8. SEO goals and available search data
9. Brand personality and the user's content taste
10. Exact artifact the downstream UX/UI process needs

## Phase 2: run adaptive discovery

Do not produce a final architecture immediately. Ask one to three high-value questions per turn. Prefer questions whose answers change page scope, journey, positioning, conversion, or localization.

For each round:

1. State any decision already resolved when it helps orient the user.
2. Ask only unresolved questions.
3. Offer concise examples or mutually exclusive options when the user may not know the vocabulary.
4. Update the decision ledger.
5. Identify contradictions explicitly and resolve them before continuing.
6. Stop asking when remaining unknowns are non-critical or can be documented as research tasks.

Do not ask questions already answered by supplied sources. Do not overwhelm the user with a static questionnaire. If the user requests a fast draft, create a clearly labeled provisional architecture with assumptions and validation needs; never disguise it as final.

Cover only relevant dimensions:

- Business: model, goal, conversion, commercial constraints
- Users: segments, jobs, knowledge, language, objections, alternatives
- Market: Iran segment, local competitors, category expectations, international ambition
- Product: capabilities, value, limitations, required understanding
- Brand: perception, personality, references, forbidden tones, copy density
- Content: inventory, gaps, proof, required and prohibited material
- SEO: intended demand, search intents, topic ownership, available datasets
- Localization: Persian/English launch scope, shared versus divergent journeys
- UX: platform, mobile constraints, design system, downstream handoff needs

## Phase 3: research selectively

Research only when it can change a decision. Use current primary or authoritative sources where available; use competitor pages as market evidence, not objective truth.

For Iran and Persian, investigate where relevant:

- Real user vocabulary and commonly retained English technical terms
- Persian search intent, result patterns, query variants, and local competitors
- Category-specific trust and proof expectations
- Local transaction, currency, support, service, or infrastructure constraints
- Mobile and connectivity constraints for this product's actual audience

For international markets, investigate country and language intent independently. Do not project English-market findings onto Iran.

Never invent search volume, keyword difficulty, rankings, traffic, conversion, pricing, competitor behavior, or audience preferences. Label unsupported needs as `Research required` and specify the method or data needed.

## Phase 4: choose the market architecture

Choose and justify one model:

| Model | Use when |
| --- | --- |
| Shared | Markets have materially similar tasks, hierarchy, proof, and conversion paths |
| Localized | Page structure can stay shared but messaging, terminology, proof, CTA, or SEO targeting must differ |
| Market-specific | Users, offers, regulations, journeys, or search demand require substantially different structures |

For every major divergence, record whether content is:

- Shared unchanged
- Translated with locale formatting
- Transcreated or rewritten for equivalent intent and effect
- Market-specific
- Omitted in one market

## Phase 5: design the architecture

Work in this order:

1. Define positioning, value proposition, messaging pillars, voice, and conversion hierarchy.
2. Map primary journeys and user questions.
3. Create page inventory, sitemap, navigation, and relationships.
4. Assign one primary purpose, audience, search intent, and conversion role to each major page.
5. Design section order from user need and decision sequence, not from a generic landing-page template.
6. Assign proof, objections, internal links, and localization behavior.
7. Classify each content element as `Critical`, `Important`, `Supporting`, or `Optional`.
8. Define mobile above-the-fold content, compression, progressive disclosure, persistent CTA needs, and removable material.
9. Define topic clusters, semantic relationships, page targeting, URL direction, headings, metadata direction, and internal links without keyword stuffing.
10. Produce a UX Design Input handoff containing only implementation-relevant content decisions.

For every major page, define:

- Purpose, audience, user question, business goal, and search intent
- Primary and secondary CTA
- Ordered sections and each section's job
- Key message and required supporting information
- Proof and objections addressed
- SEO role, target topic, and internal links
- Content priority and mobile treatment
- Iran/Persian requirements and international differences
- Dependencies, unknowns, and research needs

Use the exact schemas in [deliverable-template.md](references/deliverable-template.md). Scale the depth to the project; do not generate empty boilerplate for irrelevant fields.

## Phase 6: pass the quality gate

Before labeling the work final, verify:

- The primary market and users are explicit and evidence status is visible.
- Iranian context is product-specific rather than stereotyped.
- Persian is natural, intentional, and structurally native.
- Every major page and section has a defensible job.
- Conversion hierarchy does not overpower clarity or trust.
- SEO is integrated and unsupported metrics are absent.
- Shared, translated, rewritten, market-specific, and omitted content are distinguished.
- Mobile hierarchy is explicit enough to design without inventing priorities.
- UX Design Input contains page, section, CTA, trust, mobile, localization, SEO, and dependency constraints.
- Critical contradictions and unknowns are resolved.

If a critical input remains unresolved, return to discovery or label the deliverable `Provisional`. Never call it final.

## Copywriting boundary

Default to strategy, architecture, and hierarchy. Do not write complete production copy unless the user explicitly requests it.

When copy is requested, write only after the relevant architecture is approved. Draft in this order: headlines, subheadings, body, CTA, microcopy. Preserve meaning, intent, positioning, and emotional effect across languages; do not translate word for word.

## Interaction style

- Keep discovery short, precise, structured, and non-repetitive.
- Respond in Persian when the user writes Persian or requests Persian; otherwise follow the user's language.
- Use natural Persian terminology, with English terms in parentheses only when they improve precision.
- Keep final architecture detailed enough for UX and implementation, but remove explanatory filler.
