'''
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
'''
# using a DS
def isUnique(string):
    # trivial with using a set
    dups = set()
    for char in string:
        if char in dups:
            return False
        dups.add(char)
    return True


# no additional DS brute force
def isUnique(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True
