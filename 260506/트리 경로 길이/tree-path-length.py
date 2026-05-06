import sys
sys.setrecursionlimit(10**6)

n = int(input())
max_h = 17
tree, depth, parent = [[] for _ in range(n)], [0] * n, [[-1] * n for _ in range(max_h + 1)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    tree[v2 - 1].append(v1 - 1)

def dfs(node, p):
    for next_node in tree[node]:
        if next_node != p:
            depth[next_node] = depth[node] + 1
            parent[0][next_node] = node
            dfs(next_node, node) 

dfs(0, -1)
for h in range(1, max_h + 1):
    for i in range(n):
        if parent[h - 1][i] != -1:
            parent[h][i] = parent[h - 1][parent[h - 1][i]]

def get_lca(v1, v2):
    if depth[v1] < depth[v2]:
        v1, v2 = v2, v1
    for h in range(max_h, -1, -1):
        if depth[v1] - depth[v2] >= (1 << h):
            v1 = parent[h][v1]
    if v1 == v2:
        return v1
    for h in range(max_h, -1, -1):
        if parent[h][v1] != parent[h][v2]:
            v1 = parent[h][v1]
            v2 = parent[h][v2]
    return parent[0][v1]

q = int(input())
for _ in range(q):
    v1, v2 = map(int, input().split())
    v1, v2 = v1 - 1, v2 - 1
    print(depth[v1] + depth[v2] - 2 * depth[get_lca(v1, v2)] + 1)

