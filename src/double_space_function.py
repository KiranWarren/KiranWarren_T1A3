# Double Space Function
#
# 

from clear_terminal import *
from import_file import *
from export_file import *

def double_space():
    # Clear Terminal and show function name
    clear_terminal()
    print("####################################")
    print("       DOUBLE-SPACE TEXT FILE       ")
    print("####################################\n")

    # Import text file.
    # Return to the main menu if no file was selected.
    input_string = import_file()
    if input_string == None:
        return
    
    # Convert the single string into a list of substrings.
    substring_list = convert_string_to_list(input_string)

    # Give confirmation to user that a new file will be created.
    print('\nYour text file contents will be double-spaced and written to a new file. The new file will created in the outputs folder.')
    new_file_name = input('What would you like to name your new file (exclude file extension): ') + ".txt"

    # Convert the substring list back into a string in order to pass to export function
    # Pass the optional delimiter argument in order to double space the contents
    output_string = convert_list_to_string(substring_list, "  ")

    # Call the export file function to create the output
    export_file(output_string, new_file_name)

    # Give feedback to user that file has been successfully created.
    # Return to main menu
    print(f'\n{new_file_name} has been successfully created!')
    input('\nPress enter to return to the main menu.')

