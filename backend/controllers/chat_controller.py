from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    reply = chat_service.chat(request.message)

    return {"reply": reply}