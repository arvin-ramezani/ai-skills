# Documentation Architecture and Placement

Use this reference for `propose`, `bootstrap`, monorepo work, or any restructuring decision.

## Contents

- Layer responsibilities
- Architecture options
- Selection factors
- Adaptive baseline structures
- Index and traceability rules
- Monorepo scoping
- Migration rules

## Keep layers distinct

| Layer | Put here | Keep out |
| --- | --- | --- |
| `AGENTS.md` | Always-needed constraints, navigation, canonical commands, scoped loading rules | Product detail, long explanations, temporary plans, duplicated framework manuals |
| Tool adapter such as `CLAUDE.md` | Minimal import/route required by the tool | A second copy of canonical instructions |
| Skill | Reusable procedure and expert workflow | Project-specific facts that change with one repository |
| Project docs | Product, domain, feature, architecture, contracts, decisions, operations | Generic workflow already supplied by a skill |
| Enforcement | Tests, schema, types, lint, hooks, CI | Prose-only rules that must be mechanically guaranteed |
| Temporary artifacts | Research, active plan, progress, handoff | Stable facts without an expiry/promotion decision |

## Architecture options

### Centralized

Keep product, architecture, features, decisions, and operations under `docs/`.

Choose when the project is small/medium, ownership is shared, onboarding matters, and a single entry point improves discovery.

Risk: drift from implementation. Control it with stable relative links, ownership, and sync checks.

### Code-adjacent

Keep focused feature/package docs next to their implementation and maintain a small repository map.

Choose when services/packages have strong independent ownership or release cycles.

Risk: system knowledge fragments. Control it with a global index and centralized decisions/architecture.

### Hybrid

Centralize strategic knowledge and decisions; keep tactical package or feature details near code.

Choose for long-lived monorepos, multi-application platforms, or independently owned domains. Do not call hybrid the automatic default; it costs more routing discipline.

## Selection factors

Score the actual repository rather than team size alone:

- single app versus monorepo/microservices;
- ownership and release boundaries;
- project lifetime and expected growth;
- feature coupling and shared contracts;
- frequency of code movement;
- onboarding and cross-domain reading needs;
- agent usage and retrieval behavior;
- quality of existing conventions;
- regulatory/audit requirements;
- maintenance capacity.

Prefer the least complex option that keeps canonical ownership clear and relevant knowledge reachable within two routing hops.

## Adaptive baseline

Create directories only when they contain meaningful documents. A modest centralized project may use:

```text
AGENTS.md
docs/
├── index.md
├── product.md
├── architecture.md
├── features/
├── decisions/
└── operations.md
```

A hybrid monorepo may use:

```text
AGENTS.md
docs/
├── index.md
├── product/
├── architecture/
├── decisions/
└── operations/
apps/
├── web/docs/
└── admin/docs/
packages/
└── auth/docs/
```

Do not scaffold empty taxonomies merely to match either example. Reuse a sound existing semantic structure even if names differ.

## Index design

Keep each index a routing map. For every entry, state the document's purpose in one short phrase. Do not repeat its contents.

Target retrieval:

```text
AGENTS.md → repository index → scoped document → implementation/test
```

Allow a package index between repository index and document in large monorepos. Avoid long chains of nested indexes.

## Traceability

Link by stable relative path, not line number. Use links that answer:

- Which product/domain requirement does this feature implement?
- Which accepted decision constrains it?
- Where is current implementation evidence?
- Which tests or checks enforce the contract?
- Which operational runbook owns failures?

Do not require every document to link to code and tests. Product narratives and ADRs may link to affected domains instead. Feature contracts and runbooks should usually link to relevant implementation or enforcement.

## Monorepo scoping

- Keep repository-wide rules at the root.
- Put app/package-specific rules near that scope and route to them from the root.
- Centralize shared contracts and decisions that affect multiple packages.
- Keep package internals local unless consumers must understand them.
- State dependency direction and cross-package contracts; do not duplicate each consumer's summary of the same contract.
- Search only the target scope plus its shared dependencies during task execution.

## Migration rules

1. Inventory canonical candidates and inbound links.
2. Resolve contradictions before moving content.
3. For already-started projects, fix undiscoverable-existing facts via thin adapters/indexes before rewriting or relocating trees ([retrofit-routing.md](retrofit-routing.md)).
4. Choose the future owner for each knowledge item.
5. Migrate high-risk misleading content first, then routing, then cleanup.
6. Update indexes and links in the same change.
7. Preserve history through version control; avoid permanent archive trees unless readers need old versions.
8. Obtain approval before deletions or broad relocations.

