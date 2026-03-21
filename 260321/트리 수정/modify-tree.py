from collections import deque

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    v1, v2, weight = map(int, input().split())
    tree[v1].append([v2, weight])
    tree[v2].append([v1, weight])

def bfs(s):
    dist = [float('inf')] * n
    dist[s] = 0
    q = deque([s])
    while q:
        node = q.popleft() 
        for next_node, weight in tree[node]:
            if dist[next_node] == float('inf'):
                dist[next_node] = dist[node] + weight
                q.append(next_node)
    return dist

distance = []
for i in range(n):
    distance.append(bfs(i))

ans = 0
for i in range(n):
    for j, weight in tree[i]:
        if i < j:
            tree_i = [k for k in range(n) if distance[i][k] < distance[j][k]]
            tree_j = [k for k in range(n) if distance[i][k] > distance[j][k]]
            end_i = max(tree_i, key=lambda x: distance[i][x])
            diameter_i = max(distance[end_i][x] for x in tree_i)
            end_j = max(tree_j, key=lambda x: distance[j][x])
            diameter_j = max(distance[end_j][x] for x in tree_j)
            ans = max(ans, diameter_i + weight + diameter_j)
print(ans)