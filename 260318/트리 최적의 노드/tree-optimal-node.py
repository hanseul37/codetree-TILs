from collections import deque

n = int(input())
tree, start = dict(), None
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    if v1 not in tree:
        tree[v1] = []
    if v2 not in tree:
        tree[v2] = []
    tree[v1].append(v2)
    tree[v2].append(v1)
    if start is None:
        start = v1

def bfs(start):
    dist = dict()
    dist[start] = 0
    q = deque([start])
    end, max_dist = start, 0
    while q:
        node = q.popleft() 
        for next_node in tree[node]:
            if next_node not in dist:
                dist[next_node] = dist[node] + 1
                q.append(next_node)
                if dist[next_node] > max_dist:
                    max_dist = dist[next_node]
                    end = next_node
    return end, max_dist

end, _ = bfs(start)
_, max_dist = bfs(end)
print((max_dist + 1) // 2)
            