from collections import deque

n, m = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    tree[v2 - 1].append(v1 - 1)

visited, tree_cnt = [False] * n, 0
for i in range(n):
    if not visited[i]:
        visited[i] = True
        q = deque([i])
        node_cnt, edge_cnt = 0, 0
        while q:
            node = q.popleft()
            node_cnt += 1
            edge_cnt += len(tree[node])
            for next_node in tree[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)
        if node_cnt - 1 == edge_cnt // 2:
            tree_cnt += 1
print(tree_cnt)