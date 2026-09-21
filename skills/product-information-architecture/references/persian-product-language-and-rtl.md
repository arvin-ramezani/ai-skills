# Persian Product Language and RTL Information Architecture

Use this reference for Persian/Farsi, Iran-first, bilingual Persian-English, or RTL applications.

## Model concepts natively in Persian

Start with the user's task and established domain language. Do not finalize an English taxonomy and translate it afterward.

For each concept, navigation label, object name, status, filter, and action:

- Identify the natural Persian term used by the actual audience.
- Retain English when it is the precise and familiar domain term.
- Record synonyms used in search or legacy UI.
- Avoid literal translations that distort product meaning.
- Keep machine identifiers, URLs, code, and product codes exact.

Define an approved glossary with preferred terms, retained English, abbreviations, status labels, and prohibited alternatives.

## Handle locale-sensitive values

Document policy for:

- Persian versus Latin digits
- Jalali/Persian versus Gregorian dates
- Timezone and 12/24-hour display
- Rial, toman, and foreign currency
- Decimal/grouping separators and units
- Phone numbers, addresses, postal codes, IDs, and account numbers
- User-entered versus normalized stored values

Do not silently mix rial and toman or convert values without an explicit product rule.

## Expose RTL architecture constraints

Identify:

- Mixed Persian/LTR identifiers, email, URLs, code, commands, and product names
- Long navigation, filter, status, action, and column labels
- Breadcrumb, step, timeline, comparison, and previous/next reading order
- Tables with mixed-direction values and horizontally dense scanning
- Search inputs or values that should remain LTR
- Truncation risks that hide the meaningful end of a label or identifier
- Charts, diagrams, icons, and screenshots with directional meaning
- Locale variants whose labels differ substantially in length

Use semantic `start/end` terminology. Preserve exact physical directions only where the domain requires them.

## Support bilingual architecture

Classify information as:

| Class | Meaning |
| --- | --- |
| Shared | Same concept, purpose, and hierarchy |
| Translated | Same meaning and structure with locale formatting |
| Rewritten | Same purpose but different terminology, explanation, or microcopy |
| Locale-specific | Exists or behaves differently for one locale |
| Omitted | Intentionally absent in one locale |

Do not force identical label length, grouping, or explanation depth. Preserve concept identity while allowing locale-appropriate language.

## Check application language

- Use Persian `ی` and `ک` and intentional zero-width non-joiners.
- Check terminology across navigation, objects, lists, details, filters, statuses, actions, help, empty states, and errors.
- Test realistic mixed-direction identifiers and long labels.
- Check that search can recognize approved synonyms and retained English terms where required.
- Check localized screenshots, diagrams, and visual labels.
- Mark cultural or behavioral claims as hypotheses unless evidenced for the actual segment.
