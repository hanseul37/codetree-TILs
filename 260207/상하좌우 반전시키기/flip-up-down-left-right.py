n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]
cnt = 0
for i in range(1, n):
    for j in range(n):
        if arr[i - 1][j] == 0:
            for dx, dy in zip(dxs, dys):
                nx, ny = j + dx, i + dy
                if 0 <= nx < n and 0 <= ny < n:
                    arr[ny][nx] = 1 - arr[ny][nx]
            cnt += 1
for i in range(n):
    if arr[-1][i] == 0:
        cnt = -1
        break
print(cnt)

