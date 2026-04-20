import sys
sys.setrecursionlimit(10**6)

n, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

def find_center(node, parent):
    child = [next_node for next_node in tree[node] if next_node != parent]
    if len(child) >= 2 or not child:
        return node
    return find_center(child[0], node)

def dfs(node, parent):
    subtree = 1
    for next_node in tree[node]:
        if next_node != parent:
            subtree += dfs(next_node, node)
    return subtree

center = find_center(r, 0)      
size = []
for next_node in tree[center]:
    size.append(dfs(next_node, center))
if not size:
    print(0)
else:
    print(max(size) - min(size))