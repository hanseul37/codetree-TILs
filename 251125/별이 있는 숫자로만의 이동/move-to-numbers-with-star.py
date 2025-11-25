n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i][j - 1] + arr[i - 1][j - 1]

max_total = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        total = 0
        for l in range(max(i - k, 1), min(i + k + 1, n + 1)):
            total += prefix[l][min(j + (k - abs(i - l)), n)] - prefix[l][max(j - (k - abs(i - l)) - 1, 0)]
        max_total = max(max_total, total)
print(max_total)