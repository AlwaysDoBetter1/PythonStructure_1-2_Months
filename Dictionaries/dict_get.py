"""
A line of text is given as input to the program. Write a program that prints the word that occurs least
frequently, case insensitively. If there are several such words, print the one that is smaller in lexicographical order.

Input format
A line of text is given as input to the program.

Output format
The program should display the word (in lowercase) that occurs least often.
"""

n = [i.strip('.,!?:;-') for i in input().lower().split()]
s = {}
for i in n:
    s[i] = s.get(i, 0) + 1
print(min(s, key=lambda x: (s[x], x)))

# input:
# London is the capital of Great Britain. More than six million people live in London. London lies on both
# banks of the river Thames. It is the largest city in Europe and one of the largest cities in the world. London is
# not only the capital of the country, it is also a very big port, one of the greatest commercial centres in the
# world, a university city, and the seat of the government of Great Britain!

# output:
# also

