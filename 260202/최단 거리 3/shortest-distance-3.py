import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    v1, v2, line = map(int, input().split())
    edges[v1 - 1].append([v2 - 1, line])
    edges[v2 - 1].append([v1 - 1, line])
a, b = map(int, input().split())
a -= 1
b -= 1
distance = [float('inf')] * n
distance[a] = 0
q = [[0, a]] 
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for next_node, weight in edges[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, [cost, next_node])     
print(distance[b])
