n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k -= 1
target, found = 0, 0
for i in range(n):
    if found:
        target = i - 2
        break
    for j in range(m):
        if arr[i][k + j] != 0:
            found = 1
            break

for i in range(m):
    arr[target][k + i] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()