# Prompt patterns

These are recommended patterns, not fixed OpenAI APIs. Replace placeholders with task facts. Omit irrelevant roles and constraints.

## Normal-chat entry prompt

```text
Use codex-orchestration to prepare an orchestration for the task below.
First identify whether this chat can execute delegation/session controls or only prepare prompts.
Do not execute the example task while designing its orchestration.
Preserve my scope and authorization constraints. Ask only essential missing questions.
Return one executor prompt, required context/artifacts, and the response I should bring back if manual handoff is needed.
Task: <goal, evidence, constraints, desired outcome>
```

## Main executor prompt

An explicit invocation with an implementation task already requests the default roles.

```text
$codex-orchestration Implement <one concrete outcome>.
```

Add constraints or role exclusions as needed, for example `Defer security review.` Use the expanded form when extra context helps.

```text
$codex-orchestration Implement <one concrete outcome>.
Sources: <requirements and accessible authoritative locations>.
Scope: <included behavior>. Exclusions: <excluded behavior>.
Allowed actions: <explicit scope>. Verification owner: <person/agent and limits>.
Inspect actual tools, workspace, applicable instructions, current versions, and related work.
Use the default delivery agents within the authorized scope and wait for each prerequisite stage.
Use separate top-level tasks only where explicitly requested and supported.
Keep shared state in <existing convention or minimal chosen file>.
Assign clear edit ownership or isolated worktrees for concurrent editors.
For software delivery, finish planning before starting production coding or test writing.
Run code and test work in parallel only when their contract is stable and edit ownership is separate. Sequence dependent work.
Require applicable verification to pass on the combined candidate before code review. Start security review after code review passes or is explicitly omitted where policy permits. Apply any exclusion or restriction on security review.
Diagnose verification failures before routing fixes. Reverify changes and follow up with the original reviewer for re-review. Report a blocker when the evidence no longer supports a new action.
Do not infer approval for deployment, merging, publication, or other excluded actions.
Finish with the outcome, exact candidate, verification, unresolved findings, and acceptance status.
```

This template does not itself authorize every action in its placeholders. Ground the final prompt in what the human requested.

## Worker assignment

```text
Outcome:
Inputs and baseline version:
Scope and exclusions:
Allowed actions and test-execution limits:
Editing ownership / worktree:
Dependencies:
Required evidence and acceptance:
Return: findings, source locations, changed artifacts, exact candidate, checks actually run, blockers.
Stop when: outcome complete or a concrete dependency/permission/decision blocks it.
```

## Independent review

```text
Independently review <exact immutable candidate> against <requirements/contracts>.
Inspect source and verification evidence. Do not edit or implement.
Report actionable findings with severity, location, evidence, required behavior, and verification.
Distinguish confirmed defects from uncertain risks.
Do not approve deployment or merging. Follow the user's requested verdict/reporting convention.
```

## Feedback and continuation

```text
For <assigned outcome>, resolve these confirmed in-scope findings: <evidence>.
Preserve <contracts and exclusions>.
Return the new exact candidate, changes, verification, and unresolved blockers.
Do not broaden action permissions.
```

## Manual return handoff

Ask the user to return:
- Worker final response.
- PR/artifact link and exact candidate version.
- Check results, including NOT RUN/BLOCKED.
- Questions or unresolved findings.

Do not ask for full noisy logs unless needed to investigate a specific issue.

## Calibration example: Gate defects 3 and 4

When asked only to prepare orchestration for these defects:
- Keep helper provisioning and activation-evidence alignment as one installation outcome.
- Delegate independent source tracing if execution is later authorized.
- Preserve strict site, active-state, and revision checks.
- Do not add dashboard payload, Nginx routing, image staging, or TLS cleanup fixes from adjacent observations.
- Keep test authoring, test execution, independent review, and VPS acceptance distinct.
- Preserve the current user's exact allocation of test execution; if ambiguous, resolve it rather than assuming a coordinator may run tests.
- Do not perform repository implementation or VPS operations merely because the example describes them.
