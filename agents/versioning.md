# Stochastics Lecture Notes — Release & Versioning Guide

> **Every implementation plan must follow this protocol.**
> **IMPORTANT: Only the repository owner may push to origin or merge to main.**

---

## 1. Versioning Model (SemVer)

| Version | Meaning |
|---------|---------|
| **MAJOR** | Structural changes: new navigation layers, breaking URLs |
| **MINOR** | Content additions: new chapters, new exercises/code sections |
| **PATCH** | Fixes: typos, corrections, formatting |

---

## 2. Git Workflow (Agent Protocol)

```
For every implementation plan:

1. CREATE BRANCH: git checkout -b feat/<section>/<description>
2. IMPLEMENT: Make changes per plan
3. VERIFY: mkdocs serve, review changes
4. COMMIT: git commit -m "feat: <description>"
5. NOTIFY: User review
6. WAIT: For explicit command to merge/tag
7. MERGE (if commanded): git checkout main && git merge <branch>
8. TAG (if commanded): git tag v<X.Y.Z>
9. NOTIFY: User to push (agent cannot push)
```

**Agent Workflow Rule:** After notifying user of completion, agent waits for explicit instruction before merging or tagging. Examples of valid commands:
- "merge to main"
- "create tag v0.2.0"
- "merge and tag v0.2.0"
- "proceed with release"

### ⚠️ CRITICAL RULES

| Action | Agent | Repository Owner |
|--------|-------|------------------|
| Create branch | ✅ YES | Can also do |
| Commit to branch | ✅ YES | Can also do |
| Merge to main | ⚠️ ONLY with explicit command | Can do anytime |
| Push to origin | ❌ NO | ✅ ONLY OWNER |
| Create tags | ⚠️ ONLY with explicit command | Can do anytime |

**Agents must NEVER:**
- Run `git push origin main` (owner only)
- Run `git push origin --tags` (owner only)
- Force push

**Agents CAN (after explicit user command):**
- Merge feature branch to main
- Create git tags locally

**Explicit command required:** Agent will only merge or tag after user explicitly says something like "merge to main" or "create tag v0.2.0".

### Branch Naming

```
feat/<primary-section>/<specific-description>

Examples:
- feat/exercises/chapter-01
- feat/code/random-walk
- fix/typos-chapter-03
```

---

## 3. Version Bump Rules

| Change Type | Bump |
|-------------|------|
| New navigation layer | MINOR |
| Full chapter exercises/code | MINOR |
| Single file additions | PATCH |
| Typos, fixes | PATCH |
| URL restructuring | MAJOR |

---

## 4. Agents Subfolder Changes

The `agents/` folder contains documentation for AI agents working on this repository:

### 4.1 Files

| File | Purpose | When to Update |
|------|---------|----------------|
| `CONTEXT.md` | Repository structure, conventions | When structure changes, new conventions added |
| `lessons.md` | Complete lesson index | When new lessons added, paths changed |
| `versioning.md` | This file | When versioning rules change |

### 4.2 Handling Agents Changes

**Version Impact:** Changes to `agents/` typically do **NOT** trigger version bumps unless they document structural changes affecting the site.

| Change | Version Impact | Branch Example |
|--------|----------------|----------------|
| Update CONTEXT.md with new conventions | PATCH | `fix/agents/context-update` |
| Add lesson to lessons.md | PATCH | `fix/agents/lesson-index` |
| New agents documentation file | PATCH | `feat/agents/<new-doc>` |
| Document structural change (affects site) | MINOR | `feat/agents/structure-docs` |

### 4.3 Rules for Agents Changes

1. **No user verification needed** for agents-only changes (they don't affect published site)
2. **Still require branch** - never commit directly to main
3. **Commit message**: `docs(agents): <description>`
4. **Can be bundled** with related feature work in same branch

---

## 5. Release Procedure

### Option A: Agent Handles Merge/Tag (after explicit command)

When user explicitly commands agent to proceed:

```bash
# Agent (after explicit "merge to main" command)
git checkout main
git merge feat/<branch-name>

# Agent bumps version in docs/index.md frontmatter
# Agent updates CHANGELOG.md
git add .
git commit -m "chore: bump version to v<X.Y.Z>"

# Agent (after explicit "create tag" command)
git tag v<X.Y.Z>

# Agent notifies: "Ready for you to push"

# Owner (always)
git push origin main
git push origin v<X.Y.Z>
```

### Option B: Owner Handles Everything

If owner prefers:

```bash
# Owner handles merge, version bump, tag creation
# Agent stops after notifying of completion
```

**Push is ALWAYS owner-only** - agent never runs git push commands.

---

## 6. Changelog Format

Create `CHANGELOG.md` in root:

```markdown
# Changelog

## [Unreleased]

## [0.2.0] - 2026-03-17
### Added
- Exercises navigation layer
- Code navigation layer

## [0.1.0] - 2026-03-17
### Added
- Initial lecture notes structure
```

---

## 7. Implementation Plan Checklist

Every plan must include:

```markdown
## Release Impact
| Component | Bump | From → To | Reason |
|-----------|------|-----------|--------|
| docs | MINOR | 0.1.0 → 0.2.0 | Add exercises layer |

## Branch
- Name: `feat/exercises/chapter-01`

## Agent Steps (Phase 1)
- [ ] Create branch
- [ ] Implement changes
- [ ] Test with mkdocs serve
- [ ] Commit all changes
- [ ] Notify user for review

## Agent Steps (Phase 2 - after explicit command)
- [ ] Merge to main (only if user explicitly commands)
- [ ] Update version in docs/index.md
- [ ] Update CHANGELOG.md
- [ ] Commit version bump
- [ ] Create tag vX.Y.Z (only if user explicitly commands)
- [ ] Notify user ready for push

## Owner Steps (Phase 3 - always required)
- [ ] Review changes
- [ ] Verify mkdocs serve
- [ ] Push to origin: `git push origin main`
- [ ] Push tag: `git push origin vX.Y.Z`
```

**Agent waits for explicit commands like:**
- "merge to main"
- "create tag v0.2.0" 
- "proceed with merge and tag"

---

## 8. Quick Reference

| Task | Command | Who |
|------|---------|-----|
| Create branch | `git checkout -b feat/<name>` | Agent |
| Test locally | `mkdocs serve` | Agent/Owner |
| Commit | `git commit -m "feat: ..."` | Agent |
| Merge to main | `git merge <branch>` | Agent (after explicit command) or Owner |
| Create tag | `git tag vX.Y.Z` | Agent (after explicit command) or Owner |
| Push | `git push origin main` | **OWNER ONLY** |
| Push tags | `git push origin vX.Y.Z` | **OWNER ONLY** |

---

## Current Status

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2026-03-17 | Initial structure |
| v0.2.0 | TBD | Exercises + Code layers |
