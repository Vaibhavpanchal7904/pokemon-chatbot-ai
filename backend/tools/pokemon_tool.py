import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def get_pokemon(name: str):

    response = requests.get(f"{BASE_URL}/{name.lower()}")

    if response.status_code != 200:
        return "Pokémon not found."

    data = response.json()

    types = [t["type"]["name"] for t in data["types"]]

    return {
        "name": data["name"],
        "height": data["height"] / 10,
        "weight": data["weight"] / 10,
        "types": types
    }