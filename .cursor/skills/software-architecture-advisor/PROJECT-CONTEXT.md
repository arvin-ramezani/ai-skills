# Project Context Discovery

Use this guide for an existing project. Read the narrowest relevant sources and prefer repository evidence over assumptions.

## Source precedence

Use this order when sources disagree:

1. Explicit user requirements and accepted decisions
2. Current architecture decision records
3. Current system and product documentation
4. Deployed configuration and active implementation
5. Tests and executable contracts
6. Proposed plans and roadmaps
7. Historical or archived documents

Report material conflicts instead of silently choosing a source.

## Read only what the decision needs

Look for:

- Repository agent instructions and coding rules
- Project state or capability status
- System context and architecture documents
- Relevant feature specifications
- Architecture decision records
- Package manifests and installed dependencies
- Database schema and migration strategy
- Deployment, continuous integration, and runbook files
- Nearby implementation and tests

Do not load large documentation trees when one focused source answers the question.

## Establish current reality

Separate:

- Current and deployed
- Implemented but incomplete
- Approved target
- Proposed and undecided
- Retired or migration debt

The presence of code does not prove it is the intended architecture. The presence of a proposal does not authorize inventing its contracts.

## Identify boundaries

Confirm:

- Presentation ownership
- Business workflow ownership
- Data ownership and source of truth
- Authentication and authorization ownership
- External integration boundaries
- Background work and realtime ownership
- Deployment and operational ownership

Treat undocumented boundaries as unknown, not permission to place logic anywhere.

## Existing stack

Prefer established dependencies and conventions when they satisfy the requirement. Before recommending a new dependency or platform:

1. Verify the capability is not already available.
2. Identify the current requirement it satisfies.
3. Compare operational and learning cost.
4. Define adoption, migration, and rollback.
5. Request approval when the choice changes project architecture.

## Missing context

If expected files or repositories are unavailable:

- Search the active workspace for equivalent names and concepts.
- State what could not be verified.
- Ask the user only when the missing information can materially change the decision.
- Continue with labeled assumptions when the risk is low.
