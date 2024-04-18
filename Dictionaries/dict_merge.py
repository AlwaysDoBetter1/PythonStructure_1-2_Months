'''
Write a merge() function that merges dictionaries into one common one. The function must accept
a list of dictionaries and return a dictionary, each key of which contains a set (set data type)
of unique values collected from all dictionaries of the passed list.

Note 1. The following program code:
result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])

creates a dictionary:
result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}
'''

def merge(values):
    res = {}
    for d in values:
        for k, v in d.items():
            res.setdefault(k, set()).add(v)
    return res