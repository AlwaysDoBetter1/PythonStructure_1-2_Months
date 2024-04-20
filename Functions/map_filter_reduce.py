'''
Write a different variants of using map, filter, reduce
'''

from functools import reduce

# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example using map(): Squaring each number in the list
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# Example using filter(): Filtering out even numbers from the list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example using reduce(): Calculating the sum of all numbers in the list
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)
