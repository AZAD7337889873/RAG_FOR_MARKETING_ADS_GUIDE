from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_chat():
    response = client.post("/api/chat", json={
        "message": "How should I optimize my campaign budget?"
    })
    assert response.status_code == 200
    assert "answer" in response.json()
