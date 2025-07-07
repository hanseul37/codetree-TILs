n = int(input())
coin = [0] + list(map(int, input().split()))
dp = [[-1] * 4 for _ in range(n + 1)]
dp[0][0] = 0
dp[1][1] = coin[1]

for i in range(2, n + 1):
    for j in range(4):
        if dp[i - 2][j] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coin[i])
        if j > 0 and dp[i - 1][j - 1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coin[i])

print(max(dp[-1]))
