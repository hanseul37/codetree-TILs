import sys
sys.setrecursionlimit(10**6)

n, s, d = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

def dfs(node, parent):
    cnt, depth = 0, 0
    for next_node in tree[node]:
        if next_node != parent:
            child_depth, child_cnt = dfs(next_node, node)
            if child_depth >= d:
                cnt += child_cnt + 2
            depth = max(child_depth + 1, depth)
    return depth, cnt

print(dfs(s, 0)[1])