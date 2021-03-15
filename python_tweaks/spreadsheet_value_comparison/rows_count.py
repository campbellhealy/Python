import openpyxl
from openpyxl import Workbook

# Counts the columns in a spreadsheet

def row_count(filename, column):
    wb = openpyxl.load_workbook(filename)   # Opens the file
    sheet = wb['operators']                 # Selects the sheet
    collist = [column]                      #Choice of column input from the main function
    for rows in collist:
        collength = len(sheet[rows])
        return collength
         