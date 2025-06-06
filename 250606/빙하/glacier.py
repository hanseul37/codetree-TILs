from collections import deque 

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]   
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def mark_water():
    water = [[False] * m for _ in range(n)]
    q = deque([(0, 0)])
    water[0][0] = True
    while q:
        r, c = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = c + dx, r + dy
            if 0 <= ny < n and 0 <= nx < m and not water[ny][nx] and arr[ny][nx] == 0:
                water[ny][nx] = True
                q.append((ny, nx))
    return water

cnt, time = 0, 0
while True:
    water = mark_water()
    melting = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                for dx, dy in zip(dxs, dys):
                    nx, ny = j + dx, i + dy
                    if 0 <= ny < n and 0 <= nx < m and water[ny][nx]:
                        melting.append((i, j))
                        break
    if not melting:
        break
    cnt = len(melting)
    for r, c in melting:
        arr[r][c] = 0
    time += 1
print(time, cnt)
