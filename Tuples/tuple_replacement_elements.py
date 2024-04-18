"""
Make the new_tuples variable contain a list of tuples based on the tuples list, with the last element
of each tuple replaced by the numeric value 100.
"""
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]

new_tuples = [el[:-1] + (100,) for el in tuples]
print(new_tuples)