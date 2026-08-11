---
name: doc-strategy-engineer
description: >-
  Analyzes project structure and documentation, then designs or improves a
  documentation strategy optimized for AI agent fluency and maintainability.
  Use when documenting a new feature (place and write FA/feature docs), setting
  up docs for a new or not-yet-started project, onboarding to undocumented
  codebases, auditing documentation health, or syncing docs after code changes.
  Do not use for purely editorial edits without structural or placement impact.
---

# Skill: Documentation Strategy Engineer

## Purpose
Analyze the project and its docs, decide **where and how** to document work, **design a best-practice documentation structure** when one is missing or weak, and write feature/FA docs in the right place. Bootstrap docs for greenfield or not-yet-started projects. Write engineering FAs in English and, when humans need them, a short Persian stakeholder FA.

This skill is a **strategist that designs structure and writes when placement is clear**. Prefer analyze → place → write for feature docs; use PROPOSE/BOOTSTRAP to design the tree when the project needs one.

## When to Use
- Documenting a feature or phase (e.g. admin roles) and choosing the right doc location
- Creating a docs directory for a project that has not started yet
- Onboarding to an unfamiliar or undocumented codebase
- Existing docs feel fragmented, contradictory, or AI-unfriendly
- Periodic documentation health checks / sync after code changes

## When NOT to Use
- Purely editorial edits (grammar, style) with no placement or structural impact
- The user only wants implementation code and explicitly says skip docs

---

## Core Principles

1. **AI Fluency First** — Docs must be discoverable in 2–3 steps. Wrong placement beats no strategy only if an index/map still points to them.
2. **Progressive Complexity** — Prefer a small structure. Add hierarchy only when needed.
3. **Source of Truth** — Implementation > Schema > Tests > Docs. Docs explain intent and contracts; code proves.
4. **Uncertainty Preservation** — Missing evidence → "Unknown" / "Inferred." Never invent business reasons.
5. **Place Then Write** — For feature work: inspect dirs + docs → decide path → write FA. If the layout is missing or weak, **design** a best-practice structure (Decision Matrix + progressive complexity), then write into it — do not wait for the user to invent the tree.
6. **Follow the project when it is sound** — Prefer existing good paths and naming. Skill defaults are fallbacks. Never narrate “not the skill default” in the summary.
7. **Ask only when blocked on context** — Do **not** ask when you can place a doc or design a sensible tree from the prompt + repo. Ask only if: placement is ambiguous/conflicting, **or** greenfield/not-started and the prompt lacks enough product/context to choose a best-practice structure. Product Unknowns go in the FA; they are not a pre-write quiz.
8. **Language** — Chat and **engineering** docs (including engineering FA) in **English**. For **Persian humans** (PMs, clients, non-eng stakeholders), also produce a short Persian FA (`templates/fa-feature-fa.md`) when the audience needs it or the user asks. Customer-facing product copy may be Persian when requested.

---

## Intent Router

| User intent | Mode |
|-------------|------|
| Document a feature / add FA for upcoming work | `document-feature` |
| Create / redesign docs structure | `propose` then `bootstrap`, or `bootstrap` when empty |
| Create docs for empty / not-started project | `bootstrap` (design best-practice tree; ask only if context is missing) |
| Health check existing docs | `analyze` → optional `propose` / `audit` |
| After code changes, check doc drift | `sync` |

If the prompt mixes feature work + docs (like "use doc-strategy-engineer" + feature description), run **`document-feature`**, not a report-only analyze.

---

## Workflows

### 1. DOCUMENT-FEATURE — `doc-strategy-engineer document-feature`
**Goal:** Scan → place (or design a small best-practice layout if needed) → write FA(s).

**When to ask questions (before writing):**
- Placement is ambiguous (conflicting conventions, unclear target area), **or**
- No docs tree / not-started **and** the prompt lacks enough context to design a minimal best-practice structure.

**When not to ask:** A sound place exists, **or** you can design a small best-practice tree from the prompt + repo. Write. Put product Unknowns in the FA.

**Steps:**
1. Scan root, apps, and existing docs.
2. If the project has a good convention → use it. If missing/weak → **design** a small best-practice layout (`workflows/decision-matrix.md`), create only what this FA needs, then continue.
3. Write the **engineering FA** (English) via `templates/fa-feature.md`, adapted to local note style.
4. When Persian humans need a readable summary (stakeholders, PM, client) or the user asks → also write a **Persian FA** via `templates/fa-feature-fa.md` next to it (same slug + `.fa.md` or project naming). Keep it short; no eng jargon dump.
5. Update indexes/cross-links like sibling docs.
6. Short summary: path(s) written, structure designed/created if any, indexes touched, Unknowns in FA, optional next step.

**Summary must not:** compare to skill defaults or lecture about greenfield templates.

**Constraints:** No app code unless also requested. Persian FA is for humans; English FA remains the engineering source of truth.

---

