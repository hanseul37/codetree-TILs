def cal(n:int):
    if n == 0:
        return
    cal(n - 1)
    print(n, end=' ')

def re_cal(n:int):
    if n == 0:
        return
    print(n, end=' ')
    re_cal(n - 1)

n = int(input())
cal(n)
print()
re_cal(n)