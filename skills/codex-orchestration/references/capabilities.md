# Capabilities and limits

Evidence checked: 2026-11-13. This is a dated knowledge snapshot, not a guarantee of access in a later chat.

## Official facts

- Codex supports ChatGPT subscription sign-in; Plus users can use included Codex access subject to limits. Codex Cloud requires eligible account/workspace access. Do not assume unlimited use or universal cloud rollout. [S1]
- ChatGPT sign-in and API-key authentication are different access/billing routes. Prefer ChatGPT sign-in for the user's Plus-only setup; a custom API/SDK system is not required for this workflow. [S2]
- Chat, Work, and Codex are distinct experiences. Work handles tool-based deliverables; Codex handles repository work. Work access, model choice, and usage depend on account/workspace availability. [S3]
- Current Codex clients and eligible ChatGPT Work chats support subagents. Explicit delegation requests are the portable default. Subagents can receive follow-ups and their results can be collected by a main agent. Delegation consumes additional usage. Local custom agents can define instructions and model settings; inherited permissions still apply. Calling a worker read-only does not create a separate sandbox. [S4]
- The CLI documents session browsing with codex agents and messaging with codex queue. This is a Codex mechanism, not a universal ordinary-ChatGPT-chat messaging API. [S5]
- OpenAI recommends one chat per coherent outcome, bounded delegation, and avoiding concurrent edits of the same files without worktree isolation. [S6]

Sources are linked in sources.md. Read applicable current tool descriptions before acting.

## Execution matrix — operational recommendations

| Current environment | Select this route | Check first |
| --- | --- | --- |
| Normal ChatGPT chat without orchestration tools | Design prompts; user opens workers and returns responses | Available files/context and intended executor |
| Eligible Work chat with subagents | Delegate bounded tool-based work | Tool availability, account limits, actual source access |
| Codex desktop main session with subagents | Coordinate one repository outcome | Repo/HEAD, permissions, editing isolation |
| Codex web/cloud task | Use available cloud runtime and native subagents when exposed | Runnable environment, repository access, network and cloud eligibility |
| Desktop with separate task tools | Create/read/message/wait for explicitly requested tasks | Tool schemas, human authorization, target host/project |
| Local terminal with Codex | Use interactive or supported noninteractive commands | Local --version and --help |
| Ordinary chat with only browser automation | Prefer manual handoff unless UI interaction is explicitly requested and supported | Actual session access and computer-use rules |

Do not infer what a chat can do from its model name alone. Do not use role descriptions to bypass missing tools.

## Locally observed desktop controls — not universal public APIs

Inspected 2026-11-13; these tool contracts were exposed in the author's desktop session. A receiving agent must rediscover them; names, schemas, and policies may change.

| Observed control | Relevant contract |
| --- | --- |
| list_projects | Resolve real project identifiers before project task creation |
| create_thread | Creates a separate task only on explicit human request; nonblocking; may return pending setup rather than a ready thread |
| list_threads | Discovers task identities/status; a summary is not a complete history review |
| read_thread | Reads paginated turns/status; follow cursors when older context matters |
| send_message_to_thread | Requires explicit human authorization for the destination; a worker request to report back is not that authorization |
| wait_threads | Waits for Codex completion/attention; timeout is not completion; carry returned cursors and inspect per-target failures |

Retain threadId plus hostId when supplied. Never substitute a pending clientThreadId for a ready threadId. The inspected creation contract required explicit requests for worktree or cloud destinations and explicit model selection before overrides. Follow the current contract rather than guessing.

These observations establish what this environment exposed, not what every Plus account or ordinary chat exposes. No actual worker task was created to verify runtime behavior during research.

## Version mismatch observed

The installed executable reported codex-cli 0.157.0. Its help exposed agents, queue, resume, fork, and exec. The queue help accepted --thread and --message but did not list --resume, although current documentation describes that option. Treat this as a compatibility gap: inspect local help, omit unsupported flags, and verify the destination actually ran. Do not update software or change settings just to make an example command work without considering the user's request.

## Unestablished guarantees

Do not promise:
- Automatic opening or control of arbitrary ordinary ChatGPT chats.
- Uniform tool/model/Ultra availability for every Plus account.
- A shared mutable memory synchronized across ChatGPT web, local Codex, machines, and live workers.
- Inherited filesystem isolation or live synchronized transcripts for separately created tasks.
- Background continuation after an ordinary chat response without an actual supported task/runtime.
- Unlimited workers, fixed quota, or a fixed universal concurrency limit.
