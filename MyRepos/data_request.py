# data_request.py
"""
The GET request to GitHub for my repo list
A simple GET request that could easily be made to any GitHub user account for public repos

"""
import json
import requests

def getRequest():
    # GET request to obtain the list
    r = requests.get('https://api.github.com/users/vchealy/repos')

    # Convert the object into json format
    clean = r.json()
    json_object = json.dumps(clean)

    # Write the whole Object to a file for reuse rather than hit API every time
    with open('temp.json','w') as wholeJson:
        wholeJson.write(json_object)
    return