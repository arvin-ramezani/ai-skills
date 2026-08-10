# Revalidation & Sync Prompt

Use this prompt periodically (end of sprint, post-refactor, or monthly) to revalidate documentation against the current codebase.

## How to Use
1. Open an AI agent chat
2. Paste this prompt
3. Provide the scope: git diff, PR description, or "full project"
4. The AI will produce a `doc-sync-proposal.md`

---

## Prompt

```
You are the Documentation Strategy Engineer for this project.

Task: Revalidate all documentation against the current codebase state.

Context provided:
- {{paste git diff, PR changes, or state "full project revalidation"}}
- {{paste current docs/ directory tree}}
- {{paste AGENTS.md and key agent rules if changed}}

Follow the project's documentation conventions and traceability rules defined in docs/99-maintenance.md (or the maintenance blueprint).

For each significant change, determine:
1. Which docs are affected?
2. What update is needed? (update / create / delete / no action)
3. What is the evidence level? (Confirmed / Observed / Inferred / Unknown)
4. Does this require human approval before applying?

Rules:
- "No documentation update is necessary" is a valid and desirable conclusion.
- Do not update docs merely because code changed. Only update if the *meaning* or *contract* changed.
- Preserve uncertainty. If you don't know why something exists, say "Unknown" — do not invent reasons.
- Flag contradictions between docs and code as Critical.
- Flag missing docs for new public APIs or domain concepts as High.

Output format:
Produce a `doc-sync-proposal.md` with:
- Executive Summary (3 bullets)
- Changes Analyzed (list)
- Proposed Actions (prioritized table: File | Action | Reason | Effort | Needs Approval)
- No-Action Items (what changed but docs are fine)
- Critical Flags (anything that could mislead a developer)

Do not apply any edits unless explicitly instructed.
```

---

## Quick Version (for small changes)

```
Analyze the following code changes and determine documentation impact.
Use our doc conventions. Report only; do not edit.

Changes:
{{paste diff}}

Output:
- Affected docs:
- Proposed updates:
- No-action items:
- Questions:
```
