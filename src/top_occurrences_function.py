# Top Word Occurrences Function
#
# Find the top number of word occurrences in a specified text file.
# Output displayed in console.

from clear_terminal import *
from import_file import *
import string

def top_occurrences():
    # Clear Terminal and show function name
    clear_terminal()
    print("####################################")
    print("        TOP WORD OCCURRENCES        ")
    print("####################################\n")

    # Import text file.
    # Return to the main menu if no file was selected.
    input_string = import_file()
    if input_string == None:
        return
    
    # Strip string of punctuation and enforce lowercase.
    unwanted_punctuation = string.punctuation.replace("'", "")
    stripped_string = input_string.translate(unwanted_punctuation.maketrans(unwanted_punctuation, len(unwanted_punctuation) * " ")).lower()

    # Convert the single string into a list of substrings.
    substring_list = convert_string_to_list(stripped_string)

    # Store substrings in dictionary with values as occurrence count
    occur_dict = {}
    for i in range(0, len(substring_list)):

        # Ignore newlines
        if substring_list[i] == "\n":
            continue

        # Add new words to dictionary or increase value by 1
        if substring_list[i] in occur_dict.keys():
            occur_dict[substring_list[i]] += 1
        else:
            occur_dict[substring_list[i]] = 1

    # Request how many top occurrences the user wants to see
    print('\nHow many of the top word occurrences would you like to know?')
    print('[1] Top 1')
    print('[2] Top 3')
    print('[3] Top 10')
    print('\nPlease enter the option number in the console (1 - 3). Or enter anything else to return to the main menu.')
    try:
        option = int(input('\nOption: '))
    except:
        return

    # Exit back to the main menu if user inputs an unexpected number. Get number of required top occurrences.
    if option in (1, 2, 3):
        if option == 1:
            occur_num = 1
        elif option == 2:
            occur_num = 3
        else:
            occur_num = 10
    else:
        return

    # Check the max value in the dictionary for the required amount of times. Break if occur_num > len(occur_dict).
    # Provide output to user.
    top_word = ""
    print(f'\nThe top {occur_num} word occurrences are:')
    for i in range(0, occur_num):
        try:
            top_word = max(occur_dict, key=occur_dict.get)
            print(f'[{i + 1}] {top_word} - {occur_dict[top_word]}')
            del occur_dict[top_word]
        except:
            break
    input('\nPress enter to return to the main menu.')
