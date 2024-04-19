'''
Given two complex numbers. Write a program that calculates and displays their sum, difference, and product.

Input format
The program receives two complex numbers as input, each on a separate line.

Output format
The program should output the answer to the problem.
'''

n, k = complex(input()), complex(input())
print(f'{n} + {k} =', n+k)
print(f'{n} - {k} =', n-k)
print(f'{n} * {k} =', n*k)


# input:
# 1+2j
# -2+4j
# output:
# (1+2j) + (-2+4j) = (-1+6j)
# (1+2j) - (-2+4j) = (3-2j)
# (1+2j) * (-2+4j) = (-10+0j)
