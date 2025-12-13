n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cnt, bomb = 0, []

def dfs(r, c, cnt):
    for dx, dy in zip(dxs, dys):
        nx, ny = c + dx, r + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and arr[r][c] == arr[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, cnt)
    bomb[cnt] += 1

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bomb.append(0)
            visited[i][j] = True
            dfs(i, j, cnt)
            cnt += 1
print(sum(1 for i in bomb if i >= 4), max(bomb))