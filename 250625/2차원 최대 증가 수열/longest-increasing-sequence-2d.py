n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1
max_jump = 0

for i in range(n):
    for j in range(m):
        for k in range(i + 1, n):
            for l in range(j + 1, m):
                if arr[i][j] < arr[k][l]:
                    dp[k][l] = max(dp[k][l], dp[i][j] + 1)
        max_jump = max(dp[i][j], max_jump)

print(max_jump)

