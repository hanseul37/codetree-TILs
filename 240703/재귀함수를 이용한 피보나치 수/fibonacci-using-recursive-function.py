def fibo(n: int):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

n = int(input())
print(fibo(n))