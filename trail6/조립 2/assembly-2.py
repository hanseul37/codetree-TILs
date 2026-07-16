from collections import deque

n, m = map(int, input().split())
graph, in_degree = [[] for _ in range(n)], [0] * n
for _ in range(m):
    a, k = map(int, input().split())
    parts = list(map(int, input().split()))
    for i in range(k):
        graph[parts[i] - 1].append(a - 1)
        in_degree[a - 1] += 1

parts_cnt = int(input())
current_parts = list(map(int, input().split()))
q = deque()
for part in current_parts:
    in_degree[part - 1] = 0
    q.append(part - 1)

arr = []
while q:
    node = q.popleft()
    arr.append(node)
    for next_node in graph[node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            q.append(next_node) 

arr.sort()
print(len(arr)) 
print(*[i + 1 for i in arr])