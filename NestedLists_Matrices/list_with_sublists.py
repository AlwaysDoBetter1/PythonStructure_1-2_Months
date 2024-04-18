"""
There is a list, write the code so that it displays a single number: the sum of all numbers in the list list1,
divided by the total number of all numbers.
"""

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]  # starting list
total = 0
counter: int = 0
for i in list1:
    total += sum(i)  # sum of each sublist
    counter += len(i)  # count of all elements
print(total / counter)  # average value of all element
