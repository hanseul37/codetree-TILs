class Point:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number

points = []

n = int(input())
for i in range(n):
    x, y = input().split()
    points.append(Point(int(x), int(y), i + 1))

points.sort(key=lambda x:abs(x.x) + abs(x.y))

for point in points:
    print(point.number)