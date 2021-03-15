# Remoteok.py
"""
Returns the list of all active remote job listings on RemoteOK job board. 
Filtering is available using optional querystring parameters as described below. 
Remote job listings are sorted by publication date on Remotive job board.

Examples
    Main: https://remoteok.io/api 

"""
import json
import requests


raw = requests.get("https://remoteok.io/api")

# This writes the raw data to a text file to look over (Comment out after one run, not needed after getting first file)
# the_raw_data = open("raw.txt", "w")
# the_raw_data.write(raw.text)

# Has the API supplied information?
print(f"The status code for the request is {raw.status_code}")
# print("A status code of 200 is good")

# The information has been received in bytes
print(f"The type of data received is {type(raw.content)}")

# Convert the bytes into a str
data_str = (raw.content).decode("utf-8")
print(f"The {type(raw.content)} data has been converted into {type(data_str)} data")

# Convert into a python object, show what type the object is.
data_object = json.loads(data_str)
print(f"The jobs inside the data object are a {type(data_object)}\n")

# For the legal notice from the API provider check in the print(data_object)
# This API wanted the indice rather than the str
# print(f' This is the legal notice to show with the API call \n {data_object[0]}')
# Leave this in with the call

# Now I have a python object, I can check that interesting data
# How many records are in the object
print(f"There are {len(data_object)} records in the object.")

# loop through the joblist

index = 0
jobs = []

for index in range(len(data_object)):
    # print(data_object[index])
    for keys in data_object[index]:
        print(data_object[index][keys])
        jobs.append(data_object[index][keys])
    jobs.append(" ************** Next Job ******************")
    jobs.append(" ************** Next Job ******************")
    jobs.append(" ************** Next Job ******************")
print("End\n\n")

# # This creates a file with the information from the api
with open(
    "jobs.json", "w"
) as f:  # Writes a new file, 'jobs.json' with the altered set from elements in the python object above
    json.dump(
        jobs, f, indent=2
    )  # indent attribute helps format the data to look like JSON
