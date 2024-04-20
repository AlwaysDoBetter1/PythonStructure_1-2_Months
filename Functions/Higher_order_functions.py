'''
Write a function func_apply() that takes a function and a list of values as input and returns a list
in which each value is the result of applying the passed function to the passed list.

Note 1: The code below is assuming func_apply() is written correctly
def add3(x):
    return x + 3

def mul7(x):
    return x * 7

print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))

should output:
[7, 14, 21, 28, 35, 42]
[4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6']
'''

def func_apply(function, items):
    result = []
    for item in items:
        new_item = function(item)
        result.append(new_item)

    return result