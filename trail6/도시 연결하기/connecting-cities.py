from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys, visited = [0, 1, 0, -1], [1, 0, -1 ,0], [[False] * m for _ in range(n)]

def bfs(r, c, city_idx):
    q = deque([[r, c]])
    arr[r][c], visited[r][c] = city_idx, True
    connection = [[r, c]]
    while q:
        r, c = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = c + dx, r + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and arr[ny][nx] == 1:
                arr[ny][nx] = city_idx
                visited[ny][nx] = True
                q.append([ny, nx])
                connection.append([ny, nx])
    return connection

city_cnt, city = 0, dict()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            city_cnt += 1
            city[city_cnt] = bfs(i, j, city_cnt + 1)

edges = []
for city_idx, cities in city.items():
    for r, c in cities:
        for dx, dy in zip(dxs, dys):
            length = 0
            ny, nx = r + dy, c + dx
            while 0 <= nx < m and 0 <= ny < n:
                if arr[ny][nx] == 0:
                    length += 1
                    ny, nx = ny + dy, nx + dx
                elif arr[ny][nx] == city_idx + 1:
                    break
                else:
                    if length >= 1:
                        edges.append([city_idx + 1, arr[ny][nx], length])
                    break

edges.sort(key=lambda x:x[2])
parent = [i for i in range(city_cnt + 2)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
    
def union(x, y):
    parent[find(x)] = find(y)

cnt, edge_cnt = 0, 0
for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt += weight
        edge_cnt += 1
        if edge_cnt == city_cnt - 1:
            break

if city_cnt <= 1:
    print(0)
elif edge_cnt == city_cnt - 1:
    print(cnt)
else:
    print(-1)