'''
There are 3 types of edits that can be performed on strings: insert a
character,remove a character, or replace a character. Given two strings,
write a function to check if they are one edit (or zero edits) away
'''


def oneAway(str1, str2):
    if str1 == str2:
        return True
    set1 = set(str1)
    set2 = set(str2)

    return abs(len(set1) - len(set2)) <= 1


print(oneAway('pale', 'ple'))
print(oneAway('pale', 'pale'))
print(oneAway('pale', 'bake'))
