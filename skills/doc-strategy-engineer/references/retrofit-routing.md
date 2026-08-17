# Retrofit routing for started projects

Use when the repository already has docs, `AGENTS.md`, tool adapters, or indexes, but agents still miss existing facts. Prefer this path over rewriting the docs tree or expanding feature docs first.

## When retrofit applies

- Docs or conventions exist, but discoverability fails within two routing hops.
- High-frequency rules live only in deep docs, skills, or tribal knowledge.
- `AGENTS.md` / adapters are empty, stale, or only point at large dumps.
- The user wants better AI fluency on an **already-started** project without a full redesign.

Do **not** use retrofit as an excuse to invent a new layer model or replace a sound local taxonomy. Keep the skill's canonical layers; fix routes into them.

## Sequence (mandatory order)

```text
inventory → 2-hop gaps → thin adapter / index patches → then feature docs or redesign
```

1. **Inventory routing surfaces** (scoped to the task):
   - root and package `AGENTS.md`;
   - tool adapters (`CLAUDE.md`, Cursor rules, Codex/Claude skill adapters, etc.);
   - nearest indexes / maps;
   - high-traffic deep docs they should reach.
2. **Find undiscoverable-but-existing facts** — knowledge that already lives in the repo but cannot be reached via:
   ```text
   AGENTS.md or adapter → index (optional package index) → canonical doc
   ```
   within two hops (one extra scoped index allowed in large monorepos). Mark each gap: fact location, expected entry point, why the hop fails (missing link, wrong layer, buried in a long file, no mention of the convention).
3. **Patch routing before rewrite** — add or tighten thin adapters and indexes so they **name** high-frequency conventions and point to the canonical owner. Do not paste full rule bodies into adapters.
4. **Only then** run `document-feature`, broad `propose` migration, or large doc rewrites for remaining content gaps.
5. Run the memory checkpoint. If enabled, add memory only after canonical routing and authority are clear; if disabled or deferred, record that decision so later agents do not ask repeatedly.

If the user asked only for a feature FA, still run a **scoped** routing check for that feature's domain: if the FA would be unreachable from the nearest adapter/index, fix that route in the same change (or ask if mutation is disallowed).

## Thin adapter requirements

Adapters and high-frequency sections of `AGENTS.md` must:

| Do | Don't |
| --- | --- |
| Name the convention in one line (what / when) | Duplicate the full deep doc |
| Link to the canonical project doc or skill | Invent a second source of truth |
| List only always-needed constraints and entry points | Dump entire `docs/` trees |
| Stay small enough for frequent auto-load | Grow into a second manual |

High-frequency conventions (examples of *kinds*, not project facts): language/default style, test command, doc entry index, “where feature FAs live,” client vs server boundary pointers, lint/format commands. Put detail in project docs; keep the adapter as a labeled map.

## Audit outputs for retrofit

Report, with evidence labels:

- Routing inventory (files checked).
- Existing facts that fail 2-hop discoverability (path + gap).
- Adapter/index patches applied or proposed.
- Content gaps that still need new docs (after routing is fixed).
- Explicit “do not rewrite yet” items where routing alone unblocks agents.

Severity: undiscoverable **accepted** contracts or safety rules → High/Critical. Missing index polish → Medium/Low.

## Gate before broad work

| Requested next step | Gate |
| --- | --- |
| `document-feature` | Ensure the new/updated doc is linked from the nearest index; fix if the domain is otherwise unreachable |
| Large content rewrite | Prefer routing patches first when facts already exist |
| `propose` / restructure | Inventory and resolve undiscoverable-existing facts before moving trees |
| `bootstrap` | Only when there is no usable docs/routing system; otherwise retrofit |

## Mutation boundaries

Same as the skill: apply small routing/index/link repairs when the user asked to improve docs or retrofit. Ask before deleting docs, changing overall architecture, or relocating more than three files.
