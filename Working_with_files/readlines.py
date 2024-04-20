'''
The input to the program is a string with the name of the text file. Write a program
that displays its penultimate line.

Input format
The input to the program is a line of text with the name of an existing text file.

Output format
The program should print the penultimate line of the specified file.

Note 1: Assume that the executable program and the specified file are in the same folder.

Note 2: The file is guaranteed to contain at least two lines.
'''

k = open(fr"{input()}", 'r', encoding="utf-8")
l = list(map(str.strip, k.readlines()))
print(l[-2])
k.close()
