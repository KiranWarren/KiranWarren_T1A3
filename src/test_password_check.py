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
