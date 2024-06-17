n = int(input())
ans = [
    [0 for i in range(n)]
    for _ in range(n)
]

row = n
col = n - 1
cnt = 0
while cnt < n * n:
    cnt += 1
    if col % 2 == 1:
        if row == 0:
            col -= 1
        else:
            row -= 1
    else:
        if row == n - 1:
            col -= 1
        else:
            row += 1
    ans[row][col] = cnt

for i in range(n):
    for j in range(n):
        print(ans[i][j], end = " ")
    print()