from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_prediction():
    response = client.post("/api/predictions", json={
        "platform": "Google Ads",
        "campaign_type": "Search",
        "budget": 1000,
        "duration_days": 30
    })
    assert response.status_code == 200
    assert "predicted_clicks" in response.json()
