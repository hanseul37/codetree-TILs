n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

dist = 2000000
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        cur_dist = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) * (points[i][1] - points[j][1])
        dist = min(cur_dist, dist)

print(dist)