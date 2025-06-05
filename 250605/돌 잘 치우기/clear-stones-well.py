from collections import deque

n, k, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

r, c = [], []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

stones = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            stones.append([i, j])

max_visit = 0          
def simul(idx, pick):
    global max_visit
    if len(pick) == m:
        for i in range(k):
            q  = deque([(r[i], c[i])])
            visited = [[False] * n for _ in range(n)]
            visited[r[i]][c[i]] = True
            cnt = 0          
            while q:
                y, x = q.popleft()
                cnt += 1
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == False:
                        if arr[ny][nx] == 1 and [ny, nx] not in pick:
                            continue
                        q.append((ny, nx))
                        visited[ny][nx] = True
            max_visit = max(max_visit, cnt)
    elif len(stones) > idx:
        pick.append(stones[idx])
        simul(idx + 1, pick)
        pick.pop()
        simul(idx + 1, pick)

simul(0, [])
print(max_visit)

