n, m, k = map(int, input().split())
vertex = list(map(int, input().split()))
arr = [int(i) for i in range(n)]

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

min_cost = dict()
for i in range(n):
    root = find(i)
    if root not in min_cost:
        min_cost[root] = vertex[i]
    else:
        min_cost[root] = min(vertex[i], min_cost[root])

values = list(min_cost.values())
total_cost = min(vertex) * (len(values) - 2) + sum(values)
if total_cost <= k:
    print(total_cost)
else:
    print('NO')