arr = input().split()
n, m = int(arr[0]), int(arr[1])
list = [
    [0 for i in range(m)]
    for _ in range(n)
]
cnt = 0
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            list[j][i] = cnt
            cnt += 1
    else:
        for j in range(n):
            list[n-j-1][i] = cnt
            cnt += 1
for i in range(n):
    for j in range(m):
        print(list[i][j], end=" ")
    print()