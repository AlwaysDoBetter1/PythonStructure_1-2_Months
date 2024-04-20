'''
Examples of using any(), all(), zip(), enumerate() functions
'''

# any
# Check if any number in the list is even
numbers = [1, 3, 5, 7, 8, 9]
print(any(num % 2 == 0 for num in numbers))  # Output: True

# all
# Check if all numbers in the list are positive
numbers = [2, 4, 6, -8, 10]
print(all(num > 0 for num in numbers))  # Output: False

# zip
# Zip two lists together
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 40]
zipped_data = zip(names, ages)
# Convert the iterator to a list of tuples
zipped_list = list(zipped_data)
print(zipped_list)
# Output: [('Alice', 30), ('Bob', 25), ('Charlie', 40)]

# enumerate
# Enumerate over a list
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 cherry
