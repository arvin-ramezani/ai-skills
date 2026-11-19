# User conventions

Initial edition: 2026-11-13.

## Established from this request

- Use the name codex-orchestration.
- Prefer Codex in the desktop app; also support web/cloud and CLI.
- Keep it simple: use the fewest useful agents, prompts, and state files; avoid unnecessary ceremony.
- Support ChatGPT Plus and native Codex/ChatGPT capabilities without assuming API access.
- Make the knowledge portable enough to provide to a fresh normal ChatGPT chat.
- Cover starting sessions, waiting, subagents, separate conversations, communication, and shared working context.
- Help the receiving agent construct task-specific orchestration prompts and coordinate only when actual tools and authorization allow it.
- Keep reusable rules separate from changing platform facts.
- Allow gradual improvement as the user establishes conventions and needs.

## Software delivery

Planning complete → code and tests complete → required verification passes → code review passes → security review, when required. Follow the applicable repository rules and task authorization for each stage. Each verification and review gate applies to the exact candidate. After a fix, rerun affected gates on the updated candidate.

Start production coding and test writing after planning is complete. Run them in parallel when expected behavior and interfaces are stable and editing ownership is separate. When one task depends on the other's output, finish that dependency before starting the dependent work. Verify the combined code and test candidate before code review.

## Apply only when present in the current task

Repository-specific AGENTS.md, review verdicts, test-execution limits, security requirements, and production access must be loaded from the current task/repository. Do not apply a previous task's NOT RUN restriction or deployment permission globally.

Do not treat the Gate example as standing permission to implement, open a task, post to GitHub, run tests, or access a VPS.

## Updating conventions

Record explicit durable user decisions here. Include conditions where they apply. Do not promote suggestions, worker opinions, or one-off exceptions into approved global rules.

For a requested update, identify the affected rule, preserve compatible behavior, check realistic routing/recovery cases, and save through the supported skill update mechanism.