### 2. ANALYZE — `doc-strategy-engineer analyze`
**Goal:** Understand documentation health (report only).

**Steps:**
1. Identify stack, repo shape, tests, CI.
2. Inventory docs and agent rules.
3. Score against `references/ai-fluency-checklist.md`.
4. List gaps, redundancy, contradictions, dead links, AI friction.
5. Output via `templates/doc-analysis-report.md`.
6. Ask 3–5 concise questions when a later PROPOSE/BOOTSTRAP needs them.

**Constraints:** No edits. If undocumented, recommend BOOTSTRAP. If the user wanted a feature documented, switch to DOCUMENT-FEATURE.

---

### 3. PROPOSE — `doc-strategy-engineer propose`
**Goal:** Design a **best-practice** documentation architecture for this project (report only).

**Prerequisites:** Enough product/repo context, or ANALYZE + answers when context was missing.

**Steps:** Use `workflows/decision-matrix.md` (A/B/C); define naming, FA placement (eng + optional Persian human FA), links, diagrams, AGENTS.md vs rules; output `templates/doc-strategy-proposal.md` with Migration Path. Prefer the simplest tree that stays AI-fluent and maintainable.

**Constraints:** No file edits.

---

### 4. BOOTSTRAP — `doc-strategy-engineer bootstrap`
**Goal:** Create a **best-practice** docs tree for new, empty, or not-yet-started projects.

**Design, then create:** Prefer designing from Decision Matrix + prompt/repo clues. Ask clarifying questions **only** when context is too thin to choose a sensible tree (not as a default ritual).

**After design (and answers if any):**
1. Create the structure — include feature/FA space and note that Persian human FAs are optional siblings.
2. Lightweight templates only (eng FA + Persian FA templates).
3. Short `docs/99-maintenance.md` from the maintenance blueprint.
4. One-paragraph AGENTS.md route.
5. List created files.

**Default Minimal Structure:**
```
docs/
├── 00-index.md
├── 01-product.md
├── 02-domains.md
├── 03-architecture.md
├── 04-features/
│   ├── _fa-template.md         # Engineering FA (English)
│   ├── _fa-template.fa.md      # Human FA (Persian)
│   └── _template.md
├── 05-operations.md
├── 06-decisions/
│   └── _template.md
└── 99-maintenance.md
```

**Constraints:** No overwrite without asking. Templates scaffold; they do not invent product facts.

---

### 5. AUDIT — `doc-strategy-engineer audit`
Health-check vs strategy and AI-Fluency Checklist. Classify Critical → Info. Output `doc-audit-report.md`.

### 6. SYNC — `doc-strategy-engineer sync`
Map code changes to doc impact. Prefer **no action** when meaning/contracts did not change. Output `doc-sync-proposal.md`.

---

## Evidence Model

| Level | Meaning |
|-------|---------|
| **Confirmed** | Verified in code, tests, schema, or infra |
| **Observed** | Visible in code; intent unclear |
| **Inferred** | Reasonable but unverified |
| **Unknown** | Insufficient evidence |

Never present Inferred as Confirmed.

---

## Edit vs Report Decision Tree

```
Document a feature / FA requested?
  YES → DOCUMENT-FEATURE (scan → place or design small best-practice layout → write eng FA [+ Persian human FA when needed])
  NO  → Design or create docs structure / not-started?
          YES → PROPOSE and/or BOOTSTRAP (design best-practice tree; ask only if context too thin)
          NO  → Broken links / stale refs only?
                  YES → Auto-fix with log
                  NO  → User approved a prior proposal?
                          YES → Apply with diff summary
                          NO  → REPORT ONLY (analyze / propose / audit / sync)
```

---

## Human Approval Boundaries

**May apply without extra approval:**
- DOCUMENT-FEATURE writes when the user asked to document the feature
- Bootstrap after clarifying answers (or explicit "create the docs tree")
- Fixing broken relative links; adding missing index entries for new FA files

**Ask first:**
- Deleting docs; merging/splitting; changing overall architecture
- Rewriting architecture descriptions at scale; declaring unverified business rules
- Restructuring >3 existing files

---

## Output Quality Standards

For DOCUMENT-FEATURE / BOOTSTRAP summaries:
1. What was scanned
2. Path written (project convention only — no skill-default commentary)
3. Indexes / links updated
4. Unknowns recorded in the FA (not a blocking Q&A unless placement failed)
5. Optional next step

For reports (analyze/propose/audit/sync): Executive Summary, Findings, Questions (if any), Proposed Actions (S/M/L), Risks.

---

## References
- `references/ai-fluency-checklist.md`
- `workflows/decision-matrix.md`
- `templates/fa-feature.md` — Engineering Feature Analysis (English)
- `templates/fa-feature-fa.md` — Human Feature Analysis (Persian)
- `templates/doc-analysis-report.md`
- `templates/doc-strategy-proposal.md`
- `templates/maintenance-blueprint.md`
- `templates/revalidation-prompt.md`
