# Research and Evidence Protocol

Use this reference when architecture decisions depend on current market, competitor, user, search, pricing, regulatory, or technology information.

## Contents

1. Research questions
2. Source hierarchy
3. Evidence ledger
4. SEO research
5. Competitor analysis
6. Research output

## 1. Research questions

Start with a decision, not a broad topic. Phrase the research need as: `What evidence would change this architecture decision?`

Examples:

- Which Persian phrase best matches the audience's transactional intent?
- Do local competitors require a separate pricing-explanation page?
- Which objections appear repeatedly in support or sales evidence?
- Does the English market require a different conversion journey?

Stop when evidence is sufficient for the decision. Do not produce a generic market report unless requested.

## 2. Source hierarchy

Prefer, in order appropriate to the claim:

1. User-provided analytics, interviews, search data, CRM, support, and sales evidence
2. Product behavior and approved internal documentation
3. First-party platform, government, regulatory, or standards sources
4. Search-engine results and official competitor/product pages
5. Reputable industry research with a stated method and date
6. Community discussion as qualitative signal, never population proof

Use current sources for unstable claims. Record publication or observation date and applicable market. Distinguish what the source states from what is inferred.

## 3. Evidence ledger

For every material finding, record:

| Field | Requirement |
| --- | --- |
| Claim | Narrow, decision-relevant statement |
| Status | Confirmed, indicative, hypothesis, conflicting, or unknown |
| Source | Direct link or named user-provided artifact |
| Market/segment | Iran, another country, language, and audience |
| Date | Publication, dataset, or observation date |
| Confidence | High, medium, or low with reason |
| Architecture impact | Page, hierarchy, message, CTA, proof, SEO, or localization decision |

Never turn a competitor pattern into a user need without supporting evidence.

## 4. SEO research

Separate by language, market, intent, and funnel stage. Evaluate:

- Query vocabulary and variants
- Search intent: informational, commercial investigation, transactional, navigational
- Result-page patterns and content formats
- Topic entities and semantic relationships
- Existing site coverage, overlap, cannibalization, and gaps
- Page targeting and internal-link opportunities
- Title and metadata direction
- Localized versus market-specific page needs

Do not invent volume, difficulty, rank, traffic, click-through rate, or conversion. If tool data is unavailable, provide qualitative intent findings and a `Research required` plan specifying the desired source, market, timeframe, and decision it will inform.

## 5. Competitor analysis

Choose competitors by the user's real alternative set, not brand fame alone. Include local direct competitors, indirect alternatives, and international references only when relevant.

Compare:

- Audience and positioning
- Offer and conversion path
- Navigation and page inventory
- Message and proof hierarchy
- Objections and trust patterns
- Persian terminology and search targeting
- Content strengths, gaps, and sameness

Do not copy a competitor structure merely because it is common. Convert observations into opportunities, risks, or hypotheses.

## 6. Research output

Keep the final architecture decision-led. Include:

- Findings that changed a decision
- Conflicting evidence and chosen interpretation
- Explicit inferences
- Unknowns that remain material
- Research tasks with method and owner when applicable
- Citations beside supported claims

Exclude long source summaries that do not affect the architecture.
