n, m = map(int, input().split())
arr = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    v1, v2, weight = map(int, input().split())
    arr[v1 - 1][v2 - 1] = weight

for i in range(n):
    arr[i][i] = 0
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] + arr[k][j] < arr[i][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

min_weight = float('inf')
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            min_weight = min(arr[i][j] + arr[j][i], min_weight)
print(min_weight)