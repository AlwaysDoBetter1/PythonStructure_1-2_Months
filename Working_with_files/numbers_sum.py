'''
You have access to a text file numbers.txt, each line of which can contain one or more integers
separated by one or more spaces.

Write a program that calculates the sum of the numbers in each line and displays this sum on the screen
(for each line, the sum of the numbers in that line is displayed).

Input format
Nothing is supplied to the program as input.

Output format
The program should print the sum of the numbers in each line.
'''

from functools import reduce
with open("numbers.txt", "r", encoding="utf-8") as file:
    l, e = file.readlines(), 0
    for i in l:
        print(reduce(lambda x, y: int(x)+int(y), i.split()))
