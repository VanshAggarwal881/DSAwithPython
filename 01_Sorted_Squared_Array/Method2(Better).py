# taking two pointers and not sorting but placing into the new array accordingly

def SSA(arr):
    i = 0
    j = len(arr) -1
    newarr = [0] * len(arr)

    for k in reversed(range(len(arr))):
        sq_i = arr[i] ** 2
        sq_j = arr[j] ** 2
        if sq_i > sq_j:
            newarr[k] = sq_i
            i += 1
        else:
            newarr[k] = sq_j
            j -= 1
    return newarr
    


arr = [-3, 1, 2, 7]
print(SSA(arr))