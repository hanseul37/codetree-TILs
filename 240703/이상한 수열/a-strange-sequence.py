def cal(n: int):
    if n == 1 or n == 2:
        return n
    return cal(n // 3) + cal(n - 1)

n = int(input())
print(cal(n))