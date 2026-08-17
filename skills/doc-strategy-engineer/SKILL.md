---
name: doc-strategy-engineer
description: Design, audit, bootstrap, retrofit, and maintain context-efficient project documentation and optional long-term AI-agent memory for software development. Use when documenting a feature or behavior, choosing canonical document placement, creating or restructuring a docs system, improving AGENTS.md or tool-adapter routing on already-started projects, fixing undiscoverable existing docs, onboarding to an undocumented repository, adding cross-session coding-agent memory, capturing decisions or lessons from agent sessions, resolving documentation conflicts or drift, planning documentation for a monorepo, or syncing docs after code changes. Also use for AI-readable documentation architecture, Feature Analysis (FA), documentation context budgets, or Cursor/coding-agent documentation and memory strategy. Do not use for grammar-only edits with no structural, authority, placement, or memory impact.
---

# Documentation Strategy Engineer

Treat documentation as a context system, not a collection of Markdown files. Create the smallest structure that gives humans and agents the right authoritative information at the right time.

## Route the request

Choose one primary mode. Combine modes only when the request clearly requires it.

| Intent | Mode | Default mutation |
| --- | --- | --- |
| Document a feature or phase | `document-feature` | Write requested docs |
| Improve docs on an already-started project | `retrofit` | Patch routing before rewrite |
| Add or improve cross-session AI-agent memory | `memory-layer` | Write after the memory decision is confirmed |
| Assess documentation health | `analyze` | Report only |
| Design a better architecture | `propose` | Report only |
| Create an initial docs system | `bootstrap` | Write after scope is clear |
| Check an established strategy | `audit` | Report only |
| Evaluate drift after code changes | `sync` | Report unless updates were requested |

If the prompt combines feature work with documentation, use `document-feature`; do not substitute a general analysis report.

On repositories that already have `AGENTS.md`, adapters, indexes, or docs, prefer **`retrofit`** (audit → fix routing) when the problem is discoverability or missing high-frequency pointers—not an empty tree. Do not jump to broad rewrite, `bootstrap`, or unscoped `document-feature` until routing gaps for **existing** facts are addressed. Details: [references/retrofit-routing.md](references/retrofit-routing.md).

## Run the memory checkpoint

Never silently forget the memory option during architecture-level documentation work.

Before `bootstrap`, `retrofit`, or `propose`:

1. Look for an existing memory decision in the user's request, `AGENTS.md`, the documentation index, or the maintenance policy.
2. Treat `enabled`, `disabled`, and `deferred` as valid decisions. Preserve an existing decision unless the user asks to revisit it or the project scope materially changes.
3. If no decision exists and the work will create or materially change the documentation system, ask one concise question before writing: **“Should this project include a persistent AI memory layer for cross-session decisions, lessons, and handoffs? (Yes / Not now)”**
4. Record the answer in the maintenance policy or nearest canonical documentation index so later agents do not ask repeatedly.
5. If the task is report-only (`analyze` or `audit`), do not block the report. State whether memory is enabled, disabled, deferred, or undecided and recommend the next action.

Do not interrupt a small `document-feature` or routine `sync` task with the question unless memory is explicitly requested, the existing memory decision requires action, or the task is also changing the documentation architecture.

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
| Cross-session agent memory | Separate scoped memory area with a compact index; never the canonical contract |
| Raw session/conversation evidence | Temporary storage with an expiry or summarization trigger |
| Temporary research, plan, or progress | Explicit temporary/active artifact |

Do not duplicate complete rules across layers. Keep `AGENTS.md` focused on high-frequency routing, constraints, and commands; keep business knowledge and detailed explanations in discoverable project docs. Thin adapters must **name** high-frequency conventions and link to owners—they must not only deep-link into large docs without stating what agents should load when.

## Run the selected mode

### `retrofit`

For already-started projects. Full procedure: [references/retrofit-routing.md](references/retrofit-routing.md).

1. Inventory scoped `AGENTS.md`, tool adapters, and indexes.
2. Find facts that **exist** but fail two-hop discoverability (`adapter/AGENTS → index → doc`).
3. Patch thin adapters and indexes so high-frequency conventions are named and routed; do not rewrite deep docs first.
4. Only then run `document-feature`, content expansion, or `propose` restructuring for remaining gaps.
5. Report routing patches separately from new content needs.
6. Run the memory checkpoint; when enabled, add the memory layer only after canonical routing and authority are clear.

### `memory-layer`

Use only after the user enables memory or explicitly requests it. Read [references/agent-memory.md](references/agent-memory.md) before designing or changing the layer.

1. Reuse the project's existing AI/context directory when sound; otherwise choose the smallest scoped location that does not compete with canonical `docs/`.
2. Create a compact memory index, summarized session records, and a promotion queue using [templates/session-memory.md](templates/session-memory.md). Do not persist complete conversations by default.
3. Route agents to load the memory index at session start and retrieve only summaries relevant to the current task.
4. At compaction or session end, capture outcomes, decisions, lessons, validation, open work, and next steps; exclude secrets and raw noise.
5. Validate candidate facts before promoting stable requirements, decisions, runbooks, or enforcement into their canonical project layers.
6. Define expiry, archive, deduplication, contradiction, and health-check rules. Memory must be replaceable evidence, not a second source of truth.

