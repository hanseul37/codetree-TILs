from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
q = deque([(r1, c1, 0, 0)])
visited = [[[False] * (k + 1) for _ in range(n)]for _ in range(n)]
visited[r1][c1][0] = True
ans = -1
while q:
    r, c, cnt, wall = q.popleft()
    if r == r2 and c == c2:
        ans = cnt
        break
    for dx, dy in zip(dxs, dys):
        nx, ny = c + dx, r + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx][wall]:
            if arr[ny][nx] == 1:
                if wall < k:
                    q.append([ny, nx, cnt + 1, wall + 1])
                    visited[ny][nx][wall + 1] = True
            else:
                q.append([ny, nx, cnt + 1, wall])
                visited[ny][nx][wall] = True
print(ans)
