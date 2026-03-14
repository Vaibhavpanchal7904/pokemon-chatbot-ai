import requests

class PokemonService:

    BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    def __init__(self):
        self.cache = {}

    def get_pokemon(self, name: str):

        name = name.lower()

        # Return cached data
        if name in self.cache:
            return self.cache[name]

        url = f"{self.BASE_URL}/{name}"

        try:
            response = requests.get(url, timeout=5)

            if response.status_code != 200:
                return None

            data = response.json()

            types = [t["type"]["name"] for t in data["types"]]

            pokemon_data = {
                "name": data["name"],
                "height": data["height"]/10,
                "weight": data["weight"]/10,
                "types": types
            }

            # Save to cache
            self.cache[name] = pokemon_data

            return pokemon_data

        except requests.exceptions.RequestException:
            return None