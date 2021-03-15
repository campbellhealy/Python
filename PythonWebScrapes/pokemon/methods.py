
# medthods.py
import requests
import json

from urls import url01

def rawData(url):
     # Get RAW Data file to work with
    res = requests.get(url)
    j_res = res.json()
    j_res = json.dumps(j_res)

    with open('Pokemon.json','w') as jsonFile:
        jsonFile.write(j_res)
    return

def pokemon_index(url):
    rawData(url)
    pokemon_list = []
    with open('Pokemon.json','r') as f:
        data = json.load(f)
        for i in data:
            if i == 'results':
                i_data = (data[i])
                for k in i_data:
                    pokemon_list.append(k['name'])

    with open('pokemonList.txt', 'w') as pokemons:
        for pokemonItem in pokemon_list:
            pokemons.write(f'{pokemonItem}\n')


def evo_index(url):
    rawData(url)
    pokemon_list = []
    with open('Pokemon.json','r') as f:
        data = json.load(f)
        for i in data:
            if i == 'results':
                i_data = (data[i])
                for k in i_data:
                    pokemon_list.append(k['url'])

    with open('pokemonList.txt', 'w') as pokemons:
        for pokemonItem in pokemon_list:
            pokemons.write(f'{pokemonItem}\n')