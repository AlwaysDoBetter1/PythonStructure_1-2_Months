'''
Write a program that uses the random module to simulate coin tosses. The program takes as input the number
of attempts and displays the results of the throws: Heads or Tails (each on a separate line).
'''

import random

n = int(input())    # number of attempts
for i in range(n):
    print(["Head", "Tail"][random.randrange(0,2)])