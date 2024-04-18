"""
Given on a 10-point scale for the biology assessments of three students. Write a program that prints
the set of scores that are not found in any of the three students.
"""

s = set(int(i) for i in (input().split()))
s1 = set(int(i) for i in (input().split()))
s2 = set(int(i) for i in (input().split()))
diff = set(range(11))
print(*sorted(diff - s - s1 - s2))

# input:
# 1 5 4 2 5 6 6 2 3 3 5 2
# 2 3 5 1 2 1 2 6 7 1 1 6
# 1 4 6 8 8 7 0 6 0 3 8 1

# output
# 9 10