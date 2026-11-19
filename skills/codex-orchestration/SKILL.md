---
name: codex-orchestration
description: Prepare task-specific orchestration prompts or coordinate authorized work using ChatGPT and native Codex sessions and subagents. Use for fresh-chat setup, delegation, cross-session communication, waiting for results, shared working state, recovery, and improving orchestration conventions. Supports normal ChatGPT chats through manual handoffs when execution tools are absent. Do not execute an illustrative task while creating or updating this skill.
---

# Codex orchestration

## Keep it simple

Default to Codex in the desktop app, the user's usual environment. Also support Codex web/cloud, CLI, and normal ChatGPT chats. Adapt to actual capabilities; do not require the user to change clients.

Start with one coordinator. Add a worker only when its independent outcome justifies it. Use one compact state note when continuity is needed. Avoid mandatory role teams, elaborate approval stages, custom engines, or extra files. Read detailed references only when needed. Return one usable prompt or the requested outcome.

## Establish the request

Distinguish three requests before acting:
- Design an orchestration: return prompts, roles, dependencies, and handoffs.
- Execute an orchestration: coordinate only the work the user authorized.
- Improve this skill: change reusable guidance; do not execute the example project.

Use simple English. Prefer a coherent end-to-end outcome over splitting by file, layer, size, or time. Preserve the user's testing, review, production, and approval constraints.

Read [conventions.md](references/conventions.md) for established user preferences.
Read [capabilities.md](references/capabilities.md) before making capability claims.
Read [session-lifecycle.md](references/session-lifecycle.md) when starting, messaging, waiting, or resuming sessions.
Read [shared-state.md](references/shared-state.md) when sharing context or recovering work.
Use [prompt-patterns.md](references/prompt-patterns.md) to construct task-specific prompts.
Use [sources.md](references/sources.md) for dated official evidence and refresh targets.

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

Choose the smallest useful agent set. Prefer independent read-heavy investigations in parallel. For software delivery, follow the [stage gates and parallel work rules](references/conventions.md#software-delivery). Use separate file ownership or isolated worktrees for concurrent edits and verify actual isolation.

## Delegate and collect

Give each worker a bounded outcome, precise scope, inputs, tool/action permissions, editing ownership, baseline/version, acceptance criteria, reporting format, and stopping conditions.

For independent review, provide requirements and raw candidate artifacts rather than a desired verdict or the implementor's conclusions. Reviewers do not implement their own corrections.

Register real worker/session IDs and locations. Wait through native wait tools when available. Inspect completed output and required artifacts. A timeout, queued message, idle session, progress update, or lack of errors is not proof of success.

Route concrete feedback to the responsible worker; verify the new candidate afterward. Default recommendation: at most two correction/re-review cycles before surfacing a concrete unresolved blocker, unless the user specifies another bound. Do not abandon unrelated safe work.

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
