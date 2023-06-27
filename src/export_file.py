# Export File Function
#
# The list passed to this function will be turned back into a string
# The string will be written to the target text file
# The target text file will be created if it does not already exist, otherwise it will overwrite.

import os

def export_file(contents_list, new_file_name):

    # Convert list back into a string
    file_contents = ""
    for i in range(0, len(contents_list)):
        file_contents += contents_list[i]
        if not contents_list[i] == "\n":
            file_contents += " "

    # Determine the file path.
    outputs_file_path = os.path.join(os.path.join(os.path.dirname(__file__), "outputs"), new_file_name)

    # Write contents to file.
    with open(outputs_file_path, 'w') as file:
        file.write(file_contents)
