# webScraper.py
''' 
This is my code in relation to the API documented on https://punkapi.com
There is no authentication requirement making it an easy scrape.

rawData(url) scrape does all the lifting into a json file that the method works with.
The method is modular that could worked with to reach sub groups

I prefer the modular approach to the methods and the components. With a main file, methods and urls.
This allows me to better management of bugs(in my head) and should make for reuse elsewhere. 
Feel free to use it as you wish.
'''
import requests
import json

from urls import beers
from methods import rawData, beerList

from os import system as stm 


stm('cls')  

# rawData(url)                  # This is the initial webscrape, used in all of the following methods
beerList(beers)

