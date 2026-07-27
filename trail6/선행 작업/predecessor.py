from collections import deque

n = int(input())
graph, in_degree, arr, result = [[] for _ in range(n)], [0] * n, [], [0] * n 
for i in range(n):
    cost, _, *works = map(int, input().split())
    for work in works:
        graph[work - 1].append(i) 
        in_degree[i] += 1
    arr.append(cost)
    result[i] = cost

q = deque() 
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)

cnt = 0
while q:
    node = q.popleft()
    for next_node in graph[node]:
        in_degree[next_node] -= 1
        result[next_node] = max(result[next_node], result[node] + arr[next_node])
        if in_degree[next_node] == 0:
            q.append(next_node)
print(max(result))