n = int(input())
dp = [0] * n
dp[0] = 1
dp[1] = 3
for i in range(2, n):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]
print(dp[-1] % 10007)
