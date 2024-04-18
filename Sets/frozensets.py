"""
What is possible with frozensets
"""

# Creating a regular set
normal_set = {1, 2, 3, 4, 5}

# Creating a frozenset
frozen_set = frozenset(normal_set)

# Trying to add an element to the frozenset will raise an error
try:
    frozen_set.add(6)
except AttributeError as e:
    print("Error:", e)

# Accessing elements of the frozenset
for num in frozen_set:
    print(num)

# Operations like union, intersection, and difference can be performed on frozensets
another_frozen_set = frozenset({4, 5, 6})

# Union of two frozensets
union_set = frozen_set | another_frozen_set
print("Union set:", union_set)

# Intersection of two frozensets
intersection_set = frozen_set & another_frozen_set
print("Intersection set:", intersection_set)

# Difference of two frozensets
difference_set = frozen_set - another_frozen_set
print("Difference set:", difference_set)