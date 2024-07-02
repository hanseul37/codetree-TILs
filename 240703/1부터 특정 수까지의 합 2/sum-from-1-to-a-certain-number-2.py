def plus(n: int):
    if n == 1:
        return 1
    return plus(n - 1) + n

n = int(input())
print(plus(n))