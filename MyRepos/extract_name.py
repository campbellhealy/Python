# extract_name.py
 
import json
from username import username

user = username()
tempFile = 'temp_' + user + '.json'

def extractName():
    repoNames = []
    # Read the created file
    with open(tempFile,'r') as string:
        my_dicts=json.load(string)

    # Iterate over the file to extract the values of a specific key
    for dict in my_dicts:
        for key, value in dict.items():
            if key == "full_name":
                repoNames.append(value)
    return repoNames

if __name__ == "__main__":
   print("Name Extract executed when ran directly")
   extractName()
else:
   print("Name Extract eexecuted when imported")