# Import modules.
from clear_terminal import *
from import_file import *
import string


def occurrence():
    '''
    This function will determine the number of times a user-specified word occurs within a .txt file.
    '''
    # Clear Terminal and show function name
    clear_terminal()
    print("####################################")
    print("        WORD OCCURRENCE COUNT       ")
    print("####################################\n")

    # Import text file.
    # Return to the main menu if no file was selected.
    input_string = import_file()
    if input_string is None:
        return

    # Strip string of punctuation and enforce lowercase.
    unwanted_punctuation = string.punctuation.replace("'", "")
    stripped_string = input_string.translate(unwanted_punctuation.maketrans(
        unwanted_punctuation, len(unwanted_punctuation) * " ")).lower()

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
    user_word = input(
        '\nWhat word would you like to check the occurrences of? ')
    user_word = user_word.lower()

    # Return the count from the dictionary
    try:
        print(
            f'\nThe word "{user_word}" occurs {occur_dict[user_word]} time(s) in the txt file.')
        input("\nPress enter to return to the main menu.")
    except BaseException:
        print(f'\nThe word "{user_word}" does not occur in the txt file.')
        input("\nPress enter to return to the main menu.")
