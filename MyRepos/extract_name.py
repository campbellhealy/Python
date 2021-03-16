# extract_name.py
 
import json

def extractName():
    repoNames = []
    # Read the created file
    with open('temp.json','r') as string:
        my_dicts=json.load(string)

    # Iterate over the file to extract the values of a specific key
    for dict in my_dicts:
        for key, value in dict.items():
            if key == "full_name":
                repoNames.append(value)
    return repoNames