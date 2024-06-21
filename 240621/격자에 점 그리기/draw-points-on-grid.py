arr = input().split()
n, m = int(arr[0]), int(arr[1])
ans = [
    [0 for i in range(n)]
    for _ in range(n)
]
cnt = 0
for i in range(m):
    lis = list(map(int, input().split()))
    cnt += 1
    ans[lis[0] - 1][lis[1] - 1] = cnt
for i in range(n):
    for j in range(n):
        print(ans[i][j], end=" ")
    print()