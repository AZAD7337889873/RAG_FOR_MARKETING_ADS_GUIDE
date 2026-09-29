from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_campaign_endpoint():
    response = client.get("/api/campaigns?limit=5")
    assert response.status_code == 200
