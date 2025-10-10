n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 1], [1, 0]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
ans = 0

def dfs(r, c):
    global ans
    if r == n - 1 and c == m - 1:
        ans = 1
        return
    for dx, dy in zip(dxs, dys):
        nx, ny = c + dx, r + dy
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and arr[ny][nx] == 1:
            visited[ny][nx] = True
            dfs(ny, nx)

dfs(0, 0)
print(ans)