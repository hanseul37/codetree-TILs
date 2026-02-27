import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    v1, v2, weight = map(int, input().split())
    graph[v1 - 1].append([v2 - 1, weight])
    graph[v2 - 1].append([v1 - 1, weight])

distance = [float('inf')] * n
distance[n - 1] = 0
q = [[0, n - 1]]
while q:
    dist, node = heapq.heappop(q)
    if dist > distance[node]:
        continue
    for next_node, weight in graph[node]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, [cost, next_node])

print(max(distance))