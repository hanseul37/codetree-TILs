x, y = 0, 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
direction = ['W', 'S', 'N', 'E']
n = int(input())
for _ in range(n):
    direct, amount = input().split()
    x, y = x + dx[direction.index(direct)] * int(amount), y + dy[direction.index(direct)] * int(amount)
print(x, y)