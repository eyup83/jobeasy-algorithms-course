from itertools import zip_longest

l_keys = [1, 2, 3, 4, 5, 6, 7]
l_values = ['a', 'b', 'c', 'd', 'e', 'f']
if len(l_keys) == len(l_values):
    d_1 = zip_longest(l_keys, l_values)
    print(dict(d_1))
if len(l_keys) > len(l_values):
    d_2 = zip_longest(l_keys, l_values)
    print(dict(d_2))
if len(l_keys) < len(l_values):
    diff = len(l_values) - len(l_keys)
    l_values = l_values[:-diff]
    d_2 = zip_longest(l_keys, l_values)
    print(dict(d_2))
