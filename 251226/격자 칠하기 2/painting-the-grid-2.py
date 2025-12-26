from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def check(d):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            q = deque([[i, j]])
            visited[i][j] = True
            cnt = 1
            while q:
                r, c = q.popleft()
                for dx, dy in zip(dxs, dys):
                    nx, ny = c + dx, r + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and abs(board[ny][nx] - board[r][c]) <= d:
                        q.append([ny, nx])
                        visited[ny][nx] = True
                        cnt += 1
            if cnt >= (n * n + 1) // 2:
                return True
    return False

left, right = 0, 1000000
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left) 
