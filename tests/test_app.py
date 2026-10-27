from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_readiness_endpoint():
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}

def test_root_describes_service():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "secure-gitops-platform"

def test_metrics_endpoint_exposes_prometheus_format():
    client.get("/health")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "secure_gitops_http_requests_total" in response.text
