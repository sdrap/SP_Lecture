# Lessons Index

## Complete list of all 38 lessons organized by chapter

---

## Agent Workflow Notes

### ⚠️ Critical Rules

**Agents can NEVER:**
- Push to origin (`git push origin main`)
- Push tags (`git push origin vX.Y.Z`)
- Force push

**Agents CAN (after explicit user command):**
- Merge feature branch to main
- Create git tags locally

**Explicit command required:** Agent will only merge or tag after user explicitly commands (e.g., "merge to main", "create tag v0.2.0")

**Agents MUST:**
- Create feature branches for all work
- Commit changes to feature branches
- Notify user when ready
- Wait for explicit command before merging/tagging

See `versioning.md` for complete release protocol.

---

## Chapter 00: Introduction

| # | Lesson | File Path |
|---|--------|-----------|
| 00-001 | Notations | `docs/lecture/00-Introduction/000-notations.md` |

---

## Chapter 01: Sets, Continuity and Measurability

| # | Lesson | File Path |
|---|--------|-----------|
| 01-001 | Introduction | `docs/lecture/01-Sets-Functions/010-introduction.md` |
| 01-002 | Sets | `docs/lecture/01-Sets-Functions/011-sets.md` |
| 01-003 | Measurable/Topological Spaces | `docs/lecture/01-Sets-Functions/012-measurability-topology.md` |
| 01-004 | Measurability/Continuity | `docs/lecture/01-Sets-Functions/013-measurable-continuous-functions.md` |

---

## Chapter 02: Measure Theory, Construction

| # | Lesson | File Path |
|---|--------|-----------|
| 02-001 | Introduction | `docs/lecture/02-Measure/020-introduction.md` |
| 02-002 | Measures | `docs/lecture/02-Measure/021-measure.md` |
| 02-003 | From Semi-Ring to Ring | `docs/lecture/02-Measure/022-semi-ring-to-ring.md` |
| 02-004 | From Ring to $\sigma$-Algebra | `docs/lecture/02-Measure/023-ring-to-s-algebra.md` |
| 02-005 | Polish Spaces | `docs/lecture/02-Measure/024-polish.md` |

---

## Chapter 03: Expectation

| # | Lesson | File Path |
|---|--------|-----------|
| 03-001 | Introduction/Notations | `docs/lecture/03-Integration/030-introduction.md` |
| 03-002 | Expectation, Lebesgue's Convergence | `docs/lecture/03-Integration/031-expectation.md` |
| 03-003 | $L^p$-Spaces and Classical Inequalities | `docs/lecture/03-Integration/032-lp-spaces-inequalities.md` |
| 03-004 | Radon-Nykodym and Conditional Expectation | `docs/lecture/03-Integration/033-radon-nikodym-cond-exp.md` |
| 03-005 | Independence | `docs/lecture/03-Integration/034-independence.md` |
| 03-006 | Fubini-Tonelli | `docs/lecture/03-Integration/035-fubini-tonelli.md` |
| 03-007 | Uniform Integrability | `docs/lecture/03-Integration/036-uniform-integrability.md` |

---

## Chapter 04: Discrete Time Stochastic Processes, Martingales

| # | Lesson | File Path |
|---|--------|-----------|
| 04-001 | Introduction | `docs/lecture/04-Martingales/040-introduction.md` |
| 04-002 | Discrete Time Processes | `docs/lecture/04-Martingales/041-discrete-time-processes.md` |
| 04-003 | Martingales | `docs/lecture/04-Martingales/042-martingale-doob.md` |
| 04-004 | Martingales Almost Sure Convergence | `docs/lecture/04-Martingales/043-martingale-as-convergence.md` |
| 04-005 | Martingales $L^p$ Convergence | `docs/lecture/04-Martingales/044-martingale-lp-convergence.md` |

---

## Chapter 05: Markov Processes

| # | Lesson | File Path |
|---|--------|-----------|
| 05-001 | Introduction | `docs/lecture/05-Markov/050-introduction.md` |
| 05-002 | Markov Processes | `docs/lecture/05-Markov/051-markov-extension.md` |
| 05-003 | Markov Chains | `docs/lecture/05-Markov/052-markov-discrete.md` |
| 05-004 | Brownian Motion | `docs/lecture/05-Markov/053-brownian.md` |

---

## Chapter 06: Continuous Time Processes

| # | Lesson | File Path |
|---|--------|-----------|
| 06-001 | Introduction | `docs/lecture/06-Continuous-Time/060-introduction.md` |
| 06-002 | Continuous Time Processes | `docs/lecture/06-Continuous-Time/061-continuous-time-processes.md` |
| 06-003 | Lebesgue-Stieljes Integral | `docs/lecture/06-Continuous-Time/062-lebesgue.md` |
| 06-004 | Martingales | `docs/lecture/06-Continuous-Time/063-martingales.md` |

---

## Chapter 07: Stochastic Integral

| # | Lesson | File Path |
|---|--------|-----------|
| 07-001 | Introduction | `docs/lecture/07-Stochastic-Integral/070-introduction.md` |
| 07-002 | Doob-Meyer Decomposition | `docs/lecture/07-Stochastic-Integral/071-doob-meyer.md` |
| 07-003 | Stochastic Integral | `docs/lecture/07-Stochastic-Integral/072-stochastic-integral.md` |
| 07-004 | Quadratic Variations - Semi-Martingales | `docs/lecture/07-Stochastic-Integral/073-quadratic-variations.md` |
| 07-005 | Itô's Formula | `docs/lecture/07-Stochastic-Integral/074-ito-formula.md` |

---

## Chapter 08: Stochastic Exponential and Girsanov

| # | Lesson | File Path |
|---|--------|-----------|
| 08-001 | Introduction | `docs/lecture/08-Stochastic-Exponential/080-introduction.md` |
| 08-002 | Stochastic Exponential | `docs/lecture/08-Stochastic-Exponential/081-stochastic-exponential.md` |
| 08-003 | Girsanov Transformation | `docs/lecture/08-Stochastic-Exponential/082-girsanov.md` |

---

## Summary

| Chapter | Topic | Lessons |
|---------|-------|---------|
| 00 | Introduction | 1 |
| 01 | Sets, Continuity, Measurability | 4 |
| 02 | Measure Theory, Construction | 5 |
| 03 | Expectation | 7 |
| 04 | Discrete Martingales | 5 |
| 05 | Markov Processes | 4 |
| 06 | Continuous Time Processes | 4 |
| 07 | Stochastic Integral | 5 |
| 08 | Stochastic Exponential, Girsanov | 3 |
| **Total** | | **38** |
