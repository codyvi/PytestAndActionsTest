import requests

def get_best_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/chikorita"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_pokemon_by_name(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_pokemon_stats(name):
    pokemon = get_pokemon_by_name(name)
    if pokemon:
        return pokemon['stats']
    else:
        return None