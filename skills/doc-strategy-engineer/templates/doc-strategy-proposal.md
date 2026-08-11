# Documentation Strategy Proposal

**Project:** {{project_name}}  
**Based on Analysis:** {{analysis_report_link}}  
**Date:** {{date}}  
**Mode:** PROPOSE

---

## Chosen Architecture

**Model:** {{Code-Adjacent / Centralized / Hybrid}}  
**Rationale:** {{why this fits the project better than alternatives}}

---

## Proposed Directory Structure

```
{{tree}}
```

---

## Conventions

### File Naming
- {{rule}}

### Cross-References
- {{format, e.g., relative paths: `../../features/auth/auth.md`}}

### Diagrams
- Tool: {{Mermaid / Draw.io / PlantUML}}
- Storage: {{inline / separate files in docs/diagrams/}}

### Frontmatter
- {{minimal / none / specific fields}}

---

## Traceability Rules

```
Product
  ↓
Domain
  ↓
Feature
  ↓
Implementation (relative path)
  ↓
Tests (relative path)
```

- Domain docs link to: {{...}}
- Feature docs link to: {{...}}
- ADRs link to: {{...}}

---

## AI-Specific Optimizations

### AGENTS.md
{{What one paragraph to add}}

### Agent Rules
{{What rule files to create and their path globs}}

### Index Strategy
{{How the AI finds the right doc quickly}}

---

## Migration Path

**Current State → Proposed State**

| Step | Action | Effort | Risk |
|------|--------|--------|------|
| 1 | {{...}} | {{S/M/L}} | {{...}} |
| 2 | {{...}} | {{S/M/L}} | {{...}} |
| 3 | {{...}} | {{S/M/L}} | {{...}} |

---

## Expected Outcomes

After migration:
- AI-Fluency Score: {{predicted}} / 23
- Time for new dev to understand auth flow: {{estimate}}
- Time for AI to locate domain context: {{estimate}}

---

## Approval Request

To proceed, confirm:
- [ ] Architecture choice approved
- [ ] Directory structure approved
- [ ] I am authorized to create files (BOOTSTRAP) or produce edit proposals (SYNC)
