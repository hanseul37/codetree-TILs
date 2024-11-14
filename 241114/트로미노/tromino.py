n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

max_sum = 0
for i in range(n-1):
    for j in range(m-1):
        sum = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]
        sum -= min(arr[i][j], arr[i+1][j], arr[i][j+1], arr[i+1][j+1])
        max_sum = max(max_sum, sum)

for i in range(n):
    for j in range(1, m - 1):
        max_sum = max(max_sum, arr[i][j - 1] + arr[i][j] + arr[i][j+1])

for i in range(m):
    for j in range(1, n - 1):
        max_sum = max(max_sum, arr[j - 1][i] + arr[j][i] + arr[j + 1][i])

print(max_sum)