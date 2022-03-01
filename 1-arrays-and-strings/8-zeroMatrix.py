'''
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
'''


''''
Solution 1:
- keep a second matrix to flag the zero locations
- do a second pass through the matrix to set the zeroes O(MN) space
- don't need to keep track of the exact location of the zero--just the row, col
'''


def set_zeroes(matrix):
    row = [False] * len(matrix)
    col = [False] * len(matrix[0])

    # store row and col idx with value 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True

    # nullify rows
    for i in range(len(row)):
        if row[i]:
            nullify_row(matrix, i)

    # nullify cols
    for j in range(len(col)):
        if col[j]:
            nullify_col(matrix, j)


def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


# use sets instead to keep track of visited rows and cols
# faster lookup time
def zero_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)

    for x in range(m):
        for y in range(n):
            if (x in rows) or (y in cols):
                matrix[x][y] = 0

    return matrix


def zero_matrix_pythonic(matrix):
    matrix = [["X" if x == 0 else x for x in row] for row in matrix]
    indices = []

    for idx, row in enumerate(matrix):
        if "X" in row:
            indices = indices + [i for i, j in enumerate(row) if j == "X"]
            matrix[idx] = [0] * len(matrix[0])

        matrix = [[0 if row.index(i) in indices else i for i in row] for row in matrix]

    return matrix
