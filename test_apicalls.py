from api_calls import get_best_pokemon, get_pokemon_by_name

def test_get_best_pokemon():
    pokemon = get_best_pokemon()
    assert pokemon is not None
    assert pokemon['name'] == 'chikorita'

def test_get_pokemon_by_name():
    pokemon = get_pokemon_by_name("charizard")
    assert pokemon is not None
    assert pokemon['name'] == 'charizard'

def test_get_pokemon_by_name_invalid():
    pokemon = get_pokemon_by_name("invalid_pokemon_name")
    assert pokemon is None
