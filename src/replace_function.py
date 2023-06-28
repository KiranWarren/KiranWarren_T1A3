# Replace Word Function
#
# This function will replace all instances of a word with another word, both specified by the user.
# The name of the new text file will be specified by the user.
# A new list of substrings will be created and passed to the export file function.

from import_file import *
from export_file import *
from clear_terminal import *

def replace():
    # Clear Terminal and show function name
    clear_terminal()
    print("####################################")
    print("            REPLACE WORD            ")
    print("####################################\n")

    # Import text file
    # Return to the main menu if no file was selected
    input_string = import_file()
    if input_string == None:
        return
    
    # Convert the single string into a list of substrings
    substring_list = convert_string_to_list(input_string)

    # Get string that needs to be replaced from user
    # Add additional cases, e.g. words at the start or end of a sentence.
    remove_list = []
    remove_list.append(input('What word do you want to replace? '))
    remove_list.append(remove_list[0] + '.')
    remove_list.append(remove_list[0] + '?')
    remove_list.append(remove_list[0] + '!')
    remove_list.append(remove_list[0] + '"')
    remove_list.append(remove_list[0] + '."')
    remove_list.append(remove_list[0].capitalize())
    remove_list.append('"' + remove_list[0].capitalize())
    remove_list.append('"' + remove_list[0] + '"')
    remove_list.append('"' + remove_list[0].capitalize() + '"')

    # Get replacement string from user.
    # Add corresponding special cases for the remove list
    replace_list = []
    replace_list.append(input('What word do you want to replace? '))
    replace_list.append(replace_list[0] + '.')
    replace_list.append(replace_list[0] + '?')
    replace_list.append(replace_list[0] + '!')
    replace_list.append(replace_list[0] + '"')
    replace_list.append(replace_list[0] + '."')
    replace_list.append(replace_list[0].capitalize())
    replace_list.append('"' + replace_list[0].capitalize())
    replace_list.append('"' + replace_list[0] + '"')
    replace_list.append('"' + replace_list[0].capitalize() + '"')

    # Nested loops to check all cases against all substrings from the text file contents
    # Count how many replacements were made
    replace_counter = 0
    for i in range(0, len(remove_list)):
        for j in range(0, len(substring_list)):
            if substring_list[j] == remove_list[i]:
                substring_list[j] = replace_list[i]
                replace_counter += 1
    
    # If no changes made, return to main menu and do not output new file.
    if replace_counter == 0:
        print('\nNo replacements were made! An output text file will not be created.')
        input('Press enter to return to the main menu.')
        return

    # Give feedback to the user on the replacements made.
    # Request a new file name to call the output text file
    print(f'\n{replace_counter} replacement(s) were made!')
    print('Your new file will be created in the outputs folder.')
    new_file_name = input('What would you like to name your new file (exclude file extension): ') + ".txt"

    # Convert the substring list back into a string in order to pass to export function
    output_string = convert_list_to_string(substring_list)

    # Call the export file function to create the output
    export_file(output_string, new_file_name)

    # Give feedback to user that file has been successfully created.
    # Return to main menu
    print(f'\n{new_file_name} has been successfully created!')
    input('\nPress enter to return to the main menu.')
