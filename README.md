# AI Skills

Reusable AI agent skills, decision frameworks, and improvement roadmaps.

## Skills

### Software Architecture Advisor

Creates requirement-driven architecture and stack recommendations. It prefers the simplest viable design, evaluates technology against project constraints, explains trade-offs, applies SOLID pragmatically, and produces concise Architecture Decision Records when needed.

Location: [`skills/software-architecture-advisor`](skills/software-architecture-advisor)

Install guide: [`skills/software-architecture-advisor/INSTALL.md`](skills/software-architecture-advisor/INSTALL.md)

### Documentation Strategy Engineer

Plans documentation strategy, authors feature analyses/specifications, handles documentation-to-code synchronization, and designs optional cross-session agent memory. For repository-wide documentation structure and splitting rules, use Context Engineering.

Location: [`skills/doc-strategy-engineer`](skills/doc-strategy-engineer)

### Context Engineering

**Source of truth for repository documentation structure and document-splitting policy.** Establishes routing/indexes, audits retrieval and authority, and executes justified structural migrations with a preservation map. Documents over 150 lines trigger review, not automatic splitting; the line thresholds are local conventions, not hard limits.

Location: [`skills/context-engineering`](skills/context-engineering)

Use **Context Engineering** for large-document review/splitting, index/routing repair, and structure audits; use **Documentation Strategy Engineer** for feature documentation, documentation strategy proposals, and agent-memory lifecycle. For mixed tasks, use the latter to author content and the former's structural policy and preservation workflow for any restructuring. A justified in-scope split needs no extra approval based on file count; owner decisions about changed meaning, security/product/architecture, or scope expansion still require approval.

Install with `python scripts/install_skill.py context-engineering --project "D:\path\to\project"` or package with `python scripts/package_skill.py context-engineering`.

### Content Strategy & Architecture

Designs evidence-led content strategy, public-site information architecture, conversion and SEO structure, localization, visual communication requirements, and UX/UI handoffs for content-driven experiences.

Location: [`skills/content-strategy-architecture`](skills/content-strategy-architecture)

### Product Information Architecture

Designs user-facing concepts, objects, capability groups, navigation, lists/details, findability, role visibility, localization, visual communication requirements, and UX handoffs for functional software applications.

Location: [`skills/product-information-architecture`](skills/product-information-architecture)

Use Content Strategy & Architecture for public marketing/content surfaces and Product Information Architecture for authenticated or functional application surfaces. A mixed product may use both for separate surfaces without duplicating ownership.

### UX Flow Designer

Designs, analyses, documents, and reviews end-to-end application UX flows, including user needs, journeys, states, business rules, permissions, failures, recovery, accessibility, analytics, and implementation-ready acceptance criteria.

Location: [`skills/ux-flow-designer`](skills/ux-flow-designer)

### React 19

Builds, refactors, and reviews React 19.x TypeScript with React Compiler assumed.

Location: [`skills/react-19`](skills/react-19)

### Test Engineering

Designs, implements, reviews, and maintains lean risk-based automated test suites.

Location: [`skills/test-engineering`](skills/test-engineering)

## Distribution model

`skills/<skill-name>/` is the catalog/source layout. Each skill is a portable, self-contained package with `SKILL.md` and its direct references.

The canonical installed layout is vendor-neutral:

```text
Project: <project>/.agents/skills/<skill-name>/
Global:  ~/.agents/skills/<skill-name>/
```

Use `.agents/` as the single source of truth for installed skills. Do not maintain parallel `.cursor/`, `.claude/`, `.codex/`, or other vendor-specific copies of the same skill. Agent-specific tooling may point to, sync, or import the shared `.agents/` tree when required by that tool.

This repository does not claim that every AI product natively auto-discovers `.agents/`; the environment using these skills is responsible for exposing the shared `.agents/` installation to each agent.

Keep runtime references relative to the skill directory so the package can be moved, synchronized, zipped, or uploaded without repository-external dependencies.

## Install into `.agents`

### Project install

From this repository root:

```powershell
python scripts/install_skill.py software-architecture-advisor --project "D:\path\to\project"
```

Installs to:

```text
D:\path\to\project\.agents\skills\software-architecture-advisor\
```

### Global install

```powershell
python scripts/install_skill.py software-architecture-advisor --global
```

Installs to:

```text
~/.agents/skills/software-architecture-advisor/
```

The installer replaces only the selected skill directory and leaves other installed skills untouched.

## Package a portable skill ZIP

For consumers that accept uploaded skill packages, create a neutral archive:

```powershell
python scripts/package_skill.py software-architecture-advisor
```

Output:

```text
dist/software-architecture-advisor.zip
```

The package keeps `SKILL.md` at the ZIP root, validates required frontmatter and relative references, and excludes source-only installation guidance.

### ChatGPT upload

For ChatGPT accounts/workspaces that expose uploaded Skills, the same neutral ZIP can be uploaded through **Plugins → Skills → Create → Upload from your computer**. ChatGPT upload is one consumer path; it is not the canonical repository installation model.

See [`skills/software-architecture-advisor/INSTALL.md`](skills/software-architecture-advisor/INSTALL.md) for details.

Generated archives under `dist/` are local build artifacts and are not committed.

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
  context-engineering/
  content-strategy-architecture/
  product-information-architecture/
  ux-flow-designer/
  react-19/
  test-engineering/
scripts/
  install_skill.py
  package_skill.py
docs/
  improvements/
```

Each skill keeps its entry instructions concise and places detailed guidance in direct reference files or subdirectories owned by that skill.
