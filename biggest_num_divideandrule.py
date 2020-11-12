import sys

sys.setrecursionlimit(1500)


def find_max_num(num_list, left, right):
    if left == right:
        return num_list[left]
    mid = (left + right) // 2
    max1 = find_max_num(num_list, left, mid)
    max2 = find_max_num(num_list, mid + 1, right)
    return max1 if max1 > max2 else max2


def main():
    num_list = [1, 5, 2, 9, 3, 7, 5, 2, 10]
    print("biggest number: ", find_max_num(num_list, 0, len(num_list) - 1))


if __name__ == "__main__":
    main()
