from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
points = [list(map(int, input().split())) for _ in range(k)]
visited = [[0] * n for _ in range(n)]
q = deque()
for y, x in points:
    q.append((x - 1, y - 1))
    visited[y - 1][x - 1] = 1

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and visited[new_y][new_x] == 0 and arr[new_y][new_x] == 0:
                q.append((new_x, new_y))
                visited[new_y][new_x] = 1

bfs()
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1
print(cnt)