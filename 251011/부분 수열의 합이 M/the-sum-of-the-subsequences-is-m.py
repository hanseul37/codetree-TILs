n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [m + 1] * (m + 1)
dp[0] = 0
for i in range(n):
    for j in range(m, -1, -1):
        if j >= a[i]:
            dp[j] = min(dp[j], dp[j - a[i]] + 1)
if dp[m] == m + 1:
    print(-1)
else:
    print(dp[m])