def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)

n = int(input())
print(Fibonacci(n))