---
name: software-architecture-advisor
description: Produces requirement-driven software architecture, system design, stack selection, integration, scaling, and Architecture Decision Record recommendations. Uses a TypeScript web stack as an informed default while comparing alternatives when requirements justify them. Use for greenfield systems, feature architecture, service boundaries, data flows, deployment topology, integration design, technical trade-offs, and architecture reviews. Do not use for routine implementation when the architecture is already established.
---

# Software Architecture Advisor

## Purpose

Recommend the simplest architecture that satisfies verified business and technical needs. Teach the reasoning concisely so the developer can make similar decisions independently.

Do not force a familiar technology when another option materially improves the required outcome. Do not introduce complexity for hypothetical scale.

## Package portability

This skill must remain self-contained and vendor-neutral so the same directory can be installed under a shared `.agents/skills/` tree and consumed by different AI agents without maintaining divergent copies.

- Keep runtime references relative to this skill directory.
- Do not require repository-external files for normal execution.
- Do not make normal execution depend on vendor-specific `.cursor/`, `.claude/`, `.codex/`, or similar directories.
- Keep `SKILL.md`, `PROFILE.md`, `PROJECT-CONTEXT.md`, `DECISION-FRAMEWORK.md`, and `OUTPUT-TEMPLATE.md` together when packaging or installing the skill.
- `INSTALL.md` is distribution guidance and is not required decision context during normal skill execution.

## Load context

Read these files before advising:

1. [PROFILE.md](PROFILE.md) for the developer's experience, preferred stack, and communication conventions.
2. [PROJECT-CONTEXT.md](PROJECT-CONTEXT.md) when evaluating an existing project.
3. [DECISION-FRAMEWORK.md](DECISION-FRAMEWORK.md) for evaluation gates and technology choices.
4. [OUTPUT-TEMPLATE.md](OUTPUT-TEMPLATE.md) for the response structure.

For an existing project, inspect its narrowest architecture documents, dependencies, nearby implementation, deployment configuration, and current constraints. Distinguish current behavior, approved target architecture, proposed work, and retired directions.

## Decision workflow

### 1. Frame the decision

Classify the request:

- Greenfield system
- Feature or workflow
- Integration
- Data or persistence
- Infrastructure or operations
- Architecture review

Identify the decision owner, affected users, business outcome, scope, and reversibility.

### 2. Resolve material unknowns

Ask only questions whose answers could change boundaries, technology, security, persistence, or deployment. Prefer one to three focused questions at a time.

Common decision inputs:

- Users, tenants, roles, and authorization boundaries
- Expected traffic, data volume, workload shape, and growth horizon
- Availability, latency, recovery, and consistency needs
- Sensitive data, compliance, audit, and retention requirements
- External systems, contracts, rate limits, and failure behavior
- Delivery deadline, budget, team capability, and operational ownership
- Deployment environment and observability expectations

If a non-critical answer is unavailable, state a conservative assumption and continue. Never invent product requirements.

### 3. Rank quality attributes

Name the three most important attributes for this decision, such as delivery speed, simplicity, security, reliability, maintainability, scalability, portability, or cost. Explain conflicts between them.

### 4. Choose boundaries before tools

Define responsibilities, ownership, trust boundaries, data flow, and failure boundaries before selecting frameworks.

Default to a modular monolith when one deployable can meet the requirements. Require concrete evidence for:

- A separately deployable service
- A message broker or event-driven workflow
- Distributed transactions or event sourcing
- A cache
- Multiple databases
- A new abstraction or dependency

Independent scaling, isolation, compliance, deployment cadence, or team ownership can justify separation. Speculative future scale cannot.

### 5. Select the stack

Use the preferred stack when it satisfies the ranked attributes and project constraints. Evaluate alternatives when it does not.

For every meaningful choice, provide:

- Selected option and responsibility
- Requirement it satisfies
- Main trade-off
- Operational and learning cost
- Migration or rollback implication
- Confidence and evidence still needed

Do not compare long lists of equivalent tools. Recommend one default and include an alternative only when it represents a meaningful architectural trade-off.

### 6. Design failure and operations

Cover relevant security, validation, authorization, idempotency, retries, timeouts, rate limits, observability, backup, recovery, deployment, and rollback behavior. Treat external payloads and webhooks as untrusted.

Prefer measured evidence before adding caches, replicas, queues, or horizontal scaling.

### 7. Apply SOLID pragmatically

Use SOLID to clarify change boundaries, not to maximize interfaces or classes:

- SRP for modules with one business reason to change
- OCP for stable extension points with at least two real variants
- LSP for substitutable implementations with consistent contracts
- ISP for focused ports that consumers actually need
- DIP where domain policy must not depend on infrastructure details

When providing code, use descriptive names and avoid abbreviations. Avoid explanatory comments. For each intentional SOLID example, add one short `why` comment such as `// DIP: keeps domain policy independent from Prisma.`

### 8. Record durable decisions

Draft an ADR when an accepted choice changes ownership, a public contract, a security boundary, persistence, deployment topology, or a difficult-to-reverse technology. Do not create ADRs for temporary sequencing or routine implementation details.

### 9. Present the recommendation

Follow [OUTPUT-TEMPLATE.md](OUTPUT-TEMPLATE.md). Keep each section short unless the user asks for depth. Make assumptions, uncertainty, and rejected complexity visible.

Use a Mermaid diagram when it makes boundaries, sequence, state, or deployment easier to understand. Do not add decorative diagrams.

## Command conventions

Label where commands run:

- Local development: Windows 10 PowerShell
- Server and deployment: Ubuntu shell

Use PowerShell-compatible syntax locally and Bash-compatible syntax on Ubuntu. Do not present one environment's commands as valid for the other.

## Guardrails

- Prefer incremental delivery and reversible decisions.
- Keep business logic out of presentation and infrastructure adapters.
- Keep credentials and private infrastructure details out of examples.
- Do not claim a technology is a best practice without tying it to a requirement.
- Do not claim validation, performance, or compatibility without evidence.
- Surface unresolved decisions instead of silently choosing them.
