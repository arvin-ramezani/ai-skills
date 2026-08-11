# Documentation Strategy Engineer — Install Guide

## What This Is
Analyzes project dirs and docs, decides where/how to document work, writes Feature Analysis (FA) docs in the right place, and bootstraps a docs tree for new or not-yet-started projects (after clarifying questions).

## Best Practice Applied
- **Feature + this skill:** Scan → place **or design** a small best-practice layout → write eng FA; add Persian human FA when stakeholders need it. Ask only if context is too thin.
- **Structure design:** PROPOSE/BOOTSTRAP design best-practice trees (Decision Matrix); not ask-by-default.
- **Strategy / audit / sync:** Report-first; large restructures after approval.

## Installation

### 1. Copy the skill into your project
```
skills/doc-strategy-engineer/
```

### 2. Route AGENTS.md
```markdown
## Documentation & Architecture
When documenting features (FA), choosing doc placement, bootstrapping docs, auditing, or syncing docs with code, use the `/doc-strategy-engineer` skill.
```

### 3. (Optional) Doc convention rule
```markdown
---
description: Documentation conventions for this project
glob: "docs/**/*.md"
---
- Follow docs/00-index.md
- Default English for chat and engineering docs; Persian only for optional customer copy or when requested
- New features get an FA under docs/04-features/
- Relative paths to implementation/tests; keep docs under ~300 lines
- Tag [Inferred] / [Unknown]; update docs/99-maintenance.md on structural changes
```

## Usage

### Document a feature (existing project)
```
/doc-strategy-engineer document-feature
```
Plus your feature description. Writes FA at the right path; may create a minimal docs tree if none exists.

### Not-started / empty project docs
```
/doc-strategy-engineer bootstrap
```
Asks clarifying questions, then generates the folder structure (includes FA template).

### Strategy / health
```
/doc-strategy-engineer analyze | propose | audit | sync
```
