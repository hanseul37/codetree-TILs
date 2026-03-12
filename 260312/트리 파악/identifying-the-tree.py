from collections import deque

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    tree[v1 - 1].append(v2 - 1)
    tree[v2 - 1].append(v1 - 1)

q = deque([0])
visited = [False] * n
visited[0] = True
depth = [0] * n
while q:
    node = q.popleft()
    for next_node in tree[node]:
        if not visited[next_node]:
            q.append(next_node)
            visited[next_node] = True
            depth[next_node] = depth[node] + 1
total = 0
for i in range(1, n):
    if len(tree[i]) == 1:
        total += depth[i]
print(total % 2)
