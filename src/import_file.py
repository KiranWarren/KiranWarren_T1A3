# Import modules.
import os


def import_file():
    '''
    This function will find the .txt files available in the 'inputs' folder and display them to the user.
    The user can select which of these .txt files they would like to import for use with other functions.
    '''
    # Determine folder path of 'inputs' folder.
    # Need to use join method in case of Windows OS.
    inputs_folder_path = os.path.join(os.path.dirname(__file__), "inputs")

    # Create list of files within 'inputs' folder.
    file_list = []
    for (path, folders, files) in os.walk(inputs_folder_path):
        file_list.extend(files)

    # Remove non-.txt files from file_list.
    for i in range(0, len(file_list)):
        try:
            if file_list[i][-4:] != ".txt":
                file_list.remove(file_list[i])
        except BaseException:
            break

    # If no relevant files are in the 'inputs' folder, exit to main menu.
    if len(file_list) == 0:
        print("There are no .txt files in the 'inputs' folder. Please place a .txt file in this directory before running this application.")
        return

    # Show the user the available text files within the 'inputs' folder.
    print('Here are all the .txt files in the inputs folder:')
    for i in range(1, len(file_list) + 1):
        print(f"[{i}]   {file_list[i - 1]}")
    print('')

    # Ask the user which file they want to import.
    # Handle string error, interpret as returning to main menu.
    print('Which file would you like to choose? In the console, input the corresponding number of the file you want to import.')
    print('Or press enter to return to the main menu.')
    print('')
    try:
        file_num = int(input('File number: '))
    except BaseException:
        return

    # Exit back to the main menu if user inputs unexpected number.
    if file_num in range(1, len(file_list) + 1):
        pass
    else:
        return

    # Import the file into a usable format.
    with open(os.path.join(inputs_folder_path, file_list[file_num - 1])) as text_file:
        input_string = text_file.read()

    # Return the imported string.
    return input_string


def convert_string_to_list(input_string):
    '''
    This function will take a passed string and convert it to a list of substrings.
    '''
    # Split the text file up into a usable list.
    # Preserve newlines from document using intermediate step.
    string_lines = input_string.splitlines(True)

    # Split the contents_list up into individual words and newlines.
    # Return the words list as the output of this function.
    substring_list = []
    for i in range(0, len(string_lines)):
        substring_list.extend(string_lines[i].split())
        if i != len(string_lines) - 1:
            substring_list.extend('\n')
    return substring_list
