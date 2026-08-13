---
title: "{{feature_name}}"
purpose: "Define the intended feature contract and traceability"
scope: "{{repository/app/package/domain}}"
audience: "engineers and coding agents"
read_frequency: "medium"
authority: "{{draft-specification|accepted-contract|current-state-description}}"
status: "{{draft|planned|active|done|superseded}}"
owner: "{{owner_or_unknown}}"
last_verified: "{{YYYY-MM-DD}}"
---

# Feature Analysis: {{feature_name}}

## Outcome

{{What this feature delivers, for whom, and why it matters in 1–3 sentences.}}

## Scope

- In: {{...}}
- Out: {{...}}
- Dependencies: {{...}}
- Repository scope: {{app/package/domain}}

## Intended contract

{{Describe accepted behavior. Label undecided points as Unknown rather than inferring them from current code.}}

## Actors and access

| Actor | Capability/scope | Restrictions |
| --- | --- | --- |
| {{actor}} | {{...}} | {{...}} |

## Primary flows

1. **{{flow}}** — Given {{context}}, when {{action}}, then {{outcome}}.
2. {{...}}

## States, failures, and recovery

| State/failure | User-visible result | System behavior | Recovery |
| --- | --- | --- | --- |
| {{...}} | {{...}} | {{...}} | {{...}} |

## Data and integration boundaries

- UI/surfaces: {{...}}
- APIs/services: {{... or Unknown}}
- Data/entities: {{... or Unknown}}
- Security/privacy: {{... or Unknown}}
- Localization/accessibility: {{... or not applicable}}

## Evidence ledger

| Claim | Level | Source | Notes |
| --- | --- | --- | --- |
| {{...}} | Confirmed/Observed/Inferred/Unknown/Conflict | {{relative path, decision, or user direction}} | {{...}} |

## Acceptance and validation

- {{Observable acceptance criterion}}
- Tests/checks: {{relative paths, planned checks, or Not Tested with reason}}

## Open decisions

- {{question}} — Why it matters: {{...}} — Owner: {{...}}

## Traceability

- Product/domain: {{relative links}}
- Decisions: {{relative ADR links}}
- Implementation: {{relative paths or TBD}}
- Tests/enforcement: {{relative paths or TBD/not applicable}}
- Operations: {{relative runbook links or not applicable}}

