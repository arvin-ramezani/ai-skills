# AI Skills

Reusable AI agent skills, decision frameworks, and improvement roadmaps.

## Skills

### Software Architecture Advisor

Creates requirement-driven architecture and stack recommendations. It prefers the simplest viable design, evaluates technology against project constraints, explains trade-offs, applies SOLID pragmatically, and produces concise Architecture Decision Records when needed.

Location: [`skills/software-architecture-advisor`](skills/software-architecture-advisor)

## Repository layout

This repository uses `skills/<skill-name>/` as its distribution layout. Each skill is a portable package containing `SKILL.md` and its direct reference files.

The neutral `skills/` directory is preferable for a public catalog because `.cursor/skills/` is an installation and automatic-discovery location. Keeping source packages under `skills/` avoids activating every catalog skill when this repository is opened and leaves room for compatibility with other Agent Skills consumers.

Cursor does not automatically discover this repository's `skills/` directory. Install a skill by copying its complete directory to one of Cursor's discovery locations:

- Project: `<project>/.cursor/skills/<skill-name>/`
- Personal: `~/.cursor/skills/<skill-name>/`

## Install for one Cursor project

Local — Windows PowerShell:

```powershell
$source = Join-Path (Get-Location) "skills\software-architecture-advisor"
$destination = "D:\path\to\project\.cursor\skills\software-architecture-advisor"

New-Item -ItemType Directory -Force -Path (Split-Path $destination)
Copy-Item -Recurse -Force $source $destination
```

Replace the paths with the repository clone and target project locations.

## Install as a personal Cursor skill

Local — Windows PowerShell:

```powershell
$source = Join-Path (Get-Location) "skills\software-architecture-advisor"
$destination = Join-Path $HOME ".cursor\skills\software-architecture-advisor"

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
docs/
  improvements/
```

Each skill keeps its entry instructions concise and places detailed guidance in one-level reference files.
