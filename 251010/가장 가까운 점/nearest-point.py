import heapq

n, m = map(int, input().split())
pq = []
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(pq, ((x + y), x, y))

for _ in range(m):
    xy, x, y = heapq.heappop(pq)
    heapq.heappush(pq, (xy + 4, x + 2, y + 2))

print(pq[0][1], pq[0][2])
