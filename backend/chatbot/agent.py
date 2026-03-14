from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from backend.services.pokemon_service import PokemonService

pokemon_service = PokemonService()


@tool
def pokemon_info(name: str):
    """Get information about a Pokémon."""
    return pokemon_service.get_pokemon(name)


# LLM
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0.2
)


tools = [pokemon_info]

memory = MemorySaver()


# System instructions for the agent
system_prompt = """
You are a helpful Pokémon assistant.

You have access to a tool called `pokemon_info` that retrieves Pokémon data.

Rules:
1. If the user asks about a Pokémon, ALWAYS use the `pokemon_info` tool to get the data.
2. If the tool returns data, explain the Pokémon using that information.
3. If the tool returns None or no data, respond with:
   "I can only answer questions about Pokémon."
4. You should not answer questions using your own knowledge. Always rely on the tool.
"""


agent = create_react_agent(
    llm,
    tools,
    checkpointer=memory,
    prompt=system_prompt
)