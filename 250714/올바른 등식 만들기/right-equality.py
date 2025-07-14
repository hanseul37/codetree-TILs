n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * 41 for _ in range(n)]
dp[0][20 + arr[0]] += 1
dp[0][20 - arr[0]] += 1

for i in range(1, n):
    for j in range(41):
        if dp[i - 1][j] != 0:
            if j - 20 + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if j - 20 - arr[i] >= -20:
                dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[-1][m + 20])

