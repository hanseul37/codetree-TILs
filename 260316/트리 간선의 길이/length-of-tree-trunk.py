from collections import deque

n = int(input())
tree, start = dict(), None
for _ in range(n - 1):
    v1, v2, weight = map(int, input().split())
    if v1 not in tree:
        tree[v1] = []      
    tree[v1].append([v2, weight])
    if v2 not in tree:
        tree[v2] = []
    tree[v2].append([v1, weight])
    if start is None:
        start = v1

def bfs(start):
    dist = dict()
    dist[start] = 0
    q = deque([start])
    max_dist, end = 0, start
    while q:
        node = q.popleft()
        for next_node, weight in tree[node]:
            if next_node not in dist:
                dist[next_node] = dist[node] + weight
                q.append(next_node)
                if dist[next_node] > max_dist:
                    max_dist = dist[next_node]
                    end = next_node
    return end, max_dist

end, _ = bfs(start)
_, ans = bfs(end)
print(ans)
