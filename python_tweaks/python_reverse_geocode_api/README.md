# 
# Vincent Healy August 2019
# Written using Visual Studio Code v 1.37.1 with Python Extension
#
# Running the scripts in Visual Studio Code v 1.37.1 with Python Extension gave random errors
# Successful runs in Windows Powershell with the latest Python installation

script_one.py - The first location reverse geocode details
script_two.py - The secondlocation reverse geocode details
script_three.py - The third location reverse geocode details
script_all.py - The all locations reverse geocode details with a reusable for loop to reduce code

After a little bit of study to understand the api testng, nested dictionaries and that the python extension in VS code is 
flaky. I got the code running.

When running all four in VS code, the first ran without issue, 
the second would split, showing two or three entries, the Run OK message and the remaining entries
the third would randomly not recognise the nested dictionary Address.

Running all four scripts in powershell showed there was no issue and gave me a learning experience that was
spread over three days.