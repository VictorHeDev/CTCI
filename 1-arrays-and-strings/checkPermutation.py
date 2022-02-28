'''
Given 2 strings, write a method to decide if one is a permutation of the other
'''
from collections import Counter


def checkPermutation(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)
    counter1 == counter2
