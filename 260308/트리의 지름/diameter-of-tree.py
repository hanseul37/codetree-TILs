n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    v1, v2, weight = map(int, input().split())
    graph[v1 - 1].append([v2 - 1, weight])
    graph[v2 - 1].append([v1 - 1, weight])

visited = [False] * n
visited[0] = True
max_cost, idx = 0, -1
def dfs(node, cost):
    global max_cost
    for next_node, weight in graph[node]:
        if not visited[next_node]:
            new_cost = cost + weight
            if new_cost > max_cost:
                max_cost = new_cost
                idx = next_node
            visited[next_node] = True
            dfs(next_node, new_cost)

dfs(0, 0)
visited = [False] * n
visited[idx] = True
dfs(idx, 0)
print(max_cost)
