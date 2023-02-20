# main
'''
    Gather up all the csv files in a folder 'store' and combine them into a single xlsx file.
    A single worksheet per csv file.
    Name each worksheet after the file name. 
    As this uses glob the prefix in the path '\' has to be replaced as it would cause and worksheet naming error, 
    xlsxwriter.exceptions.InvalidWorksheetName
'''
import pandas as pd
import glob


def main_function():
    x = 0 # This is a counter to choose the correct file_name
    csv_files = glob.glob('store\*.{}'.format('csv')) # Create an object of all the csv files in the path folder
    csv_list = list(csv_files) # Create a list of all the csv file names in the path folder
    
    with pd.ExcelWriter('combined_csv_files.xlsx', engine = 'xlsxwriter') as writer:
        for file in csv_files:
            df_capture = pd.read_csv(file)
            file_name = (csv_list[x])[:-4]  # The -4 removes the file ext
            file_name = file_name.replace('\\','_')  # Remember the '\' is an escape character and needs to be added like this
            df_capture.to_excel(writer, sheet_name=file_name)
            x +=1


if __name__ == '__main__':
    main_function()