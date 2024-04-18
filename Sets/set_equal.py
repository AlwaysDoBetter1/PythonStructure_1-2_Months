"""
When hiring new employees to an online school, its director tests not only the candidate’s professional
qualities, but also his memory.

The candidate is shown briefly several different numbers and then the candidate must name them. Moreover, it does
not matter in what order he remembers them, and whether he repeats them or not, the main thing is that he must name
all the numbers without adding extra ones.

Write a program to determine whether a candidate passes a memory test.

Input format
The program receives two lines of numbers as input: in the first line those shown to the candidate, and in
the second line the candidate’s answers.

Output format
The program should output YES if the candidate has passed the test and can be hired and NO otherwise.
"""

n, k = set(int(i) for i in input().split()), set(int(i) for i in input().split())
if k == n:
    print("YES")
else:
    print("NO")

# input:
# 1 2 3 4 8 5
# 1 2 8 2 3 4 5 2

# output
# YES