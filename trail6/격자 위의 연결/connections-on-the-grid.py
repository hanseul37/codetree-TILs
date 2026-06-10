n, m = map(int, input().split())
edges = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m - 1):
        edges.append([i * m + j, i * m + j + 1, line[j]])
for i in range(n - 1):
    line = list(map(int, input().split()))
    for j in range(m):
        edges.append([i * m + j, (i + 1) * m + j, line[j]])
edges.sort(key=lambda x:x[2])
cnt, edge_cnt, arr = 0, 0, [i for i in range(n * m)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt += weight
        edge_cnt += 1
    if edge_cnt == n * m - 1:
        print(cnt)
        break