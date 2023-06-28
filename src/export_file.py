# Export File Function
#
# The string passed to this function will be written to the target text file.
# The target text file will be created if it does not already exist, otherwise it will overwrite.

import os

def export_file(output_string, new_file_name):

    # Determine the file path.
    outputs_file_path = os.path.join(os.path.join(os.path.dirname(__file__), "outputs"), new_file_name)

    # Write contents to file.
    with open(outputs_file_path, 'w') as file:
        file.write(output_string)

def convert_list_to_string(substring_list, delimiter = " "):
    output_string = ""

    # Convert passed list back into a string
    for i in range(0, len(substring_list)):
        output_string += substring_list[i]
        try:
            if substring_list[i] != "\n" and substring_list[i + 1] != "\n":
                output_string += delimiter
        except:
            pass
    return output_string