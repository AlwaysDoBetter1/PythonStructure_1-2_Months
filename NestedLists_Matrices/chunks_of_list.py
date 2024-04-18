"""
The program receives two lines as input: one contains symbols, the other contains the number n. A list is formed from
the first line. Implement the chunked() function, which takes as input a list and a number specifying the chunk size,
and returns a list of chunks of the specified length.

Input format
The input to the program is a line of text containing characters separated by a space character and the number n on
a separate line.

Output format
The program should output the specified nested list.
"""


def chunked(symbols, n):
    # Initialize an empty list to store the result
    result = []

    # Iterate over the symbols list with a step of n
    for i in range(0, len(symbols), n):
        # Append a slice of symbols from index i to i+n to the result list
        result.append(symbols[i:i + n])

    # Return the result list containing chunked parts of the symbols list
    return result

# Read input symbols separated by spaces and split them into a list
symbols = input().split()

# Read the value of n
n = int(input())

# Call the chunked function with the input symbols list and n, then print the result
print(chunked(symbols, n))

# example
# input:
# a b c d e f
# 2
# output:
# [['a', 'b'], ['c', 'd'], ['e', 'f']]