# Documentation Strategy Engineer — Install Guide

## What This Is
A reusable agent skill that analyzes your project and documentation, then designs (or improves) a documentation strategy optimized for AI fluency and human maintainability.

## Best Practice Applied
- **Existing docs:** Report-only analysis and proposals. No silent edits.
- **New/empty projects:** Auto-creates a minimal starter structure.
- **Maintenance:** Periodic revalidation via a reusable prompt. Changes applied only after approval.

## Installation

### 1. Copy the skill into your project
Place all files in:
```
skills/doc-strategy-engineer/
```

### 2. Route AGENTS.md to use it
Add to your project's `AGENTS.md`:
```markdown
## Documentation & Architecture
When analyzing documentation, suggesting doc strategy, auditing docs, or syncing docs with code changes, use the `/doc-strategy-engineer` skill.
```

### 3. (Optional) Add a doc convention rule
Create a scoped agent rule for docs, for example `docs-conventions.md`:
```markdown
---
description: Documentation conventions for this project
glob: "docs/**/*.md"
---
- Follow the documentation architecture defined in docs/00-index.md
- Default to English for chat and engineering docs; Persian only for optional customer-facing copy or when explicitly requested
- Link to implementation files using relative paths
- Keep docs under 300 lines; split if larger
- Tag uncertain claims as [Inferred] or [Unknown]
- Update docs/99-maintenance.md when structural changes occur
```

## Usage Workflows

### First Time — Undocumented Project
```
/doc-strategy-engineer bootstrap
```
Creates starter docs + maintenance blueprint.

### First Time — Existing Docs
```
/doc-strategy-engineer analyze
```
Produces analysis report + asks clarifying questions.

After you answer:
```
/doc-strategy-engineer propose
```
Produces strategy proposal (report only).

After you approve:
```
/doc-strategy-engineer bootstrap
```
Implements the approved structure.

### Ongoing Maintenance
```
/doc-strategy-engineer audit
```
Health check. Produces `doc-audit-report.md`.

```
/doc-strategy-engineer sync
```
Post-change revalidation. Produces `doc-sync-proposal.md`.

### Periodic Revalidation (Manual)
Copy the prompt from `templates/revalidation-prompt.md` and run it in an agent chat with your latest git diff.
