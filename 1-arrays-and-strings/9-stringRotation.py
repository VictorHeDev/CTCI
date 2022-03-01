'''
Assumeyou have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a
rotation of sl using only one call to isSubstring (e.g.,"waterbottle" is a
rotation of"erbottlewat").
'''


'''
Solution
- What is the point of rotation?
- need to find a way to split the strings so
s1 = xy = waterbottle
s2 = yx = erbottlewat
- notice that if we double s1 into s1s1, if s2 is a substring then it'll match
'''


def is_substring(str1, str2):
    if len(str1) == len(str2) and len(str1) > 0:
        str1str1 = str1 * 2
        return str2 in str1str1
    return False
