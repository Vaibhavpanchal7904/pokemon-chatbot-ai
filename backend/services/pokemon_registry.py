import requests

class PokemonRegistry:

    def __init__(self):
        self.pokemon_names = set()
        self.load_pokemon_names()

    def load_pokemon_names(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=2000"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            self.pokemon_names = {
                p["name"] for p in data["results"]
            }

    def is_pokemon(self, word):
        return word in self.pokemon_names