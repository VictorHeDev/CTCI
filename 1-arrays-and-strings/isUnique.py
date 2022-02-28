'''
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''


# using a DS
def isUnique(string):
    # trivial with using a set
    return len(set(string)) == len(string)


# no additional DS brute force
def isUnique(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True


'''
SOLUTION
- create an array of boolean values, where the flag at index i indicates
whether character i in the alphabet is contained in the string
- the second time you see this character, you can immediately return False
'''


def is_unique_chars(string):
    if len(string) > 128:
        return False

    char_set = [False] * 128
    for char in string:
        # ord returns the integer that represents the unicode of char
        val = ord(char)

        # if char was already found before
        if char_set[val]:
            return False
        char_set[val] = True

    return True
