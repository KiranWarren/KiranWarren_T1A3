# Import modules.
from import_file import *
from export_file import *
from clear_terminal import *
import string


def strip_punctuation(substring_list):
    unwanted_punctuation = string.punctuation.replace("'", "")
    stripped_list = []
    for i in range(0, len(substring_list)):
        stripped_list.append(
            (substring_list[i] .translate(
                unwanted_punctuation.maketrans(
                    "", "", unwanted_punctuation)) .lower()))
    return stripped_list


def replace():
    '''
    This function will replace all instances of a word with another word, both specified by the user.
    The name of the new text file will be specified by the user.
    A new list of substrings will be created and passed to the export file function.
    '''
    # Clear Terminal and show function name
    clear_terminal()
    print("####################################")
    print("            REPLACE WORD            ")
    print("####################################\n")

    # Import text file
    # Return to the main menu if no file was selected
    input_string = import_file()
    if input_string is None:
        return

    # Special case: Replace "/" with " / " so words on either side of slash do
    # not get interpreted as a single word.
    input_string = input_string.replace("/", " / ")

    # Convert the single string into a list of substrings
    substring_list = convert_string_to_list(input_string)

    # Create a copy substring list stripped of punctuation
    stripped_list = strip_punctuation(substring_list)

    # Get the replaced and replacing words from the user
    rem_word = input("What word would you like replaced? ")
    rep_word = input(
        f"What word would you like to replace '{rem_word}' with? ")
    rem_word, rep_word = rem_word.lower(), rep_word.lower()

    # Find all indices in stripped list that match with the word to be removed
    matching_indices = set()
    for i in range(0, len(stripped_list)):
        if stripped_list[i] == rem_word:
            matching_indices.add(i)

    # Replace the words at the matching indices
    replace_counter = 0
    for i in matching_indices:
        if rem_word in substring_list[i]:
            substring_list[i] = substring_list[i].replace(rem_word, rep_word)
        elif rem_word.capitalize() in substring_list[i]:
            substring_list[i] = substring_list[i].replace(
                rem_word.capitalize(), rep_word.capitalize()
            )
        elif rem_word.upper() in substring_list[i]:
            substring_list[i] = substring_list[i].replace(
                rem_word.upper(), rep_word.upper()
            )
        else:
            continue
        replace_counter += 1

    # If no changes made, return to main menu and do not output new file.
    if replace_counter == 0:
        print("\nNo replacements were made! An output text file will not be created.")
        input("Press enter to return to the main menu.")
        return

    # Give feedback to the user on the replacements made.
    # Request a new file name to call the output text file
    print(f"\n{replace_counter} replacement(s) were made!")
    print("Your new file will be created in the outputs folder.")
    new_file_name = (
        input("What would you like to name your new file (exclude file extension): ") +
        ".txt")

    # Convert the substring list back into a string in order to pass to export
    # function
    output_string = convert_list_to_string(substring_list)

    # Rectify changes made for "/" special case.
    output_string = output_string.replace(" / ", "/")

    # Call the export file function to create the output
    export_file(output_string, new_file_name)

    # Give feedback to user that file has been successfully created.
    # Return to main menu
    print(f"\n{new_file_name} has been successfully created!")
    input("\nPress enter to return to the main menu.")
