def cal(n: int):
    if n == 1 or n == 2:
        return n
    return cal(n - 2) + n

n = int(input())
print(cal(n))