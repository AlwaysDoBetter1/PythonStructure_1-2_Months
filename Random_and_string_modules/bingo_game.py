'''
To play bingo, you need a 5*5 card containing various (unique) integers from 1 to 75 (inclusive),
with the central cell being empty (filled with the number 0).

Write a program that uses the random module to generate and display a random bingo card.

Note 1. For clarity, we recommend that you allocate exactly 3 characters for the output of each number.
To do this, use the ljust() string method.

Note 2: Example of a possible answer:
1  16 31 46 61
10 30 42 47 68
3  18 0  48 63
9  19 34 49 70
5  20 35 50 65
'''

from random import sample

numbers = sample(list(range(1, 76)), 25)
bingo = [numbers[i:i + 5] for i in range(0, 21, 5)]
bingo[2][2] = 0

for i in range(5):
    for j in range(5):
        print(str(bingo[i][j]).ljust(3), end=' ')
    print()
