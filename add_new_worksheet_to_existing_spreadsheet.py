# main.py
'''
    A spreadsheet, Data_Management, is an inventory document with multiple worksheets.
    One worksheet, named NEW_DATA, is updated twice daily via an email sent to me as a csv file.
    Where I manually replace the data in NEW_DATA with the information in the csv 
    The NEW_DATA worksheet is used by another worksheet in Data_Management, named OVERVIEW, 
    that has numerous formula.

    Requirements:
    1:
        Automate the addition of NEW_DATA to Data_Management
        Without damaging the formulas on OVERVIEW
    2:
        When the file is emailed to me.
        Trigger the addition of NEW_DATA to run
    3:
        - Log the addition of the NEW_DATA file to Data_Management
        - Log the removal of old NEW_DATA files
        - Use terminal to monitor the logging, rather than write to log files
'''

import glob
import openpyxl
import pandas as pd
from time import sleep 

from os.path import getctime
from os import system, listdir

main_inventory = 'Data_Management.xlsx'


def watchdog():
    '''
        # 3, this is a terminal that monitors the \archive folder for changes
        \archive is the folder that the emailed csv files are saved to
        added: prints to console and actions update_inventory()
        removed: prints to console when another process, not included, delete a file from \archive
    '''
    system('cls')
    print('Watchdog active')
    path_to_watch = "archive"
    before = dict ([(f, None) for f in listdir (path_to_watch)])
    while 1:
        sleep (5)
        after = dict ([(f, None) for f in listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added: print(f'Added:  {added}')
        sleep(2)
        if added: update_inventory()
        if removed: print(f'Removed: {removed}')
        before = after

def update_inventory():
    '''
        Prepares the Data_Management spreadsheet by removing the old new_data worksheet
        Adds the latest new_data worksheet
    '''
    system('cls')
    inventory= openpyxl.load_workbook(main_inventory)
    new_data = get_new_data_csv()
    ams3 = pd.read_csv(new_data)

    remove_new_data_worksheet(inventory)
    add_new_data_report(ams3)
    
    print(f'The document {main_inventory}\nhas been updated with new data file:\n{new_data}\n')
    sleep(3)
    print('Watchdog Active')



def get_new_data_csv():
    # Gets the latest csv file that was added to \archive
    lastest_file = max(glob.glob(r'archive\*csv'), key=getctime)
    print(f'The latest data file is:\n{lastest_file}\n')
    return lastest_file


def remove_new_data_worksheet(inventory):
    # This removes the NEW DATA worksheet
    # I tried to do a replace but it wasnt happening
    std=inventory['PASTE NEW DATA HERE']
    inventory.remove(std)
    inventory.save(main_inventory)
    inventory = pd.read_excel(main_inventory)


def add_new_data_report(ams3):
    # This adds the latest csv data worksheet
    with pd.ExcelWriter(main_inventory, engine='openpyxl', mode='a') as writer:
        # Due to the formula setup on the Overview, do not remove the index here
        # The column the index replaces was previoiusly for a formula to counter an excel issue
        # number of chars where excel the expos the value
        ams3.to_excel(writer, sheet_name='PASTE NEW DATA HERE')


if __name__ == '__main__':
    watchdog()