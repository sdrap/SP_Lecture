# Implementation Plan: Add Exercises & Code Navigation Layers

## Overview
Add two new navigation layers (Exercises and Code) with proper directory structure, placeholder files, and versioning protocol. Include agents folder versioning documentation.

---

## Directory Structure to Create

```
docs/
├── exercises/
│   ├── index.md
│   ├── 01-sets-functions/
│   │   ├── exercises.md
│   │   └── solutions.md
│   ├── 02-measure/
│   │   ├── exercises.md
│   │   └── solutions.md
│   ├── 03-integration/
│   ├── 04-martingales/
│   ├── 05-markov/
│   ├── 06-continuous-time/
│   ├── 07-stochastic-integral/
│   └── 08-stochastic-exponential/
├── code/
│   ├── index.md
│   ├── probability-foundations.md
│   ├── random-walks.md
│   ├── stopping-times.md
│   ├── markov-chains.md
│   ├── brownian-motion.md
│   ├── martingales.md
│   ├── stochastic-integral.md
│   ├── ito-calculus.md
│   ├── sdes.md
│   ├── girsanov.md
│   ├── option-pricing.md
│   ├── monte-carlo.md
│   └── assets/
└── index.md          (add version frontmatter)

agents/
├── CONTEXT.md
├── lessons.md        (add workflow notes - DONE)
└── versioning.md     (NEW - create with protocol)

CHANGELOG.md          (NEW - create in root)
```

---

## Release Impact

| Component | Bump | From → To | Reason |
|-----------|------|-----------|--------|
| docs | MINOR | 0.1.0 → 0.2.0 | Add Exercises & Code navigation layers |

---

## Branch
- Name: `feat/exercises-code-navigation`

---

## Agent Steps

### Phase 1: Create versioning documentation
- [x] Create `agents/versioning.md` with complete protocol
- [x] Update `agents/lessons.md` with agent restrictions

### Phase 2: Create CHANGELOG.md
- [ ] Create `CHANGELOG.md` in repository root

### Phase 3: Update docs/index.md
- [ ] Add version frontmatter: `version: 0.1.0` (initial)

### Phase 4: Create exercise directories
- [ ] Create `docs/exercises/index.md`
- [ ] Create directories 01-08 with exercises.md and solutions.md

### Phase 5: Create code directories
- [ ] Create `docs/code/index.md`
- [ ] Create all topic .md files
- [ ] Create `docs/code/assets/` directory

### Phase 6: Update mkdocs.yml
- [ ] Add Exercises navigation section
- [ ] Add Code navigation section

### Phase 7: Verify
- [ ] Run `mkdocs serve`
- [ ] Verify navigation works
- [ ] Check for errors

### Phase 8: Commit and notify
- [ ] Stage all changes
- [ ] Commit: "feat: add exercises and code navigation framework"
- [ ] Notify user: "Implementation complete. Waiting for explicit command to proceed."
- [ ] **STOP: Wait for explicit command before Phase 9**

---

## Agent Steps (after explicit user command)

### Phase 9: Merge and Tag (after explicit command)
- [ ] Wait for user command: "merge to main" or "proceed with release"
- [ ] Checkout main: `git checkout main`
- [ ] Merge branch: `git merge feat/exercises-code-navigation`
- [ ] Update version in `docs/index.md` to `0.2.0`
- [ ] Update `CHANGELOG.md` with release date
- [ ] Commit: "chore: bump version to v0.2.0"
- [ ] Create tag: `git tag v0.2.0` (after explicit command)
- [ ] Notify user: "Ready for push"

## Phase 10: Owner push (always owner-only)
- [ ] Push: `git push origin main`
- [ ] Push tag: `git push origin v0.2.0`

---

## Files to Create/Modify

### New Files
1. `agents/versioning.md` - Complete versioning protocol
2. `CHANGELOG.md` - Release history
3. `docs/exercises/index.md` - Exercises overview
4. `docs/exercises/01-sets-functions/exercises.md`
5. `docs/exercises/01-sets-functions/solutions.md`
6. [All other chapter exercise files...]
7. `docs/code/index.md` - Code overview
8. [All code topic .md files...]
9. `docs/code/assets/` (empty directory)

### Modified Files
1. `agents/lessons.md` - Add agent workflow notes
2. `docs/index.md` - Add version frontmatter
3. `mkdocs.yml` - Add new navigation sections

---

## Verification Checklist

- [ ] `mkdocs serve` runs without errors
- [ ] Exercises navigation appears correctly
- [ ] Code navigation appears correctly
- [ ] All sub-items visible in navigation
- [ ] No broken links
- [ ] Math rendering works

---

## Notes

- **Agent pauses at Phase 8** - waits for explicit command
- **Agent proceeds to Phase 9 only after explicit command** like:
  - "merge to main"
  - "proceed with merge and tag"
  - "create tag v0.2.0"
- **Push (Phase 10) is always owner-only** - agent never pushes
- Version bump happens AFTER merge on main branch
- Tag created on main after version commit
