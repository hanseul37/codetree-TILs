def cal(n: int):
    if n // 10 == 0:
        return n * n
    return cal(n // 10) + (n % 10) * (n % 10)

n = int(input())
print(cal(n))