n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[-10000 * k] * (k + 1) for _ in range(n)]
dp[0][0] = arr[0]

for i in range(n):
    for j in range(k + 1):
        if arr[i] >= 0:
            if dp[i - 1][j] == -10000 * k:
                dp[i][j] = arr[i]
            else:
                dp[i][j] = max(dp[i - 1][j] + arr[i], dp[i][j])
        else:
            if j > 0:
                if dp[i - 1][j - 1] == -10000 * k:
                    dp[i][j] = arr[i]
                else:
                    dp[i][j] = max(dp[i - 1][j - 1] + arr[i], dp[i][j])

max_value = -10000 * k
for i in range(n):
    for j in range(k + 1):
        max_value = max(dp[i][j], max_value)
print(max_value)