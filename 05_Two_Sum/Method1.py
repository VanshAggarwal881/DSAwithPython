# Return indices of the array elements if they can sum up to the target element 
# Brute Force Method
def two_sum(arr, target):
    if len(arr) == 0 or len(arr) == 1:
        return []
    
    for i in range(len(arr) -1):
        for j in range(i+1 , len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return []


print(two_sum([2,-1,5,3] , 4))