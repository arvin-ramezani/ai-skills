# Research and Evidence Protocol

Use this reference when architecture decisions depend on current market, audience, competitor, search, pricing, regulatory, or technology information.

## Begin with a decision question

Phrase the research need as `What evidence would change this architecture decision?`

Examples:

- Which Persian phrase best matches transactional intent?
- Which objections recur in support or sales evidence?
- Does a market require a different conversion journey?
- Is a real screenshot necessary to substantiate this capability?

Stop when evidence is sufficient for the decision. Do not create a generic market report unless requested.

## Prefer appropriate sources

Use, in order appropriate to the claim:

1. User-provided analytics, interviews, search data, CRM, support, and sales evidence
2. Product behavior and approved internal documentation
3. First-party platform, government, regulatory, or standards sources
4. Search results and official competitor/product pages
5. Reputable industry research with a stated method and date
6. Community discussion as qualitative signal, never population proof

Use current sources for unstable claims. Record date, market, segment, and whether the source states the claim or merely supports an inference.

## Maintain an evidence ledger

| Field | Requirement |
| --- | --- |
| Claim | Narrow, decision-relevant statement |
| Status | Confirmed / indicative / hypothesis / conflicting / unknown |
| Source | Direct link or named supplied artifact |
| Market/segment | Applicable audience, language, and geography |
| Date | Publication, dataset, or observation date |
| Confidence | High / medium / low with reason |
| Architecture impact | Page, hierarchy, message, CTA, proof, SEO, localization, or visual requirement |

Never convert a competitor pattern into a user need without supporting evidence.

## Research SEO by market and intent

Evaluate query vocabulary, intent, result patterns, content formats, semantic relationships, existing coverage, overlap, gaps, page targeting, and internal links separately by language and market.

Do not invent volume, difficulty, rank, traffic, click-through, or conversion. When tool data is unavailable, provide qualitative findings and a `Research required` plan specifying source, market, timeframe, and target decision.

## Analyze competitors as alternatives

Choose real direct and indirect alternatives. Compare audience, positioning, offer, navigation, page inventory, message, proof, objections, terminology, search targeting, and content gaps. Convert observations into opportunities, risks, or hypotheses rather than copied structures.

## Keep output decision-led

Include findings that changed a decision, conflicts and interpretation, explicit inferences, material unknowns, validation tasks, and citations beside supported claims. Exclude summaries that do not affect the architecture.
