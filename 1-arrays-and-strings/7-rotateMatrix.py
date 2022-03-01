'''
Given an image represented by an NxN matrix, where each pixel in the image
is 4 bytes, write a method to rotate the image by 90 degrees. Can you do
this in place?
'''


'''
How do we implement this swap?
- implement the swap index by index
- perform swap on each layer, starting from the outermost layer and working
our way inwards (or start inwards and work outwards)
'''


def rotate_matrix(matrix):
    '''rotate matrix 90 degrees'''
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # top -> right
            matrix[i][-layer - 1] = top

    return matrix


def rotate_matrix_pythonic(matrix):
    n = len(matrix)
    res = [[0] * n for i in range(n)]   # empty list of 0's

    # i counts up, j counts down
    for i, j in zip(range(n), range(n - 1, -1, -1)):
        for k in range(n):
            res[k][i] = matrix[j][k]

    return res


def rotate_matrix_pythonic_alt(matrix):
    return [list(reversed(row)) for row in zip(*matrix)]
