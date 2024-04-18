"""
The program receives two natural numbers n and m as input—the number of rows and columns in the matrix.
Create a mult matrix of size n*m and fill it with the multiplication table using the formula mult[i][j] = i * j.

Input format
The input to the program is two numbers n and m on different lines - the number of rows and columns in the matrix.

Output format
The program should display the multiplication table, devoting exactly 3 characters to the output of each number
(to do this, use the ljust() string method).
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
# 6
# output:
# 0  0  0  0  0  0
# 0  1  2  3  4  5
# 0  2  4  6  8  10
# 0  3  6  9  12 15