x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
order = input()

direction = 0
for i in range(len(order)):
    if order[i] == 'L':
        direction -= 1
    elif order[i] == 'R':
        direction += 1
    else:
        x += dx[direction % 4]
        y += dy[direction % 4]

print(x, y)