n = int(input())
edges, arr = [], [i for i in range(n)]
points = []
for i in range(n):
    x, y, z = map(int, input().split())
    points.append([x, y, z, i])

points.sort(key=lambda x: x[0])
for i in range(n - 1):
    edges.append([points[i][3], points[i+1][3], abs(points[i][0] - points[i + 1][0])])

points.sort(key=lambda x: x[1])
for i in range(n - 1):
    edges.append([points[i][3], points[i+1][3], abs(points[i][1] - points[i + 1][1])])

points.sort(key=lambda x: x[2])
for i in range(n - 1):
    edges.append([points[i][3], points[i+1][3], abs(points[i][2] - points[i + 1][2])])

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

edges.sort(key=lambda x:x[2])
cnt, edge_cnt = 0, 0
for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt += weight
        edge_cnt += 1
    if edge_cnt == n - 1:
        break
print(cnt)