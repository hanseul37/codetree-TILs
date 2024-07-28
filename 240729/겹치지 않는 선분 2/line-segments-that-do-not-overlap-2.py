n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

cnt = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if points[i][0] <= points[j][0] and points[i][1] >= points[j][1]:
            cnt += 1
            break
        if points[i][0] >= points[j][0] and points[i][1] <= points[j][1]:
            cnt += 1
            break
print(n - cnt)