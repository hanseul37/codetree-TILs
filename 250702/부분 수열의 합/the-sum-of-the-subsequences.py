n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [False] * (m + 1)
dp[0] = True
for i in range(n):
    for j in range(m, a[i] - 1, -1):
        if dp[j - a[i]]:
            dp[j] = True
        
if dp[m]:
    print('Yes')
else:
    print('No')




