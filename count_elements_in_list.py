def count_nums(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [(lst[0], 1)]
    left = (lst[:len(lst) // 2])
    right = (lst[len(lst) // 2:])
    print(len(left) + len(right))


num_list = [12, 3, 5, 3, 12, 3, 8, 9, 11]

count_nums(num_list)
