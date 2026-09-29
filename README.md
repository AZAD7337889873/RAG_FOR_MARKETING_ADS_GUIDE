# Marketing AI Advisor

An AI-powered marketing decision-support application that combines **historical campaign data, machine learning, RAG, vector search, and a local LLM** to help marketers analyze campaigns and make data-driven decisions.

The application can answer questions such as:

- Which advertising platform is suitable for a campaign?
- What budget should be allocated?
- How many clicks and conversions can be expected?
- What revenue and ROAS might be expected?
- Which campaigns or platforms performed well historically?
- Why is a campaign underperforming?
- What could happen if the campaign budget is increased?
- Which location, audience, channel, or campaign type has historically performed better?

---

## 1. Project Overview

The Marketing AI Advisor combines four major capabilities:

### Historical Analytics

Analyzes historical campaign performance data stored locally in CSV/Parquet format.

### Machine Learning

Predicts campaign outcomes such as:

- Clicks
- Conversions
- Revenue
- ROAS

### RAG

Retrieves relevant marketing knowledge and historical context from a local ChromaDB vector store.

### LLM

Uses Ollama to generate a natural-language explanation based on:

- Historical data
- ML predictions
- Retrieved RAG context
- Recommendation rules

---

# 2. Architecture

```text
                         USER
                           │
                           ▼
                    ┌─────────────┐
                    │   Next.js   │
                    │  Frontend   │
                    └──────┬──────┘
                           │ HTTP
                           ▼
                    ┌─────────────┐
                    │   FastAPI   │
                    │   Backend   │
                    └──────┬──────┘
                           │
          ┌────────────────┼──────────────────┐
          │                │                  │
          ▼                ▼                  ▼
    CSV / Parquet      ML Models          RAG Engine
    Historical Data    Predictions             │
          │                │                    ▼
          │                │               ChromaDB
          │                │                    │
          │                │                    ▼
          │                │          Ollama Embeddings
          │                │                    │
          └────────────────┼────────────────────┘
                           │
                           ▼
                    Context + Predictions
                           │
                           ▼
                    Ollama LLM
                  llama3.1:8b
                           │
                           ▼
                  Marketing Advisor
````

---

# 3. Technology Stack

## Backend

* Python
* FastAPI
* Pydantic
* Pandas
* NumPy
* Scikit-learn
* Joblib

## AI / ML

* Scikit-learn
* Machine Learning prediction models
* Ollama
* `llama3.1:8b`
* `nomic-embed-text`

## RAG

* ChromaDB
* Vector embeddings
* Document chunking
* Similarity search
* Retrieval-Augmented Generation

## Frontend

* Next.js
* React
* TypeScript
* CSS

## Data

* CSV
* Parquet

---

# 4. Why Ollama?

This project uses Ollama instead of a cloud LLM provider.

Ollama allows the LLM to run locally.

The application uses two Ollama models:

### LLM

```text
llama3.1:8b
```

Used for generating natural-language responses.

### Embedding Model

```text
nomic-embed-text
```

Used to convert documents into embeddings for RAG.

The flow is:

```text
Marketing Documents
        │
        ▼
nomic-embed-text
        │
        ▼
Embeddings
        │
        ▼
ChromaDB
```

For answering questions:

```text
User Question
      │
      ▼
Embedding
      │
      ▼
ChromaDB
      │
      ▼
Relevant Context
      │
      ▼
Ollama llama3.1:8b
      │
      ▼
