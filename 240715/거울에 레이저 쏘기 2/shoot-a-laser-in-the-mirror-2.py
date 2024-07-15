n = int(input())
arr = []
for _ in range(n):
    row = input()
    arr.append(row)
dx1, dy1 = [1, 0, -1, 0], [0, -1, 0, 1]
dx2, dy2 = [-1, 0, 1, 0], [0, 1, 0, -1]

direction = 0
k = int(input())
if 1 <= k <= n:
    r, c = 0, k -1
elif n < k <= 2 * n:
    r, c = k - n - 1, n - 1
    direction += 1
elif 2 * n < k <= 3 * n:
    r, c = n - 1, n - (k - 2 * n) 
    direction += 2
else:
    r, c = n - (k - 3 * n), 0
    direction += 3

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

cnt = 0
while(in_range(r, c, n)):
    if arr[r][c] == '\\':
        r += dy1[direction]
        c += dx1[direction]
        if direction % 2 == 0:
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
    else:
        r += dy2[direction]
        c += dx2[direction]
        if direction % 2 == 0:
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
    cnt += 1

print(cnt)