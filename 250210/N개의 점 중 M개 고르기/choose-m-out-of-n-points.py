n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
min_dist = 20000


def choice(points, idx):
    global min_dist

    if len(points) >= m:
        dist = 0
        for i in range(m - 1):
            for j in range(i + 1, m):
                dist = max((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2, dist)
        min_dist = min(min_dist, dist)

    for i in range(idx + 1, n):
        points.append(arr[i])
        choice(points, i)
        points.pop()

choice([], -1)
print(min_dist)