from langchain_community.llms import Ollama
from backend.prompts.chatbot_prompt import CHATBOT_PROMPT


class ChatbotLogic:

    def __init__(self):

        self.llm = Ollama(model="llama3")

        self.history = []

    def generate_reply(self, user_message, pokemon_data):

        prompt = CHATBOT_PROMPT.format(
            pokemon_data=pokemon_data,
            user_message=user_message
        )

        response = self.llm.invoke(prompt)

        self.history.append((user_message, response))

        return response