def h_index(n, array):
    sort = sorted(array)
    for number in range(n):
        if (sort[number] == n - number):
            return sort[number]
        elif (sort[number] > n - number):
            return sort[number] - 1
print(h_index(5, [4,3,0,1,5]))


