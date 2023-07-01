# Import modules
import replace_function


def test_punc_stripping():
    '''
    This test will check that punctuation is being adequately removed from substring list.
    It should also enforced lowercase on all valid letters.
    When passed a substring list containing punctuation, it should return an expected list result.
    '''
    output = replace_function.strip_punctuation(
        ['A', 'QUICK', 'b/ro;wn', 'fox...'])
    assert output == ['a', 'quick', 'brown', 'fox']
