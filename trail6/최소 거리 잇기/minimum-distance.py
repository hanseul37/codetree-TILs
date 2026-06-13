import math

n, m = map(int, input().split())
nodes, edges, arr = [], [], [i for i in range(n)]
for _ in range(n):
    nodes.append(list(map(int, input().split())))

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

for _ in range(m):
    v1, v2 = map(int, input().split())
    union(v1 - 1, v2 - 1)

for i in range(n):
    for j in range(i + 1, n):
        edges.append([i, j, math.sqrt((nodes[i][0] - nodes[j][0]) ** 2 + (nodes[i][1] - nodes[j][1]) ** 2)])
edges.sort(key=lambda x:x[2])

cnt = 0
for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt += weight
print(f'{cnt:.2f}')