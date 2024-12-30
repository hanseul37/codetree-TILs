n, m, r, c = map(int, input().split())
r -= 1
c -= 1
directions = list(input().split())
arr = [[0] * n for _ in range(n)]

top, front, right = 1, 2, 3
arr[r][c] = 7 - top
for i in range(m):
    if directions[i] == 'L' and 0 <= c - 1:
        temp = top
        top = right
        right = 7 - temp
        c -= 1
    elif directions[i] == 'R' and c + 1 < n:
        temp = top
        top = 7 - right
        right = temp
        c += 1
    elif directions[i] == 'U' and 0 <= r - 1:
        temp = top
        top = front
        front = 7 - temp
        r -= 1
    elif directions[i] == 'D' and r + 1 < n:
        temp = top
        top = 7 - front
        front = temp
        r += 1
    arr[r][c] = 7 - top

cnt = 0
for i in range(n):
    for j in range(n):
        cnt += arr[i][j]
print(cnt)