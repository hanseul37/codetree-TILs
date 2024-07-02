def cal(a1:int, a2:int):
    sum = 0
    for i in range(a1 - 1, a2):
        sum += A[i]
    return sum

n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
for i in range(m):
    a1, a2 = list(map(int, input().split()))
    print(cal(a1, a2))