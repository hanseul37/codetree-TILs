import heapq 

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
rev_graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2, aw, bw = map(int, input().split())
    u = v1 - 1
    v = v2 - 1
    graph[u].append((v, aw, bw))
    rev_graph[v].append((u, aw, bw))

def dijkstra(graph, start, use_a=True):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, aw, bw in graph[u]:
            w = aw if use_a else bw
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

# A 기준
distA = dijkstra(graph, 0, True)
distA_rev = dijkstra(rev_graph, n-1, True)

# B 기준
distB = dijkstra(graph, 0, False)
distB_rev = dijkstra(rev_graph, n-1, False)

# 경고 그래프 생성
warning_graph = [[] for _ in range(n)]

for u in range(n):
    for v, aw, bw in graph[u]:
        cost = 0

        if distA[u] + aw + distA_rev[v] != distA[n-1]:
            cost += 1

        if distB[u] + bw + distB_rev[v] != distB[n-1]:
            cost += 1

        warning_graph[u].append((v, cost))

# 최종 다익스트라
dist_final = [float('inf')] * n
dist_final[0] = 0
pq = [(0, 0)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist_final[u]:
        continue
    for v, cost in warning_graph[u]:
        nd = d + cost
        if nd < dist_final[v]:
            dist_final[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist_final[n-1])