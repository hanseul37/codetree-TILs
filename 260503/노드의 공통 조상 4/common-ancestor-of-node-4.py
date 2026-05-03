import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree, parent, depth = [[] for _ in range(n)], [-1] * n, [0] * n
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    tree[v2 - 1].append(v1 - 1)

def dfs(node, p):
    for next_node in tree[node]:
        if next_node != p:
            depth[next_node] = depth[node] + 1
            parent[next_node] = node
            dfs(next_node, node)

dfs(0, -1)
q = int(input())
for _ in range(q):
    v1, v2 = map(int, input().split())
    v1, v2 = v1 - 1, v2 - 1
    while v1 != v2:
        if depth[v1] > depth[v2]:
            v1 = parent[v1]
        else:
            v2 = parent[v2]
    print(v1 + 1)
