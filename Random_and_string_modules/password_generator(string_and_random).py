'''
Write a program that, using the random module, generates n passwords of length m characters, consisting
of lowercase and uppercase English letters and numbers, except for those that are easy to confuse with each other:

"l" (L small);
“I” (i is big);
"1" (digit);
"o" and "O" (capital and small letters);
"0" (digit).
Additional condition: each password must contain at least one number and at least one letter in upper and lower case.

Input format
The program is given two numbers n and m, each on a separate line.

Output format
The program should output n passwords of length m characters in accordance with the problem conditions,
each on a separate line.
'''

import string
from random import choice, shuffle

chars1 = [с for с in string.ascii_uppercase if с not in 'OI']
chars2 = [с for с in string.ascii_lowercase if с not in 'ol']
chars3 = list(string.digits[2:])
chars = chars1 + chars2 + chars3

def generate_password(length):
    result = [choice(i) for i in (chars1, chars2, chars3)] + [choice(chars) for _ in range(3, length)]
    shuffle(result)
    return ''.join(result)

def generate_passwords(count, length):
    result = set()
    while len(result) < count:
        result.add(generate_password(length))
    return list(result)

for i in generate_passwords(int(input()), int(input())):
    print(i)