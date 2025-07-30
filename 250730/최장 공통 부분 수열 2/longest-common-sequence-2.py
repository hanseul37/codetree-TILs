a = input()
b = input()
n, m = len(a), len(b)
dp = [[[] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if len(dp[i - 1][j]) < len(dp[i][j - 1]):
                dp[i][j] = dp[i][j - 1][:]
        else:
            dp[i][j] = dp[i - 1][j][:] 
        
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1][:] + [a[i - 1]]

print(''.join(dp[n][m]))