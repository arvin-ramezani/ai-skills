# User conventions

Initial edition: 2026-11-13.

## Established from this request

- Use the name codex-orchestration.
- Prefer Codex in the desktop app; also support web/cloud and CLI.
- Use one coordinator and minimal shared state. Explicit invocation for implementation starts the default delivery roles. For other work, use the fewest useful agents.
- Support ChatGPT Plus and native Codex/ChatGPT capabilities without assuming API access.
- Make the knowledge portable enough to provide to a fresh normal ChatGPT chat.
- Cover starting sessions, waiting, subagents, separate conversations, communication, and shared working context.
- Help the receiving agent construct task-specific orchestration prompts and coordinate only when actual tools and authorization allow it.
- Keep reusable rules separate from changing platform facts.
- Allow gradual improvement as the user establishes conventions and needs.

## Software delivery

Planning → production code and test writing → verification → code review → security review. Use distinct native agents for all six roles by default where authorized and supported. Plan first. Run code and test writing in parallel only with stable interfaces and separate ownership. Verify the combined candidate before review. Each gate applies to the exact candidate. Schedule stages within the available concurrency.

- **Opt-outs.** Apply requests such as `defer security review`, `skip code review`, and `do not use a test-writing agent` before assigning work. If the request excludes only delegation for a still-authorized stage, the coordinator can handle that stage where policy permits. If it excludes the work itself, leave it deferred. Report any unmet mandatory gate as `PENDING` and honor its prerequisites before advancing. Apply the same rules when repository policy reserves verification for the owner or requires reviews in separate owner-requested sessions. Supply a handoff for a separate required review when it cannot run in this session.
- **Verification failures.** The verifier returns the command, candidate identity, observed failure, and evidence for a production defect, test defect, environment or prerequisite issue, or unresolved cause. Route confirmed production defects to the code author and confirmed test defects to the test author. Test corrections must follow the authoritative contract and preserve valid assertions. Diagnose uncertain failures before assigning edits. Resolve environment issues through authorized changes. Have the verifier rerun affected checks and any required broader gates after each fix. Continue while each cycle makes concrete progress. Report the blocker and evidence when progress stops.
- **Review corrections.** Retain the verification agent and both reviewer IDs for follow-ups. Reviewers remain read-only. Give each reviewer the requirements, exact candidate, and relevant verification evidence. Route confirmed findings to the responsible writer, reverify, and follow up with the original reviewer for that stage. Rerun any earlier gates invalidated by a security fix, including code review, before returning to security review. If a reviewer cannot resume, report why. A replacement may perform a fresh review where permitted. A required same-reviewer outcome stays pending if it cannot be fulfilled.

## Apply only when present in the current task

Repository-specific AGENTS.md, review verdicts, test-execution limits, security requirements, and production access must be loaded from the current task/repository. Do not apply a previous task's NOT RUN restriction or deployment permission globally.

Do not treat the Gate example as standing permission to implement, open a task, post to GitHub, run tests, or access a VPS.

## Updating conventions

Record explicit durable user decisions here. Include conditions where they apply. Do not promote suggestions, worker opinions, or one-off exceptions into approved global rules.

For a requested update, identify the affected rule, preserve compatible behavior, check realistic routing/recovery cases, and save through the supported skill update mechanism.
