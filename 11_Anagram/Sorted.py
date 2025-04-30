''' Higher time complexity due to sorting operation : O(nlogn)'''
def Anagram(s , t):
    return sorted(s) == sorted(t)
    


s = input()
t = input()
result = Anagram(s , t)
if result == True:
    print("true")
else:
    print("false")

