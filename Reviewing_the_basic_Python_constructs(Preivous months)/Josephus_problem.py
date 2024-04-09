"""
n people, numbered from 1 to n, stand in a circle. They begin to count, every kth person in a row leaves the circle,
after which the count continues with the next person. Write a program to determine the number of the person who will
remain in the circle last.

Input format
The input to the program is two numbers n and k, written on separate lines.

Output format
The program should output one number - the number of the person who will remain in the circle last.
"""

n = int(input())
k = int(input())

# create a list of people, where each person is simply represented by a number
people = list(range(1, n + 1))
# variable for the current position of the "counter"
cur = 0

# while we have more than one person
while len(people) > 1:
    # start counting from the current position 'cur', constantly increasing it
    for _ in range(k - 1):
        cur += 1
        # if the counter exceeds the index of the last person,
        # set it to the index of the first person
        if cur == len(people):
            cur = 0

    people.pop(cur)
    # if we remove the last person,
    # set the counter to the index of the first person
    if cur == len(people):
        cur = 0

# print the only remaining person
print(people[0])
