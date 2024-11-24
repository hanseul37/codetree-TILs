n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())
square = []
dx, dy = [[1, -1, -1, 1], [-1, 1, 1, -1]], [[-1, -1, 1, 1], [-1, -1, 1, 1]]
r -= 1
c -= 1

line = []
for i in range(m1):
    line.append(arr[r][c])
    r += dy[dir][0]
    c += dx[dir][0]
square.append(line)

line = []
for i in range(m2):
    line.append(arr[r][c])
    r += dy[dir][1]
    c += dx[dir][1]
square.append(line)

line = []
for i in range(m3):
    line.append(arr[r][c])
    r += dy[dir][2]
    c += dx[dir][2]
square.append(line)

line = []
for i in range(m4):
    line.append(arr[r][c])
    r += dy[dir][3]
    c += dx[dir][3]
square.append(line)

for i in range(m1):
    r += dy[dir][0]
    c += dx[dir][0]
    arr[r][c] = square[0][i]
for i in range(m2):
    r += dy[dir][1]
    c += dx[dir][1]
    arr[r][c] = square[1][i]
for i in range(m3):
    r += dy[dir][2]
    c += dx[dir][2]
    arr[r][c] = square[2][i]
for i in range(m4):
    r += dy[dir][3]
    c += dx[dir][3]
    arr[r][c] = square[3][i]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()