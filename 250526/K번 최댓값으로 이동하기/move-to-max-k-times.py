from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

for _ in range(k):
    q = deque([(r, c)])
    visited = [[0] * n for _ in range(n)]
    visited[r][c] = 1
    max_value, now_value = 0, arr[r][c]
    max_r, max_c = -1, -1
    while q:
        y, x = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] < now_value and visited[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = 1
                if max_value < arr[ny][nx]:
                    max_value = arr[ny][nx]
                    max_r, max_c = ny, nx
                elif max_value == arr[ny][nx]:
                    if ny < max_r or (ny == max_r and nx < max_c):
                        max_r, max_c = ny, nx
    if max_value == 0:
        break
    r, c = max_r, max_c
print(r + 1, c + 1)


