def move_zeros(lst):
    arr = []
    arr_zero = []
    for i in range(len(lst)):
        if lst[i] == 0:
            arr_zero.append(lst[i])
        else:
            arr.append(lst[i])
    arr_summa = arr + arr_zero
    print(arr_summa)



move_zeros([1, 0, 1, 2, 0, 1, 3])