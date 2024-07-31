import pytest

from main import app

from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_item():
    response = client.post("/hello-world/", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"text": "hello"}
