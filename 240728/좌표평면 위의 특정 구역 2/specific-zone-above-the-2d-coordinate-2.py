n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

area = 1600000000
for i in range(n):
    x_min, x_max, y_min, y_max = 40000, 0, 40000, 0
    for j in range(n):
        if i == j:
            continue

        x_min = min(points[j][0], x_min)
        x_max = max(points[j][0], x_max)
        y_min = min(points[j][1], y_min)
        y_max = max(points[j][1], y_max)
    area = min((x_max - x_min) * (y_max - y_min), area)
    
print(area)