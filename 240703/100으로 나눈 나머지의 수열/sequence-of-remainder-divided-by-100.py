def cal(n: int):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    return cal(n - 2) * cal(n - 1) % 100

n = int(input())
print(cal(n))