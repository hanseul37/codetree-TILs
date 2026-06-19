from collections import deque

n = int(input())
grid, total, route, arr = [], [], [], [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            start_r, start_c = i, j
            total.append([i, j])
        elif line[j] == 2:
            total.append([i, j])
        arr[i][j] = [i, j]
    grid.append(line)

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
for y, x in total:
    q = deque([[y, x, 0]])
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True
    while q:
        r, c, cnt = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + c, dy + r
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and grid[ny][nx] != -1:
                q.append([ny, nx, cnt + 1])
                visited[ny][nx] = True
                if not grid[ny][nx] == 0:
                    route.append([y, x, ny, nx, cnt + 1])

def find(x):
    r, c = x
    if arr[r][c] == x: 
        return x
    arr[r][c] = find(arr[r][c])
    return arr[r][c]

def union(x, y):
    rx, cx = find(x)
    arr[rx][cx] = find(y)

route.sort(key=lambda x:x[4])
cnt, edge_cnt = 0, 0
for r1, c1, r2, c2, weight in route:
    if find([r1, c1]) != find([r2, c2]):
        union([r1, c1], [r2, c2])
        edge_cnt += 1
        cnt += weight
    if edge_cnt == len(total) - 1:
        break
if len(total) == 1 or edge_cnt == len(total) - 1:
    print(cnt)
else:
    print(-1)