n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[[-1] * (m + 1) for _ in range(4)] for _ in range(n + 1)]

for i in range(4):
    if i + 1 == arr[0]:
        dp[1][i][0] = 1
    else:
        dp[1][i][0] = 0

for i in range(1, n):
    for j in range(4):
        for k in range(m + 1):
            if dp[i][j][k] == -1:
                continue
            for l in range(1, 5):
                sim = 0
                if arr[i] == l:
                    sim = 1
                if j + 1 != l:
                    if k < m:
                        dp[i + 1][l - 1][k + 1] = max(dp[i][j][k] + sim, dp[i + 1][l - 1][k + 1])
                else:
                    dp[i + 1][j][k] = max(dp[i][j][k] + sim, dp[i + 1][j][k])

max_sim = 0
for i in range(4):
    for j in range(m + 1):
        max_sim = max(dp[-1][i][j], max_sim)
print(max_sim)

