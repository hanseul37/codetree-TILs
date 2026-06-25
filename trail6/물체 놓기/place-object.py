import heapq

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    weight = int(input())
    graph[0].append([i, weight])
    graph[i].append([0, weight])

for i in range(1, n + 1):
    line = list(map(int, input().split()))
    for j in range(n):
        if i == j + 1:
            continue
        graph[i].append([j + 1, line[j]])

pq, dist, visited = [], [float('inf')] * (n + 1), [False] * (n + 1)
dist[0], ans = 0, 0
heapq.heappush(pq, [0, 0])
while pq:
    min_dist, min_idx = heapq.heappop(pq)
    if visited[min_idx]:
        continue
    visited[min_idx] = True
    ans += min_dist
    for next_idx, next_dist in graph[min_idx]:
        if not visited[next_idx] and dist[next_idx] > next_dist:
            dist[next_idx] = next_dist
            heapq.heappush(pq, [next_dist, next_idx])
print(ans)