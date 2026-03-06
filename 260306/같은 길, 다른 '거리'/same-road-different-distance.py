import heapq 

n, m = map(int, input().split())
a, ar, b, br, warning = [[] for _ in range(n)], [[] for _ in range(n)], [[] for _ in range(n)], [[] for _ in range(n)], [[] for _ in range(n)]  
for _ in range(m):
    v1, v2, aw, bw = map(int, input().split())
    a[v1 - 1].append([v2 - 1, aw])
    b[v1 - 1].append([v2 - 1, bw])
    ar[v2 - 1].append([v1 - 1, aw])
    br[v2 - 1].append([v1 - 1, bw])

def dijkstra(graph, start):
    distance = [float('inf')] * n
    distance[start] = 0
    q = [[0, start]]
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

dist_ar = dijkstra(ar, n - 1)
dist_br = dijkstra(br, n - 1)
for i in range(n):
    for j in range(len(a[i])):
        warn = 0
        if dist_ar[a[i][j][0]] + a[i][j][1] != dist_ar[i]:
            warn += 1
        if dist_br[b[i][j][0]] + b[i][j][1] != dist_br[i]:
            warn += 1
        warning[i].append([a[i][j][0], warn])
dist_warning = dijkstra(warning, 0)
print(dist_warning[-1])

