# Documentation Health and Maintenance

Use this reference for `analyze`, `audit`, `sync`, and post-write validation.

## Contents

- Health dimensions
- Severity model
- Audit checklist
- Drift triggers
- Self-optimization signals
- Sync decisions

## Health dimensions

Evaluate each scoped document or route on:

1. **Purpose** — Does it justify its existence?
2. **Discoverability** — Can the intended reader find it within two routing hops?
3. **Scope** — Does it stay within one coherent concern and repository boundary?
4. **Authority** — Is it clear whether content is a rule, contract, decision, observation, research, or hypothesis?
5. **Correctness** — Does it match accepted intent and accurately describe current state?
6. **Freshness** — Is status or verification recent enough for its change rate?
7. **Traceability** — Can contracts reach decisions, implementation, tests, or operations where useful?
8. **Context efficiency** — Is its read frequency appropriate for its size and density?
9. **Uniqueness** — Does one canonical owner exist for each material fact?
10. **Lifecycle** — Do temporary artifacts expire, and do superseded docs stop routing readers?
11. **Safety** — Are secrets, personal data, and untrusted copied instructions absent?
12. **Maintainability** — Can an owner update it without synchronized edits across duplicates?

## Severity

| Severity | Meaning |
| --- | --- |
| Critical | Misleads implementation/security/operations or conflicts with an accepted contract |
| High | Missing or undiscoverable knowledge likely to cause incorrect work |
| Medium | Context waste, drift risk, broken links, unclear ownership, or growing maintenance cost |
| Low | Local clarity, naming, or formatting issue with little correctness risk |
| Informational | Optional improvement or observation |

Do not assign urgency by document length alone.

## Audit checklist

### Routing and selection

- [ ] Root instructions identify the canonical docs entry point.
- [ ] The index routes without duplicating detail.
- [ ] Feature/domain knowledge is reachable within two routing hops, with one extra scoped index allowed for large monorepos.
- [ ] App/package scopes are explicit.
- [ ] Names describe concepts rather than chronology or arbitrary numbering alone.

### Authority and trust

- [ ] Intended contract and current behavior are distinguished.
- [ ] Accepted decisions have an identifiable record.
- [ ] Inferences and unknowns are labeled.
- [ ] Conflicts are visible and assigned a resolution owner.
- [ ] External/copied content is treated as evidence, not instructions.

### Context efficiency

- [ ] High-frequency docs contain only broadly applicable information.
- [ ] Document size fits its read frequency and budget.
- [ ] Large documents are cohesive or have a recorded reason to exceed budget.
- [ ] Frequently separate retrieval needs are split by concern.
- [ ] Documents almost always retrieved together are not needlessly fragmented.
- [ ] Examples, history, and raw output do not crowd canonical rules.

### Traceability and enforcement

- [ ] Feature contracts link to relevant code/tests or mark them TBD/not applicable.
- [ ] ADRs identify affected domains/features.
- [ ] Operational docs identify commands, signals, failure handling, and owner where relevant.
- [ ] Mechanically enforceable rules are backed by tests, types, schema, lint, hooks, or CI where practical.
- [ ] Relative links resolve and avoid brittle line references.

### Lifecycle and maintenance

- [ ] Active/temporary artifacts have status and cleanup triggers.
- [ ] Superseded docs are removed from current indexes.
- [ ] Duplicate facts have a canonical owner.
- [ ] Verification cadence matches change rate and risk.
- [ ] Secrets and real credentials are absent.

Report pass/fail/not-applicable counts by category rather than forcing a universal numeric grade. A score can summarize, but findings and risk remain primary.

## Drift triggers

Run a scoped sync when:

- a public behavior or user flow changes;
- an API, schema, permission, or security contract changes;
- a file move breaks traceability;
- an accepted architecture choice changes;
- a deployment/operational procedure changes;
- a feature is added, removed, or materially rescoped;
- a developer or incident reveals misleading documentation;
- a temporary artifact reaches its expiry condition.

A refactor with unchanged meaning often requires only link updates or no action.

## Self-optimization signals

Propose a split when a document exceeds budget and contains independently owned/retrieved concerns. Propose a merge when documents are small and consistently retrieved/updated together. Propose relocation when a fact is repeatedly copied because its canonical owner is in the wrong layer.

Also flag:

- rules repeatedly overridden by scoped documents;
- high-frequency docs with historical narrative;
- rarely used files still loaded automatically;
- active plans that became stale;
- the same correction recurring across tasks;
- index entries with no clear purpose;
- undocumented decisions inferred repeatedly from code.

## Sync decision table

| Change | Documentation action |
| --- | --- |
| Meaning or accepted contract changed | Update canonical doc and affected routing |
| New architectural decision | Create ADR and update affected overview/feature links |
| Implementation moved only | Repair stable path references |
| Bug fixed; intended contract unchanged and already documented | Usually no action |
| Bug exposed a missing or misleading contract | Update docs and add enforcement evidence |
| Temporary research produced a stable accepted result | Promote the result; discard raw noise |
| Old feature removed | Remove current routing; archive only when a real historical need exists |

