'''
There are 3 types of edits that can be performed on strings: insert a
character,remove a character, or replace a character. Given two strings,
write a function to check if they are one edit (or zero edits) away
'''


def one_edit_away(str1, str2):
    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return one_edit_insert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return one_edit_insert(str2, str1)
    else:
        return False


def one_edit_replace(s1, s2):
    '''
    Replacement happens when the strings are different in only one place
    '''
    found_difference = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if found_difference:
                return False
        found_difference = True
    return True


def one_edit_insert(s1, s2):
    '''
    Insertions and Removal are essentially the same (inverse of each other)
    s2 is the longer string compared to s1
    '''
    idx1, idx2 = 0, 0
    while idx2 < len(s2) and idx1 < len(s1):
        if s1[idx1] != s2[idx2]:
            if idx1 != idx2:
                return False
            idx2 += 1
        else:
            idx1 += 1
            idx2 += 1
    return True


print(one_edit_away('pale', 'ple'))     # True
print(one_edit_away('pale', 'pale'))    # True
print(one_edit_away('pale', 'bake'))    # False
