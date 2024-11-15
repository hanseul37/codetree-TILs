n = int(input())
memo = [-1] * 46
def fibo(n):
    if memo[n] != -1:
        return memo[n]
    elif 0 < n < 3:
        memo[n] = 1
    else:
        memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]
print(fibo(n))