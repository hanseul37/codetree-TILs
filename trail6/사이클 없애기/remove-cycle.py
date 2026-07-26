from collections import deque

n, m1, m2 = map(int, input().split())
graph, in_degree = [[] for _ in range(n)], [0] * n
for _ in range(m1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    in_degree[b - 1] += 1

for _ in range(m2):
    input()

q = deque()
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)
            
cnt = 0
while q:
    node = q.popleft()
    cnt += 1
    for next_node in graph[node]:
        in_degree[next_node] -= 1  
        if in_degree[next_node] == 0:
            q.append(next_node)    

if cnt == n:
    print("Yes")
else:
    print("No")