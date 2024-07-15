n = int(input())
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

max_coin = 0
for i in range(n):
    for j in range(n - 2):
        if arr[i][j] + arr[i][j + 1] + arr[i][j + 2] > max_coin:
            max_coin = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
print(max_coin)