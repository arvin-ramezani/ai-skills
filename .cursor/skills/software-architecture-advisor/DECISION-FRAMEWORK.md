# Architecture Decision Framework

## Decision standard

Connect every recommendation:

`business outcome -> constraints -> quality attributes -> boundaries -> technology -> operations`

Separate facts, assumptions, and decisions. Mark confidence as high, medium, or low. Prefer evidence from the current system over generic best practices.

## Quality attributes

Rank the three attributes that control the decision:

- Simplicity and delivery speed
- Security and tenant isolation
- Reliability and recoverability
- Maintainability and testability
- Performance and latency
- Scalability and workload isolation
- Auditability and compliance
- Cost and operational effort
- Portability and vendor dependence

Define a measurable target when the decision depends on it. “Fast” is not a requirement; a response-time percentile under a known workload can be.

## Simplicity gate

Start with the fewest deployable units and infrastructure dependencies that meet the requirements.

Approve added complexity only when:

1. A current requirement cannot be met cleanly without it.
2. The failure or ownership boundary is understood.
3. The team can operate it.
4. Monitoring, recovery, and rollback are defined.
5. Its cost is lower than the risk it removes.

Two plausible future use cases do not equal two current use cases. Extract abstractions after stable variation appears.

## Application shape

Use Next.js as the complete application boundary when the product is small, browser-focused, owned by one team, and has simple workflows without a required independent API.

Separate NestJS when the system has complex business workflows, multiple clients, independent backend delivery, background processing, external integrations, realtime authorization, or a strong security and ownership boundary.

Next.js Route Handlers and Server Actions may adapt presentation requests. They should not duplicate business policy owned by NestJS.

Default a NestJS backend to a modular monolith:

- Organize modules by business capability.
- Keep domain and application policy independent from controllers and persistence.
- Use explicit module contracts for cross-capability collaboration.
- Keep transactions inside clear consistency boundaries.
- Extract a service only for demonstrated independent scaling, isolation, deployment, compliance, or team ownership.

Do not model every entity as a separate module or service.

## Data and persistence

Prefer PostgreSQL when the system needs relational consistency, transactions, flexible querying, reporting, or auditable workflows. Define ownership, tenant scope, indexes, retention, backup, restore, and migration behavior.

Use a different primary store only when the workload has a demonstrated access pattern PostgreSQL cannot meet economically or safely.

Prefer Prisma for type-safe relational application development and migrations when its query model fits. Keep it behind backend-owned persistence adapters at meaningful domain boundaries.

Use transactions and database constraints to protect invariants. Use parameterized raw SQL for isolated advanced queries before replacing the data layer. Evaluate another data tool only when measured query control, database features, or performance requirements justify the cost.

Do not add a cache without:

- A measured bottleneck or required shared ephemeral capability
- A source of truth
- Expiration and invalidation rules
- Failure behavior when the cache is unavailable
- Protection against stale or cross-tenant data

Use PostgreSQL search for modest requirements before adding a search service. Use object storage for large or user-uploaded files; store metadata, ownership, and lifecycle policy in the application database.

## Communication and asynchronous work

Use synchronous HTTP when the caller needs an immediate result and the dependency can meet the latency and availability budget.

Use a background job when work is slow, retryable, scheduled, bursty, or should survive a request. Define:

- Idempotency key
- Retry and backoff policy
- Timeout
- Terminal failure handling
- Progress and status model
- Observability and manual recovery

Add a message broker only when durable delivery, workload buffering, fan-out, or service decoupling is required. A database-backed job or inbox can be simpler for an early modular monolith.

Use realtime delivery only when stale data harms the user experience or operation. Define authorization, reconnect behavior, missed-event recovery, and a non-realtime source of truth.

## External integrations

Treat external APIs and webhooks as unreliable and untrusted:

- Validate schemas and signatures.
- Enforce authorization and tenant ownership.
- Deduplicate deliveries.
- Make handlers idempotent.
- Bound retries with backoff and jitter.
- Respect rate limits and timeouts.
- Persist enough state for audit and replay.
- Reconcile periodically when webhooks can be missed.
- Isolate provider payloads behind an adapter.

For CMS and ecommerce integrations, keep plugins or agents narrow. Do not make an external site the source of truth for internal workflows unless an approved contract assigns that ownership.

## Multi-tenancy and authorization

Decide:

- Tenant identification and data ownership
- User-to-tenant membership
- Administrator capabilities
- Cross-tenant support access
- Database enforcement strategy
- Audit events and retention

Apply authorization server-side at every trusted boundary. Do not rely on hidden UI controls. Include tenant identifiers in uniqueness, idempotency, caching, and background-job designs where relevant.

## Security and privacy

Identify trust boundaries and sensitive data before choosing deployment topology.

Require boundary validation, least privilege, secret management, encryption in transit, safe security logging, dependency updates, restoration tests, and abuse controls for public endpoints.

Threat-model authentication, billing, file upload, infrastructure actions, and administrator support access when relevant.

## Delivery and operations

Use Docker Compose for reproducible local dependencies when it reduces onboarding and environment drift. A single Ubuntu host with containers can be appropriate for an early product if backups, health checks, deployment rollback, and acceptable downtime are explicit.

Add orchestration, replicas, or multi-region topology only for defined availability, scale, or recovery targets.

GitHub Actions should run the repository's actual formatting, linting, type, test, build, migration-safety, and image checks. Separate artifact creation from environment promotion when deployment risk warrants it.

Every production design should state:

- Logs, metrics, traces, and alerts that matter
- Health and readiness behavior
- Backup and restore objectives
- Deployment and rollback steps
- Database migration compatibility
- Ownership during incidents

## Stack deviation test

Recommend an alternative to the preferred stack only when it has a material advantage for a ranked requirement.

Document:

1. Why the preferred option falls short.
2. Why the alternative fits.
3. New operational and learning costs.
4. Integration and migration impact.
5. A small validation experiment when confidence is not high.

Compute-heavy machine learning, specialized streaming, hard realtime processing, platform-native edge constraints, or a required ecosystem integration may justify deviation. They do not automatically justify rewriting the main application.

## ADR gate

Create an ADR for an accepted, durable decision involving:

- System or data ownership
- Public or integration contracts
- Authentication or authorization boundaries
- Persistence technology or data lifecycle
- Deployment topology
- A difficult-to-reverse platform choice

Include context, decision, alternatives, consequences, and migration or rollback. Keep implementation sequencing in the delivery plan.
