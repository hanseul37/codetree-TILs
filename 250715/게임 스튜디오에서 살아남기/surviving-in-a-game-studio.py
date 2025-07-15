n = int(input())
dp = [[[0] * 3 for _ in range(3)]for _ in range(n + 1)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(3):
        for k in range(3):
            if dp[i][j][k] == 0:
                continue
            dp[i + 1][0][k] += dp[i][j][k]
            if j < 2:
                dp[i + 1][j + 1][k] += dp[i][j][k]
            if k < 2:
                dp[i + 1][0][k + 1] += dp[i][j][k]

total = 0
for i in range(3):
    total += sum(dp[n][i])
print(total % 1000000007)