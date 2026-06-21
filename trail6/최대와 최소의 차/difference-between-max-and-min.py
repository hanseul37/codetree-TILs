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
    v1, v2, option = map(int, input().split())
    edges.append([v1 - 1, v2 - 1, 1 - option])

cnt1, edge_cnt = 0, 0
edges.sort(key=lambda x:x[2])
for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt1 += weight
        edge_cnt += 1
    if edge_cnt == n - 1:
        break

cnt2, edge_cnt, arr = 0, 0, [i for i in range(n)]
edges.sort(key=lambda x:-x[2])
for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt2 += weight
        edge_cnt += 1
    if edge_cnt == n - 1:
        break
print(cnt2 ** 2 - cnt1 ** 2)