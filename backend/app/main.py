from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes import health, campaigns, predictions, recommendations, simulations, chat
    
app = FastAPI(
    title="Marketing AI Advisor API",
    version="1.0.0",
    description="API for campaign analytics, ML predictions, recommendations, simulations, and RAG chat.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api")
app.include_router(campaigns.router, prefix="/api")
app.include_router(predictions.router, prefix="/api")
app.include_router(recommendations.router, prefix="/api")
app.include_router(simulations.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

@app.get("/")
def root():
    return {"name": "Marketing AI Advisor API", "version": "1.0.0", "status": "running"}
