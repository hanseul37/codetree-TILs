n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

arr[r][c] = 0
arr[r - 1][c] = 0
arr[r + 1][c] = 0
arr[r][c - 1] = 0
arr[r][c + 1] = 0

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
