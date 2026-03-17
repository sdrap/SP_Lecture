# CONTEXT - Stochastics Lecture Notes

## Course Information

- **Title**: Stochastics
- **Level**: Graduate (Master/PhD)
- **Institution**: Shanghai Jiao Tong University
- **Topic**: Probability theory, stochastic processes, martingales, Itô calculus, SDEs

## Repository Overview

This is a MkDocs-based lecture notes repository for a graduate-level stochastics course. The notes cover:

1. **Probability Foundations**: Probability spaces, expectation, conditional expectation, independence
2. **Discrete Martingales**: Convergence theorems, Doob's decomposition
3. **Markov Processes**: Discrete-time chains, Brownian motion construction
4. **Itô Calculus**: Stochastic integral, Itô's formula, stochastic exponential, Girsanov transform
5. **Stochastic Differential Equations**: Existence, uniqueness, weak/strong solutions

## Repository Structure

```
SP_lecture/
├── agents/              # Agent documentation (this folder)
├── Code/                # Python code examples (kept in git)
│   └── lib/            # Python library files
├── docs/               # MkDocs source
│   ├── index.md        # Home page
│   ├── lecture/        # All lesson content
│   │   ├── 00-Introduction/
│   │   ├── 01-Sets-Functions/
│   │   ├── 02-Measure/
│   │   ├── 03-Integration/
│   │   ├── 04-Martingales/
│   │   ├── 05-Markov/
│   │   ├── 06-Continuous-Time/
│   │   ├── 07-Stochastic-Integral/
│   │   └── 08-Stochastic-Exponential/
│   ├── data/           # Data files
│   ├── images/         # Image assets
│   └── stylesheets/    # Custom CSS
├── overrides/          # MkDocs theme overrides
├── bibliography.bib    # BibTeX references
├── mkdocs.yml          # MkDocs configuration
└── README.md
```

## MkDocs Configuration

- **Theme**: Material for MkDocs
- **Navigation**: Tabs + index pages for chapters
- **Math**: MathJax (LaTeX rendering via `pymdownx.arithmatex`)
- **Bibliography**: BibTeX plugin
- **Diagrams**: Mermaid support via `pymdownx.superfences`
- **Code**: Syntax highlighting with copy button

### Build Commands

```bash
# Serve locally (live reload)
mkdocs serve

# Build static site
mkdocs build

# Deploy to remote
mkdocs gh-deploy
```

## Naming Conventions

### Folder Structure
- Format: `XX-Topic-Name/` (e.g., `01-Sets-Functions/`)
- Chapters numbered 00-08
- Each folder contains lesson files for that chapter

### File Naming
- Format: `XXX-topic-name.md` (e.g., `011-sets.md`)
- Three-digit prefix indicates:
  - First digit: Chapter number
  - Last two digits: Lesson order within chapter
- Introduction files use `0X0-introduction.md` pattern

### File Content
- Each lesson file should start with frontmatter (if needed)
- Use LaTeX for math: `$...$` for inline, `$$...$$` for display
- References: Use BibTeX keys from `bibliography.bib` with `[@key]` syntax

## Content Organization

### Chapters (9 total)

| Chapter | Topic | Lessons |
|---------|-------|---------|
| 00 | Introduction | 1 (notations) |
| 01 | Sets, Continuity, Measurability | 4 |
| 02 | Measure Theory, Construction | 5 |
| 03 | Expectation, Integration | 7 |
| 04 | Discrete Martingales | 5 |
| 05 | Markov Processes | 4 |
| 06 | Continuous Time Processes | 4 |
| 07 | Stochastic Integral, Itô | 5 |
| 08 | Stochastic Exponential, Girsanov | 3 |

**Total: 38 lessons**

## For Agents Working on This Repository

When asked to modify or add content:

1. **Understand the lesson structure**: Check `agents/lessons.md` for the complete lesson index
2. **Follow naming conventions**: Use the `XXX-topic-name.md` format
3. **Place in correct chapter folder**: Ensure the file goes in the right `XX-Topic/` directory
4. **Update mkdocs.yml**: If adding new lessons, update the navigation structure in `mkdocs.yml`
5. **Math formatting**: Use LaTeX; test with `mkdocs serve`
6. **Citations**: Use BibTeX keys from `bibliography.bib`

## Dependencies

- Python 3.x
- mkdocs
- mkdocs-material
- mkdocs-bibtex-plugin
- pymdownx extensions (part of Material theme)

Install with:
```bash
pip install mkdocs mkdocs-material mkdocs-bibtex-plugin
```
