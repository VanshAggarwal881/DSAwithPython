def max_area(arr):
    if len(arr) == 0 or len(arr) == 1 :
        return 0
    
    max_area = 0
    i = 0
    j = len(arr) - 1

    while i !=j:
        
        area = min(arr[i] , arr[j]) * (j-i)
        max_area = max(area, max_area)
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1



    return max_area


arr = [3,10,5,6,8,4] # ouptut 24
print(max_area(arr))

# Time Complexity : O(n)