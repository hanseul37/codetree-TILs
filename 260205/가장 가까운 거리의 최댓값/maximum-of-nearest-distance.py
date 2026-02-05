import heapq

n, m = map(int, input().split())
a, b, c = map(int, input().split())
a, b, c = a - 1, b - 1, c - 1
graph = [[] for _ in range(n)]
for _ in range(m):
    v1, v2, weight = map(int, input().split())
    graph[v1 - 1].append([v2 - 1, weight])
    graph[v2 - 1].append([v1 - 1, weight])
nearlest_len = [float('inf')] * n

def dijkstra(node):
    q = [[0, node]]
    distance = [float('inf')] * n
    distance[node] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, [cost, next_node])
    for i in range(n):
        nearlest_len[i] = min(distance[i], nearlest_len[i])

dijkstra(a)
dijkstra(b)
dijkstra(c)
print(max(nearlest_len))