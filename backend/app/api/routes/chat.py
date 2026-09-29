from fastapi import APIRouter
from backend.app.schemas.chat import ChatRequest
from backend.app.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["RAG Chat"])
service = ChatService()

@router.post("")
def chat(request: ChatRequest):
    return service.chat(request)
