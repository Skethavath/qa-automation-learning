"""Shared test fixtures for the entire test suite.

Think of this file like a "test setup library." Any fixture defined here is
automatically available to ALL test files in the tests/ directory — you don't
need to import anything.

Key concept: A fixture is pytest's way of handling test setup and teardown.
If you've written test plans with "preconditions," fixtures are the code
equivalent. They run BEFORE your test and can also clean up AFTER.

Learn more: https://docs.pytest.org/en/stable/how-to/fixtures.html
"""

import pytest


@pytest.fixture
def sample_data() -> dict[str, str]:
    """Provide sample test data that multiple tests can reuse.

    This is a simple example fixture. In real projects, fixtures often:
    - Set up database connections
    - Create test users
    - Launch browser sessions (Playwright)
    - Prepare test files

    Returns:
        A dictionary with sample user data for testing.

    Example usage in a test:
        def test_something(sample_data):
            # sample_data is automatically injected by pytest
            assert sample_data["username"] == "testuser"
    """
    # ARRANGE: This is the "Arrange" part of Arrange-Act-Assert.
    # Fixtures handle the Arrange step so your tests stay focused on Act & Assert.
    return {
        "username": "testuser",
        "email": "testuser@example.com",
        "role": "qa_engineer",
    }
