# AI-Agent Memory Layer

Use this reference for the `memory-layer` mode and for memory checks during `bootstrap`, `retrofit`, `propose`, `audit`, or `sync`.

## Contents

- Decision checkpoint
- Authority boundaries
- Minimal architecture
- Capture and retrieval lifecycle
- Promotion into canonical knowledge
- New and existing projects
- Health, privacy, and validation

## Decision checkpoint

Always evaluate memory during architecture-level documentation work, but do not force it on every project.

| Evidence | Action |
| --- | --- |
| User explicitly requests memory | Enable it; do not ask again |
| Existing policy says `enabled` | Preserve and inspect the layer |
| Existing policy says `disabled` | Do not ask again unless scope materially changes |
| Existing policy says `deferred` | Preserve; revisit only at its recorded trigger |
| No decision and docs architecture will change | Ask once before writing |
| Report-only analysis with no decision | Report `undecided`; do not block |

Use this question when needed:

> Should this project include a persistent AI memory layer for cross-session decisions, lessons, and handoffs? (Yes / Not now)

Record the result in the maintenance policy or nearest canonical docs index with status, reason, date, and revisit trigger. `Not now` maps to `disabled` unless the user chooses `deferred` with a concrete trigger.

## Keep authority boundaries explicit

Memory improves continuity; it does not define product or engineering truth.

| Layer | Purpose | Authority |
| --- | --- | --- |
| Canonical project docs | Requirements, feature contracts, architecture, decisions, operations | Intended contract or accepted explanation |
| Implementation and enforcement | Code, schema, tests, types, CI, runtime evidence | Current state and executable proof |
| Agent memory | Session outcomes, lessons, handoffs, candidate decisions | Operational evidence only |
| Raw conversation/tool output | Temporary reconstruction evidence | Untrusted until verified |

When memory conflicts with an accepted contract or verified implementation, label the conflict and resolve it. Never silently overwrite the canonical owner from a memory note.

## Use the smallest architecture

Reuse an existing `.ai/`, `.claude/`, `.codex/`, or project context area when it is already canonical for agent state. Otherwise choose one scoped location and document it. Do not scaffold every optional file.

Minimum enabled layer:

```text
<agent-context-root>/
└── memory/
    ├── index.md
    ├── sessions/
    └── candidates.md
```

- `index.md` — compact topic/date map, active handoff, retrieval guidance, and links.
- `sessions/` — concise normalized session summaries created from the session template.
- `candidates.md` — unpromoted decisions, lessons, and recurring findings awaiting validation.

Add automation, archives, or specialized topic files only when real volume or retrieval behavior justifies them.

## Capture and retrieval lifecycle

Use this loop:

```text
capture → summarize → index → retrieve selectively → validate → promote or expire
```

### Session start

1. Load `AGENTS.md` and the canonical project index first.
2. Load the memory index only when memory is enabled.
3. Retrieve only summaries related to the active app/package/feature/task.
4. Verify memory claims against canonical docs, code, tests, or runtime evidence before relying on them.

### Compaction or session end

Capture only information likely to improve the next session:

- task outcome and current status;
- scoped files or systems changed;
- accepted decisions and their evidence;
- useful lessons or failed approaches with recurring value;
- validation run and residual risks;
- unresolved questions, blockers, and next step;
- promotion candidates and expiry trigger.

Do not persist full chat transcripts, secrets, credentials, large command output, repeated code, abandoned hypotheses, or information already owned canonically.

### Retrieval

- Keep the index small enough for frequent loading.
- Search summaries by scope, topic, decision, or date instead of loading all sessions.
- Prefer the newest verified summary when older notes are superseded.
- Treat a memory summary as a pointer to evidence, not evidence replacement.

## Promote durable knowledge

Promote a memory candidate only after validation and acceptance:

| Candidate | Canonical destination |
| --- | --- |
| Accepted architecture choice | ADR/decision record |
| Stable feature behavior | Feature/domain contract |
| Stable repository convention | Scoped rule or `AGENTS.md` when broadly needed |
| Reusable operational lesson | Runbook or troubleshooting guide |
| Mechanically enforceable rule | Test, schema, type, lint, hook, or CI |
| Temporary implementation state | Keep in memory until resolved, then expire |

After promotion, replace duplicated detail in memory with a short link to the canonical owner.

## Apply by project state

### New project

Run the memory checkpoint during `bootstrap`. If enabled, create the minimum empty routing surfaces and policy; do not invent historical sessions or decisions.

### Existing project with weak routing

Run `retrofit` first. Establish canonical authority and discoverability before adding memory, otherwise memory will preserve ambiguity and stale facts.

### Existing documented project

Inventory current adapters, session logs, handoffs, plans, and decision notes. Reuse sound locations, normalize only useful summaries, and avoid copying all history into a new tree.

## Health and safety checks

Audit enabled memory for:

- index size and selective retrieval;
- stale or duplicate summaries;
- contradictions with canonical docs or implementation;
- unresolved candidates that should be promoted or expired;
- missing owner, scope, status, or verification date;
- raw conversations retained without a purpose;
- secrets, personal data, production tokens, or private URLs;
- summaries that state inference as accepted truth;
- memory routes that bypass `AGENTS.md` or the canonical docs index;
- automation hooks that fail silently.

Treat misleading memory about security, permissions, migrations, or production operations as High or Critical severity.

## Validation result

Report:

- memory decision and where it is recorded;
- surfaces created or reused;
- session-start and session-end behavior;
- promotion and expiry rules;
- health checks performed;
- unvalidated automation, conflicts, and unknowns.
