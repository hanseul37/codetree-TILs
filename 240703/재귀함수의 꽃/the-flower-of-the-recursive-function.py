def cal(n:int):
    if n == 0:
        return
    print(n, end=" ")
    cal(n - 1)
    print(n, end=" ")

n = int(input())
cal(n)