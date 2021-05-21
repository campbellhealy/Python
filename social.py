# social.py
'''
A simple way to open commonly used browser pages.
Create the .py file as below.

Create a simple two line .bat file
FInally create a shortcut to the .bat file and place it wherever you want it.

The reason for shortcut, if you try and run the .bat file directly Windows may wig out
'Security Risk'
You, well I, found the shortcut stops that craziness.

//Batch file
@echo off
c:/** Folder Path to python**/python.exe c:/** Path to Python Script**/main.py

'''
import webbrowser

def main_function():
    webbrowser.open('https://twitter.com/VincentCHealy')
    webbrowser.open('https://hashnode.com/@vchealy')


if __name__ == "__main__":
    main_function()

# GPL-3.0-or-later