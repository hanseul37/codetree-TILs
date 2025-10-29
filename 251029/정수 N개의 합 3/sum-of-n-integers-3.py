n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + prefix_sum[i - 1][j - 1] + arr[i - 1][j - 1]
print(prefix_sum)

max_cnt = 0
for i in range(1, n + 1 - k + 1):
    for j in range(1, n + 1 - k + 1):
        max_cnt = max(prefix_sum[i + k - 1][j + k - 1] - prefix_sum[i - 1][j + k - 1] - prefix_sum[i + k - 1][j - 1] + prefix_sum[i - 1][j - 1], max_cnt)
print(max_cnt)