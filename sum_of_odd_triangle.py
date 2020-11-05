#            1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29

# row1 = 1 also 1*1*1
# row2 = 3+5 = 8 also 2*2*2
# row3 = 7+9+11 = 27 also 3*3*3


def row_sum(row_number):
    return row_number * row_number * row_number


print(row_sum(1))
print(row_sum(2))
print(row_sum(3))
print(row_sum(4))
print(row_sum(5))
