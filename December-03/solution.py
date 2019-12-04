def check_sorted(array):
    if (len(array) == 1):
        return True
    else:
        return array[0] <= array[1] and check_sorted(array[1:])
def decimation(array):   
    if (check_sorted(array)):
        return array
    else:
        new_length = len(array) // 2 + 1
        return decimation(array[:new_length])
print(decimation([3,4,3,2,1]))