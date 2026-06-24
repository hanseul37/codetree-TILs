import heapq

n, m = map(int, input().split())
graph, pq = [[] for _ in range(n)], []
dist, visited = [float('inf')] * n, [False] * n
for _ in range(m):
    v1, v2, weight = map(int, input().split())
    graph[v1 - 1].append([v2 - 1, weight])
    graph[v2 - 1].append([v1 - 1, weight])

dist[0], ans = 0, 0
heapq.heappush(pq, [0, 0])
while pq:
    min_dist, min_idx = heapq.heappop(pq)
    if visited[min_idx]:
        continue
    visited[min_idx] = True
    ans += min_dist
    for target_idx, target_dist in graph[min_idx]:
        new_dist = target_dist
        if dist[target_idx] > new_dist:
            dist[target_idx] = new_dist
            heapq.heappush(pq, [new_dist, target_idx])
print(ans)