Final Answer
```

---

# 5. Project Structure

```text
marketing-ai-advisor/
│
├── README.md
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
├── backend/
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   │
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   └── settings.py
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes/
│   │   │       ├── __init__.py
│   │   │       ├── health.py
│   │   │       ├── campaigns.py
│   │   │       ├── predictions.py
│   │   │       ├── recommendations.py
│   │   │       ├── simulations.py
│   │   │       └── chat.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── campaign.py
│   │   │   ├── prediction.py
│   │   │   ├── recommendation.py
│   │   │   ├── simulation.py
│   │   │   └── chat.py
│   │   │
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   ├── connection.py
│   │   │   ├── models.py
│   │   │   └── repositories.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── campaign_service.py
│   │   │   ├── prediction_service.py
│   │   │   ├── recommendation_service.py
│   │   │   ├── simulation_service.py
│   │   │   └── chat_service.py
│   │   │
│   │   ├── ml/
│   │   │   ├── __init__.py
│   │   │   ├── features.py
│   │   │   ├── predictor.py
│   │   │   ├── model_loader.py
│   │   │   │
│   │   │   └── models/
│   │   │       ├── __init__.py
│   │   │       ├── click_model.py
│   │   │       ├── conversion_model.py
│   │   │       ├── revenue_model.py
│   │   │       └── roas_model.py
│   │   │
│   │   ├── recommendation/
│   │   │   ├── __init__.py
│   │   │   ├── platform.py
│   │   │   ├── budget.py
│   │   │   └── campaign.py
│   │   │
│   │   ├── rag/
│   │   │   ├── __init__.py
│   │   │   ├── documents.py
│   │   │   ├── embeddings.py
│   │   │   ├── vector_store.py
│   │   │   ├── retriever.py
│   │   │   ├── prompts.py
│   │   │   └── pipeline.py
│   │   │
│   │   ├── llm/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── ollama.py
│   │   │
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── logging.py
│   │       └── exceptions.py
│   │
│   └── tests/
│       ├── __init__.py
│       ├── test_campaigns.py
│       ├── test_predictions.py
│       ├── test_recommendations.py
│       ├── test_simulations.py
│       ├── test_rag.py
│       └── test_chat.py
│
├── frontend/
│   ├── package.json
│   ├── next.config.ts
│   ├── tsconfig.json
│   ├── .env.local
│   │
│   ├── app/
│   │   ├── page.tsx
│   │   ├── campaign/
│   │   │   └── page.tsx
│   │   ├── results/
│   │   │   └── page.tsx
│   │   ├── simulator/
│   │   │   └── page.tsx
│   │   └── chat/
│   │       └── page.tsx
│   │
│   ├── components/
│   │   ├── CampaignForm.tsx
│   │   ├── PredictionCards.tsx
│   │   ├── BudgetAllocation.tsx
│   │   ├── PlatformComparison.tsx
│   │   ├── HistoricalEvidence.tsx
│   │   ├── ChatBox.tsx
│   │   └── WhatIfSimulator.tsx
│   │
│   ├── lib/
│   │   ├── api.ts
│   │   └── types.ts
│   │
│   └── styles/
│       └── globals.css
│
├── data/
│   ├── raw/
│   │   └── campaigns.csv
│   └── processed/
│       └── campaigns.parquet
│
├── ml_models/
│   ├── click_model.pkl
│   ├── conversion_model.pkl
│   ├── revenue_model.pkl
│   └── roas_model.pkl
│
├── vectorstore/
│   └── chroma/
│
├── knowledge_base/
│   ├── platform_guidelines/
│   │   ├── google_ads.txt
│   │   ├── meta_ads.txt
│   │   ├── tiktok_ads.txt
│   │   ├── linkedin_ads.txt
│   │   └── amazon_ads.txt
│   │
│   ├── marketing_strategy/
│   │   ├── budget_allocation.txt
│   │   ├── campaign_optimization.txt
│   │   ├── ctr_optimization.txt
│   │   ├── conversion_optimization.txt
│   │   └── roas_optimization.txt
│   │
│   └── business_rules/
│       ├── recommendation_rules.txt
│       └── budget_rules.txt
│
├── scripts/
│   ├── generate_campaign_data.py
│   ├── load_data.py
│   ├── train_models.py
│   └── build_vectorstore.py
│
└── docs/
    ├── architecture.md
    ├── data_model.md
    ├── rag_architecture.md
    └── api.md
