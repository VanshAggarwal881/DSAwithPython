def Fibonacci(n):
    if n <= 1:
        return n
    
    prev = 0
    current = 1
    counter = 1
    while counter < n:
        next = prev + current
        prev = current
        current = next
        counter += 1
    return current



n = int(input())
print(Fibonacci(n))