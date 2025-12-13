from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = k
q = deque()
for _ in range(k):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    q.append([r, c])
    visited[r][c] = True

while q:
    r, c = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = c + dx, r + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and arr[ny][nx] == 0:
            visited[ny][nx] = True
            q.append([ny, nx])
            cnt += 1
print(cnt)


