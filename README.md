# AI Skills

Reusable AI agent skills, decision frameworks, and improvement roadmaps.

## Skills

### Software Architecture Advisor

Creates requirement-driven architecture and stack recommendations. It prefers the simplest viable design, evaluates technology against project constraints, explains trade-offs, applies SOLID pragmatically, and produces concise Architecture Decision Records when needed.

Location: [`skills/software-architecture-advisor`](skills/software-architecture-advisor)

Install guide: [`skills/software-architecture-advisor/INSTALL.md`](skills/software-architecture-advisor/INSTALL.md)

### Documentation Strategy Engineer

Designs, audits, bootstraps, retrofits, and maintains context-efficient project documentation for AI-assisted development. Supports feature documentation, routing fixes on started projects, optional cross-session agent memory, FA docs, and documentation architecture for monorepos and greenfield projects.

Location: [`skills/doc-strategy-engineer`](skills/doc-strategy-engineer)

### Content Strategy & Content Architecture

Designs evidence-led content strategy, information architecture, page structure, SEO, localization, and UX handoffs before visual design. Defaults to Iranian market, Persian-native, RTL-first context unless the user states otherwise.

Location: [`skills/content-strategy-architecture`](skills/content-strategy-architecture)

### React 19

Build, refactor, and review React 19.x TypeScript with React Compiler assumed. Thin MUST/NEVER control surface for JSX, Hooks, forms, Suspense, and performance; deep topics live in progressive references. Defer Next.js boundaries to the framework skill and project `AGENTS.md`.

Location: [`skills/react-19`](skills/react-19)

### Test Engineering

Designs, implements, reviews, and maintains lean risk-based automated test suites. Adapts to the repository's language, framework, architecture, and tooling; optimizes for confidence rather than test count.

Location: [`skills/test-engineering`](skills/test-engineering)

## Repository layout

This repository uses `skills/<skill-name>/` as its distribution layout. Each skill is a portable package containing `SKILL.md` and its direct reference files.

Keep each skill self-contained. Relative links in `SKILL.md` must resolve inside the same skill directory so the complete directory can be copied into Cursor or packaged for ChatGPT without repository-external dependencies.

## Install in ChatGPT

ChatGPT supports uploaded skills for eligible accounts/workspaces. OpenAI currently documents the account-level flow as:

1. Open **Plugins** in ChatGPT.
2. Open the **Skills** tab.
3. Select **Create**.
4. Select **Upload from your computer**.
5. Upload the skill package and review the ChatGPT scan result.

For `software-architecture-advisor`, create a ZIP from the repository root:

```powershell
python scripts/package_chatgpt_skill.py software-architecture-advisor
```

Upload:

```text
dist/software-architecture-advisor.zip
```

The packager validates the required `SKILL.md` frontmatter and places the skill files at the ZIP root so the uploaded package is self-contained.

See [`skills/software-architecture-advisor/INSTALL.md`](skills/software-architecture-advisor/INSTALL.md) for account availability notes and the distinction between ChatGPT account installation and the project-scoped OpenAI Skills API.

Generated archives under `dist/` are local build artifacts and are not committed.

## Install in Cursor

The neutral `skills/` directory is preferable for a public catalog because `.cursor/skills/` is an installation and automatic-discovery location. Keeping source packages under `skills/` avoids activating every catalog skill when this repository is opened and leaves room for compatibility with other Agent Skills consumers.

Cursor does not automatically discover this repository's `skills/` directory. Install a skill by copying its complete directory to one of Cursor's discovery locations:

- Project: `<project>/.cursor/skills/<skill-name>/`
- Personal: `~/.cursor/skills/<skill-name>/`

### One Cursor project

Local — Windows PowerShell:

```powershell
$skill = "software-architecture-advisor"  # or doc-strategy-engineer, content-strategy-architecture, react-19, test-engineering
$source = Join-Path (Get-Location) "skills\$skill"
$destination = "D:\path\to\project\.cursor\skills\$skill"

New-Item -ItemType Directory -Force -Path (Split-Path $destination)
Copy-Item -Recurse -Force $source $destination
```

Replace the paths with the repository clone and target project locations.

### Personal Cursor skill

Local — Windows PowerShell:

```powershell
$skill = "software-architecture-advisor"  # or doc-strategy-engineer, content-strategy-architecture, react-19, test-engineering
$source = Join-Path (Get-Location) "skills\$skill"
$destination = Join-Path $HOME ".cursor\skills\$skill"

New-Item -ItemType Directory -Force -Path (Split-Path $destination)
Copy-Item -Recurse -Force $source $destination
```

Personal skills are available across projects. Project skills can be committed with a project and shared with its team.

## Repository structure

```text
skills/
  software-architecture-advisor/
    SKILL.md
    PROFILE.md
    PROJECT-CONTEXT.md
    DECISION-FRAMEWORK.md
    OUTPUT-TEMPLATE.md
    INSTALL.md
  doc-strategy-engineer/
    SKILL.md
    agents/
    assets/
    references/
    templates/
  content-strategy-architecture/
    SKILL.md
    agents/
    assets/
    references/
  react-19/
    SKILL.md
    agents/
    references/
  test-engineering/
    SKILL.md
    agents/
    assets/
scripts/
  package_chatgpt_skill.py
docs/
  improvements/
```

Each skill keeps its entry instructions concise and places detailed guidance in one-level reference files.
