n, s, d = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

dist, cnt = [-1] * (n + 1), 0

def dist_dfs(node, parent):
    for next_node in tree[node]:
        if not next_node == parent:
            dist[next_node] = dist[node] + 1
            dist_dfs(next_node, node)

def dfs(node, parent):
    global cnt
    if dist[node] > d:
        flag = True
    else:
        flag = False
    for next_node in tree[node]:
        if not next_node == parent:
            if dfs(next_node, node):
                flag = True
    if node != s and flag:
        cnt += 2
    return flag

dist[s] = 0
dist_dfs(s, 0)
dfs(s, 0)
if cnt > 0:
    print(cnt - 4)
else:
    print(0)

