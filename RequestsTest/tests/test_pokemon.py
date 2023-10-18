import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '62d8b09d3a593612e8176697e7a2c59c'

def test_status_code():
    get_tr = requests.get(f'{host}/pokemons?trainer_id=2684')

    assert get_tr.status_code == 200

def test_part_of_answer():
    get_tr_body = get_tr = requests.get(f'{host}/pokemons?trainer_id=2684')

    assert get_tr_body.json()['trainer_id' == '2684']