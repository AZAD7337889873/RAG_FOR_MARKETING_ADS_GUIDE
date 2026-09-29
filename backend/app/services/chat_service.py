from backend.app.schemas.chat import ChatRequest
from backend.app.rag.pipeline import RAGPipeline

class ChatService:
    def __init__(self):
        self.pipeline = RAGPipeline()

    def chat(self, request: ChatRequest):
        return self.pipeline.ask(
            question=request.message,
            top_k=request.top_k,
        )
