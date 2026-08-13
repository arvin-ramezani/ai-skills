---
name: doc-strategy-engineer
description: Design, audit, bootstrap, and maintain context-efficient project documentation for AI-assisted software development. Use when documenting a feature or behavior, choosing canonical document placement, creating or restructuring a docs system, improving AGENTS.md routing, onboarding to an undocumented repository, resolving documentation conflicts or drift, planning documentation for a monorepo, or syncing docs after code changes. Also use when the user asks for AI-readable documentation architecture, Feature Analysis (FA), documentation context budgets, or Cursor/coding-agent documentation strategy. Do not use for grammar-only edits with no structural, authority, or placement impact.
---

# Documentation Strategy Engineer

Treat documentation as a context system, not a collection of Markdown files. Create the smallest structure that gives humans and agents the right authoritative information at the right time.

## Route the request

Choose one primary mode. Combine modes only when the request clearly requires it.

| Intent | Mode | Default mutation |
| --- | --- | --- |
| Document a feature or phase | `document-feature` | Write requested docs |
| Assess documentation health | `analyze` | Report only |
| Design a better architecture | `propose` | Report only |
| Create an initial docs system | `bootstrap` | Write after scope is clear |
| Check an established strategy | `audit` | Report only |
| Evaluate drift after code changes | `sync` | Report unless updates were requested |

If the prompt combines feature work with documentation, use `document-feature`; do not substitute a general analysis report.

## Establish the context envelope

Before reading broadly, define:

- repository, application/package, domain/feature, and task scope;
- requested output and allowed mutations;
- intended audience and language;
- current behavior versus intended contract;
- knowledge needed now versus information that can stay unloaded.

For a monorepo, descend `repository → app/package → feature → task`. Do not load sibling applications or packages without a dependency or contract reason.

Read the narrowest useful sources in this order:

1. Applicable `AGENTS.md` or tool adapter and the nearest documentation index.
2. Task-specific rules, accepted decisions, feature/domain docs, and contracts.
3. Relevant configuration, schema, implementation, tests, and recent scoped changes.
4. Only then, broader architecture or historical material when required.

Use directory trees, headings, targeted search, and small excerpts before full-file reads. Avoid loading the entire docs tree by default.

## Engineer context with WSCI

Apply all four strategies during every substantial workflow:

1. **Write** — Persist only durable findings, accepted decisions, stable constraints, and useful phase handoffs. Keep raw tool output and dead-end attempts temporary.
2. **Select** — Retrieve only sources relevant to the current scope and phase. Prefer a small routing index over duplicated summaries.
3. **Compress** — Replace repeated, stale, or verbose material with concise authoritative statements. Split by concern when independent topics are repeatedly retrieved separately.
4. **Isolate** — Separate research, planning, implementation, and validation contexts for large work. Pass compact artifacts between phases, not raw exploration history.

For the operational model, failure-mode controls, metadata, and size budgets, read [references/context-engineering.md](references/context-engineering.md).

## Preserve authority and uncertainty

Classify important claims:

| Label | Meaning |
| --- | --- |
| `Confirmed` | Proven by an accepted contract/decision or verified system evidence |
| `Observed` | Present in implementation or behavior; intent is not established |
| `Inferred` | Reasonable interpretation that still needs verification |
| `Unknown` | Evidence is insufficient |
| `Conflict` | Authoritative sources disagree or intent and behavior diverge |

Do not use a single source-of-truth slogan to hide conflicts. Separate:

- **intended contract:** current user direction, accepted specifications, ADRs, and approved contracts;
- **current state:** schema, configuration, executable tests, implementation, and runtime evidence;
- **explanation:** maintained documentation;
- **hypothesis:** inference.

When sources conflict, name both, state their authority and freshness, avoid encoding either as settled truth, and request a decision when the result changes behavior or architecture. Never turn an observed bug into the documented contract merely because code currently behaves that way.

## Choose the canonical layer

Place each fact once and route to it elsewhere. Read [references/document-architecture.md](references/document-architecture.md) before proposing, bootstrapping, or restructuring.

Use these defaults unless sound project conventions say otherwise:

| Information | Canonical layer |
| --- | --- |
| Always-needed repository rules and navigation | `AGENTS.md` |
| Tool-specific compatibility | Thin adapter pointing to canonical instructions |
| Product, domain, architecture, and project facts | Semantic directories under `docs/` |
| Feature behavior and contracts | Focused feature/domain docs |
| Architectural decisions and rationale | ADR/decision record |
| Reusable cross-project procedure | Skill |
| Mechanical enforcement | Tests, schema, lint, hooks, or CI |
| Temporary research, plan, or progress | Explicit temporary/active artifact |

