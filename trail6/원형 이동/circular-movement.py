import sys
sys.setrecursionlimit(10 ** 6)

n, m, k = map(int, input().split())
cost = list(map(int, input().split()))
edges, arr = [], [i for i in range(n + 1)]
for i in range(n):
    edges.append([i + 1, cost[i]])
edges.sort(key=lambda x:x[1])
construction = []
for _ in range(m):
    v1, v2 = map(int, input().split())
    if abs(v1 - v2) == n - 1:
        construction.append([n, 1])
    else:
        construction.append([min(v1, v2), max(v1, v2)])
construction.sort()
point = construction[-1][1]
for i in range(m):
    start, end = construction[i]
    temp = point
    while point != start:
        point = (point % n) + 1
        arr[point] = temp
    point = end

def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    arr[find(x)] = find(y)

cnt, first, flag = 0, None, False
for node, weight in edges:
    if first is None:
        first = node
    if find(first) != find(node):
        union(first, node)
        cnt += weight
        flag = True
if flag:
    k -= edges[0][1]
if cnt <= k:
    print(1)
else:
    print(0)