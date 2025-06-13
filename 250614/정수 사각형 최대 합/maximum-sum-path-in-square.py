n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    arr[i][0] += arr[i - 1][0]
    arr[0][i] += arr[0][i - 1]

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] += max(arr[i - 1][j], arr[i][j - 1])

print(arr[-1][-1])
