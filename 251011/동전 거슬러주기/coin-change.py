n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [m + 1] * (m + 1)
for elem in arr:
    dp[elem] = 1
for i in range(1, m + 1):
    for elem in arr:
        if i > elem:
            dp[i] = min(dp[i], dp[i - elem] + 1)

print(dp[m])
