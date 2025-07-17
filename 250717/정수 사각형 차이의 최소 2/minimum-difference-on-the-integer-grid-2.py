n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[set() for _ in range(n)] for _ in range(n)]
dp[0][0].add((arr[0][0], arr[0][0]))

for i in range(1, n):
    for min_value, max_value in dp[i - 1][0]:
        dp[i][0].add((min(min_value, arr[i][0]), max(max_value, arr[i][0])))
    for min_value, max_value in dp[0][i - 1]:
        dp[0][i].add((min(min_value, arr[0][i]), max(max_value, arr[0][i])))

for i in range(1, n):
    for j in range(1, n):
        for min_value, max_value in dp[i][j - 1]:
            dp[i][j].add((min(min_value, arr[i][j]), max(max_value, arr[i][j])))
        for min_value, max_value in dp[i - 1][j]:
            dp[i][j].add((min(min_value, arr[i][j]), max(max_value, arr[i][j])))

ans = 200
for min_value, max_value in dp[-1][-1]:
    ans = min(max_value - min_value, ans)
print(ans)