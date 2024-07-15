n, t = list(map(int, input().split()))
order = input()
arr = []
for _ in range(n):
    num = list(map(int, input().split()))
    arr.append(num)

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
x, y = n // 2, n // 2
direction = 0

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

sum = arr[y][x]
for i in range(len(order)):
    if order[i] == 'L':
        direction = (direction - 1) % 4
    elif order[i] == 'R':
        direction = (direction + 1) % 4
    else:
        if in_range(x + dx[direction], y + dy[direction], n):
            x += dx[direction]
            y += dy[direction]
            sum += arr[y][x]

print(sum)