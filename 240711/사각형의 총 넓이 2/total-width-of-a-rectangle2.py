arr = [
    [0 for i in range(200)]
    for _ in range(200)
]
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i + 100][j + 100] = 1
cnt = 0
for i in range(200):
    for j in range(200):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)