"""
Write a program that reads the natural number n and prints the first n numbers of the Tribonacci sequence.

Input format
The input to the program is one number n (n≤100) – the number of members of the sequence.

Output format
The program should output the terms of the Tribonacci sequence separated by a space character.

Note. Tribonacci sequence is a sequence of natural numbers, where each subsequent number is the sum of the
three previous ones: 1,1,1,3,5,9,17,31,57,105 ...
"""

n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end = " ")
    f1, f2, f3 = f2, f3, f1 + f2 + f3