n = int(input())
s = []
b = []
for _ in range(n):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

dp = [[[0] * 10 for _ in range(12)] for _ in range(n + 1)]
for i in range(n):
    for j in range(12):
        for k in range(10):
            if j < 11:
                dp[i + 1][j + 1][k] = max(dp[i][j][k] + s[i], dp[i + 1][j + 1][k])
            if k < 9:
                dp[i + 1][j][k + 1] = max(dp[i][j][k] + b[i], dp[i + 1][j][k + 1])
            dp[i + 1][j][k] = max(dp[i][j][k], dp[i + 1][j][k])

print(dp[n][11][9])
    

