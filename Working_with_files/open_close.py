'''
The input to the program is a string with the name of the text file. Write a program that
displays its contents on the screen.

Input format
The input to the program is a line of text with the name of an existing text file.

Output format
The program should output the contents of the specified file.

Note: Assume that the executable program and the specified file are in the same folder.
'''

k = open(fr"{input()}", 'r', encoding="utf-8")
l = list(map(str.strip, k.readlines()))
print(*l, sep="\n")
k.close()
