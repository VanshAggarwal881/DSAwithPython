# Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

def Count_subarray(arr):
    count = 0
    for i in range(len(arr) - 2) : 
        first = arr[i]
        middle = arr[i+1]
        last = arr[i+2]
        if first + last == middle // 2:
            print(f"Valid subarray: [{first}, {middle}, {last}]") # if they ask to print the subarrays
            count += 1
    return count

# arr = int(map(int , input("Enter the array : ").split()))
arr = [int(x) for x in input("Enter elements of array: ").split()]
subarray = Count_subarray(arr)
print(subarray)
