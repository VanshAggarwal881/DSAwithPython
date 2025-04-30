def Reverse_arr(arr, start, end):
    while(start < end):
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
    return arr


def Rotate_Array(arr,k):
    if len(arr) == 0 or k == 0 or len(arr) == k :
        return arr
    
    k = k % len(arr)

    Reverse_arr(arr, 0,len(arr) - 1)
    Reverse_arr(arr, 0, k - 1)
    Reverse_arr(arr, k ,len(arr) - 1)
    return arr

print(Rotate_Array([1,2,3,4,5],3))