```

---

# 6. Prerequisites

Install the following:

### Python

Python 3.11 or newer is recommended.

Verify:

```bash
python --version
```

### Node.js

Node.js 20+ is recommended.

Verify:

```bash
node --version
```

### Ollama

Install Ollama on your machine.

Verify:

```bash
ollama --version
```

---

# 7. Install Ollama Models

After installing Ollama, download the models required by the project.

### LLM

```bash
ollama pull llama3.1:8b
```

### Embedding Model

```bash
ollama pull nomic-embed-text
```

Verify:

```bash
ollama list
```

You should see both models.

---

# 8. Create Python Virtual Environment

From the project root:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

---

# 9. Install Python Dependencies

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

# 10. Environment Configuration

Create `.env` in the project root.

Example:

```env
APP_NAME=Marketing AI Advisor
APP_ENV=development
DEBUG=true

BACKEND_HOST=127.0.0.1
BACKEND_PORT=8000

RAW_DATA_PATH=./data/raw/campaigns.csv
PROCESSED_DATA_PATH=./data/processed/campaigns.parquet

MODEL_DIR=./ml_models

CLICK_MODEL_PATH=./ml_models/click_model.pkl
CONVERSION_MODEL_PATH=./ml_models/conversion_model.pkl
REVENUE_MODEL_PATH=./ml_models/revenue_model.pkl
ROAS_MODEL_PATH=./ml_models/roas_model.pkl

CHROMA_PERSIST_DIRECTORY=./vectorstore/chroma
CHROMA_COLLECTION=marketing_knowledge

RAG_TOP_K=5
RAG_CHUNK_SIZE=800
RAG_CHUNK_OVERLAP=100
RAG_TEMPERATURE=0.2

LLM_PROVIDER=ollama

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1:8b
OLLAMA_EMBEDDING_MODEL=nomic-embed-text

NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

# 11. Generate / Prepare Historical Data

The application uses historical campaign data.

The raw dataset is stored here:

```text
data/raw/campaigns.csv
```

The processed dataset is stored here:

```text
data/processed/campaigns.parquet
```

Run:

```bash
python scripts/generate_campaign_data.py
```

Then process/load the data:

```bash
python scripts/load_data.py
```

---

# 12. Train Machine Learning Models

Train the prediction models:

```bash
python scripts/train_models.py
```

This generates:

```text
ml_models/
├── click_model.pkl
├── conversion_model.pkl
├── revenue_model.pkl
└── roas_model.pkl
```

These models are used by the FastAPI backend.

---

# 13. Build the RAG Vector Store

The knowledge documents are stored in:

```text
knowledge_base/
```

Run:

```bash
python scripts/build_vectorstore.py
```

The documents are:

```text
knowledge_base/
├── platform_guidelines/
├── marketing_strategy/
└── business_rules/
```

The documents are:

```text
1. Loaded
2. Split into chunks
3. Converted into embeddings using Ollama
4. Stored in ChromaDB
```

The resulting vector database is stored locally:

```text
vectorstore/chroma/
```

---

# 14. Start the Backend

From the project root:

```bash
uvicorn backend.app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

FastAPI Swagger documentation:

```text
http://localhost:8000/docs
```

---

# 15. Start the Frontend

Open another terminal.

Navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start Next.js:

```bash
npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

# 16. Application Flow

The complete application flow is:

```text
User enters campaign requirements
              │
              ▼
          Next.js UI
              │
              ▼
          FastAPI API
              │
              ├───────────────┐
              │               │
              ▼               ▼
       Historical Data     ML Models
              │               │
              │               ├── Click Prediction
              │               ├── Conversion Prediction
              │               ├── Revenue Prediction
              │               └── ROAS Prediction
              │
              ▼
      Recommendation Engine
              │
              ▼
          RAG Retriever
              │
              ▼
           ChromaDB
              │
              ▼
      Relevant Marketing Docs
              │
              └───────────────┐
                              ▼
                           Ollama
                         llama3.1:8b
                              │
                              ▼
                     Final AI Response
```

---

# 17. Core API Endpoints

## Health

```http
GET /health
```

Checks whether the backend is running.

---

## Campaigns

```http
GET /api/campaigns
```

Returns historical campaigns.

```http
GET /api/campaigns/{campaign_id}
```

Returns a specific campaign.

---

## Predictions

```http
POST /api/predictions
```

Example:

