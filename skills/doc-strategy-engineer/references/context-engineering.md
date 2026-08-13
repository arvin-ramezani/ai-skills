# Context Engineering Model

Use this reference to design context flow, document metadata, and size budgets. Treat the values as starting heuristics, not universal limits.

## Contents

- WSCI operating loop
- Context failure modes
- Persistent and temporary knowledge
- Phase isolation
- Metadata
- Size and read-frequency budgets
- Split, merge, and compress tests

## WSCI operating loop

### Write

Persist information only when it will improve later decisions:

| Finding | Durable destination |
| --- | --- |
| Accepted architecture choice | ADR/decision record |
| Stable product or domain rule | Product/domain doc |
| Stable repository convention | Scoped rule or `AGENTS.md` if broadly applicable |
| Reusable cross-project procedure | Skill |
| Research needed by the next phase | Temporary research artifact |
| Implementation sequence | Active plan |
| Resolved debugging lesson with recurring value | Runbook or test |

Do not persist raw logs, discarded hypotheses, copied tool output, or conversational history without a future retrieval purpose.

### Select

For each phase, ask:

1. What decision is being made now?
2. Which sources can change that decision?
3. Which source is authoritative for intent and which proves current behavior?
4. What can stay outside the context?

Prefer just-in-time retrieval. Keep a small stable routing prefix and load focused knowledge on demand. In monorepos, select the smallest relevant app/package subtree plus shared dependencies.

### Compress

Compress before, during, and after work:

- Before: use indexes, headings, targeted search, and excerpts.
- During: maintain a compact evidence ledger and phase summary.
- After: replace raw investigation with decisions, durable findings, validation results, and unresolved questions.

Preserve exact details that affect contracts, commands, paths, schemas, and acceptance criteria. Do not compress away uncertainty or conflicting evidence.

### Isolate

Use separate phase artifacts or contexts when raw exploration would distract the next phase:

| Phase | Inputs | Compact output |
| --- | --- | --- |
| Research | Request, routing rules, scoped repository evidence | `research.md` or concise findings |
| Planning | Request, research findings, relevant contracts | Implementation or documentation plan |
| Implementation | Approved plan, relevant rules, target files | Changes plus progress state if needed |
| Validation | Requirements, diff, tests, validation rules | Results, failures, residual risks |

Do not create these artifacts for trivial work. For long work, define owner, scope, status, and removal/archive condition.

## Prevent context failure modes

| Failure | Signal | Control |
| --- | --- | --- |
| Poisoning | An early error or inference is repeatedly treated as fact | Label evidence, validate external output, remove superseded hypotheses, preserve the correction |
| Distraction | Large history overwhelms the current goal | Select narrowly, summarize completed phases, unload raw output |
| Confusion | Similar rules, documents, or tools have unclear roles | Assign canonical ownership, scope sources, use descriptive names and routing |
| Clash | Sources contradict each other | Apply explicit authority, report the conflict, obtain a decision instead of silently choosing |

## Knowledge lifecycle

Classify content before placing it:

- **Persistent:** stable requirements, domain rules, architecture, accepted decisions, conventions, operations, security constraints.
- **Temporary:** investigation, tool output, hypotheses, implementation sequence, current progress, one-off migration notes.
- **Promote:** move a temporary finding to persistent knowledge only after it becomes stable and broadly useful.
- **Expire:** delete or archive temporary artifacts at their stated trigger. Never let `active/` become permanent history.

## Lightweight metadata

Use frontmatter when authority, lifecycle, ownership, or retrieval would otherwise be ambiguous. Avoid adding it mechanically to tiny obvious documents.

```yaml
---
title: Authentication refresh contract
purpose: Define browser and server token-refresh behavior
scope: apps/web authentication
audience: engineers and coding agents
read_frequency: medium
authority: accepted-contract
status: active
owner: identity
last_verified: YYYY-MM-DD
---
```

Allowed read-frequency values: `very-high`, `high`, `medium`, `low`, `on-demand`, `temporary`.

Useful authority values: `canonical-rule`, `accepted-contract`, `accepted-decision`, `current-state-description`, `operational-runbook`, `research`, `informational`.

## Size and context budgets

| Document type | Target | Soft maximum | Typical frequency |
| --- | ---: | ---: | --- |
| Root `AGENTS.md` | 40–100 lines | 120 | Very high |
| High-frequency AI rules | 30–60 | 80 | Very high |
| Framework/library rules | 40–70 | 80 | High |
| UI/design-system rules | 40–70 | 80 | High |
| Coding conventions | 40–80 | 100 | High |
| Skill `SKILL.md` | 100–200 | 250 | On trigger |
| PRD | 120–250 | 300 | Medium |
| Feature specification/FA | 80–180 | 220 | Medium |
| Architecture overview | 100–200 | 250 | Medium |
| Architecture deep dive | 150–300 | 400 | On demand |
| ADR | 50–120 | 150 | On demand |
| Research artifact | 50–150 | 200 | Temporary |
| Implementation plan | 50–150 | 200 | Temporary |
| Progress artifact | 30–100 | 120 | Temporary/high during task |
| Troubleshooting/runbook | 50–150 | 200 | On demand |
| Documentation index | 20–80 | 100 | High |

Adjust for information density, project complexity, stability, and retrieval method. Smaller is generally better for automatically loaded documents; cohesive completeness is more important for on-demand deep dives.

## Split, merge, and compress tests

Before splitting, ask whether sections differ in at least one of:

- purpose or audience;
- authority or owner;
- stability or lifecycle;
- read frequency;
- repository scope;
- retrieval pattern.

Split when independent sections are repeatedly retrieved separately or create context distraction. Merge when documents are short, share authority and lifecycle, and are almost always retrieved together.

Before increasing a soft maximum:

1. Remove duplication.
2. Replace history with the current accepted result plus a decision link.
3. Move examples and deep detail to an on-demand reference.
4. Remove stale temporary information.
5. Keep the exception only if splitting would weaken coherence.

