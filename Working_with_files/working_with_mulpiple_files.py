'''
The input to the program is a natural number n and n lines with file names. Write a program that creates a
file output.txt and outputs the contents of all files into it without changing their order. See Note 2
for an understanding of how the program works.

Input format
The input to the program is a natural number n and n strings of names of existing files.

Output format
The program must create a file named output.txt in accordance with the task condition.

Note 1: Assume that the executable program and the specified files are in the same folder.

Note 2: If there were 2 files as input and those files contained lines (note that there is no line break
at the end of the first file)

Early in the morning
And

we
went
for mushrooms

then the resulting output.txt file would look like this:
Early in the morningwe
went
for mushrooms
'''

with open("output.txt", "w", encoding="utf-8") as ou:
    for i in range(int(input())):
        with open(input(), "r", encoding="utf-8") as tip:
            ou.write(tip.read())
