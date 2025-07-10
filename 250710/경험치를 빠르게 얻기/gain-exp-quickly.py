n, m = map(int, input().split())
e, t = [], []
total_t = 0
for _ in range(n):
    ei, ti = map(int, input().split())
    e.append(ei)
    t.append(ti)
    total_t += ti
dp = [-1] * (total_t + 1)
dp[0] = 0

for i in range(n):
    for j in range(total_t, t[i] - 1, -1):
        if dp[j - t[i]] >= 0:
            dp[j] = max(dp[j], dp[j - t[i]] + e[i])

ans = -1  
for i in range(len(dp)):
    if dp[i] >= m:
        ans = i
        break
print(ans)