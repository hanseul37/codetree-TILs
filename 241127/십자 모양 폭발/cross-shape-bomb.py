n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

for i in range(arr[r][c]):
    if 0 <= r - i < n:
        arr[r - i][c] = 0
    if 0 <= r + i < n:
        arr[r + i][c] = 0
    if 0 <= c - i < n:
        arr[r][c - i] = 0
    if 0 <= c + i < n:
        arr[r][c + i] = 0

for i in range(n):
    for j in range(n - 1, -1, -1):
        if arr[j][i] == 0:
            for k in range(j, 0, -1):
                arr[k][i] = arr[k - 1][i]
            arr[0][i] = 0

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
