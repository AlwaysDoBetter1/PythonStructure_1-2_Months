"""
check if a set is a superset of another set, meaning it contains all the elements of the other set and possibly more
"""

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}

if set1 >= set2:
    print("set1 is a superset of set2")
else:
    print("set1 is not a superset of set2")

# output
# set1 is a superset of set2