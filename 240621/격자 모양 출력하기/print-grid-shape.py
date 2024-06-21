arr = list(map(int, input().split()))
n, m = arr[0], arr[1] 
ans = [
    [0 for i in range(n)]
    for _ in range(n)
]
for i in range(m):
    lis = list(map(int, input().split()))
    ans[lis[0] - 1][lis[1] - 1] = lis[0] * lis[1]
for i in range(n):
    for j in range(n):
        print(ans[i][j], end=" ")
    print()