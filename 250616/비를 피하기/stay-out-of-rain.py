from collections import deque

n, h, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * n for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            q = deque([(i, j, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[i][j] = True
            while q:
                r, c, cnt = q.popleft()
                if arr[r][c] == 3:
                    ans[i][j] = cnt
                    break
                for dx, dy in zip(dxs, dys):
                    nx, ny = c + dx, r + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and arr[ny][nx] != 1:
                        q.append([ny, nx, cnt + 1])
                        visited[ny][nx] = True
            if ans[i][j] == 0:
                ans[i][j] = -1

for i in range(n):
    for j in range(n):
        print(ans[i][j], end=' ')
    print()