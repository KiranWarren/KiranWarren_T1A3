# Import modules.
import string
import base64
from clear_terminal import *
from import_file import *
from export_file import *
from cryptography.fernet import Fernet


def password_check(password):
    '''
    This function checks both the encrypting and decrypting password entered by the user.
    The password must be 32 characters or less, and must only contain ascii letters and digits.
    Once the password meets the requirements, it will be padded and base64 encoded before being returned.
    '''
    password_chars = set()
    for char in password:
        password_chars.update(char)
    # Ensure the password is valid. Request again on invalid.
    len_check = False
    char_check = False
    valid_chars = string.ascii_letters + string.digits
    while len_check == False and char_check == False:
        if len(password) > 32:
            password = input(
                "The password you entered is longer than 32 characters. Please try again: ")
        else:
            len_check = True
        for char in password_chars:
            if char in valid_chars:
                char_check = True
            else:
                password = input(
                    "The password you entered contains invalid characters. Please try again: ")
                password_chars = set()
                for char in password:
                    password_chars.update(char)
                break
    # Pad the remaining characters with 0s.
    # Base64 encoding required for fernet object parameter.
    password += "0" * (32 - len(password))
    password_base64_bytes = base64.b64encode(password.encode('ascii'))
    return password_base64_bytes


def encrypt():
    '''
    This function will get the contents of a .txt file.
    The user will be asked to input an encrypting password.
    The contents of the .txt file will be encrypted using Fernet.
    The encrypted contents will be stored in a new .txt file.
    '''
    # Clear Terminal and show function name.
    clear_terminal()
    print("####################################")
    print("            ENCRYPT FILE            ")
    print("####################################\n")

    # Import text file.
    # Return to the main menu if no file was selected.
    input_string = import_file()
    if input_string is None:
        return

    # Get password from user.
    print("\nThis txt file will be symmetrically encrypted with a password of your choosing.")
    print("Please record your password somewhere safe, as you will need it to decrypt your file.")
    print("Enter a password consisting of letters and digits (a-z A-Z 0-9), and is 32 characters or less.")
    password = input("Password: ")

    # Call password_check to validate password and pad to 32 characters.
    # Password needs to be base64 encoded for Fernet parameter.
    pw_key = password_check(password)

    # Create Fernet object.
    fernet_object = Fernet(pw_key)

    # Encrypt text file contents.
    encrypted_string = (fernet_object.encrypt(
        input_string.encode('ascii'))).decode()

    # Get new file name from user.
    print("Your encrypted text file will be created in the outputs folder.")
    new_file_name = input(
        "What would you like to name your new file (exclude file extension): ") + ".txt"

    # Call the export file function to create the output.
    export_file(encrypted_string, new_file_name)

    # Give feedback to user that file has been successfully created.
    # Return to main menu.
    print(f"\n{new_file_name} has been successfully created!")
    input("\nPress enter to return to the main menu.")


def decrypt():
    '''
    This function will get the contents of an encrypted .txt file.
    The user will be asked to enter the password they used to encrypt the document.
    The encrypted contents will be decrypted using Fernet.
    The decrypted contents will be written to a new .txt file.
    '''
    # Clear Terminal and show function name.
    clear_terminal()
    print("####################################")
    print("            DECRYPT FILE            ")
    print("####################################\n")

    # Import text file.
    # Return to the main menu if no file was selected.
    input_string = import_file()
    if input_string is None:
        return

    # Get decrypting password from user.
    password = input(
        'Please enter your password that you used to encrypt this file: ')

    # Call password_check to validate password and pad to 32 characters
    # Password needs to be base64 encoded for Fernet parameter
    pw_key = password_check(password)

    # Create fernet object
    fernet_object = Fernet(pw_key)

    # Decrypt string imported from text file
    output_string = (fernet_object.decrypt(
        input_string.encode('ascii'))).decode()

    # Get new file name from user.
    print("Your decrypted text file will be created in the outputs folder.")
    new_file_name = input(
        "What would you like to name your new file (exclude file extension): ") + ".txt"

    # Call the export file function to create the output.
    export_file(output_string, new_file_name)

    # Give feedback to user that file has been successfully created.
    # Return to main menu.
    print(f"\n{new_file_name} has been successfully created!")
    input("\nPress enter to return to the main menu.")
