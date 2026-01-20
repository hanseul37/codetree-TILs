from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
vals = sorted(set(sum(board, [])))

def check(l, r):
    if not (l <= board[0][0] <= r and l <= board[n - 1][m - 1] <= r):
        return False
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque([[0, 0]])
    while q:
        row, col = q.popleft()
        if row == n - 1 and col == m - 1:
            return True
        for dx, dy in zip(dxs, dys):
            nx, ny = col + dx, row + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and l <= board[ny][nx] <= r:
                visited[ny][nx] = True
                q.append([ny, nx])
    return False

left, min_diff = 0, 500
for right in range(len(vals)):
    while left <= right:
        if check(vals[left], vals[right]):
            min_diff = min(vals[right] - vals[left], min_diff)
            left += 1
        else:
            break
print(min_diff)