import requests
TOKEN = 'my_token'
BASE_URL = 'https://pokemonbattle.me:9104/'


# Создание покемона #
response = requests.post(f'{BASE_URL}pokemons', headers= {'trainer_token' : TOKEN }, json= {
    "name": "Один",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response.text)


# Смена имени покемона #
response_name = requests.put(f'{BASE_URL}pokemons', headers= {'trainer_token' : TOKEN }, json= {
    "pokemon_id": "9284",
    "name": "Два",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print (response_name.text)


# Поймать покемона в покебол #
response_pokemon = requests.post(f'{BASE_URL}trainers/add_pokeball', headers = {'trainer_token' : TOKEN }, json= {
    "pokemon_id": "9392"
})

print (response_pokemon.text)