n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
dp = [[-1] * (2 * total + 1) for _ in range(n + 1)]
dp[0][total] = 0

for i in range(n):
    for j in range(2 * total + 1):
        if dp[i][j] == -1:
            continue
        if j + arr[i] < 2 * total + 1:
            dp[i + 1][j + arr[i]] = max(dp[i + 1][j + arr[i]], dp[i][j] + arr[i])
        if j - arr[i] >= 0:
            dp[i + 1][j - arr[i]] = max(dp[i + 1][j - arr[i]], dp[i][j])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
if dp[n][total] > 0:
    print(dp[n][total])
else:
    print(0)