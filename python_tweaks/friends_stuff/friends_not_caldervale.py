# learn_friends.py

import csv

"""
# Read csv
with open('file_location/file_read.csv', 'r') as file_read:
    csv_reader = csv.reader(file_read)

    for row in csv_reader:
        print (row)

# Dict Read csv
with open("data/vehicles.csv", "r") as file_read:
    csv_dict_reader = csv.DictReader(file_read)

    for row in csv_dict_reader:
        print(row)

Data Read and Filter csv
"""

not_caldervale = []
with open("data/friends_with_schools.csv", "r") as file_read:
    csv_dict_reader = csv.DictReader(file_read)

    for row in csv_dict_reader:
        high = row["high_school"]

        if high != "Caldervale High":
            not_caldervale.append(
                {
                    "name": row["name"],
                    "surname": row["surname"],
                    "married_name": row["married_name"],
                    "location": row["location"],
                    "primary_school": row["primary_school"],
                }
            )

# Write csv

with open("data/friends_with_not_caldervale.csv", "w", newline="") as file_read:
    fieldnames = ["name", "surname", "married_name", "location", "primary_school"]
    csv_dict_writer = csv.DictWriter(file_read, fieldnames=fieldnames)
    csv_dict_writer.writeheader()

    for row in not_caldervale:
        csv_dict_writer.writerow(row)

