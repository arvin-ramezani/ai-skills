# Components and JSX (React 19)

Deep guidance for component structure and rendering. High-frequency MUST/NEVER rules live in `SKILL.md` and win on new/touched code.

## Function components

- Use function components for new code.
- Keep components and custom Hooks pure.
- Treat props, state, context values, and Hook arguments as immutable snapshots.
- Derive values during render when they can be calculated from existing props or state.
- Do not create component definitions inside other components — hoist to module scope.
- Keep render deterministic. Do not call impure APIs such as `Date.now()`, `Math.random()`, `crypto.randomUUID()`, or `performance.now()` during render.
- Use stable semantic keys from data. Never generate keys during render.

## Positive-only JSX branches

Enforce on **new and touched** branches (Style criticality in `SKILL.md`):

```tsx
// MUST
{isReady && <ReadyBanner />}
{!!title && <Title>{title}</Title>}
{items.length > 0 && <List items={items} />}

// NEVER on new/touched code
{isReady ? <ReadyBanner /> : null}
{items.length && <List items={items} />}
```

Keep a ternary when both branches are meaningful:

```tsx
{isOn ? <OnIcon /> : <OffIcon />}
```

Prefer an `if` statement or extracted variable when nested short-circuit JSX harms clarity.

**Do not** mass-convert untouched legacy `? : null` unless the task is cleanup. When editing one branch in a mixed file, make that branch correct without expanding scope.

## Composition

- Prefer composition and explicit props over `cloneElement`, `Children` transformations, or hidden coupling.
- Preserve controlled versus uncontrolled input behavior for the component’s full lifetime.

## Deprecated patterns (do not introduce)

- Function component `propTypes` / `defaultProps` (use parameter defaults)
- String refs, legacy Context APIs, module-pattern factories
- `React.createFactory`, `ReactDOM.render` / `hydrate` / `unmountComponentAtNode` / `findDOMNode`
- `react-dom/test-utils`, reliance on React internals, old JSX transform
- New `forwardRef` wrappers for React 19-only components
