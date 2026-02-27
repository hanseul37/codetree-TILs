import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    i, j, d = map(int, input().split())
    i -= 1
    j -= 1
    graph[i].append((j, d))
    graph[j].append((i, d))  # 무방향

def dijkstra(start):
    dist = [float('inf')] * N
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, node = heapq.heappop(pq)
        if cur_dist > dist[node]:
            continue

        for next_node, weight in graph[node]:
            new_dist = cur_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

    return dist

# 학교는 N번 → 인덱스 N-1
distances = dijkstra(N - 1)

# 1번 ~ N-1 중 최댓값
print(max(distances[:-1]))