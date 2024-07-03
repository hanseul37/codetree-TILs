def cal(n: int):
    if n // 10 == 0:
        return n
    return cal(n // 10) + n % 10

a, b, c = list(map(int, input().split()))
print(cal(a * b * c))