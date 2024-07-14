n, m = list(map(int, input().split()))
arr = [
    [0] * n
    for _ in range(n)
]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n 

for _ in range(m):
    r, c = list(map(int, input().split()))
    arr[r - 1][c - 1] = 1
    cnt = 0
    for i in range(4):
        y, x = c - 1 + dy[i], r - 1 + dx[i]
        if in_range(x, y, n) and arr[x][y] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)