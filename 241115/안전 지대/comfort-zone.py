n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
min_k = 100
max_area = 0

def dfs(x, y, k, visited):
    visited[y][x] = 1
    cnt = 1
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x < m and 0 <= new_y < n and visited[new_y][new_x] == 0 and arr[new_y][new_x] > k:
            cnt += dfs(new_x, new_y, k, visited)
    
    return cnt

for i in range(1, 100):
    areas = []
    visited = [[0] * m for _ in range(n)]
    for j in range(n):
        for k in range(m):
            if visited[j][k] == 0 and arr[j][k] > i:
                areas.append(dfs(k, j, i, visited))
    if len(areas) > max_area:
        max_area = len(areas)
        min_k = i

print(min_k, max_area)