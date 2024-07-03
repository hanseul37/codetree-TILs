def cal(n: int):
    if n == 1:
        return
    arr.append(n)
    if n % 2 == 0:
        return cal(n // 2)
    else:
        return cal(n // 3)

arr = []
n = int(input())
cal(n)
print(len(arr))