arr = input().split()
n, m = int(arr[0]), int(arr[1])
cnt = 0
list = [
    [0 for _ in range(m)]
    for _ in range(n)
]
for i in range(n):
    for j in range(m):
        cnt += 1
        list[i][j] = cnt
for i in range(n):
    for j in range(m):
        print(list[i][j], end=" ")
    print()