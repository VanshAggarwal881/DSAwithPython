def max_area(arr):
    if len(arr) == 0 or len(arr) == 1 :
        return 0
    
    max_area = 0

    for i in range(len(arr) - 1):
        # -1 because next loop should not go out of range
        for j in range(i+1 , len(arr)):
            area = min(arr[i] , arr[j]) * (j-i)
            max_area = max(area , max_area)

    return max_area


arr = [3,10,5,6,8,4] # ouptut 24
print(max_area(arr))

# time complexity : O(n square)