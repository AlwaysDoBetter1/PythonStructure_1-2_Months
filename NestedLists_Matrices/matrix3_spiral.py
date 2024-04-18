"""
Two natural numbers n and m are given as input to the program. Write a program that creates a matrix
of size n*m, filling it with a “spiral” according to the example pattern (at the bottom of the module).

Input format
The input to the program on one line is two natural numbers n and m - the number of rows and columns in the matrix.

Output format
The program should output the matrix according to the example.
"""

n, m = map(int, input().split())
l = [[0] * m for _ in range(n)]
num = 1
k = 0                                 # square level: 0 - outer, 1 - nested, and so on.
product = n * m + 1                   # extracted into a variable because n and m change in the loop

while num < product:
    for j in range(k, m):             # upper side
        l[k][j] = num
        num += 1
    for i in range(k + 1, n):         # right side
        l[i][j] = num
        num += 1
    if num == product:                # workaround for cases with small n, m
        break
    for j in range(m - 2, k - 1, -1): # lower side
        l[i][j] = num
        num += 1
    for i in range(n - 2, k, -1):     # left side
        l[i][j] = num
        num += 1
    m -= 1                            # adjust side size for the next square
    n -= 1
    k += 1

for row in l:
    for el in row:
        print(str(el).ljust(3), end='')
    print()

# example
# input1:
# 4 5
# output:
# 1  2  3  4  5
# 14 15 16 17 6
# 13 20 19 18 7
# 12 11 10 9  8