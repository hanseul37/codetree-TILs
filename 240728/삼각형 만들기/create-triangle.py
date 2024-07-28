n = int(input())
points = []
for _ in range(n):
    point = list(map(int, input().split()))
    points.append(point)

dist = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or i == k or j == k:
                continue
            
            if points[i][0] - points[j][0] != 0 or points[j][1] - points[k][1] != 0:
                continue
            
            cur_dist = abs(points[i][1] - points[j][1]) * abs(points[j][0] - points[k][0])
            dist = max(cur_dist, dist)
    
print(dist)