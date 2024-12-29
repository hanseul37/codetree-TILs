n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
beads = [[0] * n for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    beads[r - 1][c - 1] = 1

for _ in range(t):
    new_beads = [[0] * n for _ in range(n)]
    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(n):
        for j in range(n):
            if beads[i][j] == 1:
                max_value, direction = 0, -1
                for k in range(4):
                    if 0 <= i + dys[k] < n and 0 <= j + dxs[k] < n and max_value < arr[i + dys[k]][j + dxs[k]]:
                        max_value = arr[i + dys[k]][j + dxs[k]]
                        direction = k
                new_beads[i + dys[direction]][j + dxs[direction]] = 1
    for i in range(n):
        for j in range(n):
            if new_beads[i][j] != 1:
                new_beads[i][j] = 0
    beads = new_beads

cnt = 0
for i in range(n):
    for j in range(n):
        if beads[i][j] == 1:
            cnt += 1
print(cnt)