n = int(input())
arr = [
    [0 for i in range(200)]
    for _ in range(200)
]
for _ in range(n):
    x, y = list(map(int, input().split()))
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            arr[i + 100][j + 100] = 1

cnt = 0
for i in range(200):
    for j in range(200):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)