# Claude Code Environment Setup Guide

How this project was initialized from scratch on Windows 11 with Python 3.14.
Follow these steps to reproduce the setup on a new machine.

---

## Prerequisites

Before starting, you need:
- **Python 3.14+** installed and on PATH
- **Git** installed and on PATH
- **winget** (Windows Package Manager, built into Windows 11)

## Phase 1: Install System Tools

Run all three in parallel from any terminal:

```bash
# Node.js — needed for MCP plugins in Claude Code
winget install OpenJS.NodeJS.LTS

# GitHub CLI — manage repos, PRs, and issues from the terminal
winget install GitHub.cli

# Python quality & testing tools
pip install black ruff mypy pre-commit pytest-html pytest-cov python-dotenv
```

After installing GitHub CLI, authenticate:

```bash
gh auth login
# Select: GitHub.com → HTTPS → Authenticate with browser
```

**Why these tools?**
| Tool | Purpose |
|------|---------|
| `black` | Auto-formats Python code (no debates about style) |
| `ruff` | Fast Python linter (catches bugs and bad patterns) |
| `mypy` | Static type checker (catches type errors before runtime) |
| `pre-commit` | Runs black/ruff/mypy automatically before every git commit |
| `pytest-html` | Generates HTML test reports |
| `pytest-cov` | Measures code coverage |
| `python-dotenv` | Loads environment variables from `.env` files |

## Phase 2: Project Structure

Create the following directory layout:

```
C:\Users\giriv\claude\
├── CLAUDE.md                  # Instructions for Claude Code (teaching mode, standards)
├── pyproject.toml             # Unified config for all Python tools
├── requirements.txt           # Pinned dependency versions
├── .gitignore                 # Files Git should ignore
├── .pre-commit-config.yaml    # Pre-commit hook definitions
├── src/                       # Source code
│   └── __init__.py
├── tests/                     # Test files
│   ├── __init__.py
│   ├── conftest.py            # Shared pytest fixtures
│   └── test_setup_verification.py
├── docs/                      # Documentation and learning notes
│   ├── LEARNING_LOG.md
│   └── SETUP_GUIDE.md         # This file
└── scripts/                   # Utility scripts
```

### What Each File Does

**`CLAUDE.md`** — The most important file. Claude Code reads this at the start of every session. It contains:
- Your developer profile (QA engineer learning automation)
- Teaching mode preferences (explain "why", use QA analogies)
- Coding standards (PEP 8, type hints, Google docstrings, 100-char lines)
- Testing conventions (AAA pattern, Page Object Model, pytest markers)
- Git workflow rules (feature branches, imperative commit messages)
- Quick command reference for all tools

**`pyproject.toml`** — Single config file for multiple tools:
- pytest settings (test paths, markers, default flags)
- black settings (line length 100, Python 3.14 target)
- ruff settings (which lint rules to enable, isort config)
- mypy settings (strict mode, disallow untyped defs)
- coverage settings (source dirs, fail-under threshold)

**`.pre-commit-config.yaml`** — Defines three hooks that run on every `git commit`:
1. `black` — reformats code if needed
2. `ruff` — checks for lint errors (auto-fixes where possible)
3. `mypy` — checks types

If any hook fails, the commit is blocked until you fix the issue. This prevents bad code from ever entering the repo.

**`tests/conftest.py`** — Shared fixtures available to all test files automatically. Fixtures are pytest's way of handling test setup (like "preconditions" in a test plan).

**`.gitignore`** — Tells Git to ignore generated files: `__pycache__`, `.pytest_cache`, `.mypy_cache`, `.env`, IDE folders, coverage reports, Playwright reports, and `.claude/`.

## Phase 3: Initialize Git & Pre-commit

```bash
cd C:\Users\giriv\claude

# Initialize the repository
git init

# Configure your identity
git config user.name "Skethavath"
git config user.email "vsudha9166@gmail.com"

# Install pre-commit hooks (activates .pre-commit-config.yaml)
pre-commit install

# Pin hooks to latest versions
pre-commit autoupdate
```

## Phase 4: Claude Code Configuration

Three files outside the project configure Claude Code itself:

### `~/.claude/settings.json` — Plugins
```json
{
  "enabledPlugins": {
    "playwright@claude-plugins-official": true,
    "github@claude-plugins-official": true
  },
  "autoUpdatesChannel": "latest"
}
```

### `~/.claude/settings.local.json` — Tool Permissions
```json
{
  "permissions": {
    "allow": [
      "WebSearch",
      "Bash(git:*)",
      "Bash(pip:*)",
      "Bash(python:*)",
      "Bash(pytest:*)",
      "Bash(black:*)",
      "Bash(ruff:*)",
      "Bash(mypy:*)",
      "Bash(pre-commit:*)",
      "Bash(gh:*)",
      "Bash(node:*)",
      "Bash(npm:*)",
      "Bash(npx:*)"
    ]
  }
}
```

These permissions let Claude Code run these tools without asking for approval each time.

### `~/.claude/projects/<project>/memory/MEMORY.md` — Persistent Memory
Claude Code reads this file at the start of every session. It stores your profile, preferences, and project conventions so Claude remembers them across conversations.

## Phase 5: Create GitHub Repo

```bash
gh repo create qa-automation-learning --public --source=. --remote=origin --push \
  --description "Test automation learning project with Python, pytest, and Playwright"
```

## Verification Checklist

Run these to confirm everything works:

```bash
# Formatting — should say "All done, X files left unchanged"
black --check src/ tests/

# Linting — should say "All checks passed!"
ruff check src/ tests/

# Tests — should show 3 passed
python -m pytest tests/ -v

# Pre-commit — all hooks should show "Passed"
pre-commit run --all-files

# GitHub — should show "Logged in to github.com"
gh auth status

# Node.js — should show version number
node --version
```

## Known Issues

**Playwright + Python 3.14:** The `greenlet` DLL has a compatibility issue with Python 3.14. The Playwright pytest plugin is disabled in `pyproject.toml` (`-p no:playwright` in addopts). Remove this flag once Playwright ships a fix.

## Quick Reference

| Task | Command |
|------|---------|
| Run all tests | `python -m pytest tests/ -v` |
| Run smoke tests only | `python -m pytest tests/ -m smoke -v` |
| Run with coverage | `python -m pytest tests/ --cov=src --cov-report=html` |
| Format code | `black src/ tests/` |
| Lint code | `ruff check src/ tests/` |
| Lint + auto-fix | `ruff check --fix src/ tests/` |
| Type check | `mypy src/ tests/` |
| Run all hooks | `pre-commit run --all-files` |
| Create a branch | `git checkout -b feature/my-feature` |
| Push to GitHub | `git push` |
