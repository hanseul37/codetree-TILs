import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree, depth, parent = [[] for _ in range(n)], [0] * n, [-1] * n
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    parent[v2 - 1] = v1 - 1
for i in range(n):
    if parent[i] == -1:
        root = i
        break

def dfs(node):
    for next_node in tree[node]:
        depth[next_node] = depth[node] + 1
        dfs(next_node)

dfs(root)
v1, v2 = map(int, input().split())
v1, v2 = v1 - 1, v2 - 1
while depth[v1] != depth[v2]:
    if depth[v1] > depth[v2]:
        v1 = parent[v1]
    else:
        v2 = parent[v2]
while v1 != v2:
    v1 = parent[v1]
    v2 = parent[v2]
print(v1 + 1)

