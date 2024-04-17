"""
Just demonstrate that None is None
"""

print(None == None)  # True
print(None == 0)  # False
print(None == False)  # False
empty = ''
print(None == empty)  # False

# function without return - always return None
def func():
    i = 1+1

print(func() == None)  # True