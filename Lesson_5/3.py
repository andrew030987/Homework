# 3. У вас есть массив чисел, составьте из них максимальное число. Например:
# [61, 228, 9] -> 961228

lst = [61, 228, 9, 619, 9119, 0]


def get_largest_number(arr):
    str_lst = [str(i) for i in arr]
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if int(str_lst[j] + str_lst[j + 1]) < int(str_lst[j + 1] + str_lst[j]):
                str_lst[j], str_lst[j + 1] = str_lst[j + 1], str_lst[j]

    return ''.join(str_lst)


print(get_largest_number(lst))
