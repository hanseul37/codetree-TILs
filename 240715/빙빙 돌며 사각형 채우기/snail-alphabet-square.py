n, m = list(map(int, input().split()))
x, y = -1, 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
arr = [
    [0] * m
    for _ in range(n)
]

def in_range(x, y, n, m):
    return 0 <= x < m and 0 <= y < n

direction = 0
for i in range(n * m):
    if not in_range(x + dx[direction], y + dy[direction], n, m):
        direction = (direction + 1) % 4
    elif arr[y + dy[direction]][x + dx[direction]] != 0:
        direction = (direction + 1) % 4
    x += dx[direction]
    y += dy[direction]
    arr[y][x] = chr(i % 24 + 65)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()