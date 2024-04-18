"""
A magic square of order n is a square table of size n*n, composed of all numbers 1,2,3,...,n^2
(that is, all numbers are different) so that the sums for each column, each row and each of the two diagonals are equal
between themselves. Write a program that checks whether a given square matrix is a magic square.

Input format
The input to the program is a natural number n - the number of rows and columns in the matrix, then the elements
of the matrix: n rows, n numbers in each, separated by spaces.

Output format
The program should print the word YES if the matrix is a magic square, and the word NO otherwise.
"""


def is_magic_square(n, matrix):
    # Create a list for all numbers of the correct matrix
    correct_nums = list(range(1, n ** 2 + 1))

    # Create a list for all numbers in our matrix
    our_nums = []
    for row in matrix:
        our_nums.extend(row)

    # If these lists are not equal, then our matrix does not consist of all numbers from 1 to n ** 2
    # So, we can immediately return "NO" and skip further checks
    our_nums.sort()
    if our_nums != correct_nums:
        return "NO"

    # Rows are already stored in the matrix itself
    rows = matrix.copy()

    # Create a list for all columns
    columns = []
    for j in range(n):
        cur_column = []
        for i in range(n):
            cur_column.append(matrix[i][j])

        columns.append(cur_column)

    # Create a list for diagonals (with two empty sublists)
    diagonals = [[], []]
    for i in range(n):
        diagonals[0].append(matrix[i][i])
        diagonals[1].append(matrix[i][n - 1 - i])

    # Combine all rows, columns, and diagonals into one list
    all_lines = rows + columns + diagonals

    # Initialize variables for the maximum and minimum sum among all "lines"
    # Take the sum of the first "line" as initial values
    max_sum = sum(all_lines[0])
    min_sum = sum(all_lines[0])
    for line in all_lines:
        max_sum = max(max_sum, sum(line))
        min_sum = min(min_sum, sum(line))

    # Now simply compare the maximum and minimum sums
    # They should be equal because all sums should be equal
    if max_sum != min_sum:
        return "NO"

    return "YES"


n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]

print(is_magic_square(n, matrix))

# example
# input1:
# 3
# 8 1 6
# 3 5 7
# 4 9 2
# output:
# YES
# input2
# 3
# 8 2 6
# 3 5 7
# 4 9 1
# output2
# NO