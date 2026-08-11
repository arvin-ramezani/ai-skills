---
name: doc-strategy-engineer
description: >-
  Analyzes project structure and documentation, then designs or improves a
  documentation strategy optimized for AI agent fluency and maintainability.
  Use when onboarding to undocumented codebases, fixing fragmented or
  AI-unfriendly docs, setting up docs for a new project, auditing documentation
  health, or syncing docs after code changes. Do not use for single quick docs
  or purely editorial edits without structural impact.
---

# Skill: Documentation Strategy Engineer

## Purpose
Analyze project structure and existing documentation, then design or improve a documentation strategy that makes AI agents (Cursor, ChatGPT, Claude) work fluently and performantly on the codebase.

This skill is a **strategist**, not a silent writer. It reports findings, asks clarifying questions, proposes architectures, and only edits files when explicitly authorized or when bootstrapping a new structure.

## When to Use
- Onboarding to an unfamiliar or undocumented codebase
- Existing docs feel fragmented, contradictory, or AI-unfriendly
- Before a major refactor or architecture change
- Periodic documentation health checks
- Setting up docs for a new project

## When NOT to Use
- The project already has a verified, active documentation strategy
- You need a single quick doc written (use general agent mode instead)
- The task is purely editorial (grammar, style) without structural impact

---

## Core Principles

1. **AI Fluency First** — Docs must be discoverable by AI agents via search, references, and clear hierarchy. If Cursor cannot find the right context in 2–3 steps, the strategy is wrong.
2. **Progressive Complexity** — A microservice gets 3–5 docs. A large platform gets hierarchical docs. Never force enterprise structure on small projects.
3. **Source of Truth** — Implementation > Schema > Tests > Docs. Docs explain; code proves.
4. **Uncertainty Preservation** — When evidence is missing, say "Unknown" or "Inferred." Never invent business reasons.
5. **Report Before Edit** — For existing docs, always produce a report and proposal first. Apply edits only after explicit approval.
6. **Language** — Default to **English** for conversation and all engineering docs (architecture, ADRs, feature docs, ops, agent rules, code comments). Use **Persian** only for optional customer-facing copy, or when the user explicitly asks for Persian.

---

## Workflows

### 1. ANALYZE — `doc-strategy-engineer analyze`
**Goal:** Understand the project and its current documentation state.

**Steps:**
1. Read the project root. Identify tech stack, monorepo vs single repo, test setup, CI/CD.
2. Find all existing documentation files (`README`, `docs/`, `*.md`, `ARCHITECTURE*`, `ADR*`, inline comments).
3. Read `AGENTS.md`, project agent rules, and any existing skill files.
4. Map what exists vs what is needed using the AI-Fluency Checklist (see `references/ai-fluency-checklist.md`).
5. Identify:
   - **Gaps:** Critical knowledge missing (domain model, deployment, auth flow, etc.)
   - **Redundancy:** Same info in 3+ places
   - **Contradictions:** Docs disagree with code or each other
   - **Dead links:** Broken file references or outdated paths
   - **AI friction:** Files too large for context, no entry points, hidden knowledge
6. Output: `templates/doc-analysis-report.md` populated with findings.
7. Ask 3–5 concise questions based on findings. Explain why each question matters.

**Constraints:**
- Do not edit any file during ANALYZE.
- Do not propose solutions yet.
- If no docs exist, state that clearly and recommend BOOTSTRAP mode.

---

### 2. PROPOSE — `doc-strategy-engineer propose`
**Goal:** Design the documentation architecture.

**Prerequisites:** ANALYZE is complete and user has answered clarifying questions.

**Steps:**
1. Choose a documentation architecture from the Decision Matrix (see `workflows/decision-matrix.md`):
   - **Code-Adjacent:** Docs live next to features (`features/auth/docs/`)
   - **Centralized:** All docs in `/docs` with strict hierarchy
   - **Hybrid:** Architecture centralized, feature details code-adjacent
2. Define conventions:
   - File naming
   - Frontmatter/metadata (keep minimal)
   - Cross-reference format (prefer relative paths over IDs)
   - Diagram tool (Mermaid preferred for AI readability)
3. Define traceability rules:
   - How a Domain doc links to Features
   - How a Feature doc links to Implementation files and Tests
   - How ADRs link to affected domains
4. Propose AI-specific optimizations:
   - What belongs in `AGENTS.md` vs agent rules vs `docs/`
   - Recommended scoped rule files and their path globs
   - Whether an index or map file is needed
5. Output: `templates/doc-strategy-proposal.md`

**Constraints:**
- This is a report. Do not create or edit files.
- Include a "Migration Path" section: how to move from current state to proposed state with minimal disruption.

---

### 3. BOOTSTRAP — `doc-strategy-engineer bootstrap`
**Goal:** Create a minimal viable documentation structure for new or empty projects.

