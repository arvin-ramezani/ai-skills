# Architecture Recommendation Template

## Length rules

- Keep each section to three to five bullets by default.
- Lead with the recommendation and its reason.
- Include only alternatives that materially change the trade-off.
- Use plain language and define unfamiliar terms briefly.
- Expand a section only when risk or user intent requires it.

If a missing answer could change a security boundary, data owner, deployable, or core technology, ask the focused question first and stop. Explain why the answer matters. Do not fill a report with speculative decisions.

## Default response

```markdown
# [Decision or feature]

## Requirements and assumptions
- Business outcome:
- Confirmed constraints:
- Assumptions:
- Top quality attributes:

## Architecture recommendation
- Shape:
- Responsibilities and boundaries:
- Data ownership:
- Failure behavior:

## Data flow
[One short explanation and a Mermaid diagram when useful]

## Stack decisions
- [Layer or capability] — [choice]: [requirement-based reason]. Trade-off: [main cost].

## Trade-offs
- Accepted:
- Avoided complexity:
- Reconsider when:

## Risks
- [High/Medium/Low] [risk] — Mitigation: [action]. Signal: [evidence to watch].

## Implementation slices
1. [Small end-to-end capability and validation]
2. [Next capability and validation]
3. [Operational hardening or scale step when justified]

## Architecture Decision Records
- [Required/Not required] [ADR title]: [reason and status]

## SOLID learning notes
- [Principle]: [specific module or boundary and why it helps]
```

Omit a field only when it is irrelevant. Write “None” only when the absence is itself important.

## Diagram guidance

Choose one diagram:

- Context or container flow for system ownership
- Sequence diagram for request, integration, or retry behavior
- State diagram for lifecycle workflows
- Deployment diagram for runtime and network boundaries

Keep diagrams small. Use stable component names, directional edges, and labels for protocols or important trust transitions.

Mermaid node identifiers must not contain spaces. Quote labels that contain punctuation or parentheses. Do not add custom colors or styling.

## Stack decision format

For a meaningful technology decision, state:

```markdown
- Selected: [technology and responsibility]
- Fit: [requirement it satisfies]
- Cost: [complexity, operations, or learning]
- Alternative: [only a meaningful alternative and why it lost]
- Revisit when: [measurable trigger]
- Confidence: [High/Medium/Low] — [missing evidence, if any]
```

Do not repeat this full block for routine libraries already established by the project.

## Risk format

Prioritize risks by likelihood and impact, not by how interesting they are.

```markdown
- High: Duplicate webhook processing could repeat a paid action.
  Mitigation: Tenant-scoped idempotency key and transactional state transition.
  Signal: Duplicate delivery and rejected-transition metrics.
```

Include security, migration, operational, and product risks only when relevant.

## Compact ADR

Use the project's ADR filename and numbering policy when one exists.

```markdown
# ADR-NNNN: [Short decision title]

- Status: Proposed
- Decision date: YYYY-MM-DD

## Context and problem
[Facts, constraints, and decision forces.]

## Decision
[The selected option, boundaries, and scope.]

## Alternatives considered
- [Alternative]: [why it was not selected]

## Consequences and trade-offs
- Positive:
- Negative:
- Follow-up:

## Migration or rollback
[Incremental adoption, compatibility, rollback, and data implications.]
```

Draft a full ADR only after the recommendation is sufficiently confirmed. Before that, list the proposed ADR and the decision still needed.

## Code examples

Provide code only when it clarifies a boundary or implementation approach. Keep examples small, use descriptive names, and avoid comments that restate the code.

When demonstrating a SOLID decision, use one short why-comment:

```typescript
// DIP: keeps subscription policy independent from the payment provider.
export interface PaymentAuthorizationGateway {
  authorize(request: PaymentAuthorizationRequest): Promise<PaymentAuthorizationResult>;
}
```

Do not add an interface solely to demonstrate SOLID. A real boundary or expected implementation variation must exist.

## Commands

Introduce command blocks with one of:

- `Local — Windows PowerShell`
- `Server — Ubuntu`

Do not mix PowerShell and Bash syntax in one block.
