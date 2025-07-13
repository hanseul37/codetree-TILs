n = int(input())
red = []
blue = []

for _ in range(2 * n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

dp = [[-1] * (n + 1) for _ in range(2 * n + 1)]
dp[0][0] = 0
for i in range(2 * n):
    for j in range(n + 1):
        if dp[i][j] == -1:
            continue
        if j < n:
            dp[i + 1][j + 1] = max(dp[i][j] + red[i], dp[i + 1][j + 1])
        if i - j < n:
            dp[i + 1][j]  = max(dp[i][j] + blue[i], dp[i + 1][j])

print(dp[2 * n][n])
