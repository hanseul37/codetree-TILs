n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
dp = [[-1] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue
        if second[j] > first[i]:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        elif second[j] < first[i]:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + second[j])       
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])

max_point = 0
for i in range(n + 1):
    for j in range(n + 1):
        max_point = max(dp[i][j], max_point)
print(max_point)