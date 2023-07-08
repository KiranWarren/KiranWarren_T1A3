# Import modules.
import os


def export_file(output_string, new_file_name):
    '''
    This function will take the passed output string and write it to a new text file.
    The name of the new text file is specified in the second argument.
    '''
    # Determine the file path.
    outputs_file_path = os.path.join(os.path.join(
        os.path.dirname(__file__), "outputs"), new_file_name)
    # Write contents to file.
    # Error handling in case bad file name given by user
    try:
        with open(outputs_file_path, 'w') as file:
            file.write(output_string)
    except BaseException:
        print("The file name you have entered is resulting in an error. It is likely that the characters you've included are not permitted by your OS.")


def convert_list_to_string(substring_list, delimiter=" "):
    '''
    This function will take a list of substrings and convert it into a single string.
    The substrings will be delimited by the second argument. Default value is a single space.
    '''
    output_string = ""
    # Convert passed list back into a string
    for i in range(0, len(substring_list)):
        output_string += substring_list[i]
        try:
            if substring_list[i] != "\n" and substring_list[i + 1] != "\n":
                output_string += delimiter
        except BaseException:
            pass
    return output_string
