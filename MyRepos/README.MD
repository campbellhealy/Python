## Created this to give  a modular build to pulling the GitHub Repositories I have.

##username.py
The only file you need to change when changing user lists

## data_request.py
Created the GET Request, this would pull all the information and convert into a JSON file.
Now uses the username.py to build the GET Request url.
Builds a temp JSON file for each user searched, using the username.py file

## extract_name.py
The next step was to filter out only the information that I wanted. The name of the repo.
