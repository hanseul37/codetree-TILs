from collections import deque

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    tree[v2 - 1].append(v1 - 1)

total = 0
for i in range(1, n):
    if len(tree[i]) != 1:
        continue
    q = deque([[i, 0]])
    visited = [False] * n
    visited[i] = True
    while q:
        node, cnt = q.popleft()
        if node == 0:
            total += cnt
            break
        for next_node in tree[node]:
            if not visited[next_node]:
                q.append([next_node, cnt + 1])
                visited[next_node] = True

print(total % 2)
