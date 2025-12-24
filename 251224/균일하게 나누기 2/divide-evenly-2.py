n = int(input())
x_sort, y_sort = [], []
for _ in range(n):
    x, y = map(int, input().split())
    x_sort.append([x, y])
    y_sort.append([y, x])
x_sort.sort()
y_sort.sort()

x_idx, y_idx = {}, {}
idx = 1
for x, y in x_sort:
    if x not in x_idx:
        x_idx[x] = idx
        idx += 1
idx = 1
for y, x in y_sort:
    if y not in y_idx:
        y_idx[y] = idx
        idx += 1

arr = [[0] * (len(y_idx) + 1) for _ in range((len(x_idx) + 1))]
for x, y in x_sort:
    arr[x_idx[x]][y_idx[y]] += 1

prefix = [[0] * (len(y_idx) + 1) for _ in range(len(x_idx) + 1)]
for i in range(1, len(x_idx) + 1):
    for j in range(1, len(y_idx) + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]

min_m = n
for i in range(1, len(x_idx) + 1):
    for j in range(1, len(y_idx) + 1):
        a = prefix[i][j] - prefix[0][j] - prefix[i][0] + prefix[0][0]
        b = prefix[i][len(y_idx)] - prefix[0][len(y_idx)] - prefix[i][j] + prefix[0][j]
        c = prefix[len(x_idx)][j] - prefix[i][j] - prefix[len(x_idx)][0] + prefix[i][0]
        d = prefix[len(x_idx)][len(y_idx)] - prefix[i][len(y_idx)] - prefix[len(x_idx)][j] + prefix[i][j]
        min_m = min(min_m, max(a, b, c, d))
print(min_m)
