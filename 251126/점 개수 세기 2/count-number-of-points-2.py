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
point_dict = {}
for x, y in points:
    xi = bisect_left(x_point, x)
    yi = bisect_left(y_point, y)
    if (yi, xi) not in point_dict:
        point_dict[(yi, xi)] = 0
    point_dict[(yi, xi)] += 1

for x1, y1, x2, y2 in queries:
    a = bisect_left(x_point, x1)
    b = bisect_left(y_point, y1)
    c = bisect_left(x_point, x2)
    d = bisect_left(y_point, y2)
    if a > c: 
        a, c = c, a
    if b > d: 
        b, d = d, b
    ans = 0
    for (yi, xi), cnt in point_dict.items():
        if b <= yi <= d and a <= xi <= c:
            ans += cnt
    print(ans)
