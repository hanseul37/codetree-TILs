import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    v1, v2, weight = map(int, input().split())
    graph[v1 - 1].append([v2 - 1, weight])
    graph[v2 - 1].append([v1 - 1, weight])
for i in range(n):
    graph[i].sort()
a, b = map(int, input().split())
a -= 1
b -= 1
q = [[0, b]]
distance = [float('inf')] * n
distance[b] = 0
while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue
    for nxt, weight in graph[node]:
        cost = dist + weight
        if cost < distance[nxt]:
            distance[nxt] = cost
            heapq.heappush(q, [cost, nxt])

route, point = [a], a
while point != b:
    for nxt, weight in graph[point]:
        if distance[nxt] + weight == distance[point]:
            route.append(nxt)
            point = nxt
            break
print(distance[a])
for elem in route:
    print(elem + 1, end=' ')