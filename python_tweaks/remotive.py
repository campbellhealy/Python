# Remotive.py
"""
Returns the list of all active remote job listings on Remotive job board. 
Filtering is available using optional querystring parameters as described below. 
Remote job listings are sorted by publication date on Remotive job board.

Examples
    Main: https://remotive.io/api/remote-jobs

    Category: https://remotive.io/api/remote-jobs?category=software-dev
    Category List: https://remotive.io/api/remote-jobs/categories

    Tags: https://remotive.io/api/remote-jobs?tags=c-sharp,linux
    Tags List: https://remotive.io/api/remote-jobs/tags

    Tag Operator: https://remotive.io/api/remote-jobs?tags=c-sharp,linux&tag_operator=and
    or by default
    and

    Company Name: https://remotive.io/api/remote-jobs?company_name=remotive
    Use 'ilike' for part match

    Search: https://remotive.io/api/remote-jobs?search=front%20end
        Use 'ilike' for part match

    Limit: https://remotive.io/api/remote-jobs?limit=5
    Int value
"""
import json
import requests


raw = requests.get("https://remotive.io/api/remote-jobs?category=software-dev")
# Has the API supplied information?
print(f"The status code for the request is {raw.status_code}")
# print("A status code of 200 is good")

# The information has been received in bytes
print(f"The type of data received is {type(raw.content)}")

# Convert the bytes into a str
data_str = (raw.content).decode("utf-8")
print(f"The {type(raw.content)} data has been converted into {type(data_str)} data")

# Convert into a python object
data_object = json.loads(data_str)
print(f'The jobs inside the data object are a {type(data_object["jobs"])}\n')

# Now I have a python object, I can check that the interesting data is now a list
print(f'{data_object["0-legal-notice"]}\n')  # Leave this in with the call
print(f'The number of items in the call is {data_object["job-count"]}\n')
# print(data_object)

# loop through the categories in the joblist
# for item in data_object["jobs"]:
#     print(item["name"])

for item in data_object["jobs"]:
    print(
        f'id {item["id"]}\n\
        Location: {item["candidate_required_location"]}\n \
        {item["url"]}\n \
        Title: {item["title"]}\n \
        Company Name: {item["company_name"]}\n \
        Experience in: {item["tags"]}\n \
        Full/Part-Time: {item["job_type"]}\n \
        Publish: {item["publication_date"]}\n \
        Salary: {item["salary"]}\n \
        '
    )
# Another item can be added for the description of the job
# copy in the line below this to just below Salary:
# Description: {item["description"]}\n \

# This creates a file with the information from the api

with open(
    "jobs.json", "w"
) as f:  # Writes a new file, 'jobs.json' with the altered set from elements in the python object above
    json.dump(
        data_object["jobs"], f, indent=2
    )  # indent attribute helps format the data to look like JSON
