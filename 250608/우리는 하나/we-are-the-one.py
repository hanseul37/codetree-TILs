from collections import deque
n, k, u, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

max_cnt = 0
def simul(pick, idx):
    global max_cnt
    if len(pick) == k:
        q = deque(pick)
        visited = [[False] * n for _ in range(n)]
        for i in range(k):
            visited[pick[i][0]][pick[i][1]] = True
        cnt = 0
        while q:
            r, c = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = c + dx, r + dy
                if 0 <= nx < n and 0 <= ny < n and u <= abs(arr[ny][nx] - arr[r][c]) <= d and not visited[ny][nx]: 
                    q.append([ny, nx])
                    visited[ny][nx] = True
            cnt += 1
        max_cnt = max(max_cnt, cnt)
    else:
        for i in range(idx, n ** 2):
            pick.append([i // n, i % n])
            simul(pick, i + 1)
            pick.pop()

simul([], 0)
print(max_cnt)