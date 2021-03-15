# modules.py
import requests
import json
import urls

def rawData(url):#
     # Get RAW Data file to work with
    res = requests.get(url)
    j_res = res.json()
    j_res = json.dumps(j_res)

    with open('brewDog.json','w') as jsonFile:
        jsonFile.write(j_res)
    return

def beerList(url):
    rawData(url)
    beer_list = []
    with open('brewDog.json','r') as f:
        data = json.load(f)
        for i in data:
            beer_list.append(f"Name: {i['name']}")
            beer_list.append(f"Tagline: {i['tagline']}")
            beer_list.append(f"ABV: {i['abv']}")
            beer_list.append(f"First Brewed: {i['first_brewed']}")
            beer_list.append(f"Description: {i['description']}\n")

    with open('beerList.txt', 'w') as beers:
        for beerItem in beer_list:
            beers.write(f'{beerItem}\n')


