arr = input().split()
n, m = int(arr[0]), int(arr[1])
cnt = 0
ans = [
    [0 for i in range(m)]
    for _ in range(n)
]

for i in range(m - 1 + n):
    if i + 1 <= m:
        row = 0
        col = i
    else:
        row = i - m + 1
        col = m - 1
    while col > -1:
        cnt += 1
        ans[row][col] = cnt
        row += 1
        col -= 1
        if cnt == n * m:
            break

for i in range(n):
    for j in range(m):
        print(ans[n][m], end=" ")
    print()