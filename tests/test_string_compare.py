from string_compare import str_compare as strcmp_builtin
from string_compare import str_compare_handcrafted as strcmp_handcrafted
from string_compare import CompareResult


def test_LT():
    test_cases = [['abc', 'abd'],
                  ['abc', 'abcd'],  # unequal lengths but s1 is a subset of s2
                  ['ab<', 'ab>'],   # ASCII
                  ['ab•', 'ab◦'],   # Unicode
                  ]
    for test_case in test_cases:
        assert strcmp_builtin(test_case[0], test_case[1]) is CompareResult.LT
        assert strcmp_handcrafted(test_case[0], test_case[1]) is CompareResult.LT


def test_GT():
    test_cases = [['abd', 'abc'],
                  ['abcd', 'abc'],  # unequal lengths but s1 is a subset of s2
                  ['ab>', 'ab<'],   # ASCII
                  ['ab◦', 'ab•'],   # Unicode
                  ]
    for test_case in test_cases:
        assert strcmp_builtin(test_case[0], test_case[1]) is CompareResult.GT
        assert strcmp_handcrafted(test_case[0], test_case[1]) is CompareResult.GT


def test_EQ():
    test_cases = [['abc', 'abc'],
                  ['abcd', 'abcd'],
                  ['ab>', 'ab>'],   # ASCII
                  ['ab•', 'ab•'],   # Unicode
                  ]
    for test_case in test_cases:
        assert strcmp_builtin(test_case[0], test_case[1]) is CompareResult.EQ
        assert strcmp_handcrafted(test_case[0], test_case[1]) is CompareResult.EQ