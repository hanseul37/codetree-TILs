n = int(input())
x, y = n // 2, n // 2
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
arr = [
    [0] * n
    for _ in range(n)
]

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def check(x, y, distance):
    return abs(x - n // 2) <= distance - 1 and abs(y - n // 2) <= distance - 1

direction = 0
distance = 1
arr[y][x] = 1
for i in range(1, n * n):
    if i == (2 * distance - 1) * (2 * distance - 1):
        distance += 1
    if not in_range(x + dx[direction], y + dy[direction], n):
        direction = (direction + 1) % 4
    elif not check(x + dx[direction], y + dy[direction], distance):
        direction = (direction + 1) % 4
    x += dx[direction]
    y += dy[direction]
    arr[y][x] = i + 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()