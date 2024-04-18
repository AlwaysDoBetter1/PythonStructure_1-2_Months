"""
Dict removing and iteration
"""

my_dict = {"apple": 3, "banana": 2, "orange": 5}

# Iterating through keys
print("Keys:")
for key in my_dict:
    print(key)

# Iterating through values
print("Values:")
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
print("Key-Value pairs:")
for key, value in my_dict.items():
    print(key, ":", value)

# Removing a key-value pair
del my_dict["orange"]
print("Dictionary after removing 'orange':", my_dict)

# Removing all items from the dictionary
my_dict.clear()
print("Dictionary after clearing all items:", my_dict)




