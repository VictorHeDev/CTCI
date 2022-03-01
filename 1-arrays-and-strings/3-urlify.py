'''
Write a method to replace all spaces in a string with '%20'. You may
assume that the string has sufficient space at the end to hold the
additional characters, and that you are given the "true" length of the string.
'''


'''
Solution 1: 2-scan approach
1. Count the number of spaces. Triple the number and compute how many extra
chars we will have in the final string
2. Iterate in reverse order, and edit the string. When we see a space,
replace it with %20, else replace with original char
'''


def urlify_algo(string, length):
    # convert string to list bc strings are immutable in Python
    char_list = list(string)
    new_idx = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == ' ':
            # replace spaces
            char_list[new_idx - 3: new_idx] = '%20'
            new_idx -= 3
        else:
            # move chars
            char_list[new_idx - 1] = char_list[i]
            new_idx -= 1

    return "".join(char_list[new_idx:])


def urlify_pythonic_alt(string, length):
    return string[:length].replace(" ", '%20')


def urlify_pythonic(string):
    strArr = string.split(" ")
    return '%20'.join(strArr)
