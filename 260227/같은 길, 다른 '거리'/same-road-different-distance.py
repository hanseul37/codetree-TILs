import heapq 

n, m = map(int, input().split())
a, b, warning = [[] for _ in range(n)], [[] for _ in range(n)], [[] for _ in range(n)]  
for _ in range(m):
    v1, v2, aw, bw = map(int, input().split())
    a[v1 - 1].append([v2 - 1, aw])
    b[v1 - 1].append([v2 - 1, bw])
    warning[v1 - 1].append([v2 - 1, 2])

def dijkstra(graph):
    distance = [float('inf')] * n
    distance[0] = 0
    q = [[0, 0]]
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for next_node, weight in graph[node]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, [cost, next_node])
    return distance

dist_a = dijkstra(a)
dist_b = dijkstra(b)
for i in range(n):
    for j in range(len(warning[i])):
        if dist_a[i] + a[i][j][1] != dist_a[a[i][j][0]]:
            warning[i][j][1] -= 1
        if dist_b[i] + b[i][j][1] != dist_b[b[i][j][0]]:
            warning[i][j][1] -= 1

dist_warning = dijkstra(warning)
print(dist_warning[-1])

