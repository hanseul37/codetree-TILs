from collections import deque

n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

r, c = [], []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
max_visit = 0
for i in range(k):
    q = deque([(r[i], c[i], 1, 0)])
    visited = [[[0] * (m + 2) for _ in range(n)] for _ in range(n)]
    visited[r[i]][c[i]][0] = 1
    while q:
        y, x, move, rock = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx][rock + arr[ny][nx]] == 0:
                if rock + arr[ny][nx] == m + 1:
                    max_visit = max(max_visit, move)
                else:
                    q.append((ny, nx, move + 1, rock + arr[ny][nx]))
                    visited[ny][nx][rock + arr[ny][nx]] = 1
print(max_visit)
