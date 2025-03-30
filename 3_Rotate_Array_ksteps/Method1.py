def Rotate_Array(arr,k):
    if len(arr) == 0 or k == 0 or len(arr) == k :
        return arr
    
    k = k % len(arr)
    temp = arr[-k:]

    # now that k no. of elements is taken care of
    # reversed means : simple we take i as 0 then 1 but with reversed first 1 then 0
    for i in reversed(range(0,len(arr) - k)):
        arr[i + k] = arr[i]

    # after first for loop : [1,2,3,1,2]

    for i in range(len(temp)):
        arr[i] = temp[i]

    return arr



print(Rotate_Array([1,2,3,4,5],3))

# time complexity : O(n) and Space Complexity : O(k)