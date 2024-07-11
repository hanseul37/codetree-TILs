n = int(input())
arr = [
    [0 for i in range(200)]
    for _ in range(200)
]
for i in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    if i % 2 == 0:
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr[j + 100][k + 100] = 1
    else:
        for j in range(x1, x2):
            for k in range(y1, y2):
                arr[j + 100][k + 100] = 2

cnt = 0
for i in range(200):
    for j in range(200):
        if arr[i][j] == 2:
            cnt += 1

print(cnt)