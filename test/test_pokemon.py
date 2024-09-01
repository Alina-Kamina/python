import requests
import pytest


URL = 'https://api.pokemonbattle.ru'
TOKEN = 'f5d5fcbba81306895edb31acfb751c61'
HEADER = {'Content-Type' : 'application/json','trainer_token' : TOKEN}
TRAINER_ID = 5041 
body_create = {
    "name": "12312",
    "photo_id": 21
    }


def test_trainers():
    response_trainer = requests.get(url=f'{URL}/v2/trainers',params = {'trainer_id' : TRAINER_ID})
    assert response_trainer.status_code == 200
    assert response_trainer.json()["data"][0]["id"] == '5041'


def test_pokemon():
    response_create = requests.get(url=f'{URL}/v2/pokemons',params = {'trainer_id' : TRAINER_ID})
    assert response_create.status_code == 200


def test_create_pokemon():
    response_create = requests.post(url=f'{URL}/v2/pokemons',headers = HEADER, json = body_create)
    assert response_create.status_code == 201