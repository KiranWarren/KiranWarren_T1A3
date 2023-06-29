import secrets
import string
from clear_terminal import *
from import_file import *
from export_file import *

def key_generator():
    key = ""
    for i in range(0, 8):
        key += secrets.choice(string.ascii_letters)
    return key


def encrypt():
    # Clear Terminal and show function name
    clear_terminal()
    print("####################################")
    print("            ENCRYPT FILE            ")
    print("####################################\n")

    # Import text file.
    # Return to the main menu if no file was selected.
    input_string = import_file()
    if input_string == None:
        return

    # Notify user of key generation
    print(
        "\nThis txt file will be symmetrically encrypted with a randomly generated key."
    )
    print(
        "Use this key in the decrypt function to turn your encrypted file back into its original form."
    )
    input("Press enter to generate your key!")

    # Generate random key and give to user
    secret_key = key_generator()
    print(f"\nYour secret key is: {secret_key}")
    input("Please record this key for later. Press enter to continue.")

    print("\nYour new file will be created in the outputs folder.")
    new_file_name = (
        input("What would you like to name your new file (exclude file extension): ")
        + ".txt"
    )

    # Encrypt the input string
    encrypted_string = ''

    # Call the export file function to create the output
    export_file(encrypted_string, new_file_name)

    # Give feedback to user that file has been successfully created.
    # Return to main menu
    print(f"\n{new_file_name} has been successfully created!")
    input("\nPress enter to return to the main menu.")
