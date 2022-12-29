'''
    Using the filedate library to change created date.
    There appears to be a bug where the .set created value does not affect the expected change.
    The .set accessed does change the accessed and created date though, so I will use that functionality
'''

import filedate

from os import listdir, system
from os.path import getctime
from time import ctime, mktime, sleep
from datetime import datetime


folder = 'archive' # Folder path


def main_function():
    # Get a list of the txt/csv files in a folder
    files_filtered = set_file_type_get_file_list()
    
    # Modify the file created and modified date time stamp for each of the files in the list
    files_created_date_changed = created_date(files_filtered)
    # List the files that have been modified
    print(f'\nFiles that have been changed:')
    print(*files_created_date_changed, sep="\n")
    print('\nTask Complete')


def set_file_type_get_file_list():
    '''
        List of a specific file type, csv/txt, from files in a folder
        Set folder to be listed, This has been remarked out and set to a folder called archive
        State the folder being checked
    '''
    file_type = '.csv'
    # file_type = '.txt'
    files_filtered = []
    system('cls')
    print(f'Files Type to be changed will be: {file_type}\n')
    # folder = input(r"Enter the path of the folder: ") # Change the folder directory
    print(f'Files in the directory: {folder}')  
    sleep(2)

    files_list = listdir(folder) # Get the items list of the folder
    # This filters by file type. As the folder is not a file type this is also removed.
    for x in files_list:
        if x.endswith(file_type):
            files_filtered.append(x)
    return files_filtered


def created_date(files_filtered):
    accTime = set_created_dts()
    for x in files_filtered:
        file_n_path =  folder + '\\' + x
        print(file_n_path)
        print('Original Date Time Created')
        print(f'Created: {ctime(getctime(file_n_path))}')

        x_file = filedate.File(file_n_path)
        x_file.get()
        x_file.set(
            # created = "01.01.2001 12:00", # Doesn't change the created date
            modified =  datetime.today(), # Setting to the day of modifying the creation date on the files
            accessed = accTime  # This value affects the Created date and Access
        )

        sleep(1)
        print('\nModified Create Date')
        print(f'Created: {ctime(getctime(file_n_path))}')
        sleep(1)
    return files_filtered


def set_created_dts():
    # Sets the custom created at date time for the files
    input('Press Enter to choose a Date\n')
    system('cls')
    year = getyear()
    month = getmonth()
    day = getday()
    hour = 0
    minute = 0
    second = 0
    date = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    modTime = mktime(date.timetuple())
    return modTime

def getyear():
    year = int(input('Which year?\nChoose between 1970 and 2023\n'))
    if year > 2023 or year < 1970:
        print(f'Select a year between 1970 and 2023\nNot **{year}**')
        sleep(2)
        system('cls')
        getyear()
    return year

def getmonth():
    system('cls')
    month = int(input('Which month?\nChoose between 1 - 12\n'))
    if month > 12 or month < 1:
        print(f'Select a month between 1 and 12\n Not **{month}**')
        sleep(2)
        system('cls')
        getmonth()
    return month
    
    
def getday():
    system('cls')
    day = int(input('Which day? \nChoose between 1 -28\n'))
    if day > 28 or day < 1:
        print(f'Select a day between 1 and 28\n Not **{day}**')
        sleep(2)
        system('cls')
        getday()
    return day


if __name__ == '__main__':
   main_function()
