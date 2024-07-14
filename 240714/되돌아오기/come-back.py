n = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
direction = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

cnt = 0
find = 0
for _ in range(n):
    direct, amount = input().split()
    for _ in range(int(amount)):
        x += dx[direction[direct]]
        y += dy[direction[direct]]
        cnt += 1
        if x == 0 and y == 0:
            find = 1
            print(cnt)
            break
    if find == 1:
        break