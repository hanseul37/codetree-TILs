n, m = map(int, input().split())
vertex = list(input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])
arr, cnt, edge_cnt = [int(i) for i in range(n)], 0, 0

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

for v1, v2, weight in edges:
    v1, v2 = v1 - 1, v2 - 1
    if find(v1) != find(v2) and vertex[v1] != vertex[v2]:
        union(v1, v2)
        edge_cnt += 1
        cnt += weight
    if edge_cnt == n - 1:
        break

if edge_cnt == n - 1:
    print(cnt)
else:
    print(-1)