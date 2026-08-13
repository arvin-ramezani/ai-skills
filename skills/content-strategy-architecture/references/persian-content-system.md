# Persian Content System

Use this reference for Persian/Farsi, Iran-first, bilingual Persian-English, or RTL content work.

## Contents

1. Native Persian strategy
2. Language and editorial decisions
3. Locale-sensitive formats
4. RTL content implications
5. Iranian market discipline
6. Bilingual architecture
7. Quality checks

## 1. Native Persian strategy

Start with the Iranian user's task, vocabulary, context, evidence, and decision path. Do not write an English architecture first and translate it into Persian.

For each important page, independently decide:

- User intent and search intent
- Natural vocabulary and familiar technical terminology
- Required context and explanation depth
- Value proposition and objection order
- Proof and trust signals
- CTA wording and commitment level
- Information hierarchy and suitable content length

Retain an English term when the actual audience commonly uses it or when translation reduces precision. At first use, pair Persian and English only if it helps comprehension. Avoid ornamental English that makes the content less clear.

## 2. Language and editorial decisions

Define a small Persian editorial profile before drafting:

- Formal, neutral-professional, or conversational register
- `شما` versus impersonal constructions
- Direct versus indirect CTA style
- Technical vocabulary level
- Persian equivalents and approved retained English terms
- Numeral, date, currency, and punctuation conventions
- Brand-specific spellings and forbidden phrases

Write contemporary, natural Persian. Avoid literal calques, inflated official language, excessive Arabic-derived wording, conversational spelling in formal contexts, and repetitive promotional adjectives.

Normalize orthography consistently:

- Use Persian `ی` and `ک`, not Arabic `ي` and `ك`.
- Use the zero-width non-joiner where standard Persian compounds require it, such as `می‌شود` and `ثبت‌نام`.
- Keep punctuation attached to the preceding word and followed by appropriate spacing.
- Keep brand names, product codes, URLs, code, and machine identifiers exact.

Treat these as editorial choices, not universal rules. Preserve an established product glossary when it is intentional and usable.

## 3. Locale-sensitive formats

Decide formats from user task and product policy rather than applying one convention everywhere.

| Element | Decision to document |
| --- | --- |
| Numerals | Persian digits for reader-facing prose; Latin digits where code, IDs, technical data, or established product patterns require them |
| Decimal/grouping | Locale-aware separators with tested readability |
| Date | Jalali/Persian or Gregorian calendar, timezone, short/long format |
| Time | 12/24-hour choice and timezone visibility |
| Currency | Rial, toman, foreign currency, unit placement, rounding, and conversion disclosure |
| Phone/address | Display and input normalization, country code, line direction |
| Units | Persian or Latin symbols, spacing, and domain convention |

Do not silently mix toman and rial. State the unit beside prices when ambiguity is possible. Do not convert dates, currencies, or measurements without a defined product rule.

## 4. RTL content implications

Content architecture must give UX enough information to design correctly without prescribing visual styling.

Call out:

- Mixed-direction strings such as Persian text with URLs, email, numbers, product codes, commands, or English names
- Long labels likely to wrap in navigation, tabs, filters, buttons, and mobile cards
- Direction-sensitive sequences such as breadcrumbs, steps, timelines, previous/next, and comparison flows
- Tables or charts whose reading order or labels need explicit direction
- Inputs that should remain LTR inside an RTL page
- Truncation risks that can hide the meaningful end of Persian labels
- Paired Persian and English labels that are not similar in length

Use semantic `start/end` language in the handoff instead of hard-coded left/right except when physical direction is essential.

## 5. Iranian market discipline

Do not use generic cultural claims as facts. Statements such as “Iranian users are price-sensitive,” “do not trust websites,” or “always prefer mobile” are hypotheses until supported for the actual segment.

Investigate only relevant factors:

- Local competitors and alternative behaviors
- Category-specific proof and trust expectations
- Payment, invoicing, subscription, support, and purchasing norms
- Availability of required local or international services
- Connectivity, bandwidth, device, or accessibility constraints
- Legal or regulatory requirements from authoritative current sources

Record the segment and evidence behind every material market claim. If evidence is unavailable, turn the claim into a research question or validation hypothesis.

## 6. Bilingual architecture

For each page or component, classify the relationship:

| Class | Meaning |
| --- | --- |
| Shared | Same purpose, hierarchy, and content can be reused |
| Translated | Same meaning and structure; locale formatting changes |
| Rewritten | Same strategic job but different vocabulary, proof, examples, objections, or CTA |
| Market-specific | Exists or behaves differently for one market |
| Omitted | Intentionally absent in one locale |

Do not require matching paragraph counts or identical section order merely for translation symmetry. Keep navigation and product concepts aligned where possible, but allow divergence when user intent or market evidence justifies it.

For SEO, evaluate Persian and English URLs, titles, headings, queries, snippets, topic clusters, and internal links independently. Use locale-aware alternates and canonical rules only as technical handoff requirements, not invented implementation details.

## 7. Quality checks

- Read Persian aloud for natural rhythm and clarity.
- Check terminology consistency across navigation, headings, CTA, forms, and help content.
- Check Persian and English meanings, not surface word similarity.
- Check mixed-direction examples in realistic content.
- Check mobile labels and first-screen hierarchy in Persian, which may differ in length from English.
- Check numeral, date, currency, and timezone decisions against the product context.
- Mark unverified cultural or behavioral claims as hypotheses.
