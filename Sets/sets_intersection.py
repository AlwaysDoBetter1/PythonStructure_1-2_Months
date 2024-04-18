"""
Write a program that determines the names of students who attended all lessons.

Input format
As input to the program in the first line, the number m is given - the number of lessons taught since
the beginning of the school year. Next there are m blocks of lines describing sheets with surnames.
The first line of each block indicates the number of surnames N, then comes N lines with the names
of those who were in the i-th lesson.

Output format
The program should display the names of students who attended all lessons, sorted in lexicographical order.
Each surname must be written on a separate line.
"""

n = int(input()) # count of lessons
result = {input() for _ in range(int(input()))} # count of names at first lesson

for _ in range(n - 1):
    result &= {input() for _ in range(int(input()))} # find names which was at first and next lessons

print(*sorted(result), sep='\n')  # output rezult

# input:
# 2
# 4
# Cherkasov
# Fokin
# Samoilov
# Ustinov
# 2
# Cherkasov
# Ustinov

# output
# Cherkasov
# Ustinov