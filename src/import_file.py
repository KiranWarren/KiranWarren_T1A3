# Import File Function
#
# Identifies the text files that are within the 'inputs' folder.
# Requests the user choose one of these files to import.
# Returns a list with all of the words and newlines from the text file.

import os

def import_file():
    # Determine folder path of 'inputs' folder.
    # Need to use join method in case of Windows OS.
    inputs_folder_path = os.path.join(os.path.dirname(__file__), "inputs")

    # Create list of files within 'inputs' folder.
    file_list = []
    for (path, folders, files) in os.walk(inputs_folder_path):
        file_list.extend(files)

    # Remove non-.txt files from file_list
    for i in range(0, len(file_list)):
        if file_list[i][-4:] != ".txt":
            file_list.remove(file_list[i])
    
    # If no relevant files are in the 'inputs' folder, exit to main menu.
    if len(file_list) == 0:
        print("There are no .txt files in the 'inputs' folder. Please place a .txt file in this directory before running this application.")
        return

    # Show the user the available text files within the 'inputs' folder.
    print('Here are all the .txt files in the inputs folder:')
    for i in range(1, len(file_list) + 1):
        print(f"{i}     {file_list[i - 1]}")
    print('')

    # Ask the user which file they want to import.
    # Handle empty string error, interpret as returning to main menu
    print('Which file would you like to choose? In the console, input the corresponding number of the file you want to import.')
    print('Or press enter to return to the main menu.')
    print('')
    try:
        file_num = int(input('File number: '))
    except:
        return

    # Exit back to the main menu if user inputs 0
    if file_num in range(1, len(file_list) + 1):
        pass
    else:
        return

    # Import the file into a usable format
    with open(os.path.join(inputs_folder_path, file_list[file_num - 1])) as text_file:
        text_file_contents = text_file.read()

    # Split the text file up into a usable list.
    # Preserve newlines from document using intermediate step
    contents_lines = text_file_contents.splitlines(True)

    # Split the contents_list up into individual words and newlines
    # Return the words list as the output of this function
    words = []
    for i in range(0, len(contents_lines)):
        words.extend(contents_lines[i].split())
        if i != len(contents_lines) - 1:
            words.extend('\n')
    return words


    

