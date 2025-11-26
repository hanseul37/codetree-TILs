from bisect import bisect_left, bisect_right
from collections import defaultdict

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
point_dict = defaultdict(list)
for x, y in points:
    point_dict[bisect_left(y_point, y)].append(bisect_left(x_point, x))

for xi in point_dict.values():
    xi.sort()

for x1, y1, x2, y2 in queries:
    a = bisect_left(x_point, min(x1, x2))
    c = bisect_right(x_point, max(x1, x2)) - 1
    b = bisect_left(y_point, min(y1, y2))
    d = bisect_right(y_point, max(y1, y2)) - 1

    ans = 0
    for yi in range(b, d + 1):
        xi_list = point_dict.get(yi, [])
        if not xi_list:
            continue
        ans += bisect_right(xi_list, c) - bisect_left(xi_list, a)
    print(ans)





