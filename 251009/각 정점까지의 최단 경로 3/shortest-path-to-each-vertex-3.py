import heapq

n, m = map(int, input().split())
distance = [float('inf')] * n
distance[0] = 0
q = [(0, 0)]
graph = [[] for _ in range(n)]

for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start - 1].append([end - 1, weight])

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:    
        continue
    for next_node, weight in graph[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, [cost, next_node])

for i in range(1, n):
    print(distance[i])


