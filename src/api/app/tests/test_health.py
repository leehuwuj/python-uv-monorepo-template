from fastapi.testclient import TestClient


# Just a dummy test to check if the core is imported correctly
def test_health_endpoint(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["message"] == "Hello, World!"
