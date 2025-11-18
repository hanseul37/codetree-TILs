n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0] * n for _ in range(n)]
prefix[0][0] = arr[0][0]
for i in range(1, n):
    prefix[i][0] = prefix[i - 1][0] + arr[i][0]
    prefix[0][i] = prefix[0][i - 1] + arr[0][i]
for i in range(1, n):
    for j in range(1, n):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]

max_value = -1000 * n * n
for r1 in range(n):
    for c1 in range(n):
        for r2 in range(r1, n):
            for c2 in range(c1, n):
                total = prefix[r2][c2]
                if r1 > 0:
                    total -= prefix[r1 - 1][c2]
                if c1 > 0:
                    total -= prefix[r2][c1 - 1]
                if r1 > 0 and c1 > 0:
                    total += prefix[r1 - 1][c1 - 1]
                max_value = max(max_value, total)

print(max_value)
