'''
The input to the program is a string of natural numbers. A list of numbers is formed from the elements of the string.

Write a program to sort a list of numbers in !!!non-decreasing order of the sum of their digits!!!. Moreover,
if two numbers have the same sum of digits, they should be displayed in non-decreasing order.

Input format
The input to the program is a text string containing natural numbers separated by spaces.

Output format
The program must output a sorted list of numbers in accordance with the condition of the problem, separating
its elements with one space.
'''

n = [int(i) for i in input().split()]
n.sort()
print(*sorted(n, key=lambda x: sum([int(c) for c in str(x)])))  # lambda as key of sort

# input:
# 111 14 79 7 4 123 90 45 12 171
# output:
# 12 111 4 14 123 7 45 90 171 79
