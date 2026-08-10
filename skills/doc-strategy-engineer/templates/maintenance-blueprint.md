# Documentation Maintenance Blueprint

**Project:** {{project_name}}  
**Created by:** doc-strategy-engineer  
**Last Updated:** {{date}}

This blueprint defines how documentation stays synchronized with the codebase over time.

---

## Maintenance Cadence

| Activity | Frequency | Trigger | Owner |
|----------|-----------|---------|-------|
| Full Audit | Monthly / Per sprint | Calendar | AI + Human review |
| Sync Check | Per PR | Code change | AI (report) + Human (approve) |
| Index Update | As needed | New doc created | AI auto-update |
| ADR Review | Quarterly | Architecture changes | Tech lead |

---

## Sync Triggers & Documentation Impact

When you see a change in...

### Feature Code
Check:
- [ ] Domain doc still accurate?
- [ ] Feature doc needs update?
- [ ] Tests referenced still exist?
- [ ] API contract doc updated?
- [ ] Flow diagram still valid?

Decision: Update / No action / Flag for review

### Database Schema
Check:
- [ ] Domain model doc updated?
- [ ] API docs reflect new fields?
- [ ] Migration notes added?
- [ ] Feature docs using this entity updated?

### Refactor (File Moves / Renames)
Check:
- [ ] All relative links in docs updated?
- [ ] Architecture diagram paths updated?
- [ ] Test references updated?
- [ ] Index/map updated?

### Architecture Change
Check:
- [ ] ADR written?
- [ ] Architecture doc updated?
- [ ] Affected domain docs updated?
- [ ] Diagrams regenerated?

### Bug Fix
Determine:
- [ ] Was the bug caused by incorrect docs? → Fix docs
- [ ] Was the bug missing knowledge? → Add docs
- [ ] Was the bug implementation only? → No doc change
- [ ] Was a test missing? → Note in maintenance log

---

## Quality Gates

Before any doc is considered "maintained":
1. It links to at least one implementation file
2. It links to at least one test file OR explains why not
3. It has no broken relative paths
4. It states its evidence level (Confirmed/Observed/Inferred)
5. It fits in one context window (~300 lines)

---

## Drift Detection

Run `doc-strategy-engineer sync` when:
- A sprint ends
- A major PR merges
- A developer says "the docs are wrong"
- Before a new developer onboards

The skill will output a `doc-sync-proposal.md` with specific file-level recommendations.

---

## Escalation Rules

| Situation | Action |
|-----------|--------|
| Doc contradicts code | Critical — fix within 24h |
| Missing doc for new domain | High — create within 1 week |
| Broken link | Medium — fix at next sync |
| Outdated screenshot | Low — fix when convenient |
| Doc longer than 400 lines | Medium — split at next opportunity |

---

## Revalidation Prompt

For recurring sync sessions, use: `templates/revalidation-prompt.md`
