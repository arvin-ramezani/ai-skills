# Common agent failure modes

Patterns models often emit. Correct them before finishing the change.

## Nested components

**Wrong:** defining `function Row()` inside `function Table()`.

**Why:** remounts on every parent render; breaks state and Compiler assumptions.

**Fix:** module-scope component, or `children` / props.

## Effects for derived state

**Wrong:** `useEffect(() => setFullName(first + last), [first, last])`.

**Fix:** `const fullName = first + last` during render. Use Effects only to sync with external systems.

## `use(fetch)` / Promise in render

**Wrong:** `use(fetch(url))` or `use(load().then(...))` created during Client render.

**Fix:** pass a cached Promise from the framework, Server Component, route loader, or Suspense-compatible cache. Put the reader under Suspense; use an Error Boundary for rejection. Never `try/catch` around `use`.

## Default memoization

**Wrong:** wrapping every handler in `useCallback` and every child in `memo` “for performance.”

**Fix:** write pure components; rely on React Compiler. Add manual memo only with profiling evidence or an external stable-identity contract.

## Boolean-ish `&&` bugs

**Wrong:** `{count && <Badge />}` → React renders `0`.

**Fix:** `{count > 0 && <Badge />}` or `{!!count && <Badge />}` when appropriate.

## Ternary-to-null habit

**Wrong:** `{open ? <Drawer /> : null}` copied from nearby code or design tips.

**Fix on new/touched lines:** `{open && <Drawer />}`. Leave untouched legacy alone unless cleanup was requested. Design-guide “prefer ternaries” does not override this skill’s Style MUST when project rules agree.

## New `forwardRef`

**Wrong:** wrapping a React 19-only component in `forwardRef`.

**Fix:** `function Input({ ref, ...props }: Props) { ... }`. Keep existing `forwardRef` for libraries that still support older React.

## Framework vs React confusion

**Wrong:** encoding Next.js caching/revalidation rules as “React 19 requires…”.

**Fix:** state framework findings separately; load the framework skill for boundaries.

## Claiming green without running checks

**Wrong:** “lint/compiler are fine” after a non-trivial edit with no command run.

**Fix:** run project scripts or explicitly report that verification was skipped.
