from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[3]

class Settings(BaseSettings):
    app_name: str = "Marketing AI Advisor"
    app_env: str = "development"
    debug: bool = True
    api_prefix: str = "/api"

    database_url: str = "sqlite:///./marketing_ai.db"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"

    embedding_model: str = "all-MiniLM-L6-v2"
    chroma_path: str = str(ROOT_DIR / "vectorstore" / "chroma")
    knowledge_base_path: str = str(ROOT_DIR / "knowledge_base")

    campaigns_csv: str = str(ROOT_DIR / "data" / "raw" / "campaigns.csv")
    campaigns_parquet: str = str(ROOT_DIR / "data" / "processed" / "campaigns.parquet")
    ml_models_path: str = str(ROOT_DIR / "ml_models")

    model_config = SettingsConfigDict(
        env_file=str(ROOT_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()
