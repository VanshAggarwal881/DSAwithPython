def MonotonicArray(arr):
    if(len(arr) == 0 or len(arr) ==1):
        return True

    first = arr[0]
    last = arr[len(arr) - 1]
    if first > last :
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                return False
    elif first == last:
        for i in range(len(arr)-1):
            if arr[i] != arr[i+1]:
                return False

    else :
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                return False
    return True


arr = [1,2,3,4,5]
arr2 = [4,3,2,1,0,-1]
arr3 = [3,3,3,3]
arr4 = [4,3,5,1] # false
print(MonotonicArray(arr3))