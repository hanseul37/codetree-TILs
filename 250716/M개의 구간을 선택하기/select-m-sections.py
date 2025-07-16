n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[[-1] * 2 for _ in range(m + 1)] for _ in range(n)]
dp[0][1][1] = arr[0]
dp[0][0][0] = 0

for i in range(n - 1):
    for j in range(m + 1):
        for k in range(2):
            if dp[i][j][k] == -1:
                continue
            if k == 0:
                dp[i + 1][j][k] = max(dp[i][j][k], dp[i + 1][j][k])
                if j < m:
                    dp[i + 1][j + 1][1] = max(dp[i][j][k] + arr[i + 1], dp[i + 1][j + 1][1]) 
            else:
                dp[i + 1][j][0] = max(dp[i][j][k], dp[i + 1][j][0])
                dp[i + 1][j][1] = max(dp[i][j][k] + arr[i + 1], dp[i + 1][j][1])
                
print(max(dp[-1][m]))
