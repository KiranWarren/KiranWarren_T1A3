# Import modules.
import export_file
import import_file


def test_str_to_list():
    '''
    This test will ensure that the string to list function within the import module is performing correctly.
    Passing a string should return an expected list of substrings.
    '''
    output = import_file.convert_string_to_list("Hello, how are you today?")
    assert output == ["Hello,", "how", "are", "you", "today?"]


def test_list_to_str():
    '''
    This test will check that the list to string function is performing as expected.
    Passing a list and a delimiter should return an expected string.
    '''
    output = export_file.convert_list_to_string(
        ["abc", "def,", "ghi!", "Jkl."], "-")
    assert output == "abc-def,-ghi!-Jkl."


def test_full_conversion():
    '''
    This test will ensure that standard prose is preserved when being passed through str_to_list and list_to_str functions.
    When passing a string, the same string should be returned after passing through these two functions.
    '''
    test_string = "Hello, how are you today?"
    intermediate_list = import_file.convert_string_to_list(test_string)
    output = export_file.convert_list_to_string(intermediate_list)
    assert output == test_string
