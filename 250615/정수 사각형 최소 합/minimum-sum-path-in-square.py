n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    arr[0][n - i - 1] += arr[0][n - i]
    arr[i][n - 1] += arr[i - 1][n - 1]

for i in range(1, n):
    for j in range(n - 2, -1, -1):
        arr[i][j] += min(arr[i][j + 1], arr[i - 1][j])

print(arr[n - 1][0]) 