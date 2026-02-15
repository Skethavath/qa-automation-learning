# Playwright with Python — Learning Plan

A structured path from manual tester to automation engineer.
Each phase builds on the previous one. Don't skip ahead — the fundamentals matter.

---

## How to Use This Plan

- Work through one phase at a time
- Build a small project/test for each topic before moving on
- Add entries to `docs/LEARNING_LOG.md` as you learn
- Ask Claude Code to explain concepts — CLAUDE.md is configured for teaching mode
- All practice code goes in this repo: `src/` for page objects, `tests/` for test files

**Estimated timeline:** 8–12 weeks (1–2 hours/day)

---

## Phase 1: Python Foundations for Testers (Week 1–2)

> You don't need to master all of Python — just the parts automation uses daily.

### Topics
- [ ] **Variables, data types, f-strings** — storing test data, building dynamic values
- [ ] **Lists and dictionaries** — test data collections, config objects
- [ ] **Functions and return values** — reusable actions (like clicking a button)
- [ ] **Type hints** — `def login(username: str, password: str) -> bool:`
- [ ] **Conditionals and loops** — `if`, `for` (iterating test data, conditional waits)
- [ ] **Classes and objects** — the foundation for Page Object Model
- [ ] **Imports and modules** — organizing code across files
- [ ] **Exception handling** — `try/except` for graceful failure handling
- [ ] **File I/O with pathlib** — reading test data from files

### QA Connection
| Python Concept | QA Equivalent |
|---------------|---------------|
| Function | Reusable test step |
| Class | Test page or component |
| Dictionary | Test data row |
| List | Set of test cases |
| Exception | Defect encountered during execution |

### Practice
- Write a function that validates an email format
- Create a class representing a user with name, email, and role
- Read test data from a JSON file and loop through it

