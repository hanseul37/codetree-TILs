from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
q = deque([(0, 0, 0)])
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
ans = -1

while q:
    r, c, cnt = q.popleft()
    if r == n - 1 and c == m - 1:
        ans = cnt
        break
    for dx, dy in zip(dxs, dys):
        nx, ny = c + dx, r + dy
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and arr[ny][nx] == 1:
            visited[ny][nx] = True
            q.append([ny, nx, cnt + 1])

print(ans)