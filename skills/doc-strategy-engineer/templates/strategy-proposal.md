# Documentation Context Architecture Proposal

**Scope:** {{repository/app/package/domain}}  
**Date:** {{YYYY-MM-DD}}  
**Mode:** propose

## Recommendation

**Model:** {{Centralized / Code-adjacent / Hybrid}}  
**Why:** {{Evidence-based reason tied to repository shape, ownership, retrieval, and maintenance capacity.}}

## Knowledge model

| Knowledge | Canonical owner | Audience | Read frequency | Authority |
| --- | --- | --- | --- | --- |
| {{...}} | {{path/layer}} | {{...}} | {{...}} | {{...}} |

## Proposed structure

```text
{{Only directories/files justified by current needs}}
```

## Routing and selection

- Root route: {{AGENTS.md behavior}}
- Documentation index: {{path and scope}}
- App/package indexes: {{only if needed}}
- Expected retrieval path: {{entry → index → scoped doc → evidence}}

## Context budgets

| Document type | Target | Soft max | Split/merge rule |
| --- | ---: | ---: | --- |
| {{...}} | {{...}} | {{...}} | {{...}} |

## WSCI implementation

- Write: {{what becomes durable and where}}
- Select: {{how task-scoped retrieval works}}
- Compress: {{how duplication/history/raw output is reduced}}
- Isolate: {{how research/plans/progress expire or hand off}}

## Conflict and authority policy

{{Define intended-contract sources, current-state evidence, uncertainty labels, and decision ownership.}}

## Migration plan

| Order | Action | Risk | Approval | Validation |
| ---: | --- | --- | --- | --- |
| 1 | {{...}} | {{...}} | {{needed/not needed}} | {{...}} |

## Expected outcome

- {{Discovery improvement}}
- {{Correctness/authority improvement}}
- {{Context-cost reduction}}
- {{Maintenance impact}}

## Decisions required

- [ ] {{Only material choices that require user/owner approval}}

