# pennySaver.py
# Penny Calculator

# Year start is a fixed date to 01/01/2019

''' 
 Calculates how much you will save by the end of the year if you start on that day 
 Start on that day with the number of pennies for that day is calculated
 Increasing by a penny each day
'''
from datetime import datetime
from time import time

# Variables
yearDays = 365
janone = datetime(2019,1,1)
dtn = datetime.now()
noDays = (dtn - janone).days
amDays = noDays
leftDays = yearDays - noDays
totDays = noDays

# Days in the Year
print("Day # of Year: ", noDays)
print("Days left in Year: ", leftDays)
print()
# Initial Calculation
while noDays < yearDays:
    noDays += 1
    totDays = totDays + noDays

# Calculate Starting Value to save
print("Start today by saving ", amDays,"pennies")
print("then tomorrow ",(amDays + 1), "pennies")
print()
# Calculate Total in ££:pp If starting from today
float(totDays)
totDays = totDays/100
print("Amount if you start saving today: ", "%.2f" % totDays, "GBP")
