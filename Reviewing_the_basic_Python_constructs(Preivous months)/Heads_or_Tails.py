"""Given a string of text consisting of the letters of the Russian alphabet "O" and "P". The letter "O" corresponds
to the loss of heads, and the letter "P" to the loss of tails. Write a program that counts the greatest number of
consecutive Heads.

Input format
The input to the program is a string of text consisting of the letters of the Russian alphabet “O” and “P”.

Output format
The program should display the largest number of Tails in a row.

Note. If there are no Tails, then you need to output the number 0.
"""

a = input().split('О')
print(max(len(x) for x in a))

#example
#input
"""
ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
"""
#output
"""
31
"""
