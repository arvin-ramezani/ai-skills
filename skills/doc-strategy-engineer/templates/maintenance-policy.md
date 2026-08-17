# Documentation Maintenance Policy

**Scope:** {{project_scope}}  
**Owner:** {{owner}}  
**Last reviewed:** {{YYYY-MM-DD}}

## Canonical routes

- Agent entry: {{AGENTS.md}}
- Documentation index: {{docs/index.md}}
- Decisions: {{path}}
- Active temporary artifacts: {{path or none}}

## AI-agent memory decision

- Status: {{enabled / disabled / deferred}}
- Decision date: {{YYYY-MM-DD}}
- Reason: {{why this project does or does not need cross-session memory}}
- Revisit trigger: {{scope change, agent adoption, date, or not applicable}}
- Memory index: {{path or not applicable}}
- Session summaries: {{path or not applicable}}
- Promotion queue: {{path or not applicable}}

When enabled, memory is operational evidence—not a canonical contract. Validate and promote stable knowledge to its canonical owner; expire or archive stale summaries. When disabled, preserve this decision so agents do not ask repeatedly.

## Ownership and authority

| Knowledge type | Canonical location | Authority | Review trigger |
| --- | --- | --- | --- |
| {{...}} | {{...}} | {{...}} | {{...}} |

## Sync triggers

- Public behavior, API, schema, permission, security, architecture, or operational procedure changes.
- File moves that break traceability.
- Incidents or reviews that expose misleading or missing knowledge.
- Temporary artifacts reaching their expiry condition.

## Maintenance rules

1. Update canonical content once; update routes and links in the same change.
2. Distinguish intended contract from observed implementation.
3. Label Inferred, Unknown, and Conflict claims.
4. Prefer no documentation change when meaning and contracts remain unchanged.
5. Keep high-frequency files within their context budget or record why not.
6. Promote useful temporary findings; remove stale raw artifacts.
7. Back mechanically enforceable contracts with tests, schema, types, lint, hooks, or CI where practical.
8. When memory is enabled, summarize selectively, exclude secrets and raw noise, and promote validated durable findings.

## Temporary artifact lifecycle

| Location/type | Owner | Expiry/archive trigger |
| --- | --- | --- |
| {{research/plan/progress}} | {{...}} | {{merge/release/date/decision}} |

## Review cadence

Use risk-based triggers rather than mandatory busywork. Run targeted sync during relevant changes and a broader audit when recurring conflicts, onboarding failures, or structural growth justify it.
