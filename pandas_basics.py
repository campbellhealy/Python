# pandas_basics
'''
    Some basic functions to play with the AMS report
    I used a folder 'ams' to hold the ams.csv file
    The functions are written to only use the latest file in that folder - see glob & getctime
    system was added to clear the console for each function test
    Sometimes it was easier to output to_excel to see the result from the function
'''

import pandas as pd
import glob

from os.path import getctime
from os import system


def number_isam_in_report():
    ''' Get the total of unique ISAM in the AMS report'''
    system('cls')
    latest_file = max(glob.glob(r'ams\*csv'), key=getctime)
    df = pd.read_csv(latest_file)
    df = df.iin_isam_id

    # Count the unique ISAM ID in the df
    # unique_rows = len(df) - df.duplicated(keep=False).sum()
    unique_rows = len(df.drop_duplicates(keep=False))
    print(unique_rows)


def isam_with_processes():
    ''' Get number of processes pending for each ISAM'''
    system('cls')
    latest_file = max(glob.glob(r'ams\*csv'), key=getctime)
    df = pd.read_csv(latest_file)
    df = df[['iin_isam_id', 'process_id']] # Drop other columns
    df = df.groupby('iin_isam_id').count() # Count the Process ID for each ISAM
    df.index.names = ['ISAM ID'] # Rename the Index column
    df = df.rename(columns={'process_id': 'Processes'}) # Rename other column
    # df.to_excel('out.xlsx', index=True)
    print(df)


def isam_with_frames():
    '''GEt the number of pending frames for each ISAM'''
    system('cls')
    latest_file = max(glob.glob(r'ams\*csv'), key=getctime)
    df = pd.read_csv(latest_file)
    df = df[['iin_isam_id', 'pending']] # Drop other columns
    df = df.groupby('iin_isam_id').sum() # Count the pending frames for each ISAM
    df.index.names = ['ISAM ID'] # Rename the Index column
    df = df.rename(columns={'pending': 'Pending Frames'}) # Rename other column
    # df.to_excel('out.xlsx', index=True)
    print(df)


def greater_than_x_processes():
    ''' Get the ISAM with more than X processes'''
    system('cls')
    greater_than = 10
    latest_file = max(glob.glob(r'ams\*csv'), key=getctime)
    df = pd.read_csv(latest_file)
    df = df[['iin_isam_id', 'process_id']] # Drop other columns
    df = df.groupby('iin_isam_id').count() # Count the Process ID for each ISAM
    df.index.names = ['ISAM ID'] # Rename the Index column
    df = df.rename(columns={'process_id': 'Processes'}) # Rename other column
    df = df[df.Processes > greater_than]
    print(df)


def greater_than_x_frames():
    ''''Get the ISAM with more than X pending frames'''
    system('cls')
    greater_than = 200
    latest_file = max(glob.glob(r'ams\*csv'), key=getctime)
    df = pd.read_csv(latest_file)
    df = df[['iin_isam_id', 'pending']] # Drop other columns
    df = df.groupby('iin_isam_id').sum() # Count the Process ID for each ISAM
    df.index.names = ['ISAM ID'] # Rename the Index column
    df = df.rename(columns={'pending': 'Pending Frames'}) # Rename other column
    df = df[df['Pending Frames'] > greater_than]
    print(df)


def less_than_x_processes():
    '''Get the ISAM with less than X processes'''
    system('cls')
    less_than = 10
    latest_file = max(glob.glob(r'ams\*csv'), key=getctime)
    df = pd.read_csv(latest_file)
    df = df[['iin_isam_id', 'process_id']] # Drop other columns
    df = df.groupby('iin_isam_id').count() # Count the Process ID for each ISAM
    df.index.names = ['ISAM ID'] # Rename the Index column
    df = df.rename(columns={'process_id': 'Processes'}) # Rename other column
    df = df[df.Processes < less_than]
    print(df)


def less_than_x_frames():
    ''' Get the ISAM with less than X frames'''
    system('cls')
    less_than = 200
    latest_file = max(glob.glob(r'ams\*csv'), key=getctime)
    df = pd.read_csv(latest_file)
    df = df[['iin_isam_id', 'pending']] # Drop other columns
    df.index.names = ['ISAM ID'] # Rename the Index column
    df = df.groupby('iin_isam_id').sum() # Count the Process ID for each ISAM
    df = df.rename(columns={'pending': 'Pending Frames'}) # Rename other column
    df = df[df['Pending Frames'] < less_than]
    print(df)


def count_isam_by_processid():
    '''Get the number of ISAM per Process ID'''
    df = pd.read_csv(latest_file)
    system('cls')
    latest_file = max(glob.glob(r'ams\*csv'), key=getctime)
    df['process_id'] = df['process_id'].map(str) # Change to string to remove thousands comma
    df = df.process_id.value_counts() # Count the entries for each Process ID
    df = df.to_frame() # Change back to a df
    df.index.names = ['Process ID'] # Rename the Index column
    df = df.rename(columns={'process_id': 'ISAM Count'}) # Rename other column
    df = df.sort_values(by=['ISAM Count'], ascending=False) # Sort by ISAM Count highest to lowest
    df.to_excel('out.xlsx')
    print(df)


# number_isam_in_report()
# isam_with_processes()
# isam_with_frames()
# greater_than_x_processes()
# greater_than_x_frames()
# less_than_x_processes()
# less_than_x_frames()
# count_isam_by_processid()