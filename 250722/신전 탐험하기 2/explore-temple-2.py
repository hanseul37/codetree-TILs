n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-1] * 3 for _ in range(3)] for _ in range(n)]

for i in range(3): 
    dp[0][i][i] = arr[0][i]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if i == n - 1 and j == k:
                continue 
            for l in range(3):
                if j == l:
                    continue
                if dp[i - 1][l][k] == -1:
                    continue
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][l][k] + arr[i][j]) 

ans = 0
for i in range(3):
    for j in range(3):
        ans = max(dp[-1][i][j], ans)
print(ans)