from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_recommendations():
    response = client.post("/api/recommendations", json={
        "budget": 10000,
        "objective": "ROAS"
    })
    assert response.status_code == 200
