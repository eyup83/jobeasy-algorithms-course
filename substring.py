txt = input(str('enter a string: '))
pat = input(str('enter a substring: '))


def count_substr(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0

    for i in range(N - M + 1):

        j = 0
        while j < M:
            if txt[i + j] != pat[j]:
                break
            j += 1

        if j == M:
            res += 1
            j = 0
    return res


print(count_substr(pat, txt))
