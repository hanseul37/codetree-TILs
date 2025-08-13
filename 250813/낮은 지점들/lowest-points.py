n = int(input())
points = {}
for _ in range(n):
    x, y = map(int, input().split())
    if x in points:
        points[x] = min(points[x], y)
    else:
        points[x] = y

total = 0
for elem in points:
    total += points[elem]
print(total)
