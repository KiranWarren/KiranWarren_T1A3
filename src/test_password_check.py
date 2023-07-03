# Import modules
import encryption_functions


def test_password():
    '''
    This test will check the padding and encoding returned by the password checking function.
    When passed a string, it should return an expected encoded data.
    '''
    intermediate_data = encryption_functions.password_check(
        "abcdefghijklmnopqrstuvwxyz")
    output = intermediate_data.decode()
    assert output == 'YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMDAwMDA='


def test_empty_password():
    '''
    This test will check the helper function associated with the password check.
    When passing an empty string, the function should return False to identify an invalid password.
    '''
    output = encryption_functions.check_password_empty("")
    assert output == False


def test_long_password():
    '''
    This test will check the helper function associated with the password check.
    When passing a string that is 33 characters long, the function should return False to identify an invalid password.
    '''
    output = encryption_functions.check_password_length(
        "111111111122222222223333333333444")
    assert output == False


def test_nonbase64_password():
    '''
    This test will check the helper function associated with the password check.
    When passing a string containing an invalid character, the function should return False to identify an invalid password.
    '''
    output = encryption_functions.check_password_valid("abcdef>")
    assert output == False
