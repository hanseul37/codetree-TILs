n, m = map(int, input().split())
e, t = [], []
for _ in range(n):
    ei, ti = map(int, input().split())
    e.append(ei)
    t.append(ti)
dp = [-1] * (sum(t) + 1)
dp[0] = 0

for i in range(n):
    for j in range(sum(t), t[i] - 1, -1):
        if dp[j - t[i]] >= 0:
            dp[j] = max(dp[j], dp[j - t[i]] + e[i])
    
for i in range(len(dp)):
    if dp[i] >= m:
        print(i)
        break
