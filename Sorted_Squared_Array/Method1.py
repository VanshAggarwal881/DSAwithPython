# time complexity : O(nlogn)
def SSA(arr):
    newarr = [0]*len(arr)
    for i in range(len(arr)):
        newarr[i] = arr[i] ** 2
    
    newarr.sort()
    return newarr



arr = [-3, 1, 2, 7]
print(SSA(arr))