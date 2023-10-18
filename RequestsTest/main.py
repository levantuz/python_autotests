import requests
host = 'https://api.pokemonbattle.me:9104'
token = '62d8b09d3a593612e8176697e7a2c59c'

post_pokemons = requests.post(f'{host}/pokemons', json = 
 { 
  "name": "Незнаю",
  "photo": "https://dolnikov.ru/pokemons/albums/001.png"
    },
headers = {'Content-type': 'application/json' , 'trainer_token': token } )
print(post_pokemons.text)


put_pokemons = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "12701",
    "name": "Знаю",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
},
headers = {'Content-type': 'application/json' , 'trainer_token': token } )
print(put_pokemons.text)


apb_pokemons = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "12701"
},
headers = {'Content-type': 'application/json' , 'trainer_token': token } )
print(apb_pokemons.text)