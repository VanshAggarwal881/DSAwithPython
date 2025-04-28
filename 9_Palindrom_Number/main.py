def Palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    s = 0
    i = x
    while i > 0:
        d = i % 10
        s = s * 10 + d
        i = i // 10

    if s == x:
        return True
    return False

num = int(input())
result = Palindrome(num)
if result == False:
    print("false")
else:
    print("true")