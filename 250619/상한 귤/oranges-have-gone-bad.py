from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1] * n for _ in range(n)]
q = deque()
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            ans[i][j] = 0
            q.append([i, j, 0])
        elif arr[i][j] == 1:
            ans[i][j] = -2

while q:
    r, c, cnt = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = c + dx, r + dy
        if 0 <= nx < n and 0 <= ny < n and ans[ny][nx] == -2:
            ans[ny][nx] = cnt + 1
            q.append([ny, nx, cnt + 1])

for i in range(n):
    for j in range(n):
        print(ans[i][j], end = ' ')
    print()
