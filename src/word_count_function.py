# Import modules.
from clear_terminal import *
from import_file import *


def word_count():
    '''
    Finds the word and character count of a user-specified .txt file.
    Output displayed in the console.
    '''
    # Clear Terminal and show function name
    clear_terminal()
    print("####################################")
    print("        WORD/CHARACTER COUNT        ")
    print("####################################\n")

    # Import text file.
    # Return to the main menu if no file was selected.
    input_string = import_file()
    if input_string is None:
        return

    # Convert the single string into a list of substrings.
    substring_list = convert_string_to_list(input_string)

    # Iterate over the substring list and calculate word/character counts.
    word_count = 0
    char_count_exc_space = 0
    newline_count = 0
    for i in range(0, len(substring_list)):
        if substring_list[i] != "\n":
            word_count += 1
            char_count_exc_space += len(substring_list[i])
        else:
            newline_count += 1
    char_count_inc_space = len(input_string) - newline_count

    # Provide user feedback on calculations
    print('\nYour text file has been analysed. The results are below.')
    print(f'Word Count: {word_count}')
    print(f'Character Count (excluding spaces): {char_count_exc_space}')
    print(f'Character Count (including spaces): {char_count_inc_space}')
    input('\nPress enter to return to the main menu.')