Do not duplicate complete rules across layers. Keep `AGENTS.md` focused on high-frequency routing, constraints, and commands; keep business knowledge and detailed explanations in discoverable project docs.

## Run the selected mode

### `document-feature`

1. Inspect the nearest conventions, index, related domain/feature docs, implementation, and tests.
2. Reuse a sound existing location. If none exists, design the smallest coherent path needed for this feature.
3. Write the engineering document from [templates/feature-analysis.md](templates/feature-analysis.md), adapting it to local conventions rather than filling irrelevant sections.
4. Add a short Persian human-facing sibling from [templates/feature-analysis.fa.md](templates/feature-analysis.fa.md) only when requested or useful to Persian stakeholders. Keep the English engineering document authoritative.
5. Update the nearest index and stable cross-links without duplicating content.
6. Record open product questions as `Unknown`; ask before writing only when placement, audience, or intended contract is materially ambiguous.

### `analyze`

1. Inventory the scoped docs, routing files, source/test links, and repository shape.
2. Evaluate discoverability, authority, context cost, duplication, freshness, traceability, and conflict risk using [references/health-and-maintenance.md](references/health-and-maintenance.md).
3. Report evidence-backed findings with [templates/analysis-report.md](templates/analysis-report.md).
4. Do not edit files.

### `propose`

1. Establish project size, lifetime, ownership boundaries, repository shape, change rate, and agent usage.
2. Compare centralized, code-adjacent, and hybrid layouts using [references/document-architecture.md](references/document-architecture.md).
3. Define routing, canonical ownership, document budgets, metadata policy, temporary-artifact lifecycle, and migration order.
4. Produce [templates/strategy-proposal.md](templates/strategy-proposal.md). Do not apply it without authorization.

### `bootstrap`

1. Gather enough product, repository, audience, and lifecycle context to avoid inventing structure. Ask only for missing choices that materially change the design.
2. Choose the smallest architecture that supports current needs. Create semantic directories only when they have real content.
3. Create a compact index, minimum core docs, feature/decision templates only if useful, maintenance policy, and a short `AGENTS.md` route.
4. Mark unknown facts; do not fill templates with invented product content.
5. Validate discoverability from `AGENTS.md → index → relevant doc` in no more than two routing hops.

### `audit`

Evaluate the implemented strategy against [references/health-and-maintenance.md](references/health-and-maintenance.md). Classify findings as Critical, High, Medium, Low, or Informational. Include split/merge candidates, unused documents, repeated retrieval pairs, stale temporary artifacts, and misplaced rules.

### `sync`

1. Scope the relevant diff, release, PR, or changed paths.
2. Map changes to public behavior, contracts, decisions, operations, and links.
3. Propose `update`, `create`, `archive/delete`, or `no action` for each impacted doc.
4. Prefer `no action` when meaning and contracts did not change.
5. Apply small requested updates; ask before deletion, broad restructuring, or unresolved contract choices.

## Control document growth

Assign every substantial document a purpose, audience, scope, authority, status, read frequency, and context budget—explicitly in metadata when useful, otherwise as a design decision.

Treat line budgets as heuristics, not correctness rules. When a document exceeds its soft maximum:

1. Remove duplication and obsolete material.
2. Move temporary or historical content to the correct lifecycle layer.
3. Split only when concerns, audiences, authority, stability, or retrieval patterns differ.
4. Exceed the budget with a recorded reason when cohesion would otherwise suffer.

Never split mechanically by page count. Never keep a frequently loaded routing file large merely because the model can technically ingest it.

## Mutation boundaries

Apply without another approval when the user requested the exact write, including a feature document, bootstrap, index entry, or link repair.

Ask before:

- deleting or archiving substantive documents;
- changing canonical ownership or the overall architecture;
- merging/splitting or relocating more than three existing files;
- declaring an unresolved business rule, security contract, or architecture decision;
- rewriting large existing documents beyond the stated request.

Preserve unrelated user changes. Do not change application code unless requested.

## Validate and report

Before finishing a write:

- verify paths and relative links;
- verify each key claim's evidence label;
- verify current state is not mistaken for intended contract;
- verify indexes route without repeating content;
- verify metadata and budgets match actual read frequency;
- search for obvious duplication and contradictions in the affected scope;
- verify temporary artifacts have an owner or cleanup condition;
- report files changed, checks performed, unvalidated areas, conflicts, and remaining unknowns.

Use `templates/maintenance-policy.md` when a project needs an explicit ongoing policy. Keep final reports concise and lead with the outcome.

