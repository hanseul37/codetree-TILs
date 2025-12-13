import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2, weight = map(int, input().split())
    graph[v1].append([v2, weight])
    graph[v2].append([v1, weight]) 
a, b = map(int, input().split())
q = [[0, a]]
distance = [100000 * n for _ in range(n + 1)]
path = [0 for _ in range(n + 1)]
distance[a] = 0
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for next_node, weight in graph[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, [cost, next_node])
            path[next_node] = now
print(distance[b])

point, route = b, [b]
while point != a:
    point = path[point]
    route.append(point)
route.reverse()
print(*route)