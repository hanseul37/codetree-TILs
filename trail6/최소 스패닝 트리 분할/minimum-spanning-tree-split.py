n, m = map(int, input().split())
edges, arr = [], [i for i in range(n)]

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

for _ in range(m):
    v1, v2, weight = map(int, input().split())
    edges.append([v1 - 1, v2 - 1, weight])
edges.sort(key=lambda x:x[2])

cnt, edge_cnt = 0, 0
for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt += weight
        edge_cnt += 1
        last_weight = weight
    if edge_cnt == n - 1:
        break
print(cnt - last_weight)