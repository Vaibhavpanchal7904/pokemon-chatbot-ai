from fastapi import APIRouter
from backend.models.chat_request_model import ChatRequest
from backend.chatbot.pokemon_chat_graph import PokemonChatGraph

router = APIRouter()

chat_graph = PokemonChatGraph()


@router.post("/chat")
def chat(request: ChatRequest):

    reply = chat_graph.run(request.message)

    return {"reply": reply}