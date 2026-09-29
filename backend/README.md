# Marketing AI Advisor — Backend

FastAPI backend for the Marketing AI Advisor.

## Run

From the project root:

```bash
pip install -r requirements-backend.txt
uvicorn app.main:app --app-dir backend --reload
```

API docs:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Ollama

Install/start Ollama separately and pull your selected model:

```bash
ollama pull llama3.2
ollama serve
```

The backend defaults to:

```text
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

## Main endpoints

- GET `/api/health`
- GET `/api/campaigns`
- GET `/api/campaigns/{campaign_id}`
- GET `/api/campaigns/summary/overview`
- POST `/api/predictions`
- POST `/api/recommendations`
- POST `/api/simulations`
- POST `/api/chat`

The ML predictor contains safe fallback calculations so the API can run before trained `.pkl` models are available.
