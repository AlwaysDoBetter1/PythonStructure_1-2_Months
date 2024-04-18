"""
Creating dictionairy and add values
"""

# Creating a dictionary
my_dict = {"apple": 3, "banana": 2, "orange": 5}

# Printing the dictionary
print("Dictionary:", my_dict)

# Accessing value by key
print("Value for 'apple':", my_dict["apple"])

# Using get() method
print("Value for 'banana':", my_dict.get("banana"))

# Accessing non-existent key
print("Value for 'grape':", my_dict.get("grape", "Not found"))


