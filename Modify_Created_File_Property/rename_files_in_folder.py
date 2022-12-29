'''
    - Rename a folder of files
    - Ignore sub-folders
    - Ignore other files types

     os.listdir(path='.')
        Return a list containing the names of the entries in the directory given by path. 
        The list is in arbitrary order, and does not include the special entries '.' and '..' 
        even if they are present in the directory. If a file is removed from or added to the 
        directory during the call of this function, whether a name for that file be included 
        is unspecified.
'''
from os import listdir, rename, system

folder = 'archive' # Folder path

def main_function():
    # Get a list of the csv files in the folder
    files_filtered = get_file_type_list()

    # Prepend a value to the start of each csv file as an index number
    x = 1
    for item in files_filtered:
        item_old = folder + '\\' + item
        item_new = folder + '\\' + str(x) + '_'+ item
        print(f'Original File name: {item_old}')
        print(f'New file name: {item_new}\n')
        x += 1
        rename(item_old, item_new)

    print(f'File names changed to {files_filtered}\n')
    print('Task Complete')

def get_file_type_list():
    '''
        List of a specific file type, csv, from files in a folder
        Ignore other file types and folders
    '''
    file_type = '.csv'
    files_filtered = []
    system('cls')
    # folder = input(r"Enter the path of the folder: ") # Change the folder directory
    print(f'Files in the directory: {folder}')  
    files_list = listdir(folder) # Get the items list of the folder
    # This filters by file type. As the folder is not a file type this is also removed.
    for x in files_list:
        if x.endswith(file_type):
            files_filtered.append(x)
            # print(x)
    return(files_filtered)



if __name__ == '__main__':
   main_function()
