# Content and Product IA Forward-Test Matrix

## Evidence status and reproduction method

These are author-run exploratory forward tests from 21 September 2026, not automated CI or an independent acceptance suite. Each scenario ran in a fresh isolated agent thread with only the named skill path and the exact prompt below. The agent was not given the expected result. Outputs were manually inspected against the listed criteria. Raw transcripts are not committed; results and ZIP validation must therefore be treated as author-reported.

To reproduce a scenario, load the skill directory at the PR head in a fresh agent context, submit the exact prompt, and compare the response with the expected observations. Natural-language wording may differ; the architectural behavior is the assertion.

## Scenario matrix

### FT-CSA-01 — Persian SaaS marketing discovery

- **Skill:** `content-strategy-architecture`
- **Prompt:** “I’m building a Persian-first SaaS marketing website for an Iranian managed WooCommerce server provider. I’m a developer, not a designer. Define the content and information architecture before UX design. We have about 90 customers, custom pricing, and consultation/migration CTAs.”
- **Expected:** Inspect confirmed inputs; ask one to three material questions instead of inventing positioning, service scope, claims, or conversion behavior; preserve Persian/RTL context.
- **Observed:** Asked three questions covering primary buyer/trigger, exact managed-service scope/proof, and conversion/language model; stated confirmed inputs; avoided invented performance or service claims.
- **Result:** PASS (author-reported). No material deviation observed.

### FT-CSA-02 — Fast bilingual storefront handoff

- **Skill:** `content-strategy-architecture`
- **Prompt:** “Create an implementation-ready content architecture for a bilingual Persian-English ecommerce storefront selling technical equipment. We have category and product data but no search research or approved claims yet. I need a fast provisional handoff for UX.”
- **Expected:** Produce a clearly provisional handoff; separate Persian/English decisions; avoid invented SEO metrics and claims; define product/category hierarchy, evidence gates, mobile priorities, and justified visual requirements.
- **Observed:** Produced a provisional localized-shared architecture with assumptions, sitemap, page hierarchy, independent locale/SEO research needs, claims governance, RTL constraints, mobile priorities, and asset/no-asset decisions.
- **Result:** PASS (author-reported). No material boundary violation observed.

### FT-PIA-01 — WooCommerce CRM

- **Skill:** `product-information-architecture`
- **Prompt:** “Design the information architecture for a WooCommerce CRM with customers, orders, stores, identity observations, notes, tags, and custom fields. There are operators and administrators. Do not design database tables or detailed flows. Produce a provisional UX handoff.”
- **Expected:** Model user-facing concepts, objects, relationships, capability groups, navigation, lists/details, findability, and role visibility while avoiding database, authorization-enforcement, detailed-flow, and final-UI design.
- **Observed:** Produced a provisional object/relationship model, capability groups, navigation, collection/detail priorities, search requirements, role visibility dependencies, and downstream boundaries; did not define database tables or detailed interactions.
- **Result:** PASS (author-reported). No material deviation observed.

### FT-PIA-02 — Multi-role incident dashboard discovery

- **Skill:** `product-information-architecture`
- **Prompt:** “I need information architecture for a multi-role incident operations dashboard used by analysts, incident commanders, and auditors. Organize concepts, navigation, lists/detail views, findability, visibility requirements, Persian/English terminology, and the downstream UX handoff.”
- **Expected:** Detect that domain/lifecycle, role-visibility policy, and locale rules materially affect the architecture; ask bounded discovery questions rather than asserting them.
- **Observed:** Asked three questions covering operational domain/lifecycle, role and visibility policy, and language/format constraints; previewed the resulting deliverable scope without inventing answers.
- **Result:** PASS (author-reported). No material deviation observed.

### FT-PIA-03 — Dense accounting app with no imagery

- **Skill:** `product-information-architecture`
- **Prompt:** “Structure a dense internal reconciliation application for accountants. Users work mainly with exact amounts, IDs, dates, statuses, exceptions, and audit history. We believe imagery would distract from the work. Produce a compact provisional information-architecture handoff.”
- **Expected:** Produce a provisional operational IA; prioritize exact data and auditability; explicitly allow a no-asset decision; avoid decorative or misleading visual requirements.
- **Observed:** Defined reconciliation objects, terminology, work/review/audit navigation, lists/details and findability, exact-value content constraints, role dependencies, and an explicit `No imagery or decorative assets recommended` decision with a bounded future reporting exception.
- **Result:** PASS (author-reported). No material deviation observed.

