from collections import Counter
'''
Given 2 strings, write a method to decide if one is a permutation of the other

EDGE CASES
- case sensitive?
- is whitespace significant?

OPTIMIZATIONS
- strings of different lengths cannot be permutations of each other
'''


# Solution 1: Sort the strings
def check_permutations_sort(str1, str2):
    if len(str1) != len(str2):
        return False
    sorted1, sorted2 = sorted(str1), sorted(str2)

    for i in range(len(sorted1)):
        if sorted1[i] != sorted2[i]:
            return False

    return True


# Solution 2: Check for identical character counts
def check_permutations_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for char in str1:
        counter[ord(char)] += 1
    for char in str2:
        if counter[ord(char)] == 0:
            return False
        counter[ord(char)] -= 1

    return True


# Solution 3: Python
def check_permutations_pythonic(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    return counter1 == counter2
