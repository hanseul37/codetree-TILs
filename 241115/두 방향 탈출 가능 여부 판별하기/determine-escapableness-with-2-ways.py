n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
flag = 0

def dfs(x, y):
    global flag
    if x == m and y == n:
        flag = 1

    dxs, dys = [0, 1], [1, 0]
    for dx, dy in zip(dxs, dys):
        new_dx = x + dx
        new_dy = y + dy

        if 0 <= new_dx < m and 0 <= new_dy < n and arr[new_dy][new_dx] == 0 and visited[new_dy][new_dx] == 0:
            visited[new_dy][new_dx] = 1
            dfs(new_dx, new_dy)

dfs(-1, 0)
print(flag)