### FT-CSA-03 — Logistics website with visual explanations

- **Skill:** `content-strategy-architecture`
- **Prompt:** “Plan a public website for a complex logistics platform. Buyers struggle to understand the workflow, integrations, tracking, and proof of delivery. We have real product screens and verified operational data. Create a provisional content architecture and identify where non-text explanations may help, but leave visual design to the next stage.”
- **Expected:** Produce a provisional public-site architecture; identify evidence-backed diagram/screenshot/data opportunities and text/accessibility fallbacks; avoid final art direction, layout, or asset selection.
- **Observed:** Produced positioning, sitemap, decision journey, page structures, SEO direction, and a visual-requirements matrix covering workflow diagrams, product screens, integration flows, proof artifacts, and operational data with evidence and fallback requirements; delegated final visual decisions downstream.
- **Result:** PASS (author-reported). No material deviation observed.

## Review-correction scenarios

### FT-CORR-01 — Mixed-surface canonical-context conflict

- **Skill:** `content-strategy-architecture`
- **Prompt:** “We have one SaaS product with a public marketing website and an authenticated admin app. The approved product brief calls the capability ‘Incident Response’, but an app draft calls it ‘Issue Handling’. Use the website skill to create the website architecture handoff. The approved product brief is the shared source of truth, owned by the Product Owner and versioned 2026-09-20. Do not ask me to choose the terminology.”
- **Expected:** Cite the canonical source and owner; use the approved term for the website; record and escalate the app conflict without asking the requester to redefine shared truth; keep cross-surface alignment provisional.
- **Observed:** Cited the shared brief, owner, and version; used `Incident Response`; recorded the app term as a contradiction; escalated it to the Product Owner; prevented conflicting screenshots and cross-surface claims from being treated as final.
- **Result:** PASS (author-reported). No material deviation observed.

### FT-CORR-02-R1 — Missing UI wording owner

- **Skill:** `product-information-architecture`
- **Prompt:** “Create an implementation-ready IA handoff for a small operations app with Jobs, Exceptions, and Audit History. I am the only developer and we have no content designer. Include labels, empty states, errors, warnings, and help content so implementation can start.”
- **Expected:** Draft content requirements or authorized draft wording, but do not assign the developer as production wording owner without explicit authorization; keep production approval blocked when ownership is missing.
- **Observed:** The response correctly treated copy as draft and left approval unconfirmed, but assigned the developer/requester as interim Product UI Content Owner without explicit authorization.
- **Result:** FAIL (author-reported). The skill rule was ambiguous and required correction.

### FT-CORR-02-R2 — Corrected UI wording gate

- **Skill:** `product-information-architecture`
- **Prompt:** Same as `FT-CORR-02-R1`.
- **Expected:** Do not default ownership to the developer; mark owner, approval, and production wording blocked; allow only clearly marked placeholders/content keys until approval.
- **Observed:** Left Product UI Content Owner, draft owner, and approval owner unassigned; marked all production wording categories `Blocked`; explicitly prohibited defaulting ownership to the developer; allowed structural implementation only with placeholders or content keys; blocked release and acceptance pending approval.
- **Result:** PASS (author-reported) after correction.

### FT-CORR-03 — Cross-stage stable identifiers

- **Skill:** `product-information-architecture`
- **Prompt:** “Produce a provisional IA for a CRM with Customers, Orders, and Stores. This will go next to UX flows, screen specifications, and implementation acceptance tests, so make the handoff traceable across stages. Do not design database tables.”
- **Expected:** Use stable role, term, object, capability, navigation, and IA requirement IDs; define how downstream artifacts cite them; avoid database design.
- **Observed:** Produced `ROLE`, `TERM`, `OBJ`, `CAP`, `NAV`, and `IA-REQ` identifiers plus a cross-stage `Derived from` contract for flows, screen specifications, and acceptance tests; explicitly retained the database boundary.
- **Result:** PASS (author-reported). No material deviation observed.

## Overall disposition

- Structural validators and reference checks are deterministic and separately reported in the PR.
- Forward-test behavior is author-reported and manually inspected.
- One focused correction test exposed an ambiguous default owner (`FT-CORR-02-R1`); the rule was tightened and the repeated scenario passed (`FT-CORR-02-R2`). No unresolved critical scenario failure remains in this matrix.
- This matrix does not establish production quality, deterministic model behavior, or independent acceptance.
