from collections import Counter

'''
Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same forwards
and backwards. A permutation is a rearrangement of letters.
'''


def palindromePermutation(string):
    counter = {}

    for c in string:
        if c.lower() not in counter:
            counter[c.lower()] = 0
        counter[c.lower()] += 1

    moreThanOneOdd = False
    for val in counter.values():
        if val % 2 == 1:
            moreThanOneOdd = True
        if moreThanOneOdd and val % 2 == 1:
            return False
    return True


def is_palindrome_permutation_pythonic(phrase):
    counter = Counter(phrase)
    return sum(val % 2 for val in counter.values()) <= 1


# Solution 1: use hash table to count how many times each char appears
# then iterate through hash table to ensure that no more than one char has
# an odd count
def is_permutation_of_palindrome(string):
    table = Counter(string)
    return checkMaxOneOdd(table)


def checkMaxOneOdd(counter):
    found_odd = False

    for val in counter.values():
        if val % 2 == 1:
            if found_odd:
                return False
            found_odd = True

    return True


# Solution 2: check the number of odds as we go along
def is_palindrome_permutation(phrase):
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    count_odd = 0

    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                count_odd += 1
            else:
                count_odd -= 1

    return count_odd <= 1


def char_number(c):
    a = ord('a')
    z = ord('z')
    upper_a = ord('A')
    upper_z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    if upper_a <= val <= upper_z:
        return val - upper_a
    return -1
