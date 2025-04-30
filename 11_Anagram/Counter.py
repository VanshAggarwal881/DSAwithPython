from collections import Counter
def Anagram(s , t):
    return Counter(s) == Counter(t)
    


s = input()
t = input()
result = Anagram(s , t)
if result == True:
    print("true")
else:
    print("false")

