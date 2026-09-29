from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_simulation():
    response = client.post("/api/simulations", json={
        "current_budget": 1000,
        "new_budget": 1500,
        "platform": "Meta Ads"
    })
    assert response.status_code == 200
