import sys
sys.setrecursionlimit(100000000)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    if dp[y][x] != 0:
        return dp[y][x]
    dp[y][x] = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] < arr[y][x]:
            dp[y][x] = max(dp[y][x], dfs(nx, ny) + 1)
    return dp[y][x]

max_cnt = 0
for i in range(n):
    for j in range(n):
        max_cnt = max(max_cnt, dfs(i, j))

print(max_cnt)
