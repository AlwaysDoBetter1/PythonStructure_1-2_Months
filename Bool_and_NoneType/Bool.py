"""
Write a function func(num1, num2) that takes two natural numbers num1 and num2 as arguments and returns
True if num1 is evenly divisible by num2 and False otherwise.

The output of the program should be "divisible" (if func() returned True) and "not divisible"
(if func() returned False)
"""

# function declaration
def func(num1, num2):
    return num1 % num2

# reading data
num1, num2 = int(input()), int(input())

# calling the function
if func(num1, num2):
    print('not divisible')
else:
    print("divisible")

