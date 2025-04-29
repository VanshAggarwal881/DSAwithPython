# using dictionary or hash table , checking something in the dictionary is O(1)

def two_sum(arr, target):
    if len(arr) == 0 or len(arr) == 1:
        return []
    
    dict = {}
    
    for i in range(len(arr)):
        needed_val = target - arr[i]
        # check the keys present in dict , if present fetch the value of it otherwise save the index value of the array as the key of the dict and index as their value
        if needed_val in dict:
            return [i , dict[needed_val]]
        else:
            # add key (the values present at indexes) to the dict
            dict[arr[i]] = i
    return []


arr = [int(x) for x in input("nums : ").split()]
target = int(input("target : "))
print(two_sum(arr, target))