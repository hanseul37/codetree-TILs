n, m = map(int, input().split())
s, e, v = [], [], []
for _ in range(n):
    si, ei, vi = map(int, input().split())
    s.append(si)
    e.append(ei)
    v.append(vi)

dp = [[-1] * n for _ in range(m + 1)]   
for i in range(n):
    if s[i] <= 1 <= e[i]:
        dp[1][i] = 0
        
for i in range(1, m):
    for j in range(n):
        if dp[i][j] == -1:
            continue
        for k in range(n):
            if s[k] <= i + 1 <= e[k]:
                dp[i + 1][k] = max(dp[i][j] + abs(v[j] - v[k]), dp[i + 1][k])

print(max(dp[m]))