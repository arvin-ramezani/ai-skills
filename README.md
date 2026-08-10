# AI Skills

Reusable AI agent skills, decision frameworks, and improvement roadmaps.

## Skills

### Software Architecture Advisor

Creates requirement-driven architecture and stack recommendations. It prefers the simplest viable design, evaluates technology against project constraints, explains trade-offs, applies SOLID pragmatically, and produces concise Architecture Decision Records when needed.

Location: [`skills/software-architecture-advisor`](skills/software-architecture-advisor)

### Documentation Strategy Engineer

Analyzes project structure and documentation, then designs or improves a documentation strategy optimized for AI agent fluency and maintainability. Supports analyze, propose, bootstrap, audit, and sync workflows.

Location: [`skills/doc-strategy-engineer`](skills/doc-strategy-engineer)

### Test Engineering

Designs, implements, reviews, and maintains lean risk-based automated test suites. Adapts to the repository's language, framework, architecture, and tooling; optimizes for confidence rather than test count.

Location: [`skills/test-engineering`](skills/test-engineering)

## Repository layout

This repository uses `skills/<skill-name>/` as its distribution layout. Each skill is a portable package containing `SKILL.md` and its direct reference files.

The neutral `skills/` directory is preferable for a public catalog because `.cursor/skills/` is an installation and automatic-discovery location. Keeping source packages under `skills/` avoids activating every catalog skill when this repository is opened and leaves room for compatibility with other Agent Skills consumers.

Cursor does not automatically discover this repository's `skills/` directory. Install a skill by copying its complete directory to one of Cursor's discovery locations:

- Project: `<project>/.cursor/skills/<skill-name>/`
- Personal: `~/.cursor/skills/<skill-name>/`

## Install for one Cursor project

Local — Windows PowerShell:

```powershell
$skill = "software-architecture-advisor"  # or doc-strategy-engineer, test-engineering
$source = Join-Path (Get-Location) "skills\$skill"
$destination = "D:\path\to\project\.cursor\skills\$skill"

New-Item -ItemType Directory -Force -Path (Split-Path $destination)
Copy-Item -Recurse -Force $source $destination
```

Replace the paths with the repository clone and target project locations.

## Install as a personal Cursor skill

Local — Windows PowerShell:

```powershell
$skill = "software-architecture-advisor"  # or doc-strategy-engineer, test-engineering
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
  doc-strategy-engineer/
    SKILL.md
    README.md
    references/
    workflows/
    templates/
  test-engineering/
    SKILL.md
    agents/
    assets/
docs/
  improvements/
```

Each skill keeps its entry instructions concise and places detailed guidance in one-level reference files.
