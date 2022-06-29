# main.py
'''
    Check if a list of websites are available
    List in separate file to abstract it from the code
'''

from urllib.request import urlopen, URLError, HTTPError
from os import system
from webpages import webpages


def main_function():
    system('cls')
    for page in webpages:
        print(page)
        try:
            html = urlopen(page)

        except URLError as e:
            print("Server not found!")
            continue

        except HTTPError as e:
            print("HTTP error")
            CONTINUE

        else:
            print("Server found")
    print('Task Complete')


if __name__ == '__main__':
    main_function()
