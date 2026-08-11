# AI-Fluency Checklist for Documentation

Use this checklist when analyzing a project's documentation. A "fluent" documentation system allows an AI agent to answer questions about the codebase accurately and efficiently.

## Discoverability (Can the AI find it?)
- [ ] There is a single index/map file that lists all major knowledge areas
- [ ] `AGENTS.md` or project rules point the AI toward documentation entry points
- [ ] Domain/feature docs are reachable from the index within 2 hops
- [ ] No critical knowledge exists only in closed issues, Slack, or one developer's head
- [ ] File names are descriptive (`auth-flow.md` not `doc-3.md`)

## Granularity (Is the context window used efficiently?)
- [ ] No single doc exceeds ~300 lines (AI can ingest it in one context chunk)
- [ ] Large topics are split by domain or feature, not by arbitrary page count
- [ ] Each doc has one clear owner-concept (one domain, one feature, one decision)
- [ ] Boilerplate is minimized; templates are referenced, not repeated

## Traceability (Can the AI navigate from concept to code?)
- [ ] Domain docs link to feature docs
- [ ] Feature docs link to implementation files (relative paths)
- [ ] Feature docs link to test files
- [ ] Architecture docs link to diagrams
- [ ] ADRs link to the domains/features they affect
- [ ] Code references use stable paths (not line numbers)

## Correctness (Can the AI trust it?)
- [ ] No contradictions between docs
- [ ] No contradictions between docs and code
- [ ] Outdated docs are marked or archived
- [ ] ADRs exist for major architectural decisions
- [ ] Uncertainty is stated explicitly ("Unknown why this exists")

## AI-Specific Optimizations
- [ ] `AGENTS.md` does not contain project-specific business rules (those belong in `docs/`)
- [ ] Scoped agent rules contain conventions, not generic advice
- [ ] Engineering docs and default conversation are in English; Persian human FAs / optional customer copy when needed
- [ ] Mermaid diagrams are used over image files (AI can read Mermaid)
- [ ] No password/secrets in docs (obvious but common)
- [ ] Docs are in Markdown (AI-native format)

## Scoring
- **21–23 checks:** Excellent. Minor tweaks only.
- **16–20 checks:** Good. Targeted improvements needed.
- **11–15 checks:** Fragmented. Strategy revision recommended.
- **<11 checks:** Undocumented. Use BOOTSTRAP workflow.
