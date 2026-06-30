n, m, k = map(int, input().split())
colored = list(map(int, input().split()))
colored = [i - 1 for i in colored]
edges, arr = [], [i for i in range(n + 1)]
for _ in range(m):
    v1, v2, weight = map(int, input().split())
    edges.append([v1 - 1, v2 - 1, weight])
edges.sort(key=lambda x:x[2])

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

for node in colored:
    union(node, n)

cnt, edge_cnt = 0, 0
for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt += weight
        edge_cnt += 1
    if edge_cnt == n - len(colored):
        break
print(cnt)