import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
nodes = input().split()
m = int(input())
graph, in_degree, child = dict(), dict(), dict()
for node in nodes:
    graph[node] = []
    in_degree[node] = 0
    child[node] = []

for _ in range(m):
    x, y = input().split()
    graph[y].append(x)
    in_degree[x] += 1

q, root = deque(), []
for idx, value in in_degree.items():
    if value == 0:
        q.append(idx)
        root.append(idx)

while q:
    node = q.popleft()
    for next_node in graph[node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node)
            child[node].append(next_node)

root.sort()
nodes.sort()
print(len(root))
print(*root)
for node in nodes:
    child[node].sort()
    print(node, len(child[node]), *child[node])
