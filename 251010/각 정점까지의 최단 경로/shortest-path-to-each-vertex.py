import heapq

n, m = map(int, input().split())
k = int(input())
graph = [[] for _ in range(n)]
distance = [float('inf')] * n
distance[k - 1] = 0
q = [[0, k - 1]]

for _ in range(m):
    v1, v2, weight = map(int, input().split())
    graph[v1 - 1].append([v2 - 1, weight])
    graph[v2 - 1].append([v1 - 1, weight])

while q:
    dist, idx = heapq.heappop(q)
    if distance[idx] <  dist:
        continue
    for node, weight in graph[idx]:
        cost = dist + weight
        if cost < distance[node]:
            distance[node] = cost
            heapq.heappush(q, [cost, node])
    
for elem in distance:
    if elem == float('inf'):
        print(-1)
    else:
        print(elem)
