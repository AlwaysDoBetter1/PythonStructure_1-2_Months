"""
Write a program that multiplies two matrices.

Input format
The program receives two natural numbers n and m as input - the number of rows and columns in the first matrix,
then the elements of the first matrix, then an empty row. This is followed by the numbers m and k - the number of
rows and columns of the second matrix, then the elements of the second matrix.

Output format
The program should output the resulting matrix, separating elements with a space character.
"""

# Taking input for the dimensions of the first matrix (n rows, m columns)
n, m = [int(i) for i in input().split()]

# Taking input for the elements of the first matrix and storing them in a list of lists (matrix1)
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]

# For space between matrix
input()

# Taking input for the dimensions of the second matrix (m1 rows, k columns)
m1, k = [int(i) for i in input().split()]

# Taking input for the elements of the second matrix and storing them in a list of lists (matrix2)
matrix2 = [[int(i) for i in input().split()] for _ in range(m1)]

# Initializing an empty matrix (matrix3) with dimensions n x k to store the result of matrix multiplication
matrix3 = [[i for i in range(k)] for _ in range(n)]

# Performing matrix multiplication
for i in range(n):
    for j in range(k):
        s = 0
        for e in range(m):
            # Calculating the dot product of corresponding rows and columns of matrix1 and matrix2
            s += matrix1[i][e] * matrix2[e][j]
        # Assigning the calculated value to the corresponding position in matrix3
        matrix3[i][j] = s

    # Printing each row of matrix3 after the multiplication
    print(*matrix3[i])

# example
# input1:
# 4 5
# output:
# 1  2  3  4  5
# 14 15 16 17 6
# 13 20 19 18 7
# 12 11 10 9  8