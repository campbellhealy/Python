# data_request.py
"""
The GET request to GitHub for my repo list
A simple GET request that could easily be made to any GitHub user account for public repos

"""
import json
import requests

from username import username

user = username()
def getRequest():
    # Build URL so it is easy to see username
    url1 = 'https://api.github.com/users/'
    url2 = '/repos'
    fullUrl = url1 + user + url2

    # GET request to obtain the list
    r = requests.get(fullUrl)

    # Convert the object into json format
    clean = r.json()
    json_object = json.dumps(clean)
    tempFile = 'temp_' + user + '.json'

    # Write the whole Object to a file for reuse rather than hit API every time
    with open(tempFile,'w') as wholeJson:
        wholeJson.write(json_object)
    return tempFile

if __name__ == "__main__":
   print("Data Request executed when ran directly")
   getRequest()
else:
   print("Data Request executed when imported")