### Resources
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python — Python Basics](https://realpython.com/tutorials/basics/)

---

## Phase 2: pytest Fundamentals (Week 2–3)

> pytest is your test runner — it discovers tests, runs them, and reports results.
> Think of it as the automation equivalent of your test management tool.

### Topics
- [ ] **Test discovery** — how pytest finds tests (file naming, function naming)
- [ ] **Writing your first test** — `assert` statement, AAA pattern
- [ ] **Fixtures** — setup/teardown, `conftest.py`, fixture scopes
- [ ] **Parametrize** — run the same test with multiple data sets
- [ ] **Markers** — `@pytest.mark.smoke`, `@pytest.mark.regression`, skip, xfail
- [ ] **Command-line options** — `-v`, `-k`, `-m`, `--tb`, `-x` (stop on first failure)
- [ ] **Reporting** — `pytest-html` for HTML reports, `pytest-cov` for coverage

### QA Connection
| pytest Concept | QA Equivalent |
|---------------|---------------|
| Test function | Test case |
| Fixture | Test setup / preconditions |
| Marker | Test category (smoke, regression) |
| Parametrize | Data-driven testing |
| conftest.py | Shared test environment config |
| `pytest-html` report | Test execution report |

### Practice
- Write 5 tests for a calculator function (add, subtract, edge cases)
- Use `@pytest.mark.parametrize` to test login with valid/invalid data
- Create a fixture that provides test data and use it across tests
- Generate an HTML report with `pytest --html=report.html`

### Resources
- [pytest Official Docs](https://docs.pytest.org/en/stable/)
- [pytest Fixtures Guide](https://docs.pytest.org/en/stable/how-to/fixtures.html)

---

## Phase 3: Playwright Basics (Week 3–5)

> This is where the browser automation begins. Playwright controls Chrome, Firefox,
> and Safari with the same code.

### Topics
- [ ] **Installation and setup** — `pip install playwright && playwright install`
- [ ] **Browser, context, and page** — the three layers of Playwright
- [ ] **Your first script** — open a page, interact, close
- [ ] **Sync vs async API** — start with sync (simpler), learn async later
- [ ] **Navigation** — `page.goto()`, waiting for load states
- [ ] **Screenshots and videos** — capturing evidence (like manual test screenshots)
- [ ] **Browser contexts** — isolated sessions (like incognito mode)
- [ ] **Playwright Inspector** — `PWDEBUG=1` to step through tests visually
- [ ] **Codegen** — `playwright codegen` to record actions and generate code

### Key Concepts
```python
from playwright.sync_api import sync_playwright

# Browser = the actual browser application (Chrome, Firefox, etc.)
# Context = an isolated browser session (like an incognito window)
# Page = a single tab within a context

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # See the browser
    context = browser.new_context()               # Fresh session
    page = context.new_page()                     # New tab
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

### QA Connection
| Playwright Concept | QA Equivalent |
|-------------------|---------------|
| Browser | The application under test |
| Context | A clean test environment |
| Page | The screen you're testing |
| `headless=False` | Watching the test run manually |
| Codegen | Recording your manual test steps |
| Screenshot | Test evidence / attachment |

### Practice
- Use `playwright codegen` to record a login flow, then clean up the generated code
- Write a script that opens 3 different websites and takes a screenshot of each
- Open two browser contexts and verify they don't share cookies

### Resources
- [Playwright Python Docs](https://playwright.dev/python/docs/intro)
- [Playwright Codegen](https://playwright.dev/python/docs/codegen)

---

## Phase 4: Locators — Finding Elements (Week 5–6)

> Locators are how you tell Playwright "click THIS button" or "type in THIS field."
> This is the most important skill — bad locators = flaky tests.

### Topics (in priority order)
- [ ] **`get_by_role()`** — best option, uses accessibility roles (button, link, textbox)
- [ ] **`get_by_text()`** — find by visible text
- [ ] **`get_by_label()`** — find form fields by their label
- [ ] **`get_by_placeholder()`** — find inputs by placeholder text
- [ ] **`get_by_test_id()`** — find by `data-testid` attribute (most reliable)
- [ ] **`locator()` with CSS** — fallback using CSS selectors
- [ ] **`locator()` with XPath** — last resort, avoid when possible
- [ ] **Chaining locators** — `page.locator(".card").get_by_role("button")`
- [ ] **Filtering** — `locator.filter(has_text="Submit")`
- [ ] **Locator strictness** — Playwright fails if a locator matches multiple elements

### Locator Priority (Best → Worst)
```
1. get_by_role()        ← Most resilient, based on accessibility
2. get_by_label()       ← Great for forms
3. get_by_text()        ← Good for buttons and links
4. get_by_test_id()     ← Reliable if devs add data-testid
5. get_by_placeholder() ← Decent for search boxes, inputs
6. locator() with CSS   ← Flexible but brittle if DOM changes
7. locator() with XPath ← Avoid unless no alternative
```

### QA Connection
Think of locators like the "steps" in a manual test case:
- Manual: "Click the **Login** button"
- Playwright: `page.get_by_role("button", name="Login").click()`

The more specific and user-facing your locator, the less it breaks when developers change the code.

### Practice
- Visit a real website and find 5 elements using `get_by_role()`
- Find the same elements using CSS selectors — notice which is more readable
- Use Playwright Inspector (`PWDEBUG=1`) to explore locators interactively
- Practice chaining: find a button inside a specific card/section

### Resources
- [Playwright Locators Guide](https://playwright.dev/python/docs/locators)
- [Playwright Inspector](https://playwright.dev/python/docs/debug#playwright-inspector)

---

## Phase 5: Actions and Assertions (Week 6–7)

> Actions = what you DO (click, type, select). Assertions = what you CHECK.

### Actions to Learn
- [ ] **Click** — `click()`, `dblclick()`, `click(button="right")`
- [ ] **Type** — `fill()` (clear + type), `press_sequentially()` (key by key)
- [ ] **Keyboard** — `press("Enter")`, `press("Control+a")`
- [ ] **Select dropdown** — `select_option()`
- [ ] **Checkbox/Radio** — `check()`, `uncheck()`, `set_checked()`
- [ ] **Hover** — `hover()`
- [ ] **Drag and drop** — `drag_to()`
- [ ] **File upload** — `set_input_files()`
- [ ] **Dialogs** — handling alert/confirm/prompt popups

### Assertions to Learn
- [ ] **`expect(page).to_have_title()`** — page title check
- [ ] **`expect(page).to_have_url()`** — URL check (supports regex)
- [ ] **`expect(locator).to_be_visible()`** — element is shown
- [ ] **`expect(locator).to_have_text()`** — text content check
- [ ] **`expect(locator).to_be_enabled()`** — element is interactive
- [ ] **`expect(locator).to_have_value()`** — input field value
- [ ] **`expect(locator).to_have_count()`** — number of matching elements
- [ ] **`expect(locator).to_be_checked()`** — checkbox state

### QA Connection
| Action/Assertion | Manual Test Step |
|-----------------|------------------|
| `fill("username")` | "Enter username in the field" |
| `click()` | "Click the Submit button" |
| `expect().to_be_visible()` | "Verify the success message appears" |
| `expect().to_have_text()` | "Verify the message says 'Welcome'" |

### Practice
- Automate a complete login form (fill fields, click submit, verify result)
- Test a dropdown menu — select each option and verify the page updates
- Handle a JavaScript alert dialog in a test
- Write tests with multiple assertions using descriptive messages

### Resources
- [Playwright Actions](https://playwright.dev/python/docs/input)
- [Playwright Assertions](https://playwright.dev/python/docs/test-assertions)

---

## Phase 6: Waiting and Auto-Wait (Week 7)

> Flaky tests are the #1 problem in automation. Playwright's auto-wait
> mechanism solves most of this, but you need to understand how.

### Topics
- [ ] **Auto-wait** — Playwright automatically waits for elements before acting
- [ ] **Why `time.sleep()` is bad** — slows tests, still flaky, never use it
- [ ] **`expect()` with timeout** — assertions retry until timeout
- [ ] **`wait_for_selector()`** — wait for an element to appear/disappear
- [ ] **`wait_for_load_state()`** — wait for page load (`load`, `domcontentloaded`, `networkidle`)
- [ ] **`wait_for_url()`** — wait for navigation to complete
- [ ] **`wait_for_response()`** — wait for a specific API call to finish
- [ ] **Custom timeout** — override default 30s timeout per action or globally

### The Golden Rule
```
NEVER use time.sleep() in Playwright tests.
Playwright's auto-wait and expect() handle timing automatically.
If you think you need sleep, you need a better locator or wait strategy.
```

### QA Connection
In manual testing, you naturally wait for things to load before checking them.
Playwright does this automatically — `expect(locator).to_be_visible()` will
keep retrying for up to 30 seconds. It's like a patient manual tester who
keeps looking at the screen until the element appears.

### Practice
- Test a page with dynamic content that loads after an API call
- Use `wait_for_response()` to wait for data to load before asserting
- Verify that Playwright auto-waits by testing a slow-loading element

### Resources
- [Playwright Auto-Waiting](https://playwright.dev/python/docs/actionability)

---

## Phase 7: Page Object Model (Week 8–9)

> POM is the most important design pattern in test automation.
> It separates "what the page looks like" from "what the test checks."

### Topics
- [ ] **Why POM** — maintainability, reusability, single source of truth
- [ ] **Page class structure** — locators as properties, actions as methods
- [ ] **Constructor** — receive the `page` object
- [ ] **Navigation methods** — `goto()`, `is_loaded()`
- [ ] **Action methods** — `login()`, `search()`, `add_to_cart()`
- [ ] **Getter methods** — `get_error_message()`, `get_username()`
- [ ] **Composing pages** — shared components (header, footer, sidebar)
- [ ] **Using POM in tests** — tests read like plain English

### Structure
```python
# src/pages/login_page.py
from playwright.sync_api import Page, expect


class LoginPage:
    """Page object for the login page.

    QA analogy: This class is like a "page map" in your test plan.
    It describes what's on the page and what actions you can take.
    """

    URL = "https://example.com/login"

    def __init__(self, page: Page) -> None:
        self.page = page
        # Locators — define ONCE, use everywhere
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Log in")
        self.error_message = page.get_by_role("alert")

    def goto(self) -> None:
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        return self.error_message.text_content() or ""
```

```python
# tests/test_login.py — clean, readable tests
def test_login_with_invalid_password(login_page):
    login_page.goto()
    login_page.login("validuser", "wrongpassword")
    assert "Invalid credentials" in login_page.get_error_text()
```

### QA Connection
| POM Concept | QA Equivalent |
|------------|---------------|
| Page class | Page map / screen description |
| Locators | Element identification in test case |
| Action methods | Test steps |
| Test file | Test case that references the page map |

When the UI changes, you update ONE page class — not 50 tests.

### Practice
- Create a `LoginPage` class for a practice site
- Create a `HomePage` class for the page after login
- Write 5 tests using these page objects
- Refactor: change a locator in the page object and verify no tests break

### Resources
- [Playwright POM Guide](https://playwright.dev/python/docs/pom)
- [Martin Fowler — Page Object](https://martinfowler.com/bliki/PageObject.html)

---

## Phase 8: Test Data and Configuration (Week 9–10)

> Hard-coded test data in tests is like hard-coded URLs in production — fragile.

### Topics
- [ ] **Environment variables** — `.env` files with `python-dotenv`
- [ ] **pytest parametrize** — data-driven tests from lists/tuples
- [ ] **JSON/CSV test data** — external data files
- [ ] **Fixtures for test data** — factory fixtures that generate data
- [ ] **Configuration per environment** — dev, staging, production URLs
- [ ] **Secrets management** — never commit passwords (use `.env`, gitignored)

### Practice
- Move all hard-coded URLs to a `.env` file
- Create a parametrized test that runs login with 5 different user/password combos
- Read test data from a JSON file and use it in a test
- Create a `config.py` that loads settings from environment variables

---

## Phase 9: Advanced Playwright (Week 10–11)

> Once you're comfortable with basics, these features make your tests more powerful.

### Topics
- [ ] **API testing** — `request.get()`, `request.post()` without a browser
- [ ] **Network interception** — `page.route()` to mock API responses
- [ ] **Multiple pages/tabs** — handling popups and new windows
- [ ] **iFrames** — `frame_locator()` for embedded content
- [ ] **Visual comparison** — `expect(page).to_have_screenshot()`
- [ ] **Tracing** — `context.tracing.start()` for debugging failures
- [ ] **Video recording** — record test execution for evidence
- [ ] **Authentication state** — save/reuse login state across tests
- [ ] **Parallel execution** — `pytest-xdist` for running tests concurrently

### Practice
- Write an API test that creates a user, then a UI test that logs in as that user
- Mock a slow API response and verify the UI shows a loading spinner
- Set up authentication state reuse to skip login in every test
- Record a trace and open it in the Playwright Trace Viewer

### Resources
- [Playwright API Testing](https://playwright.dev/python/docs/api-testing)
- [Playwright Network](https://playwright.dev/python/docs/network)
- [Playwright Trace Viewer](https://playwright.dev/python/docs/trace-viewer)

---

## Phase 10: CI/CD and Reporting (Week 11–12)

> Automated tests only matter if they run automatically.

### Topics
- [ ] **GitHub Actions** — run tests on every push/PR
- [ ] **Workflow file** — `.github/workflows/tests.yml`
- [ ] **Playwright in CI** — headless mode, installing browsers
- [ ] **Test reports** — `pytest-html` report as a GitHub artifact
- [ ] **Failure screenshots** — auto-capture on test failure
- [ ] **Branch protection** — require tests to pass before merging
- [ ] **Scheduled runs** — run regression suite nightly

### Practice
- Create a GitHub Actions workflow that runs smoke tests on every push
- Add screenshot-on-failure to your conftest.py
- Upload HTML report as a workflow artifact
- Set up a nightly regression run on a schedule

### Resources
- [Playwright CI Guide](https://playwright.dev/python/docs/ci)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

---

## Practice Websites

Free sites designed for automation practice:

| Site | Best For |
|------|----------|
| [The Internet (Heroku)](https://the-internet.herokuapp.com/) | Common UI patterns (login, dropdowns, alerts, iframes) |
| [Sauce Demo](https://www.saucedemo.com/) | E-commerce flow (login, cart, checkout) |
| [UI Testing Playground](http://uitestingplayground.com/) | Tricky UI scenarios (dynamic IDs, AJAX) |
| [Automation Exercise](https://automationexercise.com/) | Full e-commerce with API |
| [DemoQA](https://demoqa.com/) | Forms, widgets, interactions |

---

## Milestones Checklist

Track your overall progress:

- [ ] **Milestone 1:** Can write and run a pytest test independently
- [ ] **Milestone 2:** Can open a browser with Playwright and navigate to a site
- [ ] **Milestone 3:** Can find elements using 3+ locator strategies
- [ ] **Milestone 4:** Can automate a complete user flow (login → action → verify)
- [ ] **Milestone 5:** Can build a Page Object Model with 2+ pages
- [ ] **Milestone 6:** Can run data-driven tests with parametrize
- [ ] **Milestone 7:** Can set up tests in CI/CD (GitHub Actions)
- [ ] **Milestone 8:** Can debug a flaky test and fix it
- [ ] **Milestone 9:** Can write API tests alongside UI tests
- [ ] **Milestone 10:** Can present your automation framework to a team
