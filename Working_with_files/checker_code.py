'''
When writing your own functions, it is recommended to describe the purpose of the function,
its parameters and return value in comments. Often programmers put off writing such comments
until last, and then completely forget about them.

The input to the program is a line of text with the name of a text file in which code is written in Python.
Write a program that displays the names of all functions for which there is no explanatory comment. We will
assume that any line starting with the word def and a space is the beginning of a function definition.
The function contains a comment if the first character of the previous line is #.

Input format
The input to the program is a string of text containing the name of an existing text file with Python code.

Output format
The program should display the names of all functions (without changing their order in the source file),
each on a separate line, for which there is no explanatory comment. If all functions in the file have
an explanatory comment, then you should output: Best Programming Team.

Note 1: If the file contained the code:
# Function to calculate the powers of a given number 'a'
def powers(a):
    return a, a**2, a**3

# Function to compute the sum of all passed numbers
def sum_all(*args):
    return sum(args)

# Placeholder function for a matrix operation (currently empty)
def matrix():
    pass

# Function to return the count of passed arguments
def count_args(*args):
    return len(args)

# Function to calculate the mean (average) of passed numbers
def mean(*args):
    total = 0.0
    count = 0
    for i in args:
        if type(i) in (int, float):
            total += i
            count += 1
    if count == 0:
        return 0.0
    else:
        return total / count

# Function to greet with a provided name and optional additional greetings
def greet(name, *args):
    args = (name,) + args
    return f'Hello, {" and ".join(args)}!'

# Function to calculate the factorial of a given number 'n'
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

Then should return:
powers
matrix
mean
greet
'''

# We read one line at a time, so as not to overload the memory, we store the value of the previous line
with open(input()) as f:
    prev, without_comments = ' ', []
    for line in f:
        if line.startswith('def') and not prev.startswith('#'):
            without_comments.append(line[line.find(' ') + 1: line.find('(')])
        prev = line
    print('\n'.join(without_comments) if without_comments else 'Best Programming Team')
