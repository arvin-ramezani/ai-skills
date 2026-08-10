# Documentation Architecture Decision Matrix

Use this matrix to recommend the right documentation architecture for a project.

## Option A: Code-Adjacent (Distributed)
**Structure:** Docs live next to the code they describe.
```
src/
├── features/
│   ├── auth/
│   │   ├── auth.service.ts
│   │   └── auth.md          ← feature doc
│   └── payment/
│       ├── payment.service.ts
│       └── payment.md
```

**Best for:**
- Microservices
- Teams >5 people with clear ownership
- Projects where features change independently
- AI agents that search by file path

**Pros:**
- Docs naturally stay close to code changes
- Easy to find "what does this feature do?"
- Low cognitive load per doc

**Cons:**
- Hard to get a "whole system" view
- Risk of fragmentation
- Requires a top-level index/map

---

## Option B: Centralized
**Structure:** All docs in `/docs` with strict hierarchy.
```
docs/
├── 01-product.md
├── 02-architecture.md
├── 03-features/
│   ├── auth.md
│   └── payment.md
```

**Best for:**
- Small to medium monoliths
- Onboarding new developers
- Projects needing a single source of truth

**Pros:**
- One place to look
- Easy to enforce conventions
- Natural hierarchy

**Cons:**
- Docs can drift from code location
- Large files if not carefully split
- Requires discipline to maintain

---

## Option C: Hybrid (Recommended for most projects)
**Structure:**
- Centralized architecture, product, and domain docs
- Code-adjacent feature details and API specs
- ADRs centralized

```
docs/
├── 00-index.md
├── 01-product.md
├── 02-domains.md
├── 03-architecture.md
├── 04-decisions/
└── 05-operations.md
src/
├── features/
│   ├── auth/
│   │   ├── auth.service.ts
│   │   └── README.md        ← feature-specific only
```

**Best for:**
- Medium to large applications
- NestJS / NextJS projects with clear module boundaries
- Long-lived projects that will scale

**Pros:**
- Strategic knowledge centralized
- Tactical knowledge close to code
- Scales from small to large

**Cons:**
- Two places to maintain conventions
- Requires explicit traceability links

---

## Selection Guide

| Factor | Choose |
|--------|--------|
| < 3 developers, < 6 months old | Centralized (B) |
| Microservices, team per service | Code-Adjacent (A) |
| Monorepo, multiple domains, > 1 year lifespan | Hybrid (C) |
| Heavy AI-agent usage, frequent agent searches | Hybrid (C) with strong index |
| Existing docs are heavily fragmented | Hybrid (C) with migration plan |
