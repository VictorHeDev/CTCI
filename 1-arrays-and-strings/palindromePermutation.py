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
