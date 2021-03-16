# main.py
"""
Created this to give  a modular build to pulling the GitHub Repositories I have.
I slowly worked through the various tasks.

Created the GEt Request, this would pull all the information and convert into a JSON file.
Thus not needing to use this module again and consume the API more.

The next step was to filter out only the information that I wanted. The name of the repo.

Finally back to the main file and print it out. I thought about creating another file but 
there isn't enough repos there yet for that.
"""
import json, requests

from data_request import getRequest
from extract_name import extractName
from os import system

system('cls') # This just clears the console

getRequest()
extractName()

# This is the final output
print(extractName())

if __name__ == "__main__":
    print("Main executed when ran directly")
    getRequest()
    extractName()
else:
    print("Blah")