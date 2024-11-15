import sys
sys.setrecursionlimit(1000000)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(x, y, k):
    visited[y][x] = 1
    cnt = 1
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < n and 0 <= new_y < n and visited[new_y][new_x] == 0 and arr[new_y][new_x] == k:
            cnt += dfs(new_x, new_y, k)
    return cnt

blocks = []

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            blocks.append(dfs(j, i, arr[i][j]))

blocks.sort(reverse=True)
cnt, max_block = 0, 0
for block in blocks:
    if block >= 4:
        cnt += 1
        max_block = max(max_block, block)

print(cnt, max_block)