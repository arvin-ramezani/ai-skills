# AI Skills

Reusable AI agent skills, decision frameworks, and improvement roadmaps.

## Skills

### Software Architecture Advisor

Creates requirement-driven architecture and stack recommendations. It prefers the simplest viable design, evaluates technology against project constraints, explains trade-offs, applies SOLID pragmatically, and produces concise Architecture Decision Records when needed.

Location: [`.cursor/skills/software-architecture-advisor`](.cursor/skills/software-architecture-advisor)

## Install for one Cursor project

Local — Windows PowerShell:

```powershell
$source = Join-Path (Get-Location) ".cursor\skills\software-architecture-advisor"
$destination = "D:\path\to\project\.cursor\skills\software-architecture-advisor"

New-Item -ItemType Directory -Force -Path (Split-Path $destination)
Copy-Item -Recurse -Force $source $destination
```

Replace the paths with the repository clone and target project locations.

## Install as a personal Cursor skill

Local — Windows PowerShell:

```powershell
$source = Join-Path (Get-Location) ".cursor\skills\software-architecture-advisor"
$destination = Join-Path $HOME ".cursor\skills\software-architecture-advisor"

New-Item -ItemType Directory -Force -Path (Split-Path $destination)
Copy-Item -Recurse -Force $source $destination
```

Personal skills are available across projects. Project skills can be committed with a project and shared with its team.

## Repository structure

```text
.cursor/skills/
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
