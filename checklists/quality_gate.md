# Zero AI-Slop Quality Gate Checklist

Use this checklist during PR reviews, autonomous agent task verification, and pre-deployment sanity checks.

## 1. UI & Visual Design (Anti-Slop)
- [ ] **No Generic Gradients**: No `#667eea` / `#764ba2` or repetitive purple-indigo background sweeps.
- [ ] **No Unmotivated Glassmorphism**: Cards have solid contrast and legible borders, not random blurry backdrops.
- [ ] **No Template Clichés**: No predictable 3-column card layouts with generic centered icons.
- [ ] **Strict Typographic Hierarchy**: Maximum 2 primary font families; intentional scale, line height, and tracking.
- [ ] **Responsive Breakpoints**: Verified on Mobile (375px), Tablet (768px), and Desktop (1280px+). Minimum touch target >= 44px.

## 2. Frontend Engineering
- [ ] **Strict TypeScript**: No `any` escape hatches; props and API contracts are fully typed.
- [ ] **Zero Leaked Secrets**: No service keys, admin secrets, or database URLs in frontend code.
- [ ] **Real Functionality**: Every button, input, toggle, and dropdown actually functions; zero dummy `onClick={() => {}}`.
- [ ] **Performance & CLS**: Explicit width/height on images and media, lazy-loaded offscreen assets.

## 3. Backend & Data Integrity
- [ ] **Input Validation**: Server-side validation using Zod/Pydantic/Joi on every incoming request.
- [ ] **Transactions & Relations**: Atomic transactions for multi-step mutations; foreign key constraints respected.
- [ ] **Error Handling**: Graceful error envelopes with semantic HTTP codes; no internal stack traces leaked.
- [ ] **Security**: Parameterized queries, CSRF defenses, rate limiting, and RBAC / RLS checks.

## 4. Engineering Discipline (Ponytail)
- [ ] **Minimal Working Diff**: No unrequested files, unused abstractions, or speculative boilerplate.
- [ ] **Existing Code Reused**: Reused existing utilities, design tokens, and components instead of duplicating.
- [ ] **Verified with Proof**: Build passed, linter passed, tests executed with real output captured.
