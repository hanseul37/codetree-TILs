from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
colored = [list(map(int, input().split())) for _ in range(m)]
colored_cnt, color = 0, []
for i in range(m):
    for j in range(n):
        if colored[i][j] == 1:
            colored_cnt += 1
            color.append([i, j])

def check(d):
    y, x = color[0]
    q = deque([[y, x]])
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[False] * n for _ in range(m)]
    visited[y][x] = True
    cnt = 1
    while q:
        r, c = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = c + dx, r + dy
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and abs(board[ny][nx] - board[r][c]) <= d:
                q.append([ny, nx])
                visited[ny][nx] = True
                if colored[ny][nx] == 1:
                    cnt += 1
    return cnt == colored_cnt

left, right = 0, 10 ** 9
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)
    