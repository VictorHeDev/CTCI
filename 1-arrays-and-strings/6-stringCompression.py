'''
Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
'''


def string_compression_brute(string):
    if len(string) == 0:
        return ''
    left = 0
    right = 0
    resArr = []

    while right < len(string):
        if string[left] != string[right]:
            letter = string[left]
            digit = right - left
            resArr.append(letter)
            if digit > 1:
                resArr.append(str(digit))

            left = right
        right += 1

    last_letter = string[left]
    last_digit = right - left
    resArr.append(last_letter)

    if last_digit > 1:
        resArr.append(str(last_digit))
    compressed_str = "".join(resArr)

    if len(compressed_str) >= len(string):
        compressed_str = string

    return compressed_str


def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last char
    if counter:
        compressed.append(string[-1] + str(counter))
    return min(string, "".join(compressed), key=len)


print(string_compression_brute('aabcccccaaa'))    # "a2b1c5a3"
print(string_compression_brute('abcdef'))         # "abcdef"
print(string_compression_brute('aabb'))           # "aabb"
print(string_compression_brute('aaa'))            # "a3"
print(string_compression_brute('a'))              # "a"
print(string_compression_brute(''))              # ""
