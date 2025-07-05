n, m = map(int, input().split())
w, v = [], []
for _ in range(n):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)
dp = [0] * (m + 1)

for i in range(n):
    for j in range(w[i], m + 1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(max(dp))



