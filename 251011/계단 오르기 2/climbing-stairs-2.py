n = int(input())
arr = list(map(int, input().split()))
dp = [[-1] * 4 for _ in range(n + 1)]
dp[0][0] = 0
dp[1][1] = arr[0]

for i in range(2, n + 1):
    for j in range(4):
        if dp[i - 2][j] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + arr[i - 1])
        if j > 0 and dp[i - 1][j - 1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + arr[i - 1])
print(max(dp[n]))