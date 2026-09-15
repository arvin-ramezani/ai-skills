# Install Software Architecture Advisor

This skill package is self-contained. Keep these files together when installing it:

- `SKILL.md`
- `PROFILE.md`
- `PROJECT-CONTEXT.md`
- `DECISION-FRAMEWORK.md`
- `OUTPUT-TEMPLATE.md`

## ChatGPT

ChatGPT supports uploaded skills for eligible accounts/workspaces. Availability and permissions are controlled by the current ChatGPT plan and workspace settings.

### Recommended install path

1. Package this directory as `software-architecture-advisor.zip` so `SKILL.md` is at the ZIP root.
2. In ChatGPT, open **Plugins**.
3. Open the **Skills** tab.
4. Select **Create**.
5. Select **Upload from your computer**.
6. Upload `software-architecture-advisor.zip`.
7. Review any scan or review notice shown by ChatGPT.
8. Install/enable the skill when the upload is accepted.

From the repository root, create the upload ZIP with:

```powershell
python scripts/package_chatgpt_skill.py software-architecture-advisor
```

The generated file is:

```text
dist/software-architecture-advisor.zip
```

The packaging script validates that `SKILL.md` exists and contains the expected `name` and `description` frontmatter before creating the archive.

### ChatGPT account availability

As of September 2026, OpenAI documents ChatGPT Skills for eligible Business, Enterprise, Healthcare, and Edu users, subject to workspace settings and product availability. If the **Skills** tab or upload action is not available, the package is still valid but the current ChatGPT account/workspace cannot install uploaded skills yet.

## OpenAI API

The OpenAI Skills API is separate from ChatGPT account installation. It creates project-scoped API skills and accepts directory files or a ZIP. Use the API only when the skill is intended for an OpenAI API project; do not treat an API skill ID as proof that the skill is installed in the ChatGPT account UI.

## Cursor

For Cursor, copy the whole directory to one of Cursor's discovery locations:

```text
<project>/.cursor/skills/software-architecture-advisor/
~/.cursor/skills/software-architecture-advisor/
```

Do not copy only `SKILL.md`; its linked reference files are part of the skill.