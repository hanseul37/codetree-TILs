from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque([(0, 0)]) 
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
visited = [[0] * m for _ in range(n)]

ans = 0
while q:
    r, c = q.popleft()
    if r == n - 1 and c == m - 1:
        ans = arr[r][c]
        break
    for dx, dy in zip(dxs, dys):
        nx, ny = c + dx, r + dy
        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1:
            arr[ny][nx] += arr[r][c]
            q.append([ny, nx])
print(ans - 1)  