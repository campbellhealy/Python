# webScraper.py
''' 
This is my code in relation to the API documented on https://pokeapi.co/api/v2/
There is no authentication requirement making it an easy scrape.
There are a lot of sub groups that I have not dug into yet.

rawData(url) scrape does all the lifting into a json file that all the other methods work with.
The methods are modular that could worked with to reach sub groups

I prefer the modular approach to the methods and the components. With a main file, methods and urls.
This allows me to better management of bugs(in my head) and should make for reuse elsewhere. 
Feel free to use it as you wish.
'''
import requests
import json

from urls import url01, url02, url03
from methods import rawData, pokemon_index, evo_index

from os import system as stm 


stm('cls')  



# rawData(url03) 
# rawData(url02) 
pokemon_index(url01)
# evo_index(url03)