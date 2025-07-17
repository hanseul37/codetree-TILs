n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[{} for _ in range(n)] for _ in range(n)]
dp[0][0][arr[0][0]] = arr[0][0]

for i in range(1, n):
    for min_value, max_value in dp[i - 1][0].items():
        new_min = min(min_value, arr[i][0])
        new_max = max(max_value, arr[i][0])
        if new_min not in dp[i][0] or dp[i][0][new_min] > new_max:
            dp[i][0][new_min] = new_max
    for min_value, max_value in dp[0][i - 1].items():
        new_min = min(min_value, arr[0][i])
        new_max = max(max_value, arr[0][i])
        if new_min not in dp[0][i] or dp[0][i][new_min] > new_max:
            dp[0][i][new_min] = new_max

for i in range(1, n):
    for j in range(1, n):
        for min_value, max_value in dp[i][j - 1].items():
            new_min = min(min_value, arr[i][j])
            new_max = max(max_value, arr[i][j])
            if new_min not in dp[i][j] or dp[i][j][new_min] > new_max:
                dp[i][j][new_min] = new_max
        for min_value, max_value in dp[i - 1][j].items():
            new_min = min(min_value, arr[i][j])
            new_max = max(max_value, arr[i][j])
            if new_min not in dp[i][j] or dp[i][j][new_min] > new_max:
                dp[i][j][new_min] = new_max

ans = 200
for min_value, max_value in dp[-1][-1].items():
    ans = min(max_value - min_value, ans)
print(ans)