import heapq

n, m = map(int, input().split())
graph, in_degree = [[] for _ in range(n)], [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    in_degree[b - 1] += 1

pq = []
for i in range(n):
    if in_degree[i] == 0:
        heapq.heappush(pq, i)

arr = []
while pq:
    node = heapq.heappop(pq)
    arr.append(node)
    for next_node in graph[node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            heapq.heappush(pq, next_node)
print(*[i + 1 for i in arr])