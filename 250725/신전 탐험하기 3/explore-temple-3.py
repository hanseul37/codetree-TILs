n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for i in range(m):
    dp[0][i] = a[0][i]

for i in range(1, n):
    for j in range(m):
        for k in range(m):
            if j == k:
                continue
            dp[i][j] = max(dp[i - 1][k] + a[i][j], dp[i][j])

print(max(dp[-1]))