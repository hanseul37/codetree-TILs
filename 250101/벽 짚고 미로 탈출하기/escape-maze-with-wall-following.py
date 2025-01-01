n = int(input())
x, y = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]
x -= 1
y -= 1
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
time, direction = 0, 0
visited = set()

while True:
    if not (0 <= x < n and 0 <= y < n):
        print(time)
        break
    if (x, y, direction) in visited:
        print(-1)
        break

    visited.add((x, y, direction))
    rx, ry = x + dxs[(direction + 1) % 4], y + dys[(direction + 1) % 4]
    
    if 0 <= rx < n and 0 <= ry < n and arr[ry][rx] == '#':
        nx, ny = x + dxs[direction], y + dys[direction]
        if 0 <= x + dxs[direction] < n and 0 <= y + dys[direction] < n and arr[y + dys[direction]][x + dxs[direction]] != '#':
            x, y = x + dxs[direction], y + dys[direction]
            time += 1
        else:
            direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
        x, y = x + dxs[direction], y + dys[direction]
        time += 1
