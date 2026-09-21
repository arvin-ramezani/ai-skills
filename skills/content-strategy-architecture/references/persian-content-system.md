# Persian Content System

Use this reference for Persian/Farsi, Iran-first, bilingual Persian-English, or RTL website content.

## Start from Persian intent

Start with the Iranian user's task, vocabulary, context, evidence, and decision path. Do not create an English architecture first and translate it into Persian.

For each important page, decide independently:

- User and search intent
- Natural vocabulary and familiar technical terms
- Explanation depth and information order
- Value proposition, proof, objections, and CTA commitment
- Suitable content length and mobile priority
- Locale-specific visual evidence or screenshots

Retain an English term when the actual audience commonly uses it or translation reduces precision. Pair Persian and English at first use only when it improves comprehension.

## Define an editorial profile

Document:

- Formal, neutral-professional, or conversational register
- `شما` versus impersonal constructions
- Direct versus indirect CTA style
- Technical vocabulary level
- Approved Persian equivalents and retained English terms
- Numeral, date, currency, punctuation, and brand-spelling conventions
- Forbidden phrases and unsupported claims

Write contemporary, natural Persian. Avoid literal calques, inflated official language, excessive Arabic-derived wording, and repetitive promotional adjectives.

Normalize intentionally:

- Use Persian `ی` and `ک`, not Arabic `ي` and `ك`.
- Use zero-width non-joiners where standard compounds require them, such as `می‌شود` and `ثبت‌نام`.
- Preserve brand names, URLs, code, product identifiers, and machine values exactly.
- Follow an established product glossary when it is intentional and usable.

## Decide locale-sensitive formats

| Element | Decision to document |
| --- | --- |
| Numerals | Persian digits for reader-facing prose; Latin digits where code, IDs, technical data, or established patterns require them |
| Decimal/grouping | Locale-aware separators with tested readability |
| Date/time | Calendar, timezone, short/long format, and 12/24-hour policy |
| Currency | Rial, toman, foreign currency, unit placement, rounding, and conversion disclosure |
| Phone/address | Display normalization, country code, and direction |
| Units | Persian or Latin symbols, spacing, and domain convention |

Do not silently mix toman and rial or convert dates, currencies, or measurements without a defined rule.

## Expose RTL content constraints

Call out:

- Persian text mixed with URLs, email, numbers, product codes, commands, or English names
- Long navigation, filter, button, and mobile-card labels
- Direction-sensitive breadcrumbs, steps, timelines, and previous/next sequences
- Tables or charts whose reading order needs explicit direction
- Values or inputs that should remain LTR in an RTL context
- Truncation that can hide the meaningful end of Persian labels
- Screenshots or diagrams that require localized variants

Use semantic `start/end` terminology instead of hard-coded left/right unless physical direction is essential.

## Apply Iranian market discipline

Do not treat generic cultural claims as facts. Claims about price sensitivity, trust, mobile preference, or behavior remain hypotheses until supported for the actual segment.

Investigate only relevant factors: real alternatives, category-specific proof, payment and purchasing norms, service availability, connectivity, accessibility, and current legal requirements. Record evidence scope and date.

## Architect bilingual content

Classify each page or section as:

| Class | Meaning |
| --- | --- |
| Shared | Purpose, hierarchy, and content are materially the same |
| Translated | Meaning and structure stay the same; locale formatting changes |
| Rewritten | Strategic job is the same but vocabulary, proof, objections, or CTA differ |
| Market-specific | Exists or serves a different job in one market |
| Omitted | Intentionally absent in one locale |

Do not force matching paragraph counts or section order merely for symmetry. Evaluate Persian and English queries, headings, snippets, topics, internal links, proof assets, and visual evidence independently.

## Check quality

- Read Persian aloud for natural rhythm.
- Check terminology across navigation, headings, CTA, forms, and help content.
- Check meaning rather than surface word similarity across languages.
- Test mixed-direction examples and realistic long labels.
- Check dates, numerals, currency, and timezone decisions.
- Check that screenshots and diagrams do not embed untranslated essential content.
- Mark unverified behavioral claims as hypotheses.
