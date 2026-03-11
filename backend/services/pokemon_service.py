import requests


class PokemonService:

    BASE_URL = "https://pokeapi.co/api/v2/pokemon"

    def get_pokemon(self, name: str):

        url = f"{self.BASE_URL}/{name.lower()}"

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        types = [t["type"]["name"] for t in data["types"]]

        return {
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "types": types
        }