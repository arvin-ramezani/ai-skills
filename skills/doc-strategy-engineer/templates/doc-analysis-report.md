# Documentation Analysis Report

**Project:** {{project_name}}  
**Analyzed by:** doc-strategy-engineer  
**Date:** {{date}}  
**Mode:** ANALYZE

---

## Executive Summary

- {{finding_1}}
- {{finding_2}}
- {{finding_3}}
- {{finding_4}}
- {{finding_5}}

**Overall Assessment:** {{Excellent / Good / Fragmented / Undocumented}}

---

## Project Context

| Attribute | Value |
|-----------|-------|
| Tech Stack | {{stack}} |
| Repo Type | {{monorepo / single / microservice}} |
| Existing Docs | {{count}} files found |
| AGENTS.md | {{yes/no}} |
| Agent Rules | {{count}} rules found |
| Tests | {{test framework + coverage signal}} |

---

## Findings by Category

### Gaps (Missing Knowledge)
| Priority | Topic | Evidence | Impact |
|----------|-------|----------|--------|
| {{P0/P1/P2}} | {{topic}} | {{where you looked, what you found}} | {{why it matters}} |

### Redundancy
| Topic | Locations | Recommendation |
|-------|-----------|----------------|
| {{topic}} | {{file1, file2, file3}} | {{merge or pick source of truth}} |

### Contradictions
| Topic | Doc A Says | Doc B / Code Says | Severity |
|-------|------------|-------------------|----------|
| {{topic}} | {{...}} | {{...}} | {{Critical/High}} |

### Dead Links / Stale References
| File | Broken Reference | Suggested Fix |
|------|-----------------|---------------|
| {{file}} | {{broken path}} | {{correct path or remove}} |

### AI Friction
| Issue | Example | Fix Strategy |
|-------|---------|--------------|
| {{e.g., 800-line README}} | {{...}} | {{split into indexed sections}} |

---

## AI-Fluency Score

{{score}} / 22 — {{rating}}

See `references/ai-fluency-checklist.md` for full checklist.

---

## Questions for You

Based on this analysis, I need clarification on:

1. **{{Question 1}}**  
   *Why this matters:* {{reason}}

2. **{{Question 2}}**  
   *Why this matters:* {{reason}}

3. **{{Question 3}}**  
   *Why this matters:* {{reason}}

4. **{{Question 4 (if needed)}}**  
   *Why this matters:* {{reason}}

5. **{{Question 5 (if needed)}}**  
   *Why this matters:* {{reason}}

---

## Recommended Next Step

{{Recommended workflow mode: PROPOSE / BOOTSTRAP / AUDIT / SYNC}}
