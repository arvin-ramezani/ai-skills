# Feature Analysis (FA)

**Feature:** {{feature_name}}  
**Slug / path:** {{path}}  
**Phase:** {{phase}}  
**Status:** Planned | In progress | Done  
**Evidence:** Confirmed / Observed / Inferred / Unknown

---

## Summary

{{1–3 sentences: what this feature delivers and for whom}}

## Scope

- **In:** {{...}}
- **Out:** {{...}}
- **Depends on:** {{modules, prior phases, Unknown}}

## Actors & Roles

| Role | Type (e.g. Admin / Sub-admin / Operator) | Notes |
|------|------------------------------------------|-------|
| {{role}} | {{type}} | {{...}} |

## Access Model

Describe **different** vs **higher** access (capabilities + privilege order). Prefer a short matrix over prose.

| Capability | Admin | Sub-admin | Operator ({{kinds}}) |
|------------|-------|-----------|----------------------|
| {{capability}} | {{Y/N/scope}} | {{...}} | {{...}} |

Hierarchy (if any):
```text
{{e.g. Main Admin → Sub-admin → Operators (design | server | data-entry | development)}}
```

## Primary Flows

1. {{flow name}} — Given / When / Then (short)
2. {{...}}

## Surfaces

- **UI / apps:** {{e.g. admin-panel}}
- **APIs / services:** {{or Unknown}}
- **Data:** {{entities or Unknown}}

## Open Questions

- {{question}} — *why it matters*

## Traceability

- Implementation: {{paths or TBD}}
- Tests: {{paths or TBD}}
- Related docs: {{index, domain, ADR}}
