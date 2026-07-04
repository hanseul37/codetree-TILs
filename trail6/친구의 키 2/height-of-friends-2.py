from collections import deque

n, m = map(int, input().split())
graph, in_degree = [[] for _ in range(n)], [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    in_degree[b - 1] += 1

q = deque()
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)

arr = []
while q:
    node = q.popleft()
    arr.append(node)
    for next_node in graph[node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node)

if len(arr) == n:
    print('Consistent')
else:
    print('Inconsistent')