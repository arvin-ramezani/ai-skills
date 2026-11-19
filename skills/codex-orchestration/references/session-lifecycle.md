# Session lifecycle

This is a recommended operating procedure. Platform facts are identified in capabilities.md and sources.md.

## 1. Start from a fresh coordinator chat

Load this skill and the task. Determine whether the user wants prompt design or execution. Recover explicit constraints before deciding roles.

Build a compact capability record:
- Product/client and local version if applicable.
- Repository/workspace/source location and current version.
- Subagent spawn/message/wait capabilities.
- Separate-task create/read/message/wait capabilities.
- File sharing, runtime continuity, permissions, and usage constraints.
- Chosen automatic or manual route.

Do not ask the user to enumerate capabilities already visible through tools.

## 2. Open a worker

For subagents, use the native spawn tool and retain its returned identity. Read the current instructions on context inheritance. Supply explicit task context even if the worker can inherit a transcript.

For separate desktop tasks, resolve the destination project/host and permitted target type first. Follow setup completion until a usable identity exists; do not assume creation means readiness or completion. Creating a new task may start it immediately.

For a manual worker, provide a self-contained prompt and say exactly which response/artifacts the user should bring back. Do not claim that the worker already exists.

For a fresh CLI session, start Codex in the intended directory using supported syntax:
```text
codex -C <absolute-project-directory>
```
This opens an interactive Codex session, not an ordinary ChatGPT web chat. Use real paths, never literal placeholders. A separate user terminal may be needed.

## 3. Send instructions and establish communication

For separate tasks, follow the current tool's explicit human-authorization rules. Where needed, obtain a scoped authorization identifying the relevant sessions and permitting both coordinator-to-worker and worker-to-coordinator messages. Include the original authorization or an approved discoverable reference in each worker's context; never fabricate it.

Suggested human authorization:
"I authorize you to create the named worker tasks for this outcome and exchange task-related messages with them in both directions, subject to the tools' permission rules."

A user request merely to design this arrangement is not permission to execute it.

Prefer native subagent returns over creating extra peer sessions just to exchange status.

## 4. Wait, inspect, and react

Track requested, starting, running, needs-input, completed, failed, and cancelled states as coordinator labels; do not assume these are platform enum values.

Use native wait controls for relevant tasks. Carry cursors to avoid repeatedly consuming old results. Inspect errors and attention states before continuing. Keep waits bounded so user updates can still be handled.

- Timeout: retain the task and wait again or inspect progress.
- Needs input: read the request; answer within scope or escalate a real missing decision.
- Completed: inspect final output and expected artifacts; validate the version.
- Failed: record evidence and choose recovery without repeating destructive actions.
- Cancelled: do not consume partial output as an accepted deliverable.

For top-level tasks, a completed turn may only contain a question. Inspect the response rather than equating turn completion with task success.

If no wait tools exist, use an explicit manual checkpoint: the user returns the response. Never say "I will monitor this" without a mechanism.

## 5. Continue, resume, or fork

Keep follow-ups in the same worker when they continue its assigned outcome. Use a new reviewer context for independent review.

CLI examples documented in [S5], subject to local help:
```text
codex agents
codex queue --thread <real-session-uuid> --message "<task-related follow-up>"
codex resume <real-session-id>
codex fork <real-session-id>
```

Prefer UUIDs when names collide. A queue command is not a result collector. Current docs describe --resume on queue, but the inspected installed version did not list it. Verify support before using it. Documentation also warns that a queue resume failure can still exit successfully; inspect actual task status.

For scripted local execution, the inspected CLI offered:
```text
codex exec -C <absolute-project-directory> --json -o <result-file> -
```
Supply the prompt on stdin using safe shell-specific handling. Check process exit status, emitted events, and the result file together. This is an optional adapter, not the default architecture; it is not cross-chat shared memory. Check authentication, permissions, and local help before running.

## 6. Stop and recover cleanly

Before switching coordinators, write a current handoff. Include active worker identities and cursor state. A new chat must reconnect to actual tasks and sources; it must not blindly restart all workers.

Stop unnecessary workers through supported controls only. Do not delete task history, worktrees, or artifacts merely to tidy up an orchestration.
