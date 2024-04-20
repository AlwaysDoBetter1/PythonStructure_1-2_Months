'''
Examples of anonymous functions which also known as lambda functions
'''

square = lambda x: x**2
print(square(5))  # Output: 25

addition = lambda a, b: a + b
print(addition(3, 7))  # Output: 10

is_even = lambda x: x % 2 == 0
print(is_even(6))  # Output: True

reverse_string = lambda s: s[::-1]
print(reverse_string("hello"))  # Output: "olleh"

is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("radar"))  # Output: True


