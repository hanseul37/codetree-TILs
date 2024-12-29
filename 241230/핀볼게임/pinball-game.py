n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
max_cnt = 0

for i in range(n):
    direction, cnt = 0, 1
    r, c = 0, i
    while 0 <= r < n and 0 <= c < n:
        if arr[r][c] == 1:
            if direction % 2 == 0:
                direction += 1
            else:
                direction -= 1
        elif arr[r][c] == 2:
            if direction % 2 == 0:
                direction = (direction + 3) % 4
            else:
                direction = (direction + 5) % 4
        r += dys[direction]
        c += dxs[direction]
        cnt += 1
    max_cnt = max(max_cnt, cnt)

for i in range(n):
    direction, cnt = 1, 1
    r, c = i, n - 1
    while 0 <= r < n and 0 <= c < n:
        if arr[r][c] == 1:
            if direction % 2 == 0:
                direction += 1
            else:
                direction -= 1
        elif arr[r][c] == 2:
            if direction % 2 == 0:
                direction = (direction + 3) % 4
            else:
                direction = (direction + 5) % 4
        r += dys[direction]
        c += dxs[direction]
        cnt += 1
    max_cnt = max(max_cnt, cnt)


for i in range(n):
    direction, cnt = 2, 1
    r, c = n - 1, i
    while 0 <= r < n and 0 <= c < n:
        if arr[r][c] == 1:
            if direction % 2 == 0:
                direction += 1
            else:
                direction -= 1
        elif arr[r][c] == 2:
            if direction % 2 == 0:
                direction = (direction + 3) % 4
            else:
                direction = (direction + 5) % 4
        r += dys[direction]
        c += dxs[direction]
        cnt += 1
    max_cnt = max(max_cnt, cnt)

for i in range(n):
    direction, cnt = 3, 1
    r, c = i, 0
    while 0 <= r < n and 0 <= c < n:
        if arr[r][c] == 1:
            if direction % 2 == 0:
                direction += 1
            else:
                direction -= 1
        elif arr[r][c] == 2:
            if direction % 2 == 0:
                direction = (direction + 3) % 4
            else:
                direction = (direction + 5) % 4
        r += dys[direction]
        c += dxs[direction]
        cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)