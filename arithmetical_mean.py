a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_of_list = sum(a_list)
print(sum_of_list)

list_mean = sum_of_list / len(a_list)
print(list_mean)

list_below_mean = []
for i in a_list:
    if i < list_mean:
        list_below_mean.append(i)
print(list_below_mean)

