n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    graph[v1 - 1].append(v2 - 1)
    graph[v2 - 1].append(v1 - 1)

parent, visited, q = [0] * n, [False] * n, [0]
parent[0] = -1
visited[0] = True
while q:
    node = q.pop(0)
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            parent[next_node] = node
            q.append(next_node)
for i in range(1, n):
    print(parent[i] + 1)