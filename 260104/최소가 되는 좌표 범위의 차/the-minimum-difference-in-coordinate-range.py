n, d = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort()
left, min_range = 0, 1000000
for right in range(1, n):
    for left in range(right - 1, -1, -1):
        if points[right][0] - points[left][0] >= min_range:
            break   
        min_y, max_y = points[right][1], points[right][1]
        for i in range(left, right):
            min_y = min(points[i][1], min_y)
            max_y = max(points[i][1], max_y)
        if max_y - min_y >= d:
            min_range = points[right][0] - points[left][0]
print(min_range)
