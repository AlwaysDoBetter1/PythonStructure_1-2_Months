'''
A lottery ticket contains 7 numbers from the range 1 to 49 (inclusive).

Write a program that uses the random module to generate 7 different random numbers for a lottery ticket.
The program should print the numbers in ascending order on one line, separated by one space character.
'''

import random
fff = set()
while len(fff) < 7:
    n = random.randint(1, 49)
    if n not in fff:
        fff.add(n)
print(*sorted(fff))