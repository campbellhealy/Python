import os

def name_changer(a):
    """
    I am using this to convert the file name of some of the music I have that the name was formatted in a way that I was not happy with

    The script should change to the directory of the folder
    Break down the original file name
    Reconstruct the file name in the way I want it
    Change the file name in the directory
    It is looped to convert all the files in the directory

    Remarked full lines were used to test the operation of the preceding change

    """
    os.chdir(
        a
    )  # Change to the directory where files are to be renamed
    # print(os.getcwd())  # To confirm the correct folder is opened

    for f in os.listdir():
        # print(f)    # 1.To confirm the files in the folder
        # print(os.path.splitext(f))   # 2. Gives a tuple of the file name split (filename, ext)
        file_name, file_ext = os.path.splitext(f)  # 3. Unpack the tuple
        file_num, file_group, file_album, file_song = file_name.split(
            "-"
        )  # 4. Splits the file name for the group, album & song name ( This is how the file I had were named)

        # 5. To remove any whitespace either end of the names
        file_num = file_num.strip().zfill(
            2
        )  # zfill ensures that the numbers are two digits to prevent reordering error (ie 1 then 10)
        file_album = file_album.strip()
        file_song = file_song.strip()

        # print(f'{file_num}-{file_album}-{file_song}{file_ext})  # 6. Used this to check the file name construction
        new_filename = f"{file_num}-{file_album}-{file_song}{file_ext}"

        os.rename(f, new_filename)  # completes the loop to rename all files in the folder


name_changer(C:/Users/User/Music/Group/AlbumOne)