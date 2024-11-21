n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
winds = [list(map(int, input().split())) for _ in range(q)]

def arround(y, x):
    global arr
    total, cnt = arr[y][x], 1
    if 1 <= y:
        total += arr[y - 1][x]
        cnt += 1
    if n - 1 > y:
        total += arr[y + 1][x]
        cnt += 1
    if 1 <= x:
        total += arr[y][x - 1]
        cnt += 1
    if m - 1 > x:
        total += arr[y][x + 1]
        cnt += 1
    return total // cnt


def change(r1, c1, r2, c2):
    global arr
    copy_arr = [row[:] for row in arr]
    for i in range(c2, c1, -1):
        copy_arr[r1][i] = arr[r1][i - 1]
    for i in range(r2, r1, -1):
        copy_arr[i][c2] = arr[i - 1][c2]
    for i in range(c1, c2):
        copy_arr[r2][i] = arr[r2][i + 1]
    for i in range(r1, r2):
        copy_arr[i][c1] = arr[i + 1][c1]
    arr = [row[:] for row in copy_arr]

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            copy_arr[i][j] = arround(i, j)
    arr = [row[:] for row in copy_arr]

for i in range(q):
    change(winds[i][0] - 1, winds[i][1] - 1, winds[i][2] - 1, winds[i][3] - 1)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()