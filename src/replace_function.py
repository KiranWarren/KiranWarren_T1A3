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
    file_contents = import_file()

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

    print(remove_list)
    print(replace_list)
    print(file_contents)

    # Nested loops to check all cases against all substrings from the text file contents
    # Count how many replacements were made
    replace_counter = 0
    for i in range(0, len(remove_list)):
        for j in range(0, len(file_contents)):
            if file_contents[j] == remove_list[i]:
                file_contents[j] = replace_list[i]
                replace_counter += 1

    print(file_contents)
    
    print('')
    print(f'{replace_counter} replacement(s) were made!')
    print('Your new file will be created in the outputs folder.')
    new_file_name = input('What would you like to name your new file (exclude file extension): ') + ".txt"

    export_file(file_contents, new_file_name)


