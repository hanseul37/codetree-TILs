from bisect import bisect_left

n, q = map(int, input().split())
points = []
x_point, y_point = [], []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    x_point.append(x)
    y_point.append(y)

queries = []
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    queries.append((x1, y1, x2, y2))
    x_point.append(x1) 
    x_point.append(x2)
    y_point.append(y1)
    y_point.append(y2)

x_point = sorted(set(x_point))
y_point = sorted(set(y_point))
x_len, y_len = len(x_point), len(y_point)
arr = [[0] * (x_len + 1) for _ in range(y_len + 1)]
for x, y in points:
    arr[bisect_left(y_point, y) + 1][bisect_left(x_point, x) + 1] = 1

prefix = [[0] * (x_len + 1) for _ in range(y_len + 1)]
for i in range(1, y_len + 1):
    for j in range(1, x_len + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]
        
for x1, y1, x2, y2 in queries:
    a = bisect_left(x_point, x1) + 1
    b = bisect_left(y_point, y1) + 1
    c = bisect_left(x_point, x2) + 1
    d = bisect_left(y_point, y2) + 1
    if a > c: 
        a, c = c, a
    if b > d: 
        b, d = d, b
    print(prefix[d][c] - prefix[b - 1][c] - prefix[d][a - 1] + prefix[b - 1][a - 1])
