from enum import Enum

"""
Problem statement:
    Given two strings, return if the first string is lexicographically GT, LT or EQ to the second string 
Definitions:
    str1 is < str2 IFF all([ord(s1) < ord(s2) for s1, s2 in zip(str1, str2)])
    str1 is < str2 IFF all([ord(s1) > ord(s2) for s1, s2 in zip(str1, str2)])
    str1 is < str2 IFF hash(str1) == hash(str2)
"""


class CompareResult(Enum):
    GT = 1,
    LT = 2,
    EQ = 3,


def str_compare(str1, str2):
    """
    Python makes life easy for comparing strings
    The < and > signs do lexicographic comparison (using the ord() function) behind the scenes.
    This approach works for any Unicode character based on the documentation:
        https://docs.python.org/3/reference/expressions.html#value-comparisons
        https://docs.python.org/3/library/functions.html#ord
    A caveat with the way Unicode represents some characters:
        https://docs.python.org/3/reference/expressions.html#id19
    Which could be fixed using the normalize() function to make the comparison more intuitive for humans
    As such, the best solution, is the one available in the platform.
    """
    if str1 == str2:
        return CompareResult.EQ
    elif str1 < str2:
        return CompareResult.LT
    else:
        return CompareResult.GT


def str_compare_handcrafted(str1, str2):
    current_answer = CompareResult.EQ

    # Check every pair of characters in each string
    for s1, s2 in zip(str1, str2):
        # As long as they are equal, continue iterating
        if ord(s1) == ord(s2):
            continue
        # If s1 != s2, set current_answer to correct value and break
        elif ord(s1) < ord(s2):
            current_answer = CompareResult.LT
            break
        elif ord(s1) > ord(s2):
            current_answer = CompareResult.GT
            break

    # After finishing lexicographic comparison, make sure we return the correct answer if
    # the first n characters of each string match, but are of unequal length
    if current_answer is CompareResult.EQ:
        if len(str1) < len(str2):
            current_answer = CompareResult.LT
        elif len(str1) > len(str2):
            current_answer = CompareResult.GT

    return current_answer
