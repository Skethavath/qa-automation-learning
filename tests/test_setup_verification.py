"""Verify that the project setup is working correctly.

This is your first test file! It tests nothing fancy — just confirms
that pytest, fixtures, and markers all work as expected.

Think of it like a "smoke test" for your dev environment.
"""

import pytest


def test_pytest_runs() -> None:
    """Confirm pytest can discover and run a test."""
    assert True


def test_fixture_injection(sample_data: dict[str, str]) -> None:
    """Confirm fixtures from conftest.py are injected automatically.

    Notice: we didn't import sample_data — pytest finds it in conftest.py
    and passes it in as a parameter. This is called "dependency injection."

    QA analogy: It's like a test environment that's pre-configured for you
    before each test run. You just show up and the data is ready.
    """
    # ARRANGE: sample_data is provided by the fixture (the "arrange" step)
    # ACT: Access the data
    username = sample_data["username"]
    # ASSERT: Verify it matches what the fixture defined
    assert username == "testuser"
    assert sample_data["role"] == "qa_engineer"


@pytest.mark.smoke
def test_smoke_marker_works() -> None:
    """Confirm pytest markers are registered and usable.

    You can run just smoke tests with: pytest -m smoke
    This is useful for quick sanity checks before a full regression run.
    """
    assert 1 + 1 == 2
