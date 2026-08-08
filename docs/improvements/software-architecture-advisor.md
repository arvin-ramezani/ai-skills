# Software Architecture Advisor Improvements

This roadmap records improvements to make after observing the skill on real architecture decisions. Add guidance in response to repeated failures, not hypothetical completeness.

## Priority 1: Evaluation cases

Create `EVALUATION-CASES.md` with at least eight representative prompts:

- Small Next.js-only application
- NestJS modular monolith
- Multi-tenant SaaS boundary
- External webhook with retries and idempotency
- Background job without a message broker
- A justified queue or broker
- A rejected microservices proposal
- A requirement that justifies leaving the preferred stack

For each case, define:

- Expected questions
- Required architectural properties
- Acceptable technology choices
- Unacceptable recommendations
- Expected ADR decision

Success criterion: the skill selects boundaries from requirements and does not force the preferred stack.

## Priority 2: Worked examples

Add concise examples that demonstrate the full output template:

1. A simple application that should remain Next.js-only.
2. A business workflow that benefits from a NestJS modular monolith.
3. An unreliable ecommerce webhook integration.
4. A workload where a non-TypeScript component is justified.

Keep examples separate from `SKILL.md` and link them directly for progressive disclosure.

Success criterion: examples teach decision quality without becoming copy-and-paste architectures.

## Priority 3: Trigger precision

Review false-positive and false-negative invocations.

Potential adjustments:

- Exclude routine implementation where architecture is already accepted.
- Include architecture review, scaling, integration boundaries, deployment topology, and ADR language.
- Distinguish feature design from UI-only implementation.

Success criterion: the skill activates for decisions and stays out of established implementation work.

## Priority 4: Portability

Remove assumptions about repository names or local directory layouts from reusable guidance.

When project-specific context is needed:

- Keep it in the target project's skill or architecture documents.
- Discover equivalent files by purpose rather than one fixed path.
- State unavailable context and ask only when it blocks the decision.
- Never publish private project details in this public repository.

Success criterion: the skill works when installed personally or copied into an unrelated project.

## Priority 5: Validation

Add `scripts/validate-skill.ps1` to verify:

- Required YAML frontmatter
- Valid lowercase skill name
- Specific description with trigger terms
- `SKILL.md` under 500 lines
- One-level reference files exist
- No private absolute paths or known secret patterns
- Required output sections remain present

Document how to run it from Windows PowerShell and add it to continuous integration.

Success criterion: malformed or non-portable skill changes fail before merge.

## Priority 6: Feedback loop

After every five real uses, review:

- Questions that did not affect the recommendation
- Missing questions that changed the result later
- Unnecessary services, dependencies, or abstractions
- Incorrect stack choices
- Risks discovered too late
- Sections users repeatedly skipped or requested in more depth

Promote a lesson into the skill only when it is broadly reusable or has failed repeatedly.

Success criterion: revisions are supported by observed outcomes.

## Guardrails

- Keep `SKILL.md` concise.
- Put detailed scenarios in direct reference files.
- Do not create long catalogs of interchangeable technologies.
- Do not duplicate changing project documentation.
- Do not turn SOLID into mandatory layers or interfaces.
- Do not add a fixed rule without defining when it should be reconsidered.
