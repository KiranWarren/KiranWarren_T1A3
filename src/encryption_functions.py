# Import modules.
import string
import base64
from clear_terminal import *
from import_file import *
from export_file import *
from cryptography.fernet import Fernet


def check_password_empty(password):
    '''Helper function for password check. Will return true if password is not an empty string.'''
    if len(password) == 0:
        return False
    return True


def check_password_valid(password):
    '''Helper function for password check. Will return true if password contains valids characters.'''
    valid_chars = string.ascii_letters + string.digits
    for char in password:
        if char not in valid_chars:
            return False
    return True


def check_password_length(password):
    '''Helper function for password check. Will return true if password is 32 characters or less.'''
    if len(password) > 32:
        return False
    return True


def password_check(password):
    '''
    This function checks both the encrypting and decrypting password entered by the user.
    The password must be 1 to 32 characters in length, and must only contain ascii letters and digits.
    Once the password meets the requirements, it will be padded and base64 encoded before being returned.
    '''
    password_chars = set()
    for char in password:
        password_chars.update(char)
    # Ensure the password is valid. Request again on invalid.
    len_check = False
    char_check = False
    empty_check = False

    # Run while loop until a valid password is entered.
    while True:
        len_check = check_password_length(password)
        char_check = check_password_valid(password)
        empty_check = check_password_empty(password)
        if len_check and char_check and empty_check:
            break
        print('\nSorry, but that is not a valid password. Please input a password that is 1 to 32 characters in length, containing only letters and numbers.')
        password = input('Password: ')

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
    print("Enter a password consisting of letters and digits (a-z A-Z 0-9), and is 1 to 32 characters in length.")
    password = input("Password: ")

    # Call password_check to validate password and pad to 32 characters.
    # Password needs to be base64 encoded for Fernet parameter.
    password_key = password_check(password)

    # Create Fernet object.
    fernet_object = Fernet(password_key)

    # Encrypt text file contents.
    encrypted_string = (fernet_object.encrypt(
        input_string.encode('ascii'))).decode()

    # Get new file name from user.
    print("\nYour encrypted text file will be created in the outputs folder.")
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
    password_key = password_check(password)

    # Create fernet object
    fernet_object = Fernet(password_key)

    # Decrypt string imported from text file
    # Error handling in case of wrong password resulting in Fernet error
    try:
        output_string = (fernet_object.decrypt(
            input_string.encode('ascii'))).decode()
    except BaseException:
        print('\nYou have entered the wrong password for this file!')
        input("\nPress enter to return to the main menu.")
        return

    # Get new file name from user.
    print("\nYour decrypted text file will be created in the outputs folder.")
    new_file_name = input(
        "What would you like to name your new file (exclude file extension): ") + ".txt"

    # Call the export file function to create the output.
    export_file(output_string, new_file_name)

    # Give feedback to user that file has been successfully created.
    # Return to main menu.
    print(f"\n{new_file_name} has been successfully created!")
    input("\nPress enter to return to the main menu.")
