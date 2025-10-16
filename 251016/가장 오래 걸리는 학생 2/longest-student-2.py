import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    i, j, d = map(int, input().split())
    edges[j - 1].append([i - 1, d])

distance = [float('inf')] * n
distance[n - 1] = 0
q = [[0, n - 1]]
while q:
    dist, idx = heapq.heappop(q)
    if distance[idx] < dist:
        continue
    for node, d in edges[idx]:
        cost = dist + d
        if cost < distance[node]:
            distance[node] = cost
            heapq.heappush(q, [cost, node])

print(max(distance))
