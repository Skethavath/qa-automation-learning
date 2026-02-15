# CLAUDE.md — Project Instructions for Claude Code

## About the Developer

I'm a manual QA engineer transitioning into test automation. I understand testing
concepts deeply (test plans, edge cases, regression, exploratory testing) but I'm
building my programming skills. When explaining code concepts, connect them to QA
knowledge I already have.

## Teaching Mode

- **Explain "why" before "how"** — Don't just show code; explain the reasoning behind
  the approach. Why this pattern? Why not an alternative?
- **Use QA analogies** — Relate programming concepts to testing concepts I know.
  For example: "A fixture is like test setup/teardown in a test plan."
- **Reference official docs** — Link to Python docs, pytest docs, or Playwright docs
  when introducing new concepts so I can learn more on my own.
- **Call out common mistakes** — When showing a pattern, mention what beginners
  typically get wrong and how to avoid it.
- **Incremental complexity** — Start simple, then layer on complexity. Don't jump to
  advanced patterns without building up from basics.

## Tech Stack

- **Language:** Python 3.14
- **Test framework:** pytest
- **Browser automation:** Playwright for Python
- **Formatter:** black (line length 100)
- **Linter:** ruff
- **Type checker:** mypy (strict mode)
- **Pre-commit hooks:** pre-commit (runs black, ruff, mypy on every commit)

## Coding Standards

- Follow **PEP 8** style guidelines
- **Type hints on all functions** — parameters and return types
- **Google-style docstrings** on all public functions and classes
- **Line length:** 100 characters (configured in black and ruff)
- Use **f-strings** for string formatting (not .format() or %)
- Use **pathlib.Path** instead of os.path for file operations
- Use **snake_case** for functions/variables, **PascalCase** for classes
- Imports: stdlib first, then third-party, then local (isort order)

## Testing Conventions

- **AAA pattern:** Arrange-Act-Assert — every test should have clear sections
- **Page Object Model (POM):** All Playwright tests use page objects in `src/pages/`
- **pytest markers:**
  - `@pytest.mark.smoke` — Critical path tests, run on every commit
  - `@pytest.mark.regression` — Full regression suite
  - `@pytest.mark.slow` — Tests that take >5 seconds
- **Fixtures** go in `tests/conftest.py` with clear docstrings
- **Test naming:** `test_<what>_<expected_behavior>` (e.g., `test_login_with_valid_credentials_succeeds`)
- **One assertion per test** when possible; group related assertions with descriptive messages

## Project Structure

```
C:\Users\giriv\claude\
├── CLAUDE.md              # This file — project instructions
├── pyproject.toml         # Unified tool configuration
├── requirements.txt       # Pinned dependencies
├── .pre-commit-config.yaml
├── src/                   # Source code (page objects, utilities)
│   ├── __init__.py
│   └── pages/             # Page Object Model classes
├── tests/                 # All test files
│   ├── __init__.py
│   ├── conftest.py        # Shared fixtures
│   └── ...
├── docs/                  # Learning notes and documentation
│   └── LEARNING_LOG.md
└── scripts/               # Utility scripts
```

## Git Workflow

- **Feature branches:** Always work on a branch, never commit directly to main
- **Branch naming:** `feature/<description>`, `fix/<description>`, `learn/<description>`
- **Commit messages:** Imperative mood, concise ("Add login page object", not "Added login page object")
- **Small commits:** One logical change per commit

## Quick Command Reference

```bash
# Run all tests
python -m pytest tests/ -v

# Run only smoke tests
python -m pytest tests/ -m smoke -v

# Run with coverage report
python -m pytest tests/ --cov=src --cov-report=html

# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Lint and auto-fix
ruff check --fix src/ tests/

# Type check
mypy src/ tests/

# Run all pre-commit hooks
pre-commit run --all-files
```
