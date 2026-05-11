import sys
sys.setrecursionlimit(10**6)

n = int(input())
max_h = 17
tree, parent, depth, count = [[] for _ in range(n)], [[-1] * n for _ in range(max_h + 1)], [0] * n, [0] * n
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    tree[v2 - 1].append(v1 - 1)
k = int(input())
colored = {int(input()) - 1 for _ in range(k)}

def dfs(node, p, cnt):
    next_cnt = cnt
    if node in colored:
        next_cnt += 1
    count[node] = next_cnt
    for next_node in tree[node]:
        if next_node != p:
            depth[next_node] = depth[node] + 1
            parent[0][next_node] = node
            dfs(next_node, node, next_cnt)

def get_lca(v1, v2):
    if depth[v1] < depth[v2]:
        v1, v2 = v2, v1
    for i in range(max_h - 1, -1, -1):
        if depth[v1] - depth[v2] >= (1 << i):
            v1 = parent[i][v1]
    if v1 == v2:
        return v1
    for i in range(max_h, -1, -1):
        if parent[i][v1] != parent[i][v2]:
            v1, v2 = parent[i][v1], parent[i][v2]
    return parent[0][v1]

dfs(0, -1, 0)
for h in range(1, max_h + 1):
    for i in range(n):
        if parent[h - 1][i] != -1:
            parent[h][i] = parent[h - 1][parent[h - 1][i]]

q = int(input())
for _ in range(q):
    v1, v2 = map(int, input().split())
    v1, v2 = v1 - 1, v2 - 1
    lca = get_lca(v1, v2)
    ans = count[v1] + count[v2] - 2 * count[lca]
    if lca in colored:
        ans += 1
    print(ans)