```json
{
  "platform": "Meta",
  "location": "Dubai",
  "campaign_type": "Conversion",
  "budget": 10000,
  "duration": 30
}
```

Possible response:

```json
{
  "predicted_clicks": 24500,
  "predicted_conversions": 780,
  "predicted_revenue": 43800,
  "predicted_roas": 4.38
}
```

---

# 18. Recommendations

```http
POST /api/recommendations
```

Example:

```json
{
  "objective": "conversion",
  "location": "Dubai",
  "budget": 30000,
  "duration": 30,
  "target_audience": "18-34"
}
```

The recommendation engine considers:

* Historical campaign performance
* Platform performance
* Location
* Campaign objective
* Audience
* Budget
* ML predictions
* Marketing rules
* RAG evidence

---

# 19. What-If Simulation

```http
POST /api/simulations
```

Example:

```json
{
  "platform": "Meta",
  "location": "Dubai",
  "current_budget": 10000,
  "new_budget": 20000,
  "duration": 30
}
```

The simulator can estimate changes in:

* Clicks
* Conversions
* Revenue
* ROAS
* Spend efficiency

---

# 20. AI Chat

```http
POST /api/chat
```

Example:

```json
{
  "message": "Which platform should I use for a conversion campaign in Dubai with a 30K budget?"
}
```

The chat pipeline:

```text
Question
   │
   ▼
Retrieve relevant knowledge
   │
   ▼
Retrieve historical evidence
   │
   ▼
Generate ML predictions
   │
   ▼
Build prompt
   │
   ▼
Ollama
   │
   ▼
Marketing recommendation
```

---

# 21. Important Design Principle

The LLM should **not be responsible for calculating marketing metrics**.

For example, if the user asks:

> What will happen if I increase my budget from 10K to 20K?

The application should first use the data and ML models to calculate/predict the values.

Then Ollama explains the result.

```text
Historical Data
       │
       ▼
    ML Model
       │
       ▼
Predicted Metrics
       │
       ▼
Recommendation Engine
       │
       ▼
      RAG
       │
       ▼
     Ollama
       │
       ▼
Natural Language Explanation
```

This separates:

```text
DATA → FACTS

ML → PREDICTIONS

RAG → KNOWLEDGE / EVIDENCE

LLM → EXPLANATION
```

---

# 22. RAG Knowledge Sources

The knowledge base can contain information about:

### Advertising Platforms

```text
Google Ads
Meta Ads
TikTok Ads
LinkedIn Ads
Amazon Ads
```

### Marketing Strategies

```text
Budget Allocation
Campaign Optimization
CTR Optimization
Conversion Optimization
ROAS Optimization
```

### Business Rules

```text
Platform Recommendation Rules
Budget Allocation Rules
Campaign Optimization Rules
```

These documents are embedded and stored in ChromaDB.

---

# 23. No PostgreSQL Required

This project intentionally does not require PostgreSQL.

Historical campaign data is stored using:

```text
CSV
 ↓
Parquet
 ↓
Pandas
```

RAG data is stored using:

```text
Documents
 ↓
Ollama Embeddings
 ↓
ChromaDB
```

Therefore the local project does not require:

```text
PostgreSQL
Docker
Cloud database
Cloud LLM
```

---

# 24. No Docker Required

The application runs locally using:

```text
Python
FastAPI
Next.js
Ollama
ChromaDB
```

You can start each component independently.

```text
Terminal 1
──────────
Ollama

Terminal 2
──────────
FastAPI

Terminal 3
──────────
Next.js
```

---

# 25. Testing

Run backend tests:

```bash
pytest
```

Run a specific test:

```bash
pytest backend/tests/test_predictions.py
```

Run with verbose output:

```bash
pytest -v
```

---

# 26. Example Use Cases

### Use Case 1 — Platform Recommendation

```text
User:
I have a $50K budget for a conversion campaign
targeting users in Dubai. Which platform should I use?
```

The application retrieves:

```text
Historical platform performance
+
Location performance
+
Campaign objective
+
ML predictions
+
Marketing knowledge
```

Then generates an explanation.

---

