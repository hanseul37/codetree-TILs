n, k = map(int, input().split())
crystal = input()
dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(k + 1):
        for l in range(2):
            curr = -1
            if crystal[i] == 'L':
                curr = 0
            else:
                curr = 1              
            dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][l])  
            if l == curr:
                dp[i + 1][j][curr] = max(dp[i][j][l] + 1, dp[i + 1][j][curr])
            else:
                #dp[i + 1][j][l] = max(dp[i + 1][j][l], dp[i][j][l])
                if j < k:
                    dp[i + 1][j + 1][curr] = max(dp[i][j][l] + 1, dp[i + 1][j + 1][curr])             

max_crystal = 0
for i in range(k + 1):
    for j in range(2):
        max_crystal = max(dp[-1][i][j], max_crystal)
print(max_crystal)