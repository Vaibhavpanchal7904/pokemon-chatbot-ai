from langgraph.graph import StateGraph
from backend.services.pokemon_service import PokemonService
from backend.chatbot.chatbot_logic import ChatbotLogic


class PokemonChatGraph:

    def __init__(self):

        self.pokemon_service = PokemonService()

        self.chatbot = ChatbotLogic()

    def run(self, message):

        words = message.lower().split()

        pokemon_name = None

        for word in words:
            data = self.pokemon_service.get_pokemon(word)
            if data:
                pokemon_name = word
                pokemon_data = data
                break

        if not pokemon_name:
            return "I'm designed to answer Pokémon-related questions."

        return self.chatbot.generate_reply(message, pokemon_data)