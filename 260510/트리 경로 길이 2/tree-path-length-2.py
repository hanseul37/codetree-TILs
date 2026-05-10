import sys
sys.setrecursionlimit(10**6)

n = int(input())
max_h = 17
tree, parent, depth, dist = [{} for _ in range(n)], [[-1] * n for _ in range(max_h + 1)], [0] * n, [0] * n
for _ in range(n - 1):
    v1, v2, weight = map(int, input().split())
    tree[v1 - 1][v2 - 1] = tree[v2 - 1][v1 - 1] = weight

def dfs(node, p, cost):
    dist[node] = cost
    for next_node, weight in tree[node].items():
        if next_node != p:
            parent[0][next_node] = node
            depth[next_node] = depth[node] + 1
            dfs(next_node, node, cost + weight)

dfs(0, -1, 0)
for h in range(1, max_h + 1):
    for i in range(n):
        if parent[h - 1][i] != -1:
            parent[h][i] = parent[h - 1][parent[h - 1][i]]

q = int(input())
for _ in range(q):
    v1, v2 = map(int, input().split())
    v1, v2 = v1 - 1, v2 - 1
    orig_v1, orig_v2 = v1, v2
    if depth[v1] < depth[v2]:
        v1, v2 = v2, v1
    for i in range(max_h - 1, -1, -1):
        if depth[v1] - depth[v2] >= (1 << i):
            v1 = parent[i][v1]
    lca = v1
    if v1 != v2:
        for i in range(max_h - 1, -1, -1):
            if parent[i][v1] != parent[i][v2]:
                v1, v2 = parent[i][v1], parent[i][v2]
        lca = parent[0][v1]
    print(dist[orig_v1] + dist[orig_v2] - 2 * dist[lca])