# Install Software Architecture Advisor

This skill is designed to be installed once through a shared, vendor-neutral `.agents/` tree and then exposed to whichever AI agents you use.

Keep these runtime files together:

- `SKILL.md`
- `PROFILE.md`
- `PROJECT-CONTEXT.md`
- `DECISION-FRAMEWORK.md`
- `OUTPUT-TEMPLATE.md`

`INSTALL.md` is distribution guidance and is not required at runtime.

## Canonical installation

Use one of these paths:

```text
Project: <project>/.agents/skills/software-architecture-advisor/
Global:  ~/.agents/skills/software-architecture-advisor/
```

Do not create separate canonical copies under `.cursor/`, `.claude/`, `.codex/`, or other vendor-specific directories. If an agent requires its own discovery mechanism, configure that tool to consume, sync, or import the shared `.agents/` installation instead of maintaining a second divergent copy.

The `.agents/` directory is the repository's portable installation convention. Individual AI products may require separate configuration to discover it.

## Install for one project

From the `ai-skills` repository root:

```powershell
python scripts/install_skill.py software-architecture-advisor --project "D:\path\to\project"
```

This installs the complete package to:

```text
D:\path\to\project\.agents\skills\software-architecture-advisor\
```

## Install globally

```powershell
python scripts/install_skill.py software-architecture-advisor --global
```

This installs to:

```text
~/.agents/skills/software-architecture-advisor/
```

## Portable ZIP

Some consumers support direct skill upload/import. Build a neutral ZIP with:

```powershell
python scripts/package_skill.py software-architecture-advisor
```

Output:

```text
dist/software-architecture-advisor.zip
```

The archive contains the runtime package with `SKILL.md` at its root.

## ChatGPT

ChatGPT uploaded Skills are an optional consumer path, not the canonical source layout.

For eligible ChatGPT accounts/workspaces:

1. Build `dist/software-architecture-advisor.zip` using the neutral packager above.
2. Open **Plugins** in ChatGPT.
3. Open **Skills**.
4. Select **Create** → **Upload from your computer**.
5. Upload the ZIP and review the scan result.

Official ChatGPT guidance:

- https://help.openai.com/en/articles/20001066

The OpenAI Skills API is separate from ChatGPT account installation and creates project-scoped API skills.

Official API reference:

- https://developers.openai.com/api/reference/python/resources/skills/methods/create

## Portability rule

Never make normal execution depend on files outside this skill directory. Relative references in `SKILL.md` must stay self-contained so the same package can be installed under `.agents/`, synchronized to another agent environment, or uploaded as a ZIP without editing the skill.