from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dxs, dys = [-2, -1, 1, 2, 2, 1, -1, -2], [-1, -2, -2, -1, 1, 2, 2, 1]
q = deque([(r1 - 1, c1 - 1, 0)])
visited = [[False] * n for _ in range(n)]
visited[r1 - 1][c1 - 1] = True
ans = -1
while q:
    r, c, cnt = q.popleft()
    if r == r2 - 1 and c == c2 - 1:
        ans = cnt
    for dx, dy in zip(dxs, dys):
        nx, ny = c + dx, r + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
            q.append([ny, nx, cnt + 1])
            visited[ny][nx] = True
print(ans)