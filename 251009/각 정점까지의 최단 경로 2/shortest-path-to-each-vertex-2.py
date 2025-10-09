n, m = map(int, input().split())
arr = [[100001] * n for _ in range(n)]
for _ in range(m):
    start, end, weight = map(int, input().split())
    arr[start - 1][end - 1] = min(arr[start - 1][end - 1], weight)

for i in range(n):
    arr[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 100001:
            print(-1, end=' ')
        else:
            print(arr[i][j], end=' ')
    print() 


