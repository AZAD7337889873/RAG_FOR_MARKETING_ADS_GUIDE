from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    session_id: str = "default"
    top_k: int = Field(default=5, ge=1, le=20)

class ChatResponse(BaseModel):
    answer: str
    sources: list[dict] = []
