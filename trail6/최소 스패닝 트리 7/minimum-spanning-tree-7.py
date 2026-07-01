from collections import deque

n, m = map(int, input().split())
edges, arr = [], [i for i in range(n)]
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

cnt, edge_cnt, graph = 0, 0, [[] for _ in range(n)]
for v1, v2, weight in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cnt += weight
        edge_cnt += 1
        graph[v1].append([v2, weight])
        graph[v2].append([v1, weight])
    if edge_cnt == n - 1:
        break

def bfs(node):
    q = deque([[node, 0]])
    visited = [False] * n
    visited[node] = True
    max_dist, max_node = 0, node
    while q:
        curr, curr_dist = q.popleft()
        if curr_dist > max_dist:
            max_dist = max(curr_dist, max_dist)
            max_node = curr
        for next_node, weight in graph[curr]:
            if not visited[next_node]:
                q.append([next_node, curr_dist + weight])
                visited[next_node] = True
    return max_node, max_dist

root_node, _ = bfs(0)
_, ans = bfs(root_node)
print(cnt)
print(ans)