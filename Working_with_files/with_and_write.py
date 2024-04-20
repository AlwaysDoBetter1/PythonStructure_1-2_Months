'''
Write a program that writes 25 random numbers in the range from 111 to 777 (inclusive) into a text
file random.txt, each on a new line.

Input format
Nothing is supplied to the program as input.

Output format
The program must create a file named random.txt and write random numbers into it in accordance
with the problem conditions.
'''

from random import randrange
with open("random.txt", "w", encoding="utf-8") as rand:
    for i in range(25):
        print(randrange(111, 777), file=rand)
