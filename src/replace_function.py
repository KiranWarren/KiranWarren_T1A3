from import_file import *
from export_file import *
from clear_terminal import *

def replace():
    # Clear Terminal and show function name
    clear_terminal()
    print("####################################")
    print("            REPLACE WORD            ")
    print("####################################")
    print('')

    # Import text file
    # Return to the main menu if no file was selected
    file_contents = import_file()
    if file_contents == None:
        return

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
        for j in range(0, len(file_contents)):
            if file_contents[j] == remove_list[i]:
                file_contents[j] = replace_list[i]
                replace_counter += 1

    # Give feedback to the user on the replacements made.
    # Request a new file name to call the output text file
    print('')
    print(f'{replace_counter} replacement(s) were made!')
    print('Your new file will be created in the outputs folder.')
    new_file_name = input('What would you like to name your new file (exclude file extension): ') + ".txt"

    # Call the export file function to create the output
    export_file(file_contents, new_file_name)

    # Give feedback to user that file has been successfully created.
    # Return to main menu
    print('')
    print(f'{new_file_name} has been successfully created!')
    input('Press enter to return to the main menu.')