### Use Case 2 — Budget Recommendation

```text
User:
How should I distribute a $100K budget across platforms?
```

The system evaluates historical performance and prediction outputs before producing a proposed allocation.

---

### Use Case 3 — Campaign Forecast

```text
User:
If I spend $20K on Meta for 30 days,
how many clicks and conversions could I expect?
```

The ML prediction layer generates estimated metrics.

---

### Use Case 4 — Campaign Diagnosis

```text
User:
Why is my campaign performing poorly?
```

The application can examine:

```text
CTR
CPC
Conversion Rate
ROAS
Spend
Clicks
Conversions
Historical benchmarks
```

and use RAG knowledge to explain possible optimization actions.

---

### Use Case 5 — What-If Analysis

```text
User:
What happens if I increase the budget by 50%?
```

The simulator compares:

```text
Current Scenario
       vs
New Scenario
```

and returns estimated changes.

---

# 27. Development Roadmap

## Phase 1 — Data

* Generate campaign dataset
* Clean data
* Create Parquet dataset
* Implement data access layer

## Phase 2 — Machine Learning

* Feature engineering
* Train click model
* Train conversion model
* Train revenue model
* Train ROAS model
* Model evaluation
* Model persistence

## Phase 3 — Recommendation Engine

* Platform recommendation
* Budget allocation
* Campaign recommendation
* Performance analysis

## Phase 4 — RAG

* Create knowledge base
* Document loading
* Chunking
* Ollama embeddings
* ChromaDB
* Retrieval
* Prompt construction

## Phase 5 — LLM

* Ollama integration
* Context injection
* Response generation
* Chat service

## Phase 6 — FastAPI

* API schemas
* Routes
* Services
* Error handling
* API documentation

## Phase 7 — Frontend

* Campaign form
* Prediction dashboard
* Recommendation dashboard
* Platform comparison
* Historical evidence
* What-if simulator
* AI chat

## Phase 8 — Testing

* Unit tests
* API tests
* RAG tests
* ML tests
* End-to-end testing

---

# 28. Local URLs

| Component | URL                        |
| --------- | -------------------------- |
| Next.js   | http://localhost:3000      |
| FastAPI   | http://localhost:8000      |
| Swagger   | http://localhost:8000/docs |
| Ollama    | http://localhost:11434     |

---

# 29. Final Technology Architecture

```text
┌──────────────────────────────────────────────┐
│                  FRONTEND                    │
│                  Next.js                     │
│                  React                       │
└──────────────────────┬───────────────────────┘
                       │
                       │ REST API
                       ▼
┌──────────────────────────────────────────────┐
│                  BACKEND                     │
│                  FastAPI                     │
│                                              │
│  ┌────────────┐   ┌───────────────────────┐ │
│  │ Data Layer │   │ Recommendation Engine │ │
│  └─────┬──────┘   └───────────┬───────────┘ │
│        │                      │             │
│        ▼                      ▼             │
│  CSV / Parquet          ML Predictions     │
│                                              │
│              ┌─────────────────────┐         │
│              │      RAG Engine      │         │
│              └──────────┬──────────┘         │
└─────────────────────────┼────────────────────┘
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
        ┌───────────┐           ┌────────────┐
        │ ChromaDB  │           │   Ollama   │
        │           │           │            │
        │ Vectors   │           │ llama3.1:8b│
        │ Retrieval │           │ embeddings │
        └───────────┘           └────────────┘
```

---

# 30. Project Goal

The goal of this project is to demonstrate an end-to-end AI/data product architecture combining:

```text
Data Engineering
       +
Machine Learning
       +
RAG
       +
Vector Database
       +
LLM
       +
FastAPI
       +
Next.js
       +
API Architecture
       +
Data-driven Recommendations
```

The application is designed as a **local-first AI marketing decision-support system**, where numerical predictions are generated from data/ML and the LLM provides contextual reasoning and natural-language interaction.

```

This README now matches the architecture we've settled on: **Ollama + ChromaDB + CSV/Parquet + ML + FastAPI + Next.js**, with PostgreSQL, Docker, and OpenAI removed from the core setup.
