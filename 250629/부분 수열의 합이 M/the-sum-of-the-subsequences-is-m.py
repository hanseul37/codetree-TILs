n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [-1] * (m + 1)
dp[0] = 0

for i in range(n):
    for j in range(m, -1, -1):
        if dp[j] >= 0 and j + a[i] <= m:
            if dp[j + a[i]] == -1:
                dp[j + a[i]] = dp[j] + 1
            else:
                dp[j + a[i]] = min(dp[j + a[i]], dp[j] + 1)
print(dp[-1])
        
