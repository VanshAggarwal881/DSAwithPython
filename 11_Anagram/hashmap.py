# taking two hashmaps and comparing the no. of occurences of same characters in both hasmaps
#! this method takes extra space because of two hash maps
def Anagram(s , t):
    if len(s) != len(t):
        return False
    hashS , hashT = {} , {}
    for i in range(len(s)):
        # initially the key doesnot exist so hashmap can give error so to prevent the error using get function ... if not there insert 0.
        hashS[s[i]] = 1 + hashS.get(s[i] , 0)
        hashT[t[i]] = 1 + hashT.get(t[i] , 0)

    for c in hashS:
        # same error can be occured here what if the key that is present in the hashs not present in hasht , so give 0 with the help of get.
        if hashS[c] != hashT.get(c , 0):
            return False

    return True


s = input()
t = input()
result = Anagram(s , t)
if result == True:
    print("true")
else:
    print("false")

