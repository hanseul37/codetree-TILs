from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
q = deque()

def bfs(x, y):
    q.append((x, y)) 
    visited[y][x] = 1
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            if new_x == m - 1 and new_y == n - 1:
                return True
            elif 0 <= new_x < m and 0 <= new_y < n and visited[new_y][new_x] == 0 and arr[new_y][new_x] == 1:
                visited[new_y][new_x] = 1
                q.append((new_x, new_y))
    return False

if bfs(0, 0):
    print(1)
else:
    print(0)
