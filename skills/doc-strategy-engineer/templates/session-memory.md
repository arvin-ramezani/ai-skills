---
title: "{{YYYY-MM-DD}} — {{task_or_session_name}}"
purpose: "Preserve a concise cross-session engineering handoff"
scope: "{{repository/app/package/domain/feature}}"
audience: "coding agents and engineers"
read_frequency: "on-demand"
authority: "operational-memory"
status: "{{active|completed|blocked|superseded}}"
owner: "{{owner_or_unknown}}"
last_verified: "{{YYYY-MM-DD}}"
expiry: "{{condition_or_date}}"
---

# Session Memory: {{task_or_session_name}}

## Outcome

{{What was accomplished or why the session stopped.}}

## Scope and changes

- Scope: {{...}}
- Changed paths/systems: {{...}}
- Explicitly untouched: {{...}}

## Decisions and evidence

| Decision or finding | Status | Evidence/canonical owner | Promotion action |
| --- | --- | --- | --- |
| {{...}} | Confirmed/Observed/Inferred/Unknown/Conflict | {{path/test/user direction}} | Promote/link/keep temporary |

## Validation

- Checks run: {{...}}
- Result: {{...}}
- Not validated: {{...}}

## Lessons and failed approaches

- {{Keep only recurring value; omit raw debugging history.}}

## Open work and next step

1. {{Concrete next action}}

## Lifecycle

- Promotion candidates: {{... or none}}
- Expire/archive when: {{...}}
- Supersedes: {{relative link or none}}
