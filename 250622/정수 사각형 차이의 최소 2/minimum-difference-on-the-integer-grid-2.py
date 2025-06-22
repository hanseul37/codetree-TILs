n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 2 for _ in range(n)] for _ in range(n)]
dp[0][0][0], dp[0][0][1] = arr[0][0], arr[0][0]

for i in range(1, n):
    dp[0][i][0] = min(dp[0][i - 1][0], arr[0][i])
    dp[0][i][1] = max(dp[0][i - 1][1], arr[0][i])
    dp[i][0][0] = min(dp[i - 1][0][0], arr[i][0])
    dp[i][0][1] = max(dp[i - 1][0][1], arr[i][0])

for i in range(1, n):
    for j in range(1, n):
        if dp[i - 1][j][1] - dp[i - 1][j][0] > dp[i][j - 1][1] - dp[i - 1][j][0]:
            dp[i][j][0] = min(dp[i][j - 1][0], arr[i][j])
            dp[i][j][1] = max(dp[i][j - 1][1], arr[i][j])
        else:
            dp[i][j][0] = min(dp[i - 1][j][0], arr[i][j])
            dp[i][j][1] = max(dp[i - 1][j][1], arr[i][j])

print(dp[-1][-1][1] - dp[-1][-1][0])