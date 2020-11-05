dup_list = ["a", "b", "a", "c", "c", "d", 5, 5, 6, 'apple', 'apple']


def remove_dups(x):
    return list(dict.fromkeys(x))


print(remove_dups(dup_list))
