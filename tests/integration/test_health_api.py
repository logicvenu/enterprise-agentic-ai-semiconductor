from fastapi.testclient import TestClient

from semiconductor_ai_platform.api.main import create_app
from semiconductor_ai_platform.config.settings import get_settings


def test_liveness_endpoint():
    client = TestClient(create_app())
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}


def test_readiness_endpoint():
    client = TestClient(create_app())
    response = client.get("/health/ready")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"
    assert response.json()["environment"] == get_settings().environment


def test_request_id_is_returned():
    client = TestClient(create_app())
    response = client.get("/health/live", headers={"X-Request-ID": "build01a-test"})
    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == "build01a-test"
