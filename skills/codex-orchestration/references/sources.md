# Official sources and evidence record

Access date for all sources: 2026-11-13.
Use URLs directly when exporting or checking claims. No internal citation tokens are required.

| ID | Official page | Relevant section / supported claim |
| --- | --- | --- |
| S1 | [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) | Availability; account sign-in; Cloud eligibility and usage |
| S2 | [Authentication](https://learn.chatgpt.com/docs/auth.md) | OpenAI authentication; subscription vs API-key access |
| S3 | [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) | Choose an experience; usage/billing and account availability |
| S4 | [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents.md) | Availability; triggering; thread controls; permissions; custom agents |
| S5 | [Developer commands](https://learn.chatgpt.com/docs/developer-commands.md) | codex agents; codex queue; resume caveats |
| S6 | [Best practices](https://learn.chatgpt.com/docs/learn/best-practices) | Organize long-running chats; common mistakes |
| S7 | [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) | Project-only/default memory; settings and Work limitation |
| S8 | [Memories](https://learn.chatgpt.com/docs/customization/memories.md) | Separate local/web stores; delayed generation; durable guidance |
| S9 | [Customization](https://learn.chatgpt.com/docs/customization/overview) | AGENTS.md, memories, skills, MCP, subagents |
| S10 | [CLI reference](https://learn.chatgpt.com/docs/cli/reference) | Interactive, session, and noninteractive command reference |

## Evidence levels

- Documented: current official pages above.
- Locally observed: exposed desktop tool descriptions and installed CLI help.
- Recommended: skill workflow, state templates, role selection, feedback bounds, and prompt patterns.
- Unestablished: portability of every control to every normal chat or Plus account.

The desktop task-control contracts have no verified public documentation URL in this research. They were inspected directly from tools exposed to this session. Do not cite this observation as a universal platform guarantee.

Local CLI checks:
- codex --version -> codex-cli 0.157.0.
- codex --help -> agents, exec, resume, queue, fork present.
- codex queue --help -> --thread and --message present; --resume absent.
- codex exec --help -> --json, --output-last-message, stdin prompt support present.
- These were help/version checks; no orchestration execution or end-to-end runtime test was performed.

## Refresh procedure

When asked for latest behavior, or when a capability/command fails:
1. Read current local tool schemas/help first.
2. Reopen the applicable official sources; verify current page content and relevant surface.
3. Record access date, client version, and precise discrepancy.
4. Update capability claims without overwriting user conventions.
5. Mark unavailable or conflicting claims explicitly; prefer a working supported route.

Do not assume a newer documentation example is supported by an older installed client. Do not automatically install updates or enable experimental settings solely to satisfy a sample prompt.

Some guessed documentation paths failed during research; only successfully retrieved pages are listed as evidence. Recheck live links when freshness matters.

## Extending the skill

Keep short operational instructions in SKILL.md. Keep platform details and dated evidence here and in capabilities.md. Add scripts only when a repeated deterministic operation warrants them; no custom orchestration engine, API client, daemon, or external memory service is required by this first edition.
