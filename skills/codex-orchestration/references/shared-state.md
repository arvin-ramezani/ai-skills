# Shared state and recovery

## Documented memory distinctions

ChatGPT project context can reference related chats/files subject to memory settings. Project-only memory restricts context to that project. The current Projects article also says Work is unavailable within a project using project-only memory; do not assume that arrangement supports Work orchestration. Recheck the account and current documentation before combining them. [S7]

Local Codex memories are separate from ChatGPT web memory. They are generated asynchronously from eligible prior chats and can lag or skip active sessions. Required rules belong in AGENTS.md or checked-in documentation rather than memory alone. [S8]

## Recommended working-state design

Use memory to discover useful context, then read the actual source. Use explicit state for current work, authorization, dependencies, and version-sensitive evidence.

| Mechanism | Intended role | Never assume |
| --- | --- | --- |
| Main transcript | Active reasoning and coordination | Every worker sees it or later compaction preserves every detail |
| Subagent context | Bounded delegated work | Live synchronized parent history or a private filesystem |
| ChatGPT project context | Related background | Reliable task queue, locking, or exact latest status |
| Local Codex memories | Recall from prior work | Immediate propagation, web synchronization, or current permission |
| Versioned files/artifacts | Explicit working state and deliverables | A local path is readable from another host |

Choose an existing state convention before inventing files. For a small job, one coordinator-owned Markdown file is enough. For larger work, add separate worker reports only when useful.

State template:
```markdown
# Orchestration state
Updated: <timestamp and timezone>
Outcome:
Scope / exclusions:
Authoritative requirements:
Allowed actions / verification owner:
Baseline / candidate version:
Workspace or artifact location:
Coordinator:
Workers: <role, actual ID, host, scope, ownership, status, last cursor>
Confirmed facts: <source and version>
Decisions: <decision, authority, rationale>
Unresolved questions / blockers:
Verification: <command/check, executor, version, result, evidence>
Next action:
```

Keep secrets out of state. Link to approved secret-management mechanisms instead of copying values.

## Concurrent workers

Give each worker its own report location. Let the coordinator update shared status and decisions. If two writers must change one file, serialize integration or use isolated worktrees and review the merged result.

Do not assume worktrees isolate databases, ports, containers, generated outputs, or external services. Allocate these resources explicitly when used.

Use messages to notify another session that an artifact changed. Include the path or accessible URL, version/commit, and requested action. The recipient must reread it. A filename alone is not evidence of freshness.

Across hosts or cloud/local boundaries, transfer through an accessible authorized artifact/repository mechanism. Verify access and version before delegating. Do not give a cloud worker an inaccessible local Windows path.

## Recovery protocol

1. Read the latest authoritative state and user instruction.
2. Verify current source/artifact versions and existing worker status.
3. Identify uncommitted work and partially completed actions.
4. Resolve stale reports or conflicting decisions using source evidence.
5. Resume the smallest pending action; do not replay completed mutations.
6. Update state and report any unresolved uncertainty.

A failed read, unavailable worker, or missing file is a blocker for dependent work, not permission to invent its contents.
