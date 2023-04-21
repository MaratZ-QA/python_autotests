import requests
import pytest

TOKEN = 'my_token'
BASE_URL = 'https://pokemonbattle.me:9104/'

# Статус кода 200 на GET /trainers #
def test_status_code():
    response = requests.get(f'{BASE_URL}trainers', headers = {'trainer_token' : TOKEN}, 
    json={'trainer_id' : "4041"})
    assert response.status_code == 200


# Имя тренера #
def test_name_of_trainer():
    response = requests.get(f'{BASE_URL}trainers', params = {'trainer_id' : 4041})
    assert response.json()['trainer_name'] == 'Гагарри'