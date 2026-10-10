# Context Engineering — Skill Selection and Approval Cases

Use these scenarios to evaluate implicit skill selection and structural authority.
These are expected behavior cases, not evidence of a model evaluation run.

| User request | Primary skill | Expected result |
| --- | --- | --- |
| Review and reorganize a 320-line mixed handbook | `context-engineering` | Choose justified SPLIT/KEEP, execute in authorized scope, compare every requirement against baseline, repair navigation |
| Improve repository docs and split six independent files | `context-engineering` | No three-file approval checkpoint; map content and run checks for all affected files |
| Audit a cohesive 164-line protocol without edits | `context-engineering` | Read-only audit; explain KEEP if cohesive; no mutation |
| Write a feature's behavior specification and acceptance criteria | `doc-strategy-engineer` | Author feature document and sync relevant index/contract without inventing behavior |
| Propose cross-session agent memory for the project | `doc-strategy-engineer` | Follow memory checkpoint and lifecycle; no restructuring unless requested |
| Write feature docs and reorganize scattered canonical docs | `doc-strategy-engineer` for content, `context-engineering` for structure | Complete authorized structural changes with preservation evidence; no arbitrary file-count stop |
| Splitting exposes conflicting accepted security requirements | `context-engineering` | Preserve both, request owner decision on meaning, complete unaffected structural work |
| User requests moving docs outside stated scope | Whichever is primary | Escalate scope change; do not assume permission to rewrite unrelated docs |
| Sync code changes and reorganize eight related docs within explicitly authorized scope | `doc-strategy-engineer` for sync, `context-engineering` for structure | Perform justified restructuring and preservation checks without broad-restructure approval |
| Migration finds contradictory accepted security rules but other docs are unaffected | `context-engineering` | Preserve disputed evidence, escalate contract decision, finish unaffected authorized moves |

Evaluation gate: confirm the selected skill(s), authorized changes, preserved units,
owner-decision boundaries, and reported verification. A line threshold triggers
review, not mandatory splitting; no example authorizes changing application behavior
or merging a PR.
