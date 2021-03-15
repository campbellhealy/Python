# add_colums_with_default_data.py

from csv import writer
from csv import reader

"""
Used to add an extra column to a csv file
The column is added at the right hand side.
Each record in the file will have the same value as the header initially added to the cell

# Open the initial_file in read mode and output_file in write mode
# Create a csv.reader object from the initial_file object
# Create a csv.writer object for the output_file object
# Read each row of the csv.reader object as list
# Append the header text to each row
# Add the updated row to the output_file

Issues:
I had tried DictReader/Writer but found issues using these
"""
# Variables
header = "new_column"

# Open the initial_file in read mode and output_file in write mode
with open("data/initial_file.csv", "r") as file_read_obj, open(
    "output_file.csv", "w", newline=""
) as write_obj:
    # Create a csv.reader object from the initial_file object
    csv_reader = reader(file_read_obj)

    # Create a csv.writer object for the output_file object
    csv_writer = writer(write_obj)

    # Read each row of the csv.reader object as list
    for row in csv_reader:
        # Append the header text to each row / list
        row.append(header)
        # Add the updated row / list to the output_file
        csv_writer.writerow(row)

print("Process Done")

