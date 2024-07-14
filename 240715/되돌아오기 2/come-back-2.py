x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
order = input()
direction = 0
find = False
for i in range(len(order)):
    if order[i] == 'L':
        direction = (direction - 1) % 4
    elif order[i] == 'R':
        direction = (direction + 1) % 4
    else:
        x += dx[direction]
        y += dy[direction]
    
    if x == 0 and y == 0:
        find = True
        print(i + 1)
        break

if not find:
    print(-1)