"""
Write a program to decipher a secret word using frequency analysis.

Input format
The first line contains the encrypted word. The second line contains one integer n – the number
of letters in the dictionary. The next n lines record how many times a specific letter of the
alphabet appears in this word - <letter>: <frequency>.

Output format
The program should output the decrypted word.
"""

# Take input from the user
n = input()

# Initialize an empty dictionary
dic = {}

# Count the occurrence of each character in the input string and store it in the dictionary
for i in n:
    # If the character already exists in the dictionary, increment its count by 1
    # If not, set its count to 1
    dic[i] = dic.setdefault(i, 0) + 1

# Take input for the number of replacements to be made
for _ in range(int(input())):
    # Take input for the replacement in the format 'k: m'
    k, m = input().split(': ')
    # Iterate through the dictionary
    for i in dic:
        # If the count of a character matches 'm', replace it with 'k'
        if dic[i] == int(m):
            dic[i] = k

# Reconstruct the original string with replacements
for j in n:
    # Print the replaced character from the dictionary
    print(dic[j], end="")


# input:
# *!*!*?
# 3
# а: 3
# н: 2
# с: 1

# output:
# ананас




