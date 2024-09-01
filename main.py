import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'f5d5fcbba81306895edb31acfb751c61'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}


body_create = {
    "name": "Покемошка",
    "photo_id": 21
}
response_create = requests.post(url=f'{URL}/v2/pokemons',headers = HEADER, json = body_create)
print(response_create)
print(response_create.text)


body_rename = {
    "pokemon_id": "66026",
    "name": "НовыйПокемошка",
    "photo_id": 8
}
response_rename = requests.put(url=f'{URL}/v2/pokemons',headers = HEADER, json = body_rename)
print(response_rename.text)
print(requests)


body_add_pokeball = {
    "pokemon_id": "66026"
}
response_add_pokeball = requests.put(url=f'{URL}/v2/trainers/add_pokeball',headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball)
print(response_add_pokeball.text)

