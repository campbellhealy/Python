# webScraper.py
''' 
This is my code in relation to the API documented on http://www.dnd5eapi.co/
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

from urls import spells,  classes,  races,  monsters
from methods import rawData, spell_index, class_index, races_index, monsters_index

from os import system as stm 


stm('cls')  

# rawData(url)                  # This is the initial webscrape, used in all of the following methods
# spell_index(spells)
# class_index(classes)
# races_index(races)
monsters_index(monsters)
