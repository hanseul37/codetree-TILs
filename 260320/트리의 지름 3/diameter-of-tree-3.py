from collections import deque

n = int(input())
tree, start = dict(), None
for _ in range(n - 1):
    v1, v2, weight = map(int, input().split())
    if v1 not in tree:
        tree[v1] = []
    if v2 not in tree:
        tree[v2] = []
    tree[v1].append([v2, weight])
    tree[v2].append([v1, weight])
    if start == None:
        start = v1

def bfs(s):
    dist = dict()
    dist[s] = 0
    q = deque([s])
    e, max_dist = s, 0
    while q:
        node = q.popleft()
        for next_node, weight in tree[node]:
            if next_node not in dist:
                dist[next_node] = dist[node] + weight
                q.append(next_node)
                if dist[next_node] > max_dist:
                    max_dist = dist[next_node]
                    e = next_node
    return e, dist

end1, _ = bfs(start)
end2, dist1 = bfs(end1)
_, dist2 = bfs(end2)
ans = 0
for node in tree:
    if node == end1 or node == end2:
        continue
    ans = max(ans, dist1[node])
    ans = max(ans, dist2[node])
print(ans)