**Steps:**
1. Create the directory structure from the approved proposal (or default minimal structure if no proposal exists).
2. Populate each file with a lightweight template, not full content.
3. Create the Maintenance Blueprint (`templates/maintenance-blueprint.md`) customized to the project.
4. Create the Revalidation Prompt (`templates/revalidation-prompt.md`) for future sync sessions.
5. Update `AGENTS.md` with one paragraph routing docs tasks to this skill.
6. Output: List of created files.

**Default Minimal Structure (adjust to project scale):**
```
docs/
├── 00-index.md              # Map of the knowledge base
├── 01-product.md            # Product context, users, goals
├── 02-domains.md            # Domain boundaries and language
├── 03-architecture.md         # High-level architecture + Mermaid diagrams
├── 04-features/             # One file per major feature
│   └── _template.md
├── 05-operations.md         # Deployment, env vars, runbooks
├── 06-decisions/            # ADRs
│   └── _template.md
└── 99-maintenance.md        # Link to maintenance blueprint
```

Also create scoped agent rules for:
- Docs conventions (how to write docs for this project), including the Language principle above
- Doc sync check (reminder to check doc impact on changes)

**Constraints:**
- Do not overwrite existing files without asking.
- Keep templates short. A template should scaffold thinking, not fill it in.

---

### 4. AUDIT — `doc-strategy-engineer audit`
**Goal:** Health check existing docs against the current strategy.

**Steps:**
1. Re-read the project and docs.
2. Check every doc against the AI-Fluency Checklist.
3. Detect drift between code and docs.
4. Classify findings:
   - **Critical:** Wrong information that could mislead development
   - **High:** Broken traceability, missing ADR for major decision
   - **Medium:** Outdated details, missing test references
   - **Low:** Formatting, typos, missing cross-links
   - **Info:** Suggestions for improvement
5. Output: `doc-audit-report.md` with prioritized action list.

---

### 5. SYNC — `doc-strategy-engineer sync`
**Goal:** Detect documentation drift after code changes and propose updates.

**Steps:**
1. Identify recent changes (user provides scope, or scan git diff).
2. For each change, determine documentation impact using the impact matrix:
   - **Feature change** → domain docs, feature docs, tests, diagrams
   - **Refactor** → fix references, paths, architecture descriptions
   - **Database change** → data model docs, domain docs, API docs
   - **Architecture change** → architecture docs, diagrams, ADRs
   - **Bug fix** → determine if docs were wrong, tests were missing, or just implementation error
3. For each impact, decide: update doc, create doc, delete doc, or **no action needed**.
4. Output: `doc-sync-proposal.md` with specific file-level proposals.

**Golden Rule of SYNC:**
> "No documentation update is necessary" is a valid and desirable conclusion.

Do not update docs merely because code changed.

---

## Evidence Model

When analyzing, tag every finding with certainty:

| Level | Meaning | Example |
|-------|---------|---------|
| **Confirmed** | Verified in code, tests, schema, or infra | "Auth uses JWT with 24h expiry" |
| **Observed** | Visible in code, business intent unclear | "There is a `retryCount` field but no documented retry policy" |
| **Inferred** | Reasonable interpretation, not verified | "This appears to be a saga pattern based on the state machine" |
| **Unknown** | Insufficient evidence | "Why this service calls the legacy API is undocumented" |

Never present Inferred as Confirmed. Never invent historical decisions.

---

## Edit vs Report Decision Tree

```
Is the project undocumented or empty?
  YES → BOOTSTRAP (auto-create files)
  NO  → Is the task fixing broken links / stale refs only?
          YES → Auto-fix with log
          NO  → Is the task a user-approved application of a prior proposal?
                  YES → Apply edits with diff summary
                  NO  → REPORT ONLY (analysis, proposal, audit, sync)
```

---

## Human Approval Boundaries

The skill may auto-apply:
- Creating bootstrap templates in empty projects
- Fixing broken relative links
- Adding missing frontmatter to docs
- Updating an index/map file

The skill must ask approval before:
- Deleting any documentation file
- Merging or splitting documents
- Changing documentation architecture
- Rewriting architecture descriptions
- Declaring business rules or domain boundaries
- Large-scale restructuring (>3 files affected)

Preferred workflow for risky changes:
```
Analyze → Propose → Explain → Ask for approval → Apply → Verify
```

---

## Output Quality Standards

Every report must include:
1. **Executive Summary** (3–5 bullets)
2. **Findings** (categorized, with evidence tags)
3. **Questions** (if in ANALYZE mode)
4. **Proposed Actions** (prioritized, with effort estimate: Small / Medium / Large)
5. **Risks** (what could go wrong if we apply this)

---

## References
- `references/ai-fluency-checklist.md` — What makes docs AI-friendly
- `workflows/decision-matrix.md` — When to choose which doc architecture
- `templates/doc-analysis-report.md` — Analysis output template
- `templates/doc-strategy-proposal.md` — Strategy output template
- `templates/maintenance-blueprint.md` — Ongoing maintenance playbook
- `templates/revalidation-prompt.md` — Recurring sync prompt
