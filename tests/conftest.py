import pytest
from flask import Flask

from app import create_app


@pytest.fixture
def app() -> Flask:
    """Sample flask app for API testing."""
    app = create_app()
    app.app_context().push()
    yield app


@pytest.fixture
def sample_app(app):
    """Sample app in test client for automated testing."""
    return app.test_client()
