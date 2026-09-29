# Marketing AI Advisor Frontend

Next.js frontend for the Marketing AI Advisor application.

## Run

```bash
npm install
npm run dev
```

Open `http://localhost:3000`.

The frontend expects the FastAPI backend at:

```text
http://localhost:8000/api
```

Change this in `.env.local` if required.

## Expected backend endpoints

```text
POST /api/campaigns
POST /api/predictions
POST /api/recommendations
POST /api/simulations
POST /api/chat
```

The UI includes fallback demo values for predictions, recommendations and simulation so the frontend can be explored before the backend is connected.

## Pages

- `/` — landing/dashboard
- `/campaign` — campaign input
- `/results` — prediction + recommendation dashboard
- `/simulator` — what-if budget simulator
- `/chat` — RAG/Ollama chat interface
