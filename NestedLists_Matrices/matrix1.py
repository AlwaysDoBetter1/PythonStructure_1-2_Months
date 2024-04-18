"""
Write a program that prints the maximum element in the shaded region of a square matrix.
* * * * *
**\   /**
***\ /***
***/ \***
**/   \**
* * * * *

Input format
The input to the program is a natural number n - the number of rows and columns in the matrix,
then the elements of the matrix (integers) line by line separated by a space.

Output format
The program should print one number - the maximum element in the shaded area of the square matrix.
"""

# Take input for the size of the matrix
n = int(input())

# Initialize an empty matrix
matrix = []

# Loop to input the elements of the matrix
for _ in range(n):
    # Take input for each row and split it into a list of integers
    row = [int(i) for i in input().split()]
    # Append the row to the matrix
    matrix.append(row)

# Initialize a variable to store the largest element in the matrix
largest = matrix[0][0]

# Loop through each element in the matrix
for i in range(n):
    for j in range(n):
        # Check if the element is on one of the diagonals of the matrix
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            # If the current element is larger than the largest found so far, update the largest
            if matrix[i][j] > largest:
                largest = matrix[i][j]

# Print the largest element found in the specified diagonals
print(largest)

# example
# input:
# 4
# 0 1 4 6
# 0 0 2 5
# 0 0 0 7
# 0 0 0 0
# output:
# 7