### `document-feature`

1. Inspect the nearest conventions, index, related domain/feature docs, implementation, and tests. If this domain’s existing facts are undiscoverable from the nearest adapter/index, fix that route first (or include the route patch with the FA).
2. Reuse a sound existing location. If none exists, design the smallest coherent path needed for this feature.
3. Write the engineering document from [templates/feature-analysis.md](templates/feature-analysis.md), adapting it to local conventions rather than filling irrelevant sections.
4. Add a short Persian human-facing sibling from [templates/feature-analysis.fa.md](templates/feature-analysis.fa.md) only when requested or useful to Persian stakeholders. Keep the English engineering document authoritative.
5. Update the nearest index and stable cross-links without duplicating content.
6. Record open product questions as `Unknown`; ask before writing only when placement, audience, or intended contract is materially ambiguous.

### `analyze`

1. Inventory the scoped docs, routing files, source/test links, and repository shape.
2. Evaluate discoverability, authority, context cost, duplication, freshness, traceability, and conflict risk using [references/health-and-maintenance.md](references/health-and-maintenance.md). Explicitly list existing facts that fail two-hop routing.
3. Report evidence-backed findings with [templates/analysis-report.md](templates/analysis-report.md). Recommend `retrofit` when routing gaps dominate.
4. Do not edit files.

### `propose`

1. Establish project size, lifetime, ownership boundaries, repository shape, change rate, and agent usage.
2. Compare centralized, code-adjacent, and hybrid layouts using [references/document-architecture.md](references/document-architecture.md).
3. Define routing, canonical ownership, document budgets, metadata policy, temporary-artifact lifecycle, and migration order. Prefer routing fixes for undiscoverable-existing facts before tree moves.
4. Run the memory checkpoint and include the resulting `enabled`, `disabled`, `deferred`, or `undecided` state in the proposal.
5. Produce [templates/strategy-proposal.md](templates/strategy-proposal.md). Do not apply it without authorization.

### `bootstrap`

1. Gather enough product, repository, audience, and lifecycle context to avoid inventing structure. Ask only for missing choices that materially change the design.
2. Run the memory checkpoint before choosing the final structure.
3. Choose the smallest architecture that supports current needs. Create semantic directories only when they have real content.
4. Create a compact index, minimum core docs, feature/decision templates only if useful, maintenance policy, and a short `AGENTS.md` route. If memory is enabled, also create only the minimum memory surfaces justified by [references/agent-memory.md](references/agent-memory.md).
5. Mark unknown facts; do not fill templates with invented product content.
6. Validate discoverability from `AGENTS.md → index → relevant doc` in no more than two routing hops.
7. If a usable docs or routing system already exists, switch to `retrofit` instead of scaffolding a parallel tree.

### `audit`

Evaluate the implemented strategy against [references/health-and-maintenance.md](references/health-and-maintenance.md). Classify findings as Critical, High, Medium, Low, or Informational. Include split/merge candidates, unused documents, repeated retrieval pairs, stale temporary artifacts, misplaced rules, and **existing facts that fail two-hop discoverability**. Report the memory decision. If memory is enabled, audit it with [references/agent-memory.md](references/agent-memory.md). When routing gaps dominate, recommend `retrofit` before rewrite.

### `sync`

1. Scope the relevant diff, release, PR, or changed paths.
2. Map changes to public behavior, contracts, decisions, operations, and links.
3. Propose `update`, `create`, `archive/delete`, or `no action` for each impacted doc.
4. Prefer `no action` when meaning and contracts did not change.
5. If memory is enabled, promote validated durable findings to canonical docs and keep session summaries operational rather than authoritative.
6. Apply small requested updates; ask before deletion, broad restructuring, or unresolved contract choices.

## Control document growth

Assign every substantial document a purpose, audience, scope, authority, status, read frequency, and context budget—explicitly in metadata when useful, otherwise as a design decision.

Treat line budgets as heuristics, not correctness rules. When a document exceeds its soft maximum:

1. Remove duplication and obsolete material.
2. Move temporary or historical content to the correct lifecycle layer.
3. Split only when concerns, audiences, authority, stability, or retrieval patterns differ.
4. Exceed the budget with a recorded reason when cohesion would otherwise suffer.

Never split mechanically by page count. Never keep a frequently loaded routing file large merely because the model can technically ingest it.

## Mutation boundaries

Apply without another approval when the user requested the exact write, including a feature document, bootstrap, retrofit routing/index/link repair, or index entry.

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
- verify high-frequency conventions are named in thin adapters/`AGENTS.md`, not only buried in deep docs;
- verify metadata and budgets match actual read frequency;
- search for obvious duplication and contradictions in the affected scope;
- verify temporary artifacts have an owner or cleanup condition;
- verify the memory decision is recorded for architecture-level work;
- when memory is enabled, verify summaries are selectively routed, secrets are absent, contradictions are visible, and stable facts are promoted to canonical owners;
- report files changed, checks performed, unvalidated areas, conflicts, and remaining unknowns.

Use `templates/maintenance-policy.md` when a project needs an explicit ongoing policy. Keep final reports concise and lead with the outcome.
