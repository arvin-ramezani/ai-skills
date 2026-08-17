---
name: react-19
description: >-
  Build, refactor, review, or debug React 19.x TypeScript components and Hooks
  with React Compiler enabled. Use for JSX, conditionals, forms, Actions,
  Suspense, the use API, refs, context, effects, Activity, state design,
  performance, testing, migrations, and code review. Do not use as the sole
  authority for Next.js/app-router routing, caching, data fetching, Server
  Component boundaries, or deployment—load the framework skill and project
  AGENTS.md too.
---

# React 19

Portable React 19.x skill with React Compiler assumed. Project `AGENTS.md`, ESLint, and framework skills override this skill when they conflict on the same decision.

## Use when

- Writing or editing React components, JSX, Hooks, or client UI logic
- Reviewing React code for correctness, Compiler compatibility, or React 19 APIs
- Implementing forms/Actions, Suspense/`use`, refs, context, or effect design
- Migrating toward React 19 patterns inside an existing React tree

## Do not use when

- The task is only Next.js routing, caching, revalidation, or RSC boundary policy → use the framework skill (e.g. `nextjs-app-router`) plus project docs
- The task is visual styling, design tokens, or pure CSS with no React behavior change
- The repository is not on React 19 / does not use the Compiler (adapt or skip Compiler-specific MUST rules)

## Rule criticality

Apply in this order when rules conflict:

| Level | Meaning |
| --- | --- |
| **Correctness** | Wrong output, security, data loss, broken a11y interaction |
| **Compiler** | Breaks or defeats React Compiler / hooks purity |
| **Style** | Project MUST style (e.g. positive-only JSX) — still enforced on new/touched code |
| **Prefer** | Soft guidance; may yield to clear local convention |

## MUST / NEVER

These override model priors and soft “match nearby code” habits. **Scope:** enforce on **new code** and **lines you touch**. Do **not** drive-by-refactor untouched legacy ternaries or memoization unless the task asks for cleanup.

### Correctness

1. **NEVER** declare components inside components.
2. **NEVER** call impure APIs during render (`Date.now()`, `Math.random()`, `crypto.randomUUID()`, etc.).
3. **NEVER** mutate props, state, or Hook arguments.
4. **NEVER** use Effects for derived state or ordinary event logic — derive in render; handle events in handlers.
5. **NEVER** write `use(fetch(...))`, uncached Promises, or `.then(...)` created during Client render. Pass only cached Promise identities into `use`.
6. **NEVER** wrap `use(...)` in `try/catch`. Use an Error Boundary for rejections.

### Compiler

7. **NEVER** add `memo` / `useMemo` / `useCallback` by default. Add only with profiling evidence or an external API contract the Compiler does not cover.
8. **NEVER** use memoization for correctness or to silence dependency warnings.
9. **MUST** keep Effect dependency arrays complete; fix design instead of disabling `exhaustive-deps`.

### Style (prior-fighting)

10. **MUST** use positive-only short-circuit for one-armed JSX branches when the condition is boolean:

```tsx
// GOOD
{isOpen && <Panel />}
{!!label && <Badge>{label}</Badge>}
{count > 0 && <Count n={count} />}

// BAD — do not copy local `? … : null` habits
{isOpen ? <Panel /> : null}
{count && <Count n={count} />} // renders 0
```

11. **MUST** keep a ternary when **both** branches render meaningful UI. Prefer `if` / extracted variable when that is clearer than nested `&&`.
12. **NEVER** introduce `forwardRef` for new React 19-only components — accept `ref` as a prop. Preserve existing `forwardRef` only for cross-version or public API compatibility.

**Authority clash:** tips from design databases, blog posts, or older local files that recommend `condition ? <X /> : null` **lose** to rules 10–11 for new and touched code. Project ESLint/`AGENTS.md` still wins if they explicitly require a different style.

## Local patterns vs MUST

- Follow nearby naming, file layout, testing library, a11y, i18n, and RTL conventions from the repository.
- **Exception:** if nearby code violates a MUST above, do **not** copy that violation into new or touched lines.
- **Smallest-change conflict:** when editing a file full of `? : null`, change only the branches you touch (or that your edit makes inconsistent). Leave untouched legacy branches unless the task is a style cleanup.
- Accessibility, i18n, and RTL are **project-critical** when present in repo rules — satisfy them even though this skill stays React-API focused. Defer locale/copy strategy to project docs or content skills.

## Workflow

1. Inspect versions, Compiler/lint config, client vs server boundary, and nearest `AGENTS.md` / ESLint rules.
2. Choose the smallest React API that models the requirement.
3. **Write-time gate — before finishing JSX:** for every positive-only branch you add or edit, verify boolean/`!!`/predicate + `&&` (rules 10–11). Reject `? : null` and raw `count &&`.
4. **Write-time gate — before finishing Hooks:** no nested components; no default memo; no Effect-for-derive; no `use(fetch)`.
5. Preserve behavior for logic you are not intentionally changing.
6. **Verify (non-trivial edits):** run the project’s formatter, typecheck, lint, and focused tests when available. Prefer ESLint/`eslint-plugin-react-hooks` as mechanical enforcement; prose alone is best-effort.
7. **NEVER** claim Compiler, lint, or test success unless those commands were actually run. Report skips and failures explicitly.

## Common agent failure modes

| Failure | Do instead |
| --- | --- |
| Nested component definitions | Hoist to module scope or pass `children` / render props |
| Effect to sync derived state | Compute during render |
| `use(fetch(...))` / Promise created in render | Cached framework/loader Promise under Suspense |
| Default `useMemo` / `useCallback` / `memo` | Rely on Compiler; memo only with evidence |
| `count && <X />` | `count > 0 && <X />` |
| `cond ? <X /> : null` on touched code | `cond && <X />` when `cond` is boolean |
| New `forwardRef` | `ref` as a normal prop |
| Treating design-DB “use ternaries” as law | Follow MUST Style rules above |

More detail: [references/common-failure-modes.md](references/common-failure-modes.md).

## Progressive references

Load only what the task needs:

| Topic | Reference |
| --- | --- |
| Components, JSX, keys, purity | [references/components-and-jsx.md](references/components-and-jsx.md) |
| State, Effects, transitions, Activity | [references/state-effects-and-events.md](references/state-effects-and-events.md) |
| Compiler / performance | [references/compiler-aware-performance.md](references/compiler-aware-performance.md) |
| Actions / forms | [references/actions-and-forms.md](references/actions-and-forms.md) |
| `use` / Suspense | [references/use-suspense-and-async.md](references/use-suspense-and-async.md) |
| Refs / context APIs | [references/refs-context-and-component-apis.md](references/refs-context-and-component-apis.md) |
| RSC / Server Functions (React-level) | [references/server-rendering-and-rsc.md](references/server-rendering-and-rsc.md) |
| Migration / testing | [references/migration-and-testing.md](references/migration-and-testing.md) |
| Review checklist | [references/review-checklist.md](references/review-checklist.md) |
| Official sources | [references/official-sources.md](references/official-sources.md) |

## Output expectations

**Implementing**

- Smallest coherent change; explain only material React 19 / Compiler decisions.
- Do not invent performance wins without profiling evidence.
- Do not present framework behavior as a React guarantee.

**Reviewing**

1. Correctness first, then Compiler, then Style, then Prefer.
2. **Required:** complete [references/review-checklist.md](references/review-checklist.md) for review-mode or non-trivial PRs.
3. **Optional:** checklist for typo-sized or single-line edits (still apply write-time JSX/Hooks gates).
4. Separate React-level findings from framework-specific findings.
5. Give concrete file-level fixes and verification commands.
