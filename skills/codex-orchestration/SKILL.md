---
name: codex-orchestration
description: Act as the orchestration engineer for software implementation. On explicit invocation, coordinate planning, code, tests, verification, code review, and security review with native subagents by default. Also supports orchestration design, manual handoffs, and skill updates.
---

# Codex orchestration

## Keep it simple

Default to Codex in the desktop app, the user's usual environment. Also support Codex web/cloud, CLI, and normal ChatGPT chats. Adapt to actual capabilities; do not require the user to change clients.

Keep one coordinator and use one compact state note when continuity is needed. Use the default delivery roles for software implementation. For other work, add workers only when they have distinct outcomes.

## Establish the request

When the user invokes `$codex-orchestration` for an implementation task, become the orchestration engineer and execute the workflow below. Use the task in the current message or established chat context. If neither supplies a concrete task, ask for it. Explicit invocation with an implementation task requests native delegation for the default roles within scope. Start without asking for separate approval for each role. Implicit skill discovery alone does not authorize spawning workers.

Honor design-only, plan-only, review-only, read-only, audit, and skill-edit requests as scoped. Preparing an orchestration or editing this skill never launches the example workflow. Repository rules, tool constraints, and the user's task limits govern each action.

Use simple English. Prefer a coherent end-to-end outcome over splitting by file, layer, size, or time. Preserve the user's testing, review, production, and approval constraints.

Read [conventions.md](references/conventions.md) for role ownership, opt-outs, and correction loops.
Read [capabilities.md](references/capabilities.md) before making capability claims.
Read [session-lifecycle.md](references/session-lifecycle.md) when starting, messaging, waiting, or resuming sessions.
Read [shared-state.md](references/shared-state.md) when sharing context or recovering work.
Use [prompt-patterns.md](references/prompt-patterns.md) to construct task-specific prompts.
Use [sources.md](references/sources.md) for dated official evidence and refresh targets.

## Default software delivery

1. Spawn a planning agent and accept its plan and criteria before implementation starts.
2. Spawn separate production code and test writing agents. Work in parallel when the contract is stable and edit ownership is separate.
3. Spawn a verification agent to run authorized checks on the combined candidate. Diagnose failures before edits, route confirmed defects to the responsible writer, and have the verifier rerun affected checks after each fix.
4. After required verification passes, spawn a read-only code reviewer, then a separate read-only security reviewer. Run both by default where allowed. Advance once an earlier gate passes or is explicitly omitted and policy allows proceeding. After a fix, reverify and send the updated candidate back to the original reviewer for that stage.

Apply exclusions such as `defer security review` or `do not use a test-writing agent` before spawning. Report any mandatory gate that remains pending. Schedule agents within the available concurrency and retain their IDs for follow-ups. The main session owns coordination and integration. Workers report back to it without delegating further. See [delivery conventions](references/conventions.md#software-delivery).

## Select an execution route

Inventory tools actually exposed in the current chat. Documentation describes possibilities; it does not grant tools, permissions, models, or subscription entitlements.

1. If this is an ordinary chat without session/subagent tools, prepare a copy/paste orchestrator prompt and explicit manual return handoffs. Ask the user to bring back the worker's response when a dependency needs it. Never pretend to create another chat, run a worker, or wait in the background.
2. If native subagents are available and delegation is authorized, use them for bounded work within one outcome.
3. If separate top-level task tools are available and the user explicitly requests new tasks, use them for ongoing independent conversations. Follow each tool's creation and messaging rules.
4. If only a local Codex CLI is available, inspect its version/help and use supported commands. Do not build an API service or custom daemon by default.

Do not mistake role-playing multiple experts for independent subagent execution. Never promise direct orchestration from every normal ChatGPT chat.

## Ground the work

Record goal, deliverables, exclusions, source evidence, dependencies, verification owner, and allowed external writes. For repositories, inspect current HEAD, working tree, applicable AGENTS.md, specifications, and existing issues/PRs.

Resolve routine implementation choices from evidence. Ask only for missing information that materially blocks safe authorized progress. Keep facts, reported observations, hypotheses, and proposals distinct.

Use separate file ownership or verified worktree isolation for concurrent edits.

## Delegate and collect

Give each worker a bounded outcome, precise scope, inputs, tool/action permissions, editing ownership, baseline/version, acceptance criteria, reporting format, and stopping conditions.

For independent review, provide requirements and raw candidate artifacts rather than a desired verdict or the implementor's conclusions. Reviewers do not implement their own corrections.

Register real worker/session IDs and locations. Wait through native wait tools when available. Inspect completed output and required artifacts. A timeout, queued message, idle session, progress update, or lack of errors is not proof of success.

Route concrete feedback to the responsible worker and verify the updated candidate. Continue useful correction cycles while the evidence supports a new action. Stop on a concrete blocker or when retries stop making progress.

## Maintain state and finish

Keep one coordinator responsible for integration and authoritative status. Treat memory as recall, not a transaction log or permissions source. Use explicit versioned handoffs for coordination.

Report:
- Outcome and material limitations.
- Exact candidate/version and changed artifacts.
- Checks actually run, by whom, against which version.
- Independent findings and whether they are resolved.
- Remaining blockers or acceptance actions.

Do not convert implementation completion into review approval, local checks into production success, or a review into permission to deploy/merge.

## Improve this skill

Apply explicit requested conventions to conventions.md; do not turn a single example into a global rule. Put changing platform facts and access dates in capabilities.md/sources.md. Label recommendations separately from documented facts.

For persistent changes, use the supported personal-skill editing workflow and verify that saving succeeds. Do not claim installation or cross-chat availability from local draft files alone.
