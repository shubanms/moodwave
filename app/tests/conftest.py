import pytest

from main import app

from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client
