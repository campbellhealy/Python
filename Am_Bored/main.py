# main.py
'''
    This uses the boredapi.com api to get activity suggestions.
    Yes, I made it out of boredom and used a few techniques to build on this rather
    than a single function.
'''

from logo import logo  # Makes it easier to change
from os import system
import requests
from ast import literal_eval as le
# Used this library to convert the str into a dict from the get request
'''
    https://docs.python.org/3/library/ast.html
    The ast module helps Python applications to process trees of the Python 
    abstract syntax grammar. The abstract syntax itself might change with 
    each Python release; this module helps to find out programmatically 
    what the current grammar looks like.
'''

# I always separate modules I have written, below, from the others, above


def am_bored():
    system('cls')  # To give a clean console
    print(logo)
    url = 'https://www.boredapi.com/api/activity'
    response = getapi(url)
    giveoutput(response)
    again = input(' Do you want another suggestion? (Y/N)\n').lower()
    if again == 'y':
        am_bored()
    else:
        exit()


def getapi(url):
    # This GETs the info from the API
    response = requests.get(url).text
    response = le(response)
    return response


def giveoutput(response):
    # Presentation of the information wanted from the API
    for k, v in response.items():
        k = k.capitalize()
        if type(v) == str:
            v = v.capitalize()
        if k == 'Price':
            print(k, ': £', v)
        elif k == 'Link' or k == 'Key':
            continue
        elif k == 'Accessibility':
            v = int(v * 10)
            print(k, ': ', v, '%')
        else:
            print(k, ': ', v)
    print('\nboredapi.com')


if __name__ == "__main__":
    am_bored()
